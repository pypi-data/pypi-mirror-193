from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import Period
from valuation.engine import QLObjectDB
from valuation.engine.check import ObjectType
from valuation.engine.mappings import InterpolatorType, QLInterpolatorType, QLCompounding, QLFrequency, Compounding, Frequencies
from valuation.engine.market_data import QLMarketData, QLYieldCurve

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import DefaultParameters, Storage


class QLInterpolatedZSpread(QLYieldCurve):  # pylint: disable=abstract-method, invalid-name
    _signature = signatures.yield_curve.z_spread_interpolated

    @property
    def is_base_curve(self) -> bool:
        return False

    @property
    def base_curve_handle(self) -> ql.YieldTermStructureHandle:
        return self._base_curve.handle

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._spread_curve: QLMarketData = self.data(fields.SpreadCurve, check=ObjectType(signatures.z_spread_collection), exclude_from_greeks=True)
        self._base_curve: QLYieldCurve = self._spread_curve.base_curve  # type: ignore[attr-defined]
        self._interpolator_class: QLInterpolatorType = self.data(fields.InterpolationType, ql_map=InterpolatorType, default_value='LinearInterpolation')

        self._currency = self.data(fields.Currency, default_value=self._base_curve.currency, check=ObjectType(signatures.currency.all))
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=self._base_curve.daycount, allow_fallback_to_default_parameters=True)

        self._compounding: QLCompounding = self.data(fields.Compounding, default_value='Continuous', ql_map=Compounding,
                                                     allow_fallback_to_default_parameters=True)
        self._frequency: QLFrequency = self.data(fields.Frequency, default_value=Period(1, 'Y'), ql_map=Frequencies)

        self._additive_factor: float = self.data(fields.AdditiveFactor, default_value=.0)
        self._maturity: ql.Date = self.data(fields.Maturity)

    def _post_init(self) -> None:
        dates: list[ql.Date]
        spreads: list[float]
        dates, spreads = self._spread_curve.curve_data  # type: ignore[attr-defined]
        if dates[0] > self.valuation_date:
            dates = [self.valuation_date] + dates
            spreads = [spreads[0]] + spreads
        if not self._enable_extrapolation and dates[-1] < self._base_curve.handle.maxDate():
            dates = dates + [self._base_curve.handle.maxDate()]
            spreads = spreads + [spreads[-1]]
        if self._maturity < dates[0]:
            interpolated_spread: float = 0.0
        else:
            interpolator = self._interpolator_class([float(date.serialNumber()) for date in dates], spreads)
            interpolated_spread: float = interpolator(float(self._maturity.serialNumber()), self._enable_extrapolation) + self._additive_factor
        interpolated_spreads: list[ql.QuoteHandle] = [ql.QuoteHandle(ql.SimpleQuote(interpolated_spread)),
                                                      ql.QuoteHandle(ql.SimpleQuote(interpolated_spread))]
        curve_dates: list[ql.Date] = [self._valuation_date, min(self._base_curve.handle.maxDate(), max(dates))]

        # SWIGs\termstructures.i
        # SpreadedLinearZeroInterpolatedTermStructure  --> None
        #       curveHandle     Handle<YieldTermStructure>
        #       spreadHandles   vector<Handle<Quote>>
        #       dates           vector<Date>
        #       comp            Compounding         (QuantLib::Continuous)
        #       freq            Frequency           (QuantLib::NoFrequency)
        #       dc              DayCounter          (DayCounter())
        #       factory         Interpolator        (Linear)
        yield_curve: ql.YieldTermStructure = ql.SpreadedLinearZeroInterpolatedTermStructure(self._base_curve.handle, interpolated_spreads, curve_dates, ql.Compounded, ql.Annual)
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()
