from __future__ import annotations

from typing import Any, Optional

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from daa_utils.daalogging import Log
from valuation.engine import QLObject
from valuation.engine.check import Currency, Differs, IsOrdered, Length, ObjectType, OneNotNone, Range
from valuation.engine.defaults import calendar, daycount, settlement_days_fx
from valuation.engine.exceptions import DAARuntimeException, QLInputError
from valuation.engine.mappings import InterpolatorType, QLInterpolator, QLInterpolatorType
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import add_tenor
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.universal_output import result_items
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLFXRateBase(QLMarketData):   # pylint: disable=abstract-method

    @property
    def base_currency(self) -> QLCurrency:
        return self._base_currency

    @property
    def quote_currency(self) -> QLCurrency:
        return self._quote_currency

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._base_currency: QLCurrency
        self._quote_currency: QLCurrency

    def get(self, date: ql.Date, base_currency: QLCurrency, quote_currency: QLCurrency) -> float:
        rate: float = self[date]
        if quote_currency.ql_currency == self.quote_currency.ql_currency and base_currency.ql_currency == self.base_currency.ql_currency:
            return rate
        if quote_currency.ql_currency == self.base_currency.ql_currency and base_currency.ql_currency == self.quote_currency.ql_currency:
            return 1 / rate
        raise QLInputError('FxRate does not match ' + base_currency.id + '|' + quote_currency.id)

    def evaluate(self, fixing_date: ql.Date, optional_info: str) -> dict[str, Any]:
        if optional_info == self.base_currency.id[:3]:
            data: dict[str, Any] = {
                fields.BaseCurrency.key: self.base_currency.id[:3],
                fields.QuoteCurrency.key: self.quote_currency.id[:3],
                'rate': self[fixing_date]
            }
        elif optional_info == self.quote_currency.id[:3]:
            data: dict[str, Any] = {
                fields.BaseCurrency.key: self.quote_currency.id[:3],
                fields.QuoteCurrency.key: self.base_currency.id[:3],
                'rate': 1.0 / self[fixing_date]
            }
        else:
            raise QLInputError(f'Optional info {optional_info} does not match either currencies{self.base_currency.id[:3]} or {self.quote_currency.id[:3]}')
        return data


class QLFXRateNoForward(QLFXRateBase):
    _signature = signatures.fx_rate.no_forward
    _supported_greeks = (result_items.Delta,)
    _initializes_past = False

    @property
    def scenario_divisor(self) -> float:
        return (self._scenario_modifier - 1.0) * self.shift_unit * self._spot_for_greek

    @property
    def shift_unit(self) -> int:
        return 100

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_currency: QLCurrency = self.data(fields.BaseCurrency, check=ObjectType(signatures.currency.all))
        self._quote_currency: QLCurrency = self.data(fields.QuoteCurrency, check=[Differs(self._base_currency), ObjectType(signatures.currency.all)])

        self._scenario_modifier: float = 1.0
        self._spot_for_greek: float = float('NaN')

    # Reminder: EUR/USD
    # EUR: Base CCY
    # USD: Quote CCY
    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date <= self._valuation_date:
            return self._quote_currency.fx_rate(self._base_currency, date)
        raise QLInputError('In order to get the FX-Forward, a base and quote curve need to be given!')

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Delta:
            return [result_items.Delta]
        raise ProgrammingError(f'Unsupported greek {greek}')

    def _change_to(self, scenario: str, shift: float) -> None:
        self._spot_for_greek = self[self.valuation_date]
        if scenario != result_items.Delta:
            raise ProgrammingError(f'Unsupported scenario {scenario}')
        if shift <= -self.shift_unit:
            raise DAARuntimeException(f'Greek/Range calc: Negative {shift = } leads to nonpositive fx spot rate')
        self._scenario_modifier = 1.0 + shift / self.shift_unit

    def _change_back(self, scenario: str) -> None:  # pylint: disable=unused-argument
        self._scenario_modifier = 1.0
        self._spot_for_greek = float('NaN')


class QLFXRate(QLFXRateNoForward):
    _signature = signatures.fx_rate.standard
    _supported_greeks = (result_items.Delta,)
    _initializes_past = False

    @property
    def base_curve(self) -> QLYieldCurve:
        return self._base_curve

    @property
    def quote_curve(self) -> QLYieldCurve:
        return self._quote_curve

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_curve: QLYieldCurve = self.data(fields.BaseCurve, check=[Currency(self._base_currency), ObjectType(signatures.yield_curve.all)])
        self._quote_curve: QLYieldCurve = self.data(fields.QuoteCurve, check=[Currency(self._quote_currency), ObjectType(signatures.yield_curve.all)])

        self._calendar = self.data(fields.Calendar, default_value=self._quote_curve.calendar)
        self._daycount = self.data(fields.DayCount, default_value=self._quote_curve.daycount)

    # Reminder: EUR/USD
    # EUR: Base CCY
    # USD: Quote CCY
    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date <= self._valuation_date:
            fx_rate: float = self._quote_currency.fx_rate(self._base_currency, date)
        else:
            fx_rate = self._quote_currency.fx_rate(self._base_currency, self._valuation_date) * self._base_curve[date] / self._quote_curve[date]
        if date >= self._valuation_date:
            return fx_rate * self._scenario_modifier
        return fx_rate


class QLFXRateDirectParity(QLFXRate):                     # pylint: disable=abstract-method
    _signature = signatures.fx_rate.direct_parity
    _initializes_past = True

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date <= self._valuation_date:
            fx_rate: float = QLMarketData.__getitem__(self, date)
        else:
            fx_rate = QLMarketData.__getitem__(self, self.valuation_date) * self._base_curve[date] / self._quote_curve[date]
        if date >= self._valuation_date:
            return fx_rate * self._scenario_modifier
        return fx_rate


class QLFXRateDirectNoForward(QLFXRateNoForward):                     # pylint: disable=abstract-method
    _signature = signatures.fx_rate.direct_spot
    _initializes_past = True

    # Reminder: EUR/USD
    # EUR: Base CCY
    # USD: Quote CCY
    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date > self._valuation_date:
            raise QLInputError('Object does not provide values for the future')
        return QLMarketData.__getitem__(self, date)


class QLFXRateDirect(QLFXRateDirectNoForward):                     # pylint: disable=abstract-method
    _signature = signatures.fx_rate.direct

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        # Relevant for parsers only
        trade_date: ql.Date = self.data(
            fields.TradeDate,
            default_value=self._valuation_date
        )

        allow_date_mismatch: bool = self.data(
            fields.AllowTradeDateMismatch,
            allow_fallback_to_default_parameters=True,
            default_value=False
        )
        if self._valuation_date != trade_date:
            if not allow_date_mismatch:
                raise QLInputError(f'Trade / Valuation Date mismatch: {trade_date} / {self._valuation_date}')
            Log.warning(f'TRADE / VALUATION DATE MISMATCH: {trade_date} / {self._valuation_date}')

        self._settlement_days: int = self.data(
            fields.SettlementDays,
            default_value=settlement_days_fx(self._quote_currency.id, self._base_currency.id)
        )
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=calendar(self._quote_currency.id))

        dates: Optional[list[ql.Date]] = self.data(
            fields.Dates,
            default_value=None
        )
        tenors: Optional[list[Period]] = self.data(
            fields.Tenors,
            check=OneNotNone(dates),
            default_value=None
        )

        values: list[float] = self.data(fields.Values)

        if dates:
            self.check(dates, Range(lower=self._valuation_date, strict=False))
            self.check(dates, IsOrdered())
            self.check(values, Length(dates))
            if self._documentation_mode:
                self.check(tenors, IsOrdered())
                self.check(values, Length(tenors))  # type: ignore[arg-type]
        else:
            self.check(tenors, IsOrdered())
            self.check(values, Length(tenors))  # type: ignore[arg-type]

        self._interpolator_class: QLInterpolatorType = self.data(
            fields.InterpolationType,
            ql_map=InterpolatorType,
            default_value='LinearInterpolation'
        )
        self._enable_extrapolation: bool = self.data(fields.EnableExtrapolation, default_value=True)

        # only needed for financial program!
        self._daycount = self.data(fields.DayCount, default_value=daycount(self._quote_currency.id))

        self._forward_dates: list[ql.Date] = []
        self._forward_values: list[float] = []
        self._interpolator: QLInterpolator

        if not self._documentation_mode:
            self._initialize_forwards(dates, tenors, values)

    def _initialize_forwards(self, dates: Optional[list[ql.Date]], tenors: Optional[list[Period]], values: list[float]) -> None:
        if not values:
            raise QLInputError(f'No values given: {values}')
        if dates is not None:
            self._forward_dates = dates
            self._forward_values = values
        elif tenors is not None:
            current_date: ql.Date = self._valuation_date
            current_tenor: Period = tenors[0]
            current_value: float = values[0]
            for tenor, value in zip(tenors, values):
                new_date = add_tenor(self._valuation_date, tenor, self._calendar, ql.Following, self._settlement_days)
                if new_date == current_date and tenor.short_term != 'SPOT':
                    Log.warning(f'{self.reference}: Already given: {current_date}, Value: {current_value} from Tenor: {current_tenor.short_term}; skipping Tenor: {tenor.short_term}, Value: {value}')
                    continue
                current_date = new_date
                current_tenor = tenor
                current_value = value
                self._forward_dates.append(new_date)
                self._forward_values.append(value)
        else:
            raise QLInputError(f'Missing {fields.Tenors} or {fields.Dates}')

    def _post_init(self) -> None:
        if self._valuation_date not in self._forward_dates:
            self._forward_dates.insert(0, self._valuation_date)
            self._forward_values.insert(0, QLMarketData.__getitem__(self, self._valuation_date))
        # Interface see mappings.py/InterpolatorType
        self._interpolator = self._interpolator_class(
            [float(date.serialNumber()) for date in self._forward_dates],
            self._forward_values)

    @QLMarketData.moves_to_shifted
    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date >= self._valuation_date:
            fx_rate: float = self._interpolator(float(date.serialNumber()), self._enable_extrapolation) * self._scenario_modifier
        else:
            fx_rate = QLMarketData.__getitem__(self, date)
        return fx_rate


class QLFXTriangle(QLFXRateBase):       # pylint: disable=abstract-method
    _signature = signatures.fx_rate.triangle

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_rate: QLFXRateNoForward = self.data(fields.BaseRate, check=ObjectType(signatures.fx_rate.all))
        self._quote_rate: QLFXRateNoForward = self.data(fields.QuoteRate, check=ObjectType(signatures.fx_rate.all))
        self._triangle_currency: QLCurrency
        self._base_currency: QLCurrency
        self._quote_currency: QLCurrency

    def _post_init(self) -> None:
        first_pair: set[QLCurrency] = {self._base_rate.base_currency, self._base_rate.quote_currency}
        second_pair: set[QLCurrency] = {self._quote_rate.base_currency, self._quote_rate.quote_currency}

        match = first_pair.intersection(second_pair)
        if len(match) != 1:
            raise QLInputError('FxRates do not match')
        self._triangle_currency = list(match)[0]
        self._base_currency = list(first_pair - match)[0]
        self._quote_currency = list(second_pair - match)[0]

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        return self._base_rate.get(date, self._base_currency, self._triangle_currency) * self._quote_rate.get(date, self._triangle_currency, self._quote_currency)
