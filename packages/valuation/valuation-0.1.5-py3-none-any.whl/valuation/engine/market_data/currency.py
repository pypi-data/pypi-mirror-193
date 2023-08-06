from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import QLAlias, QLObject
from valuation.engine.check import Range
from valuation.engine.mappings import Currencies
from valuation.engine.market_data import QLMarketData

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


# The rate given via 'Fixing' is always relative to the Currency|Standard
class QLCurrency(QLMarketData):                 # pylint: disable=abstract-method
    _signature = signatures.currency.variable
    _additional_fixing_checks = [Range(lower=0.0)]

    @property
    def ql_currency(self) -> ql.Currency:
        return self._currency

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._currency = self.data(fields.CurrencyName, default_value=self.id[:3], ql_map=Currencies)
        self._calendar = self.data(fields.Calendar, default_value=self.id[:3])

    # Reminder: EUR/USD
    # EUR: Base CCY
    # USD: Quote CCY
    @QLObject.static
    def fx_rate(self, base_currency: QLCurrency, date: ql.Date) -> float:
        return self[date] / base_currency[date]


class QLCurrencyStandard(QLCurrency):           # pylint: disable=abstract-method
    _signature = signatures.currency.standard
    _initializes_past = False

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        return 1.0


class QLCurrencyAlias(QLAlias):
    _signature = signatures.currency.alias
