from __future__ import annotations

import itertools
import math
from typing import Any, Callable, Generator, Iterator, Optional, Union

import QuantLib as ql
import numpy
import scipy.integrate

from valuation.consts import global_parameters
from valuation.consts.pl import PathAll, PathDiscount, PathSeparatedDiscount, PathSeparatedRaw, PathSeparatedSummation, PathSeparatedValue, PathSummation, PathValue, PathVolatility
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import QLInputError
from valuation.engine.utils import year_fraction2date
from valuation.utils.decorators import memoize

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.market_data import QLYieldCurve
    from valuation.engine.utils import StockDividends
    from valuation.engine.process import QLProcess


SEED = 1


QLPathGenerator = Any               # pylint: disable=invalid-name


# It is hard to find which of the random generators is assumed to perform best.
# Most likely, one should go with Sobol, a low discrepancy pseudo random generator
# which provides an excellent spatial sampling, as long as one uses 2^n - 1 paths
# If we head for pseudo random numbers instead, the choices become manifold, both
# for the generation of uniform sequences (Knuth, L'Ecuyer, Mersenne-Twister) and
# for the generation of gaussian random variables (the most well-known might be
# Box-Muller).
# Here we currently decided to go for the ones, which seem to be defined as
# "standard" in the quantlib.
def path_generator_factory(generator_type: str, process: ql.StochasticProcess, year_fractions: list[float], brownian_bridge: bool, seed: int = SEED) -> QLPathGenerator:
    is_multi_process: bool = process.size() > 1
    length = (len(year_fractions) - 1) * process.size()
    if generator_type == 'Sobol':
        # SWIGs\randomnumbers.i
        # UniformLowDiscrepancySequenceGenerator
        #         dimensionality Size
        #         BigInteger seed=0,
        #         directionIntegers = QuantLib::SobolRsg::Jaeckel
        # GaussianLowDiscrepancySequenceGenerator
        #         u UniformLowDiscrepancySequenceGenerator
        uniform_sequence_generator = ql.UniformLowDiscrepancySequenceGenerator(length, seed)
        gaussian_sequence_generator = ql.GaussianLowDiscrepancySequenceGenerator(uniform_sequence_generator)
    elif generator_type == 'Standard':
        # SWIGs\randomnumbers.i
        # UniformRandomGenerator  --> None
        # 		seed	BigInteger		(0)
        # UniformRandomSequenceGenerator  --> None
        # 		dimensionality	Size
        # 		rng	UniformRandomGenerator
        # GaussianRandomSequenceGenerator --> None
        # 		UniformRandomSequenceGenerator uniformSequenceGenerator
        uniform_sequence_generator = ql.UniformRandomSequenceGenerator(length, ql.UniformRandomGenerator(seed))
        gaussian_sequence_generator = ql.GaussianRandomSequenceGenerator(uniform_sequence_generator)
    else:
        raise QLInputError('Unknown process type given')
    if is_multi_process:
        # SWIGs\montecarlo.i
        # GaussianMultiPathGenerator --> None
        # 		process	<StochasticProcess>
        # 		times	vector<Time>
        # 		generator	GaussianRandomSequenceGenerator
        # 		brownianBridge	bool		(false)
        return ql.GaussianMultiPathGenerator(process, year_fractions, gaussian_sequence_generator, brownian_bridge)

    # SWIGs\grid.i
    # TimeGrid --> None
    # 		times	vector<Time>
    time_grid = ql.TimeGrid(year_fractions)
    if generator_type == 'Sobol':
        # SWIGs\montecarlo.i
        # template(GaussianSobolPathGenerator) PathGenerator<GaussianLowDiscrepancySequenceGenerator>
        # PathGenerator
        #       timeGrid TimeGrid
        #       generator GSG
        #       brownianBridge bool
        return ql.GaussianSobolPathGenerator(process, time_grid, gaussian_sequence_generator, brownian_bridge)
    if generator_type == 'Standard':
        # SWIGs\montecarlo.i
        # template(GaussianPathGenerator) PathGenerator<GaussianRandomSequenceGenerator>
        # PathGenerator
        #       timeGrid TimeGrid
        #       generator GSG
        #       brownianBridge bool
        return ql.GaussianPathGenerator(process, time_grid, gaussian_sequence_generator, brownian_bridge)
    raise QLInputError('Unknown process type given')


class PathDescriptor:
    @property
    def processes_and_generators(self) -> Iterator[tuple[ql.StochasticProcess, Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]]]:
        return zip(self._processes, self._process2generator_factories)

    @property
    def all_price_parts(self) -> list[str]:
        return self._all_price_parts

    @property
    def stock_modifier(self) -> dict[str, StockDividends]:
        return self._stock_modifier

    @property
    def allow_discount(self) -> set[str]:
        return self._allow_discount

    @property
    def assignments(self) -> dict[Union[int, tuple[int, int]], str]:
        return self._assignments

    @property
    def process2generator_factories(self) -> list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]]:
        return self._process2generator_factories

    @property
    def aliases(self) -> dict[str, str]:
        return self._aliases

    @property
    def summations(self) -> dict[str, set[str]]:
        return self._summations

    def __init__(self, process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]],
                 assignments: dict[Union[int, tuple[int, int]], str], aliases: dict[str, str], allow_discount: set[str], stock_modifier: dict[str, StockDividends],
                 summations: dict[str, set[str]]) -> None:
        self._processes: list[ql.StochasticProcess] = []
        self._process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = process2generator_factories
        self._assignments: dict[Union[int, tuple[int, int]], str] = assignments
        self._aliases: dict[str, str] = aliases
        self._allow_discount: set[str] = allow_discount
        self._stock_modifier: dict[str, StockDividends] = stock_modifier
        prices: set[str] = set()
        for entry in self._assignments.values():
            if entry.endswith(PathSeparatedValue):
                prices.add(entry)
            elif entry.endswith(PathSeparatedRaw):
                prices.add(entry.replace(PathSeparatedRaw, PathSeparatedValue))
        self._all_price_parts: list[str] = sorted(prices)
        self._summations = summations

    def attach_processes(self, processes: list[ql.StochasticProcess]) -> None:
        assert not self._processes
        self._processes = processes

    def clear_processes(self) -> None:
        self._processes = []

    def alias(self, item: str) -> Optional[str]:
        return self._aliases.get(item, None)

    def discount_base(self, item: str) -> Optional[str]:
        if item in self._allow_discount:
            return item.replace(PathSeparatedDiscount, PathSeparatedValue)
        return None

    def stock_base(self, item: str) -> Optional[str]:
        if item in self._stock_modifier:
            return item.replace(PathSeparatedValue, PathSeparatedRaw)
        return None


class SimulatedPath:

    def __init__(self, path_descriptor: PathDescriptor, full_path: Path, generator_type: str, simulation_times: list[float], brownian_bridge: bool, antithetic: bool, seed: int = SEED) -> None:
        self._simulation_times: list[float] = simulation_times
        self._path_descriptor: PathDescriptor = path_descriptor
        self._antithetic: bool = antithetic
        self._full_path: Path = full_path
        self._paths: dict[str, list[Union[float, list[float]]]] = {}
        self._counter: int = -1

        self._generators: list[tuple[int, QLPathGenerator, bool]] = [(count, process_factory(generator_type, process, simulation_times, brownian_bridge, seed + count), process.size() > 1) for count, (process, process_factory) in enumerate(self._path_descriptor.processes_and_generators)]

        self._addons: dict[str, dict[int, float]] = {}
        self._scalars: dict[str, dict[int, float]] = {}

        for entry, stock_dividend in self._path_descriptor.stock_modifier.items():
            self._addons[entry] = {}
            self._scalars[entry] = {}
            for observation in self._full_path.future_points_of_interest:
                addon, scalar = stock_dividend.affine_modifiers(self._full_path.date_from_observation(observation, 0))
                self._addons[entry][observation] = addon
                self._scalars[entry][observation] = scalar
            if not any(self._addons[entry].values()):
                self._addons[entry] = {}
            if all(value == 1 for value in self._scalars[entry].values()):
                self._scalars[entry] = {}
        self._full_path.set_path(self)

    def _generate_future(self, item: str) -> None:
        if item in self._paths:
            return
        # Alias
        if alias := self._path_descriptor.alias(item):
            self._generate_future(alias)
            self._paths[item] = self._paths[alias]
        # Discount
        elif item.endswith(PathSeparatedDiscount):
            if price_item := self._path_descriptor.discount_base(item):
                self._paths[item] = numpy.exp(-scipy.integrate.cumtrapz(self._paths[price_item], self._simulation_times, initial=0.))
        elif item == PathAll + PathSeparatedValue:
            all_parts: list[str] = self._path_descriptor.all_price_parts
            for sub_item in all_parts:
                self._generate_future(sub_item)
            new_list_data: list[Union[float, list[float]]] = [float('nan')] * len(self._simulation_times)
            entry: int
            for entry in self._full_path.future_points_of_interest:
                new_list_data[entry] = [self._paths[sub_item][entry] for sub_item in all_parts]     # type: ignore[misc]
            self._paths[item] = new_list_data
        # StockPrice
        elif item.endswith(PathSeparatedValue):
            scalars: dict[int, float] = self._scalars[item]
            addons: dict[int, float] = self._addons[item]
            raw_item = self._path_descriptor.stock_base(item)
            assert raw_item is not None
            raw_data: list[float] = self._paths[raw_item]               # type: ignore[assignment, index]
            if not scalars and not addons:
                new_data: list[float] = raw_data
            else:
                new_data = [float('nan')] * len(raw_data)
                for entry in self._full_path.future_points_of_interest:
                    if scalars and addons:
                        new_data[entry] = raw_data[entry] * scalars[entry] + addons[entry]
                    elif scalars:
                        new_data[entry] = raw_data[entry] * scalars[entry]
                    else:
                        new_data[entry] = raw_data[entry] + addons[entry]
            self._paths[item] = new_data        # type: ignore[assignment]
        elif item.endswith(PathSeparatedSummation):
            for sub_item in self._path_descriptor.summations[item]:
                self._generate_future(sub_item)
            new_list_data = [float('nan')] * len(self._simulation_times)
            for entry in self._full_path.future_points_of_interest:
                new_list_data[entry] = 0.0
                for sub_item in self._path_descriptor.summations[item]:
                    new_list_data[entry] += self._paths[sub_item][entry]        # type: ignore[operator]
            self._paths[item] = new_list_data

    def __next__(self) -> None:
        self._paths = {}
        for generator_counter, generator, multi_process in self._generators:
            if not self._antithetic or self._counter % 2:
                next_path = generator.next().value()
            else:
                next_path = generator.antithetic().value()
            if multi_process:
                for sub_generator_counter, sub_path in enumerate(next_path):
                    self._paths[self._path_descriptor.assignments[(generator_counter, sub_generator_counter)]] = list(sub_path)
            else:
                self._paths[self._path_descriptor.assignments[generator_counter]] = next_path
        self._counter += 1

    def __getitem__(self, item: str) -> list[Union[float, list[float]]]:
        if item not in self._paths:
            self._generate_future(item)
        return self._paths[item]


class Path:

    @property
    def future_points_of_interest(self) -> list[int]:
        return self._future_points_of_interest

    @property
    def calendar(self) -> ql.Calendar:
        return self._calendar

    @property
    def continuous_mask(self) -> dict[int, bool]:
        return self._continuous_mask

    @property
    def second_yield_curve(self) -> Optional[QLYieldCurve]:
        return self._second_yield_curve

    def __init__(self, observation_mask: dict[int, ql.Date], continuous_mask: dict[int, bool], non_observation_dates: dict[ql.Date, float], simulation_times: list[float], simulation_time_map: dict[int, float], process: QLProcess, path_descriptor: PathDescriptor) -> None:
        try:
            self._second_yield_curve: Optional[QLYieldCurve] = process.attached_market_data.yield_curve           # type: ignore[attr-defined]
        except AttributeError:
            self._second_yield_curve = None
        self._calendar: ql.Calendar = process.attached_market_data.calendar
        self._daycount: ql.DayCounter = process.attached_market_data.daycount
        self._valuation_date: ql.Date = process.valuation_date

        self._observation_mask: dict[int, ql.Date] = observation_mask
        self._inverse_observation_mask: dict[ql.Date, int] = {date: count for count, date in observation_mask.items()}
        self._continuous_mask: dict[int, bool] = continuous_mask
        self._path_descriptor: PathDescriptor = path_descriptor

        points_of_interest: list[tuple[float, Optional[int], ql.Date]] = [(simulation_time_map[observation], observation, self._observation_mask[observation]) for observation in self._observation_mask]
        points_of_interest += [(simulation_time_map[observation], observation, self._observation_mask.get(observation, global_parameters.DummyQLDate)) for observation in continuous_mask]
        point_of_interest_dates = {entry[2] for entry in points_of_interest}
        for date, value_ in non_observation_dates.items():
            if date not in point_of_interest_dates:
                # In the case of a collision, bring the non-observation date 1ms before the date it is coliding with. Otherwise there should be no real effect.
                points_of_interest.append((value_ - 3.17e-11, None, date))
        self._points_of_interest: list[tuple[Optional[int], ql.Date]] = [(observation, date) for __, observation, date in sorted(set(points_of_interest))]

        self._simulation_times: list[float] = simulation_times

        self._future_points_of_interest: list[int] = [observation for observation, __ in self._points_of_interest if observation is not None and observation >= 0]

        self._past_values: dict[int, dict[str, float]] = {}
        for observation, date in itertools.chain(self._observation_mask.items(), [(0, self._valuation_date)]):
            if observation > 0:
                continue
            self._past_values[observation] = {}
            past_value = process[date]
            if isinstance(past_value, float):
                self._past_values[observation][process.attached_market_data.reference.id + PathSeparatedValue] = past_value
            else:
                self._past_values[observation] = {key + PathSeparatedValue: value for key, value in past_value.items()}

                self._past_values[observation][PathAll + PathSeparatedValue] = [self._past_values[observation][entry] for entry in self._path_descriptor.all_price_parts]

        self._path: SimulatedPath = None            # type: ignore[assignment]

    def set_path(self, path: SimulatedPath) -> None:
        if self._path:
            raise ProgrammingError('Just one path can be attached!')
        self._path = path

    @memoize
    def date_from_observation(self, observation: int, shifting_days: int) -> ql.Date:
        if not shifting_days:
            if observation in self._observation_mask:
                return self._observation_mask[observation]
            return year_fraction2date(self._valuation_date, self._simulation_times[observation], self._daycount)
        base_date = self.date_from_observation(observation, 0)
        return self._calendar.advance(base_date, shifting_days, ql.Days)

    def value(self, observation: int, variable_name: str) -> Union[float, list[float]]:
        if observation <= 0:
            if variable_name not in self._past_values[observation]:
                variable_name = self._path_descriptor.alias(variable_name) or variable_name
            if variable_name in self._past_values[observation]:
                return self._past_values[observation][variable_name]
            if variable_name.endswith(PathDiscount):
                return 1.0
            if variable_name.endswith(PathVolatility):
                return 0.0
            if variable_name.endswith(PathSummation):
                return self.value(observation, variable_name.replace(PathSummation, PathValue))
            raise QLInputError()
        return self._path[variable_name][observation]

    @memoize
    def advanced_inverse_observation(self, date: ql.Date) -> tuple[int, int]:
        if date in self._inverse_observation_mask:
            return self._inverse_observation_mask[date], 0
        for helper_date in sorted(self._inverse_observation_mask):
            if helper_date < date:
                final_helper_date = helper_date
            else:
                break
        return self._inverse_observation_mask[final_helper_date], date - final_helper_date

    def discount_from_date(self, date: ql.Date, variable_name: str) -> float:
        observation, settlement_days = self.advanced_inverse_observation(date)
        return self.discount_from_observation(observation, settlement_days, variable_name)

    def discount_from_observation(self, observation: int, settlement_days: int, variable_name: str) -> float:
        assert variable_name == PathDiscount or variable_name.endswith(PathSeparatedDiscount)
        if observation <= 0:
            return 1.0
        if not settlement_days:
            return self._path[variable_name][observation]       # type: ignore[return-value]
        rate = self._path[variable_name.replace(PathDiscount, PathValue)][observation]
        return self._path[variable_name][observation] * math.exp(-rate * settlement_days / 365.0)  # type: ignore[index, no-any-return, operator]

    def observations(self) -> Generator[tuple[Optional[int], ql.Date], None, None]:
        yield from self._points_of_interest
