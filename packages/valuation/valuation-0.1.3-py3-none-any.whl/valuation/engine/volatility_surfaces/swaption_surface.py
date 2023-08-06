from __future__ import annotations

from typing import NamedTuple, Optional

import QuantLib as ql

from valuation.consts import signatures, types, global_parameters
from valuation.consts import fields
from valuation.engine import QLObject, QLObjectBase
from valuation.engine import defaults
from valuation.engine.check import IsOrdered, Range
from valuation.engine.exceptions import QLInputError
from valuation.engine.mappings import VolatilityType
from valuation.engine.utils import period2qlperiod
from valuation.engine.volatility_surfaces.base_object import QLVolatility
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness, QLVolatilityType
    from valuation.engine.market_data import QLCurrency
    from valuation.universal_transfer import DefaultParameters, Storage


class CalibrationData(NamedTuple):
    option_tenor: Period
    swap_tenor: Period
    volatility: float


class QLSwaptionPoint(QLObjectBase):
    _signature = signatures.swaption_point

    @property
    def swap_tenor(self) -> Period:
        return self._swap_tenor

    @property
    def option_tenor(self) -> Period:
        return self._option_tenor

    @property
    def value(self) -> float:
        if self._value is None:
            raise QLInputError('Swaption Point has no value')
        return self._value

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Optional[QLObject] = None, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._swap_tenor: Period = self.data(fields.SwapTenor)
        self._option_tenor: Period = self.data(fields.OptionTenor)
        self._value: Optional[float] = self.data(fields.Value, default_value=None)


class QLSwaptionVolatility(QLVolatility):
    _signature = signatures.empty

    @property  # type: ignore[misc]
    @QLObject.moves_to_shifted
    def ql_surface(self) -> ql.SwaptionVolatilityMatrix:
        return self._ql_surface

    @property
    def enable_extrapolation(self) -> bool:
        return self._enable_extrapolation

    def short_term_swaption_volatility(self, swap_period: Period) -> float:
        swap_counter = self._swap_tenors.index(swap_period)
        return self._vol_surface[0][swap_counter]  # type: ignore[no-any-return]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)

        self._currency: QLCurrency = self.data(fields.Currency)
        self._option_tenors: list[Period]
        self._swap_tenors: list[Period]
        self._vol_surface: list[list[float, ...], ...]
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=defaults.daycount(self._currency.id))
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.id)
        self._business: QLBusiness = self.data(fields.Business, default_value=defaults.business(self._currency.id))
        self._distribution: QLVolatilityType = self.data(fields.Distribution, ql_map=VolatilityType)
        self._settlement_days: int = self.data(fields.SettlementDays,
                                               default_value=defaults.settlement_days(self._currency.id,
                                                                                      Period(3, 'M')),
                                               check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum,
                                                           strict=False))
        self._enable_extrapolation: bool = self.data(fields.EnableExtrapolation, default_value=True)

        self._ql_surface: ql.SwaptionVolatilityMatrix

    def _post_init(self) -> None:
        #  SWIGs\volatilities.i
        # 	SwaptionVolatilityMatrix --> None
        # 		calendar	Calendar
        # 		bdc	BusinessDayConvention
        # 		optionTenors	vector<Period>
        # 		swapTenors	vector<Period>
        # 		vols	vector< vector<Handle<Quote> > >
        # 		dayCounter	DayCounter
        # 		flatExtrapolation	bool		(false)
        # 		type	VolatilityType		(ShiftedLognormal)
        # 		shifts	vector< vector<Real> >		(vector< vector<Real> > ( ))
        self._ql_surface = ql.SwaptionVolatilityMatrix(
            self._calendar,
            self._business,
            period2qlperiod(self._option_tenors),
            period2qlperiod(self._swap_tenors),
            ql.Matrix(self._vol_surface),
            self._daycount,
            False,
            self._distribution,
        )

        if self._enable_extrapolation:
            self._ql_surface.enableExtrapolation()

    def calibration_data(self) -> list[CalibrationData]:
        # http://gouthamanbalaraman.com/blog/short-interest-rate-model-calibration-quantlib.html

        data: list[CalibrationData] = []
        for option_counter, option_tenor in enumerate(self._option_tenors):
            data.extend(CalibrationData(option_tenor, swap_tenor, self._vol_surface[option_counter][swap_counter]) for
                        swap_counter, swap_tenor in enumerate(self._swap_tenors))

        return data


class QLSwaptionVolatilitySurface(QLSwaptionVolatility):  # pylint: disable=abstract-method
    _signature = signatures.swaption_volatility.surface

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)
        self._option_tenors, self._swap_tenors, self._vol_surface = self.data_matrix(fields.Surface,
                                                                                     row_type=types.Periods,
                                                                                     col_type=types.Periods,
                                                                                     content_type=types.FloatMatrix,
                                                                                     row_check=IsOrdered(),
                                                                                     col_check=IsOrdered(),
                                                                                     content_check=Range(lower=0.0,
                                                                                                         upper=global_parameters.VolatilityMaximum))


class QLSwaptionVolatilityPoints(QLSwaptionVolatility):  # pylint: disable=abstract-method
    _signature = signatures.swaption_volatility.points

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)
        self.add_linetype(QLSwaptionPoint, fields.VolaPoints)

        points: list[QLSwaptionPoint] = self.data(fields.VolaPoints)
        unsorted_option_tenors: set[Period] = set()
        unsorted_swap_tenors: set[Period] = set()
        value_map: dict[tuple[Period, Period], float] = {}
        for point in points:
            unsorted_swap_tenors.add(point.swap_tenor)
            unsorted_option_tenors.add(point.option_tenor)
            value_map[(point.swap_tenor, point.option_tenor)] = point.value
        self._option_tenors = sorted(unsorted_option_tenors)
        self._swap_tenors = sorted(unsorted_swap_tenors)
        try:
            self._vol_surface = [
                [value_map[(swap_tenor, option_tenor)] for swap_tenor in self._swap_tenors]
                for option_tenor in self._option_tenors
            ]
        except KeyError:
            raise QLInputError('Surface is not complete.')
