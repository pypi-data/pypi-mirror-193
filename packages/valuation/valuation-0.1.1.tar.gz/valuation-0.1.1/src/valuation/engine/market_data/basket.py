from __future__ import annotations

from typing import Optional

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import QLObject
from valuation.engine.market_data import QLCurrency, QLMarketData, QLYieldCurve

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.utils import StockDividends
    from valuation.universal_transfer import DefaultParameters, Storage


class QLMarketDataBasket(QLMarketData):                 # pylint: disable=abstract-method
    _signature = signatures.market_data_basket
    _initializes_past = False

    @property
    def sub_market_data(self) -> list[QLMarketData]:
        return self._sub_market_data

    @property
    def stock_dividends(self) -> list[Optional[StockDividends]]:
        result: list[Optional[StockDividends]] = []
        for market_data in self._sub_market_data:
            try:
                result.append(market_data.stock_dividends)  # type: ignore[attr-defined]
            except:  # pylint: disable=bare-except   # noqa: E722
                result.append(None)
        return result

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._sub_market_data: list[QLMarketData] = self.data(fields.MarketDataBasket)
        self._daycount = self.data(fields.DayCount, default_value=self._sub_market_data[0].daycount)
        self._calendar = self.data(fields.Calendar, default_value=self._sub_market_data[0].calendar)

    def _post_init(self) -> None:
        for sub_market_data in self._sub_market_data:
            self._market_data_objects.add(sub_market_data)

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> dict[str, float]:       # type: ignore[override]
        return {sub_market_data.id: sub_market_data[date] for sub_market_data in self._sub_market_data}


# The following class should just be generated automatically, a generation manually is not intended.
# _sub_market_data[0] : InterestRateIndex
# _sub_market_data[1] : CMSIndex based on the InterestRateIndex
class QLIndexAndCMSVIRTUAL(QLMarketDataBasket):     # pylint: disable=abstract-method
    _signature = signatures.index_and_cms

    @property
    def currency(self) -> QLCurrency:
        return self._sub_market_data[0].currency

    @property
    def yield_curve(self) -> QLYieldCurve:
        return self._sub_market_data[0].yield_curve  # type: ignore[no-any-return, attr-defined]


# The following class should just be generated automatically, a generation manually is not intended.
# _sub_market_data[0] : InterestRateIndex
# _sub_market_data[1] : CMSIndex based on the InterestRateIndex (short)
# _sub_market_data[2] : CMSIndex based on the InterestRateIndex (long)
# Though being currently identical to the upper class, it seems sensible to keep the two apart.
class QLIndexAndCMSSpreadVIRTUAL(QLMarketDataBasket):     # pylint: disable=abstract-method
    _signature = signatures.index_and_cms_spread

    @property
    def currency(self) -> QLCurrency:
        return self._sub_market_data[0].currency

    @property
    def yield_curve(self) -> QLYieldCurve:
        return self._sub_market_data[0].yield_curve  # type: ignore[no-any-return, attr-defined]
