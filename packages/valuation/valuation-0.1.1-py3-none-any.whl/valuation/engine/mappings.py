from collections.abc import Mapping
from typing import Callable, Optional, TypeVar, Union, Any, Generator

import QuantLib as ql

from valuation.engine import calendar_loader
from valuation.universal_transfer import NoValue, Period, finance_types

KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')


class AugmentedDict(Mapping[KeyType, ValueType]):
    def __init__(self, data: dict[KeyType, ValueType]) -> None:
        self._data: dict[KeyType, ValueType] = data

    def __iter__(self) -> Generator[KeyType, Any, Any]:
        yield from self._data

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: Union[KeyType, list[KeyType]]) -> Union[ValueType, list[ValueType]]:  # type: ignore[override]
        if isinstance(key, NoValue):
            return key  # type: ignore[return-value]
        if isinstance(key, list):
            return [self._data[entry] for entry in key]  # pylint: disable=unsubscriptable-object
        return self._data[key]  # pylint: disable=no-member, unsubscriptable-object

    def __str__(self) -> str:
        result = [f'{entry}:\t{self[entry]}' for entry in sorted(self)]  # type: ignore[type-var]
        return '\n'.join(result) + '\n'


class LazyDict(Mapping[KeyType, ValueType]):
    def __init__(self, data: dict[KeyType, Union[ValueType, str]], converter: Callable[[str], ValueType]) -> None:
        self._data: dict[KeyType, Union[ValueType, str]] = data
        self._converter: Callable[[str], ValueType] = converter

    def __iter__(self) -> Generator[KeyType, Any, Any]:
        yield from self._data

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: KeyType) -> ValueType:
        value: Union[ValueType, str] = self._data[key]
        if isinstance(value, str):
            value = self._converter(value)
            self._data[key] = value
        return value


DayCountMap: dict[str, ql.DayCounter] = {
    '1/1': ql.OneDayCounter(),
    'ACT/ACT': ql.ActualActual(),
    'ACT/ACT_BOND': ql.ActualActual(ql.ActualActual.Bond),
    'ACT/ACT_ISMA': ql.ActualActual(ql.ActualActual.ISMA),
    'IACT/ACT': ql.ActualActual(ql.ActualActual.ISDA),
    'ACT/360': ql.Actual360(),
    'ACT/364': ql.Actual364(),
    'ACT/365': ql.Actual365Fixed(),
    '30/360': ql.Thirty360(),
    '30U/360': ql.Thirty360(ql.Thirty360.USA),
    'E30/360': ql.Thirty360(ql.Thirty360.European),
    'G30/360': ql.Thirty360(ql.Thirty360.German),
    '30I/360': ql.Thirty360(),
    '30/360_ISDA': ql.Thirty360(ql.Thirty360.ISDA),
    '30/365': ql.Thirty365(),
    'BU/252': ql.Business252()
}
finance_types.DayCounts.register_list(list(DayCountMap.keys()))

CalendarMap: dict[str, ql.Calendar] = LazyDict({  # type: ignore[assignment]
    'EUR': ql.TARGET(),
    'EUR|Finland': ql.Finland(),
    'EUR|Germany': ql.Germany(),
    'EUR|Italy': ql.Italy(),
    'EUR|Slovakia': ql.Slovakia(),
    'EUR|Austria': 'AUSTRIA',
    'EUR|Belgium': 'BELGIUM',
    'EUR|France': 'FRANCE',
    'EUR|Greece': 'GREECE',
    'EUR|Ireland': 'IRELAND',
    'EUR|Luxembourg': 'LUXEMBOURG',
    'EUR|Netherlands': 'NETHERLANDS',
    'EUR|Portugal': 'PORTUGAL',
    'EUR|Spain': 'SPAIN',
    'ARS': ql.Argentina(),
    'AUD': ql.Australia(),
    'BRL': ql.Brazil(),
    'CAD': ql.Canada(),
    'CLP': 'CHILE',
    'CNY': ql.China(),
    'COP': 'COLOMBIA',
    'CZK': ql.CzechRepublic(),
    'DKK': ql.Denmark(),
    'HKD': ql.HongKong(),
    'HRK': 'CROATIA',
    'HUF': ql.Hungary(),
    'ISK': ql.Iceland(),
    'INR': ql.India(),
    'IDR': ql.Indonesia(),
    'ILS': ql.Israel(),
    'JPY': ql.Japan(),
    'MAD': 'MOROCCO',
    'MXN': ql.Mexico(),
    'NZD': ql.NewZealand(),
    'NOK': ql.Norway(),
    'PEN': 'PERU',
    'PLN': ql.Poland(),
    'RUB': ql.Russia(),
    'RON': ql.Romania(),
    'SAR': ql.SaudiArabia(),
    'SGD': ql.Singapore(),
    'ZAR': ql.SouthAfrica(),
    'KRW': ql.SouthKorea(),
    'SEK': ql.Sweden(),
    'CHF': ql.Switzerland(),
    'TWD': ql.Taiwan(),
    'THB': ql.Thailand(),
    'TRY': ql.Turkey(),
    'UAH': ql.Ukraine(),
    'GBP': ql.UnitedKingdom(),
    'USD': ql.UnitedStates(),
    'XAG': ql.UnitedStates(),
    'XAU': ql.UnitedStates(),
    'XPT': ql.UnitedStates(),
    'XPD': ql.UnitedStates(),
    'AngloAmerica': 'ANGLO_AMERICAN',
    'WeekendsOnly': ql.WeekendsOnly()
}, calendar_loader.get_calendar)
finance_types.Calendars.register_list(list(CalendarMap.keys()))

QLBusiness = int

BusinessMap: dict[str, QLBusiness] = {
    'Unadjusted': ql.Unadjusted,
    'Following': ql.Following,
    'Modified Following': ql.ModifiedFollowing,
    'Preceding': ql.Preceding,
    'Modified Preceding': ql.ModifiedPreceding
}
finance_types.BusinessConventions.register_list(list(BusinessMap.keys()))

QLPeriodUnit = int

PeriodUnitMap: dict[str, QLPeriodUnit] = {
    'D': ql.Days,
    'W': ql.Weeks,
    'M': ql.Months,
    'Y': ql.Years
}

Currencies: AugmentedDict[str, ql.Currency] = AugmentedDict({
    'ARS': ql.ARSCurrency(),
    'ATS': ql.ATSCurrency(),
    'AUD': ql.AUDCurrency(),
    'BDT': ql.BDTCurrency(),
    'BEF': ql.BEFCurrency(),
    'BGL': ql.BGLCurrency(),
    'BRL': ql.BRLCurrency(),
    'BYR': ql.BYRCurrency(),
    'CAD': ql.CADCurrency(),
    'CHF': ql.CHFCurrency(),
    'CLP': ql.CLPCurrency(),
    'CNY': ql.CNYCurrency(),
    'COP': ql.COPCurrency(),
    'CYP': ql.CYPCurrency(),
    'CZK': ql.CZKCurrency(),
    'DEM': ql.DEMCurrency(),
    'DKK': ql.DKKCurrency(),
    'EEK': ql.EEKCurrency(),
    'ESP': ql.ESPCurrency(),
    'EUR': ql.EURCurrency(),
    'FIM': ql.FIMCurrency(),
    'FRF': ql.FRFCurrency(),
    'GBP': ql.GBPCurrency(),
    'GRD': ql.GRDCurrency(),
    'HKD': ql.HKDCurrency(),
    'HUF': ql.HUFCurrency(),
    'IDR': ql.IDRCurrency(),
    'IEP': ql.IEPCurrency(),
    'ILS': ql.ILSCurrency(),
    'INR': ql.INRCurrency(),
    'IQD': ql.IQDCurrency(),
    'IRR': ql.IRRCurrency(),
    'ISK': ql.ISKCurrency(),
    'ITL': ql.ITLCurrency(),
    'JPY': ql.JPYCurrency(),
    'KRW': ql.KRWCurrency(),
    'KWD': ql.KWDCurrency(),
    'LTL': ql.LTLCurrency(),
    'LUF': ql.LUFCurrency(),
    'LVL': ql.LVLCurrency(),
    'MTL': ql.MTLCurrency(),
    'MXN': ql.MXNCurrency(),
    'MYR': ql.MYRCurrency(),
    'NLG': ql.NLGCurrency(),
    'NOK': ql.NOKCurrency(),
    'NPR': ql.NPRCurrency(),
    'NZD': ql.NZDCurrency(),
    'PEH': ql.PEHCurrency(),
    'PEI': ql.PEICurrency(),
    'PEN': ql.PENCurrency(),
    'PKR': ql.PKRCurrency(),
    'PLN': ql.PLNCurrency(),
    'PTE': ql.PTECurrency(),
    'ROL': ql.ROLCurrency(),
    'RON': ql.RONCurrency(),
    'RUB': ql.RUBCurrency(),
    'SAR': ql.SARCurrency(),
    'SEK': ql.SEKCurrency(),
    'SGD': ql.SGDCurrency(),
    'SIT': ql.SITCurrency(),
    'SKK': ql.SKKCurrency(),
    'THB': ql.THBCurrency(),
    'TRL': ql.TRLCurrency(),
    'TRY': ql.TRYCurrency(),
    'TTD': ql.TTDCurrency(),
    'TWD': ql.TWDCurrency(),
    'USD': ql.USDCurrency(),
    'VEB': ql.VEBCurrency(),
    'VND': ql.VNDCurrency(),
    'ZAR': ql.ZARCurrency(),
    'XAG': ql.Currency(),  # Silver
    'XAU': ql.Currency(),  # Gold
    'XPT': ql.Currency(),  # Platinum
    'XPD': ql.Currency(),  # Palladium
    'EmptyFallback': ql.Currency()
})
finance_types.Currencies.register_list(list(Currencies.keys()))

QLFrequency = int

Frequencies: AugmentedDict[Period, QLFrequency] = AugmentedDict({
    Period(1, 'D'): ql.Daily,
    Period(1, 'W'): ql.Weekly,
    Period(2, 'W'): ql.Biweekly,
    Period(1, 'M'): ql.Monthly,
    Period(3, 'M'): ql.Quarterly,
    Period(6, 'M'): ql.Semiannual,
    Period(12, 'M'): ql.Annual,
    Period(1, 'Y'): ql.Annual
})

QLCompounding = int

Compounding: AugmentedDict[str, QLCompounding] = AugmentedDict({
    'Simple': ql.Simple,
    'Compounded': ql.Compounded,
    'Continuous': ql.Continuous,
    'SimpleThenCompounded': ql.SimpleThenCompounded,
    'CompoundedThenSimple': ql.CompoundedThenSimple
})

QLDateGeneration = int  # pylint: disable=invalid-name
DateGeneration: AugmentedDict[str, QLDateGeneration] = AugmentedDict({
    'Backward': ql.DateGeneration.Backward,
    'Forward': ql.DateGeneration.Forward,
    'Zero': ql.DateGeneration.Zero,
    'ThirdWednesday': ql.DateGeneration.ThirdWednesday,
    'ThirdWednesdayInclusive': ql.DateGeneration.ThirdWednesdayInclusive,
    'Twentieth': ql.DateGeneration.Twentieth,
    'TwentiethIMM': ql.DateGeneration.TwentiethIMM,
    'OldCDS': ql.DateGeneration.OldCDS,
    'CDS': ql.DateGeneration.CDS,
    'CDS2015': ql.DateGeneration.CDS2015
})

QLVolatilityType = int

VolatilityType: AugmentedDict[str, QLVolatilityType] = AugmentedDict({
    'Normal': ql.Normal,
    'LogNormal': ql.ShiftedLognormal
})

QLSwapPositionType = int

QLSwapPosition: AugmentedDict[str, QLSwapPositionType] = AugmentedDict({
    'Payer': ql.VanillaSwap.Payer,
    'Receiver': ql.VanillaSwap.Receiver
})

QLVanillaOptionType = int

VanillaOptionType: dict[str, QLVanillaOptionType] = {
    'Call': ql.Option.Call,
    'Put': ql.Option.Put
}

QLBarrierOptionType = int
BarrierOptionType: dict[str, QLBarrierOptionType] = {
    'UpIn': ql.Barrier.UpIn,
    'UpOut': ql.Barrier.UpOut,
    'DownIn': ql.Barrier.DownIn,
    'DownOut': ql.Barrier.DownOut,
    'DownInUpIn': ql.DoubleBarrier.KnockIn,
    'DownOutUpOut': ql.DoubleBarrier.KnockOut,
    'DownInUpOut': ql.DoubleBarrier.KIKO,
    'DownOutUpIn': ql.DoubleBarrier.KOKI
}

QLInterpolator = Callable[[float, Optional[bool]], float]
QLInterpolatorType = Callable[[list[float], list[float]], QLInterpolator]
# SWIGs\interpolation.i
#   [...]Interpolation  --> None
# 	    x   Array(Real)
#       y   Array(Real)
#
#       operator() --> Real
#           x   Real
#           allowExtrapolation  bool [false]
InterpolatorType: AugmentedDict[str, QLInterpolatorType] = AugmentedDict({
    'LinearInterpolation': ql.LinearInterpolation,
    'LogLinearInterpolation': ql.LogLinearInterpolation,
    'BackwardFlatInterpolation': ql.BackwardFlatInterpolation,
    'ForwardFlatInterpolation': ql.ForwardFlatInterpolation,
    'ConvexMonotoneInterpolation': ql.ConvexMonotoneInterpolation
})
