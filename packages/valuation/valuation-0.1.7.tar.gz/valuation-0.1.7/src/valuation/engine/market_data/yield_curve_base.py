from __future__ import annotations

from typing import Any, Union

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.engine import QLObject
from valuation.engine.mappings import Compounding, Frequencies, QLCompounding, QLFrequency
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import add_tenor, date2qldate
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.universal_output import result_items
from valuation.universal_transfer import DefaultParameters, Period, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    import datetime
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency
    from valuation.engine.mappings import QLBusiness


class QLYieldCurve(QLMarketData):                 # pylint: disable=abstract-method
    """
    Object structure inside the QLYieldCurve and it's inheritances:

    yc_handle[ql.YieldTermStructureHandle](
        ql.SpreadedLinearZeroInterpolatedTermStructure(
            yc_proxy[ql.RelinkableYieldTermStructureHandle](
                yc_handle_noshift[ql.YieldTermStructureHandle],
            ),
            rho_adjustment[dates, ql.SimpleQuote]
        )
    )

    yc_handle: object to use from the outside
    yc_proxy: internal object of the virtual class; is relinkable; used to link the inheritances' handle to
    yc_handle_noshift: handle of the inheritance
    rho_adjustment: collection of adjustable simple quotes that are changed for the rho calculation
    """
    _signature = signatures.empty
    _supported_greeks: tuple[str, ...] = (result_items.Rho,)
    _initializes_past: bool = False

    @property
    def is_base_curve(self) -> bool:
        return True

    @property
    def handle(self) -> ql.YieldTermStructureHandle:
        return self._yc_handle

    @property
    def scenario_divisor(self) -> float:
        return self._shift_in_bp

    @property
    def shift_unit(self) -> int:
        return 10000

    @property               # type: ignore[misc]
    @QLObject.static
    def base_curve_handle(self) -> ql.YieldTermStructureHandle:
        return self._yc_handle_noshift

    @property
    def base_curve_handle_risk_free(self) -> ql.YieldTermStructureHandle:
        return self.base_curve_handle

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._enable_extrapolation: bool = self.data(fields.EnableExtrapolation,
                                                     allow_fallback_to_default_parameters=True, default_value=False)
        self._rho_scenarios_raw: list[Period] = self.data(fields.RhoScenarios,
                                                          default_value=tuple(),
                                                          allow_fallback_to_default_parameters=True)
        self._rho_business_convention: QLBusiness = self.data(fields.RhoBusiness,
                                                              default_value='Modified Following',
                                                              allow_fallback_to_default_parameters=True)
        self._rho_calendar: ql.Calendar = self.data(fields.RhoCalendar, default_value='EUR',
                                                    allow_fallback_to_default_parameters=True)

        self._currency: QLCurrency
        self._calendar: ql.Calendar
        self._yc_handle_noshift: ql.YieldTermStructureHandle
        self._yc_handle: ql.YieldTermStructureHandle
        self.__yc_proxy = ql.RelinkableYieldTermStructureHandle()
        self._rho_scenarios: list[str]
        self._rho_scenario_map: dict[str, ql.SimpleQuote]
        self._shift_in_bp: float = float('NaN')

    def _post_init(self) -> None:
        rho_dates: dict[ql.Date, str] = {add_tenor(self._valuation_date, scenario, self._rho_calendar,
                                                   self._rho_business_convention, 0): str(scenario)
                                         for scenario in self._rho_scenarios_raw}
        rho_dates[self._valuation_date] = result_items.Rho if not rho_dates else '0D'
        if self._enable_extrapolation:
            self._yc_handle_noshift.enableExtrapolation()
        else:
            self._yc_handle_noshift.disableExtrapolation()
            for date in list(rho_dates):
                try:
                    self._yc_handle_noshift.discount(date)
                except RuntimeError as exception:
                    if 'is past max curve time' not in str(exception):
                        raise exception
                    rho_dates.pop(date)
        spreads: list[ql.Quote] = [ql.SimpleQuote(0.0) for __ in range(len(rho_dates))]
        quotes: list[ql.QuoteHandle] = [ql.QuoteHandle(quote) for quote in spreads]
        self._rho_scenarios = [rho_dates[date] for date in sorted(rho_dates)]
        self._rho_scenario_map = {tenor: spreads[count] for count, tenor in enumerate(self._rho_scenarios)}
        if self._yc_handle_noshift.maxDate() not in rho_dates:
            rho_dates[self._yc_handle_noshift.maxDate()] = 'MAXDATE'
            spreads.append(spreads[-1])
            quotes.append(quotes[-1])
        if len(spreads) == 1:
            rho_dates[ql.Date(30, 12, 2099)] = 'Dummy'
            quotes.append(quotes[0])

        self.__yc_proxy.linkTo(self._yc_handle_noshift.currentLink())
        # SWIGs\termstructures.i
        # SpreadedLinearZeroInterpolatedTermStructure  --> None
        #       curveHandle     Handle<YieldTermStructure>
        #       spreadHandles   vector<Handle<Quote>>
        #       dates           vector<Date>
        #       comp            Compounding         (QuantLib::Continuous)
        #       freq            Frequency           (QuantLib::NoFrequency)
        #       dc              DayCounter          (DayCounter())
        #       factory         Interpolator        (Linear)
        rho_curve: ql.YieldTermStructure = ql.SpreadedLinearZeroInterpolatedTermStructure(self.__yc_proxy,
                                                                                          quotes, sorted(rho_dates))
        rho_curve.enableExtrapolation()
        self._yc_handle = ql.YieldTermStructureHandle(rho_curve)
        self._yc_handle.enableExtrapolation()
        if self._enable_extrapolation:
            self._yc_handle.enableExtrapolation()
        else:
            self._yc_handle.disableExtrapolation()

    @QLMarketData.static
    def _get_discount_curve_from_handle(self, dates: list[ql.Date], handle: ql.YieldTermStructureHandle) -> ql.DiscountCurve:
        discount_factors: list[float] = [handle.discount(date) for date in dates]
        return ql.DiscountCurve(
            dates, discount_factors, self._daycount, self._calendar
        )

    def get_discount_curve(self, dates: list[ql.Date]) -> ql.DiscountCurve:
        return self._get_discount_curve_from_handle(dates, self.base_curve_handle)

    def get_discount_curve_risk_free(self, dates: list[ql.Date]) -> ql.DiscountCurve:
        return self._get_discount_curve_from_handle(dates, self.base_curve_handle_risk_free)

    @QLObject.static
    def __getitem__(self, date: Union[ql.Date, float]) -> float:
        if date <= self._valuation_date:
            return 1.0
        return self._yc_handle.discount(date)          # type: ignore[no-any-return]

    def zero_rate(self, date: ql.Date, daycount: ql.DayCounter, compounding: str = 'Continuous',
                  frequency: Period = Period(1, 'Y')) -> float:
        # SWIGs\termstructures.i
        # YieldTermStructure (TermStructure)
        # 	zeroRate --> InterestRate
        # 		d	Date
        # 		[UNKNOWN]	DayCounter
        # 		[UNKNOWN]	Compounding
        # 		f	Frequency		(Annual)
        compounding_ql: QLCompounding = Compounding[compounding]  # type: ignore[assignment]  # pylint: disable=unsubscriptable-object
        frequency_ql: QLFrequency = Frequencies[frequency]                # type: ignore[assignment]
        if date <= self._valuation_date:
            raise ProgrammingError('Zero rates for the past do not make sense!')
        return self._yc_handle.zeroRate(date, daycount, compounding_ql, frequency_ql).rate()  # type: ignore[no-any-return]

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        return self._rho_scenarios

    def _change_to(self, scenario: str, shift: float) -> None:            # pylint: disable=arguments-differ
        self._shift_in_bp = shift
        self._rho_scenario_map[scenario].setValue(shift / self.shift_unit)

    def _change_back(self, scenario: str) -> None:
        self._rho_scenario_map[scenario].setValue(0.0)

    def _market_shift(self, sub_market_data: QLMarketData) -> None:
        assert isinstance(sub_market_data, QLYieldCurve)
        self.__yc_proxy.linkTo(sub_market_data.base_curve_handle.currentLink())

    def _shift_back(self) -> None:
        self.__yc_proxy.linkTo(self._yc_handle_noshift.currentLink())

    def generate_discount_curve(self, dates: list[datetime.date]) -> Storage:
        result_dates: list[datetime.date] = []
        result_dfs: list[float] = []
        for date in sorted(dates):
            try:
                result_dfs.append(self[date2qldate(date)])
                result_dates.append(date)
            except Exception:       # pylint: disable=broad-except
                pass
        result: Storage = Storage()
        result[fields.Id] = self._id
        result[fields.Type] = self.object_type
        result[fields.SubType(self.object_type)] = 'Discount'
        result[fields.Currency] = self._currency.reference
        result[fields.Dates] = tuple(result_dates)
        result[fields.Values] = tuple(result_dfs)
        result.make_immutable()
        return result

    def evaluate(self, fixing_date: ql.Date, optional_info: str) -> dict[str, Any]:
        assert optional_info == ''
        data: dict[str, Any] = {
            fields.Currency.key: self._currency.id[:3],
            'discountFactor': self[fixing_date]
        }
        return data
