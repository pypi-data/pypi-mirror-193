from dataclasses import dataclass

import QuantLib as ql

from daa_utils import Log
from valuation.engine import mappings
from valuation.universal_transfer import NoValue, Period


@dataclass(frozen=True)
class DefaultContainer:
    daycount: str
    business: str
    calendar: str
    settlement_days: int


@dataclass(frozen=True)
class DefaultSet:
    fixed: DefaultContainer
    floating: DefaultContainer


_data: dict[str, DefaultSet] = {
    'EUR': DefaultSet(fixed=DefaultContainer("E30/360", "Modified Following", "EUR", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "EUR", 2)),
    'GBP': DefaultSet(fixed=DefaultContainer("ACT/365", "Modified Following", "GBP", 0),
                      floating=DefaultContainer("ACT/365", "Modified Following", "GBP", 0)),
    'USD': DefaultSet(fixed=DefaultContainer("30I/360", "Modified Following", "USD", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "USD", 2)),
    'JPY': DefaultSet(fixed=DefaultContainer("ACT/365", "Modified Following", "JPY", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "JPY", 2)),
    'CAD': DefaultSet(fixed=DefaultContainer("ACT/365", "Modified Following", "CAD", 0),
                      floating=DefaultContainer("ACT/365", "Modified Following", "CAD", 0)),
    'AUD': DefaultSet(fixed=DefaultContainer("ACT/365", "Modified Following", "AUD", 2),
                      floating=DefaultContainer("ACT/365", "Modified Following", "AUD", 2)),
    'CHF': DefaultSet(fixed=DefaultContainer("ACT/360", "Modified Following", "CHF", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "CHF", 2)),
    'NZD': DefaultSet(fixed=DefaultContainer("ACT/365", "Modified Following", "NZD", 0),
                      floating=DefaultContainer("ACT/365", "Modified Following", "NZD", 0)),
    'DKK': DefaultSet(fixed=DefaultContainer("30/360", "Modified Following", "DKK", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "DKK", 2)),
    'SEK': DefaultSet(fixed=DefaultContainer("30/360", "Modified Following", "SEK", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "SEK", 2)),
    'NOK': DefaultSet(fixed=DefaultContainer("30/360", "Modified Following", "NOK", 2),
                      floating=DefaultContainer("ACT/360", "Modified Following", "NOK", 2)),
    'RUB': DefaultSet(fixed=DefaultContainer("ACT/ACT", "Modified Following", "RUB", 1),
                      floating=DefaultContainer("ACT/ACT", "Modified Following", "RUB", 1))
}
_fallback_default: DefaultSet = _data['EUR']


def _fetch_by_currency(currency: str, coupon_type: str, allow_fallback: bool) -> DefaultContainer:
    assert coupon_type in {'fixed', 'floating'}
    if not allow_fallback and currency not in _data:
        Log.info(f"Currency '{currency}' has no default conventions defined")  # TODO: check code later, allow_fallback is useless with this fix
        # raise QLInputError(f"Currency '{currency}' has no default conventions defined")
    default_set = _data.get(currency, _fallback_default)
    if coupon_type == 'fixed':
        return default_set.fixed
    return default_set.floating


def daycount(currency: str, coupon_type: str = 'floating', allow_fallback: bool = True) -> ql.DayCounter:
    if isinstance(currency, NoValue):
        return 'Currency based default'
    _daycount: str = _fetch_by_currency(currency, coupon_type, allow_fallback).daycount
    return mappings.DayCountMap[_daycount]


def business(currency: str, coupon_type: str = 'floating', allow_fallback: bool = True) -> int:
    if isinstance(currency, NoValue):
        return 'Currency based default'
    _business: str = _fetch_by_currency(currency, coupon_type, allow_fallback).business
    return mappings.BusinessMap[_business]


def calendar(currency: str, coupon_type: str = 'floating', allow_fallback: bool = True) -> ql.Calendar:
    if isinstance(currency, NoValue):
        return 'Currency based default'
    _calendar: str = _fetch_by_currency(currency, coupon_type, allow_fallback).calendar
    return mappings.CalendarMap[_calendar]


def settlement_days(currency: str, tenor: Period, coupon_type: str = 'floating', allow_fallback: bool = True) -> int:
    if isinstance(currency, NoValue):
        return 'Currency based default'
    if not tenor or tenor == Period(1, 'D'):
        return 0
    return _fetch_by_currency(
        currency, coupon_type, allow_fallback
    ).settlement_days


def settlement_days_fx(quote_currency: str, base_currency: str) -> int:
    # docs\WebSites\FXConventions\Settlement\Foreign exchange spot - Wikipedia.html
    # docs\WebSites\FXConventions\Settlement\Just Technologies AS.html
    if isinstance(quote_currency, NoValue):
        return 'Currency based default'
    if base_currency == 'USD' and quote_currency in ('CAD', 'TRY', 'PHP', 'RUB'):
        return 1
    return 2
