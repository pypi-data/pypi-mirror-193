from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Equals, IsOrdered, Length, ObjectType, Range
from valuation.engine.mappings import Compounding, Frequencies, QLCompounding, QLFrequency
from valuation.engine.market_data import QLYieldCurve
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency
    from valuation.universal_transfer import DefaultParameters, Storage


class QLSpreadCurveBase(QLYieldCurve):                  # pylint: disable=abstract-method

    @property
    def is_base_curve(self) -> bool:
        return False

    @property
    def base_curve_handle_risk_free(self) -> ql.YieldTermStructureHandle:
        return self._base_curve.base_curve_handle_risk_free

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_curve: QLYieldCurve = self.data(fields.BaseCurve, check=ObjectType(signatures.yield_curve.all))
        self._curve_dates: list[ql.Date] = self.data(fields.Dates,
                                                     check=[Range(lower=self._valuation_date, strict=False),
                                                            IsOrdered()])
        self._spreads: list[float] = self.data(fields.Values, check=[Range(lower=global_parameters.InterestRateMinimum,
                                                                           upper=global_parameters.InterestRateMaximum),
                                                                     Length(self._curve_dates)])
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=self._base_curve.daycount,
                                                  allow_fallback_to_default_parameters=True)
        self._compounding: QLCompounding = self.data(fields.Compounding, default_value='Continuous', ql_map=Compounding, allow_fallback_to_default_parameters=True)
        self._frequency: QLFrequency = self.data(fields.Frequency, default_value=Period(1, 'Y'), ql_map=Frequencies)

    def _post_init(self) -> None:
        spreads: list[ql.QuoteHandle] = [ql.QuoteHandle(ql.SimpleQuote(spread)) for spread in self._spreads]
        # SWIGs\termstructures.i
        # SpreadedLinearZeroInterpolatedTermStructure  --> None
        #       curveHandle     Handle<YieldTermStructure>
        #       spreadHandles   vector<Handle<Quote>>
        #       dates           vector<Date>
        #       comp            Compounding         (QuantLib::Continuous)
        #       freq            Frequency           (QuantLib::NoFrequency)
        #       dc              DayCounter          (DayCounter())
        #       factory         Interpolator        (Linear)
        yield_curve: ql.YieldTermStructure = ql.SpreadedLinearZeroInterpolatedTermStructure(self._base_curve.handle,
                                                                                            spreads,
                                                                                            self._curve_dates,
                                                                                            self._compounding,
                                                                                            self._frequency,
                                                                                            self._daycount)
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()


class QLConstantSpreadCurve(QLYieldCurve):                  # pylint: disable=abstract-method
    _signature = signatures.yield_curve.constant_spread

    @property
    def is_base_curve(self) -> bool:
        return False

    @property
    def base_curve_handle_risk_free(self) -> ql.YieldTermStructureHandle:
        return self._base_curve.base_curve_handle_risk_free

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_curve: QLYieldCurve = self.data(fields.BaseCurve, check=ObjectType(signatures.yield_curve.all))
        self._spread: float = self.data(fields.Value, check=Range(lower=global_parameters.InterestRateMinimum,
                                                                  upper=global_parameters.InterestRateMaximum))
        self._currency = self.data(fields.Currency, default_value=self._base_curve.currency,
                                   check=ObjectType(signatures.currency.all))
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=self._base_curve.daycount,
                                                  allow_fallback_to_default_parameters=True)
        self._compounding: QLCompounding = self.data(fields.Compounding, default_value='Continuous', ql_map=Compounding, allow_fallback_to_default_parameters=True)
        self._frequency: QLFrequency = self.data(fields.Frequency, default_value=Period(1, 'Y'), ql_map=Frequencies)

    def _post_init(self) -> None:
        spread: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._spread))
        # SWIGs\termstructures.i
        # ZeroSpreadedTermStructure  --> None
        #       curveHandle     Handle<YieldTermStructure>
        #       spreadHandle    Handle<Quote>
        #       comp            Compounding         (QuantLib::Continuous)
        #       freq            Frequency           (QuantLib::NoFrequency)
        #       dc              DayCounter          (DayCounter())
        yield_curve: ql.YieldTermStructure = ql.ZeroSpreadedTermStructure(self._base_curve.handle, spread,
                                                                          self._compounding, self._frequency,
                                                                          self._daycount)
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()


class QLSpreadCurve(QLSpreadCurveBase):
    _signature = signatures.yield_curve.spread

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency = self._base_curve.currency
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)


class QLCrossCurrencySpreadCurve(QLSpreadCurveBase):
    _signature = signatures.yield_curve.cross_currency_spread

    @property
    def base_currency(self) -> QLCurrency:
        return self._base_currency

    @property
    def quote_currency(self) -> QLCurrency:
        return self._quote_currency

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_currency: QLCurrency = self.data(fields.BaseCurrency, check=[ObjectType(signatures.currency.all), Equals(self._base_curve.currency)])
        self._quote_currency: QLCurrency = self.data(fields.QuoteCurrency, check=[ObjectType(signatures.currency.all)])
        self._currency = self._base_currency
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)
