from __future__ import annotations

import math
from contextlib import contextmanager
from typing import Any, Generator, Optional, Union

import QuantLib as ql

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.engine import QLObject
from valuation.engine.check import BothNoneOrGiven, Length, ObjectType, Range
from valuation.engine.exceptions import QLInputError, ql_require
from valuation.engine.utils import date2year_fraction, qldate2date
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency
    from valuation.engine.function import QLFunction
    from valuation.engine.mappings import QLBusiness
    from valuation.engine.check import Check
    from valuation.universal_transfer import DefaultParameters, Storage


class QLMarketData(QLObject):                             # pylint: disable=abstract-method
    _additional_fixing_checks: list[Check] = []
    _initializes_past: bool = True

    @property
    def business(self) -> QLBusiness:
        return self._business

    @property
    def calendar(self) -> ql.Calendar:
        return self._calendar

    @property
    def currency(self) -> QLCurrency:
        return self._currency

    @property
    def daycount(self) -> ql.DayCounter:
        return self._daycount

    @property
    def scenario_divisor(self) -> float:
        raise NotImplementedError

    @property
    def shift_unit(self) -> int:
        raise NotImplementedError

    @property
    def provides_range(self) -> bool:
        return self._provides_range

    @property
    def state(self) -> QLMarketData:
        return self._state

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        if self._initializes_past:
            fixing_dates: list[ql.Date] = self.data(fields.FixingDates, default_value=tuple(), check=[Range(upper=self._valuation_date, strict=False)])
            fixing_values: list[float] = self.data(fields.Fixings, default_value=tuple(), check=Length(fixing_dates))
            self._fixings: dict[ql.Date, float] = {fixing_date: fixing_value for fixing_date, fixing_value in zip(fixing_dates, fixing_values)}  # pylint: disable=unnecessary-comprehension
            self._fixing_function: QLFunction = self.data(fields.FixingFunction, default_value=None, check=[ObjectType(signatures.function.all)])
            if self._fixing_function and not self._fixing_function.return_type == types.Float:
                raise QLInputError('Function needs to have same type (float) as fixings!')

        self._low_market_data: QLMarketData = self.data(fields.LowMarketData, default_value=None, check=ObjectType(self.signature), exclude_from_greeks=True)
        self._high_market_data: QLMarketData = self.data(fields.HighMarketData, default_value=None, check=[ObjectType(self.signature),
                                                                                                           BothNoneOrGiven(self._low_market_data)], exclude_from_greeks=True)
        self._provides_range: bool = not (self._low_market_data is None and self._high_market_data is None)
        if self._provides_range and not self._documentation_mode and not self._data_only_mode:
            ql_require(not self._low_market_data.provides_range, 'High and low referenced objects cannot have references themselves')
            ql_require(not self._high_market_data.provides_range, 'High and low referenced objects cannot have references themselves')

        self._currency: QLCurrency
        self._calendar: ql.Calendar
        self._daycount: ql.DayCounter
        self._business: QLBusiness

        self._state: QLMarketData = self

    def generate_validation_report(self) -> Storage:
        raise NotImplementedError

    def has_fixing(self, date: ql.Date) -> bool:
        if not self._initializes_past:
            raise ProgrammingError(f'{self.__class__.__name__} does not initialize the past.')
        return date in self._fixings

    def add_fixing(self, date: ql.Date, value: float, overwrite: bool = False) -> None:
        if not self._initializes_past:
            raise ProgrammingError(f'{self.__class__.__name__} does not initialize the past.')
        if not overwrite and self.has_fixing(date):
            raise QLInputError(f'{self.reference} already has a fixing for {date}')
        self._fixings[date] = value
        _ = self[date]

    @QLObject.static
    @QLObject.moves_to_shifted
    def __getitem__(self, date: ql.Date) -> float:
        if date in self._fixings:
            return self._fixings[date]
        if self._fixing_function:
            value: float = self._fixing_function(qldate2date(date))
            if __debug__:
                for sub_check in self._additional_fixing_checks:
                    sub_check(value)
            self._fixings[date] = value
            return value
        raise QLInputError(f'No past fixing at {date} available!')

    def scenarios(self, greek: str) -> list[str]:       # type: ignore[return]
        if greek not in self._supported_greeks:
            raise ProgrammingError()

    def _change_to(self, scenario: str, shift: float) -> None:
        raise NotImplementedError

    def _change_back(self, scenario: str) -> None:
        raise NotImplementedError

    @contextmanager
    def change_to(self, scenario: str, shift: float) -> Generator[None, None, None]:
        try:
            self._change_to(scenario, shift)
            yield
        except Exception as exception:
            raise exception
        finally:
            self._change_back(scenario)

    def _market_shift(self, sub_market_data: QLMarketData) -> None:
        self._state = sub_market_data

    def _shift_back(self) -> None:
        self._state = self

    @property
    def market_data_scenarios(self) -> list[str]:
        return ['high', 'low']

    @contextmanager
    def market_shift(self, scenario: str) -> Generator[None, None, None]:
        if scenario == 'high':
            new_market_data: QLMarketData = self._high_market_data or self
        elif scenario == 'low':
            new_market_data = self._low_market_data or self
        else:
            raise ProgrammingError()
        try:
            self._market_shift(new_market_data)
            yield
        except Exception as exception:
            raise exception
        finally:
            self._shift_back()

    @contextmanager
    def safe_access_checks_only(self) -> Generator[None, None, None]:
        assert self._listens_for_observers
        self._listens_for_observers = False
        yield
        self._listens_for_observers = True

    def generate_simulation_year_fractions(self, observation_dates: list[ql.Date], non_observation_dates: list[ql.Date], maximal_time_stepping_in_days: float,
                                           continuous_period: Optional[tuple[ql.Date, ql.Date]], continuous_time_stepping_in_days: Optional[float]) -> tuple[list[float], dict[int, ql.Date], dict[int, bool], dict[ql.Date, float], dict[int, float]]:

        def linear_excluding_start(start: float, end: float, step: float, smooth_start: bool = False) -> list[float]:
            number_steps = math.floor((end - start) / (step / 365.0))
            adjusted_step = (end - start) / (number_steps + 1)
            result = [start + adjusted_step * (count + 1) for count in range(number_steps)] + [end]
            if smooth_start:
                while result[0] - start > (1 / 8) / 365.0:
                    result = [result[0] / 2] + result
            return result

        non_observation_dates_augmented: dict[ql.Date, float] = {date: date2year_fraction(self._valuation_date, date, self._daycount) for date in non_observation_dates}

        past_observation_dates: list[ql.Date] = []
        observation_times: list[tuple[float, Union[ql.Date, bool]]] = []
        for observation_date in observation_dates:
            if observation_date < self._valuation_date:
                past_observation_dates.append(observation_date)
            else:
                observation_times.append((date2year_fraction(self._valuation_date, observation_date, self._daycount), observation_date))
        if continuous_period:
            if continuous_period[0] < self._valuation_date:
                continuous_period = (self._valuation_date, continuous_period[1])
            if continuous_period[1] < self._valuation_date:
                continuous_period = None
        if continuous_period:
            continuous_start = date2year_fraction(self._valuation_date, continuous_period[0], self._daycount) + 3.17e-11            # Adjust the start for 1ms
            continuous_end = date2year_fraction(self._valuation_date, continuous_period[1], self._daycount) + 0.5 / 365              # Adust continuous period for half a day!!!
            continuous_steps = linear_excluding_start(continuous_start, continuous_end, continuous_time_stepping_in_days)          # type: ignore[arg-type]
            observation_times.append((continuous_start, True))
            last_time = continuous_start
            for continuous_step in continuous_steps:
                observation_times.append(((last_time + continuous_step) / 2.0, False))
                observation_times.append((continuous_step, True))
                last_time = continuous_step
        observation_mask: dict[int, ql.Date] = {-len(past_observation_dates) + count: date for count, date in enumerate(sorted(past_observation_dates))}
        continuous_mask: dict[int, bool] = {}
        simulation_times: list[float] = [0.0]
        smooth_start = True
        last_time = 0.0
        for observation_time in sorted(observation_times):
            if observation_time[0] < 0.0:
                continue
            if observation_time[0] > simulation_times[-1] + 1.0 / (365 * 24 * 60):
                simulation_times += linear_excluding_start(last_time, observation_time[0], maximal_time_stepping_in_days, smooth_start)
                smooth_start = False
            if isinstance(observation_time[1], ql.Date):
                observation_mask[len(simulation_times) - 1] = observation_time[1]
            else:
                continuous_mask[len(simulation_times) - 1] = observation_time[1]
            last_time = simulation_times[-1]
        simulation_time_map: dict[int, float] = dict(enumerate(simulation_times))
        simulation_time_map.update({observation: date2year_fraction(self._valuation_date, date, self._daycount) for observation, date in observation_mask.items() if observation < 0})

        return simulation_times, observation_mask, continuous_mask, non_observation_dates_augmented, simulation_time_map

    def evaluate(self, fixing_date: ql.Date, optional_info: str) -> dict[str, Any]:
        raise NotImplementedError
