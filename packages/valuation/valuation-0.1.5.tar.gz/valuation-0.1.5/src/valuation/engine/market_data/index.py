from __future__ import annotations

import datetime
from typing import Any

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.engine import QLAlias, QLObject
from valuation.engine import defaults
from valuation.engine.check import Currency, ObjectType
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import add_tenor, period2qlperiod
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.engine.mappings import QLBusiness
    from valuation.universal_transfer import DefaultParameters, Storage


class QLIRIndexAlias(QLAlias):
    _signature = signatures.ir_index.alias


class QLInterestRateIndex(QLMarketData):  # pylint: disable=abstract-method
    _signature = signatures.ir_index.base

    @property
    def ql_index(self) -> ql.IborIndex:
        return self._index

    @property
    def is_overnight_index(self) -> bool:
        return self._tenor == Period(1, 'D')

    @property
    def yield_curve(self) -> QLYieldCurve:
        return self._yield_curve  # type: ignore[no-any-return]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency: QLCurrency = self.data(fields.Currency, check=ObjectType(signatures.currency.all), ignore_data_only_mode=True)
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)
        self._tenor: Period = self.data(fields.Tenor)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True, default_value=defaults.daycount(self._currency.id))
        self._business: QLBusiness = self.data(fields.Business, allow_fallback_to_default_parameters=True, default_value=defaults.business(self._currency.id))
        self._settlement_days: int = self.data(fields.SettlementDays, allow_fallback_to_default_parameters=True, default_value=defaults.settlement_days(self._currency.id, self._tenor))

        self._yield_curve = self.data(fields.DiscountCurve, check=[Currency(self._currency), ObjectType(signatures.yield_curve.all)])  # noqa: E225

        self._index: ql.IborIndex
        if self._documentation_mode:
            return
        self._set_index()

    def _set_index(self) -> None:
        index_name: str = self.reference.id + '_' + datetime.datetime.now().isoformat()
        if self._data_only_mode:
            yield_curve_handle = ql.YieldTermStructureHandle()
            index_name += '_safe'
            currency: ql.Currency = ql.DEMCurrency()
        else:
            yield_curve_handle = self._yield_curve.handle
            currency = self._currency.ql_currency
        if self._tenor == Period(1, 'D'):
            # SWIGs\indexes.i
            # OvernightIndex (IborIndex) --> None
            # 		familyName	string
            # 		settlementDays	Integer
            # 		currency	Currency
            # 		calendar	Calendar
            # 		dayCounter	DayCounter
            # 		h	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            self._index = ql.OvernightIndex(index_name, self._settlement_days, currency, self._calendar, self._daycount, yield_curve_handle)
        else:
            # SWIGs\indexes.i
            # IborIndex (InterestRateIndex) --> None
            # 		familyName	string
            # 		tenor	Period
            # 		settlementDays	Integer
            # 		currency	Currency
            # 		calendar	Calendar
            # 		convention	BusinessDayConvention
            # 		endOfMonth	bool
            # 		dayCounter	DayCounter
            # 		h	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            period = period2qlperiod(self._tenor)
            self._index = ql.IborIndex(index_name, period, self._settlement_days, currency, self._calendar, self._business, False, self._daycount, yield_curve_handle)

    def _post_init(self) -> None:
        for date, rate in self._fixings.items():
            if not self._calendar.isHoliday(date):
                self._index.addFixing(date, rate)

    def has_fixing(self, date: ql.Date) -> bool:  # TODO : consider market data as a dictionary and change this to __in__
        if self._index.hasHistoricalFixing(date):
            return True
        return super().has_fixing(date)

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date <= self._valuation_date:
            rate = super().__getitem__(date)
            if not self._calendar.isHoliday(date):
                self._index.addFixing(date, rate)
        else:
            fwd_date = add_tenor(date, self._tenor, self._calendar, self._business, 0)
            rate = self._yield_curve.handle.forwardRate(date, fwd_date, self._daycount, ql.Simple).rate()
        return rate

    def evaluate(self, fixing_date: ql.Date, optional_info: str) -> dict[str, Any]:
        assert optional_info == ''
        data: dict[str, Any] = {
            fields.Currency.key: self._currency.id[:3],
            fields.Tenor.key: str(self._tenor),
            'Rate': self[fixing_date]
        }
        return data
