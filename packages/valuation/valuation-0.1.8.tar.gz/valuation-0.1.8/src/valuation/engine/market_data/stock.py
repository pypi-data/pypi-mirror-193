from __future__ import annotations

from typing import Optional
import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.exceptions import ProgrammingError  # pylint: disable=wrong-import-order
from valuation.global_settings import __type_checking__
from valuation.engine import QLObject
from valuation.engine.check import Length, ObjectType, Range
from valuation.engine.exceptions import DAARuntimeException  # pylint: disable=wrong-import-order
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import StockDividends
from valuation.universal_output import result_items

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage

# TODO(2021/11) Find reason for greeks deviation between FP and Ql in barrier options


class QLStock(QLMarketData):
    _signature = signatures.stock
    _supported_greeks = (result_items.Delta,)

    @property
    def scenario_divisor(self) -> float:
        return (self._scenario_modifier - 1.0) * self.shift_unit * self._spot_for_greek

    @property
    def shift_unit(self) -> int:
        return 100

    @property
    def stock_dividends(self) -> StockDividends:
        return self._stock_dividends

    @property
    def dividend_yield(self) -> float:
        return self._dividend_yield

    @property
    def dividend_yield_handle(self) -> ql.YieldTermStructureHandle:
        return self._dividend_handle

    @property
    def quote_curve(self) -> QLYieldCurve:
        return self._quote_curve

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._quote_curve: QLYieldCurve = self.data(fields.RiskFreeCurve, check=ObjectType(signatures.yield_curve.all))
        self._dividend_yield: float = self.data(fields.ContinuousDividendYield, check=Range(lower=0.0, upper=global_parameters.ContinuousDividendYieldMaximum, strict=False))
        self._currency: QLCurrency = self._quote_curve.currency
        self._calendar = self._quote_curve.calendar
        self._daycount = self._quote_curve.daycount
        dividend_dates: Optional[list[ql.Date]] = self.data(fields.DividendDates, default_value=None)
        if dividend_dates is None:
            dividend_dates = [self.valuation_date]
        dividend_absolute: list[float] = self.data(fields.DividendAbsolute, default_value=None, check=Length(dividend_dates[:-1]))
        dividend_relative: list[float] = self.data(fields.DividendRelative, default_value=None, check=Length(dividend_dates[:-1]))

        if not self._documentation_mode:
            self._stock_dividends = StockDividends(dividend_dates, dividend_absolute, dividend_relative)
            self._dividend_handle: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(
                ql.FlatForward(
                    ql_db.valuation_date,
                    ql.QuoteHandle(
                        ql.SimpleQuote(
                            self._dividend_yield
                        )
                    ),
                    self._daycount
                )
            )

        self._scenario_modifier = 1.0
        self._spot_for_greek: float = float('NaN')

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date < self.valuation_date:
            return super().__getitem__(date)
        value = super().__getitem__(self.valuation_date)
        if date > self.valuation_date:
            value = self.stock_dividends(date, self._stock_dividends.inverse(self.valuation_date, value) / self._quote_curve[date] * self._dividend_handle.discount(date))
        return value * self._scenario_modifier

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Delta:
            return [result_items.Delta]
        raise ProgrammingError(f'Unsupported scenario {greek}')

    def _change_to(self, scenario: str, shift: float) -> None:
        self._spot_for_greek = self[self.valuation_date]
        if scenario != result_items.Delta:
            raise ProgrammingError(f'Unsupported scenario {scenario}')
        if shift <= -self.shift_unit:
            raise DAARuntimeException(f'Greek/Range calc: Negative {shift = } leads to nonpositive spot')
        self._scenario_modifier = 1.0 + shift / self.shift_unit

    def _change_back(self, scenario: str) -> None:      # pylint: disable=unused-argument
        self._scenario_modifier = 1.0
        self._spot_for_greek = float('NaN')
