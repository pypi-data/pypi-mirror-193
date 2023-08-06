from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import IsOrdered, Length, ObjectType, Range
from valuation.engine.market_data import QLMarketData

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLZSpreadCollection(QLMarketData):        # pylint: disable=abstract-method
    """
    This Object carries no functionalities on it's own. It is simply a container for ZSpreads.
    """
    _signature = signatures.z_spread_collection

    @property
    def base_curve(self) -> QLYieldCurve:
        return self._base_curve

    @property
    def curve_data(self) -> tuple[list[ql.Date], list[float]]:
        return self._dates.copy(), self._z_spreads.copy()

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._base_curve: QLYieldCurve = self.data(fields.BaseCurve, check=ObjectType(signatures.yield_curve.all))

        self._currency: QLCurrency = self.data(fields.Currency, default_value=self._base_curve.currency, check=ObjectType(signatures.currency.all))
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=self._base_curve.daycount, allow_fallback_to_default_parameters=True)

        self._dates: list[ql.Date] = self.data(fields.Dates, check=[Range(lower=self._valuation_date, strict=False), IsOrdered()])
        self._z_spreads: list[float] = self.data(fields.Values, check=Length(self._dates))
