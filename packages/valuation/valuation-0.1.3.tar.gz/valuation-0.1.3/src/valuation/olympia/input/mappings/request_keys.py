from __future__ import annotations

import inspect
from typing import Any, Optional, Callable

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.olympia.input.exception import OlympiaImportError
from valuation.universal_transfer import TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Signature


class OlympiaMappingError(OlympiaImportError):  # pylint: disable=too-few-public-methods
    pass


class KeyCollection:

    @classmethod
    def get_all(cls) -> tuple[Any, ...]:
        return tuple(value for key, value in inspect.getmembers(cls) if
                     not (key.startswith('__') and key.endswith('__')) and not inspect.ismethod(value))


# 1 Preprocessing

# # 1.1 Request navigation

class ExcelRequestParams(KeyCollection):  # pylint: disable=too-few-public-methods
    """Keys, sheet names, data positions that are used for parsing excel requests"""
    CommentColumn: str = 'column'
    ConstantSpreadCurveId: str = 'curveId'
    InstrumentSheet: str = 'Instrument'
    LegColumns: str = 'leg'
    RequestColumn: str = 'request'
    RequiresScheduleColumn = 'requiresSchedule'
    ScheduleSheet: str = 'Schedules'
    SpreadSheet: str = 'Spreads'
    MarketDataSheet: str = 'MarketData'
    ProcessSheet: str = 'StochasticProcesses'
    ValuationDateAndVersion: str = 'VALUATION_DATE'
    ValuationSheet: str = 'Valuations'
    Version: str = 'templateVersion'


class Keys(KeyCollection):  # pylint: disable=too-few-public-methods
    """Keys that are used in olympia requests"""
    InstrumentData: str = 'instrumentData'
    InstrumentId: str = 'instrumentId'
    InstrumentFeatures: str = 'instrumentFeatures'
    InstrumentReferences: str = 'instrumentReference'
    InstrumentType: str = 'instrumentType'
    LegNumber: str = 'legNumber'
    Legs: str = 'legs'
    MarketDataReferences: str = 'marketDataReferences'
    ObjectId: str = 'id'
    PriceClassifier: str = 'priceClassifier'
    RequestId: str = 'id'
    Security: str = 'security'
    Type: str = 'type'
    SubType: str = 'subType'
    ValuationDate: str = 'valuationDate'
    Valuations: str = 'valuation'
    Version: str = 'version'


class MarketDataBuckets(KeyCollection):  # pylint: disable=too-few-public-methods
    """Bucket names that are used in olympia requests"""
    CapFloorVolatilities: str = 'capFloorVolatilities'
    Currencies: str = 'currencies'
    DiscountCurves: str = 'discountCurves'
    FxRates: str = 'fxRates'
    Indexes: str = 'indexes'
    MarketData: str = 'marketData'
    Processes: str = 'processes'
    SpreadCurves: str = 'spreadCurves'
    SwaptionVolatilities: str = 'swaptionVolatilities'


class Names(KeyCollection):  # pylint: disable=too-few-public-methods
    """Request names for assigning names during request processing"""
    Info: str = 'info'
    Leg: str = 'Leg'
    RequestId: str = 'requestId'


# # 1.2 Objects
BUCKET_TO_OBJECT: dict[str, Signature] = {
    MarketDataBuckets.CapFloorVolatilities: signatures.cap_floor_surface,
    MarketDataBuckets.Currencies: signatures.currency.variable,
    MarketDataBuckets.DiscountCurves: signatures.yield_curve.discount,
    MarketDataBuckets.Indexes: signatures.ir_index.base,
    MarketDataBuckets.SpreadCurves: signatures.yield_curve.constant_spread,
    MarketDataBuckets.SwaptionVolatilities: signatures.swaption_volatility.surface}

REFERENCES_INFERRED_BY_KEY: dict[str, Callable[[str], str]] = {  # fixme: this will be removed when all market data references are uri's
    'hullWhiteProcessName': lambda val: f'mdh://HULL_WHITE_PROCESS/{val}',
    'swaptionVolatilityProcessName': lambda val: f'mdh://SWAPTION_VOLATILITY_PROCESS/{val}',
    'capletVolatilityProcessName': lambda val: f'mdh://CAPLET_VOLATILITY_PROCESS/{val}',
}


# Reference generation
def field2object(field_name: str) -> str:
    if 'currency' in field_name.lower():
        return signatures.currency.all.type
    if 'curve' in field_name.lower():
        return signatures.yield_curve.all.type
    if 'fxrate' in field_name.lower():
        return signatures.fx_rate.all.type
    if 'irspreadswapindex' in field_name.lower():
        return signatures.ir_spread_index.type
    if 'irswapindex' in field_name.lower():
        return signatures.ir_swap_index.type
    if 'irindex' in field_name.lower():
        return signatures.ir_index.base.type
    if 'process' in field_name.lower():
        return signatures.process.all.type
    if 'function' in field_name.lower():
        return signatures.function.all.type
    if 'swaptionvolatility' in field_name.lower():
        return signatures.swaption_volatility.all.type
    if 'capfloorvolatility' in field_name.lower():
        return signatures.cap_floor_surface.type
    if field_name.lower() == 'marketdata':
        return 'MarketData'
    if field_name.lower() == 'instrument':
        return signatures.instrument.all.type
    raise OlympiaMappingError(f'Unknown reference field {field_name}')


# 2 Mappings

# # 2.1 Field mapping


FIELDS: dict[str, TypeKey] = {
    'accrualBusinessDayConvention': fields.AccrualBusiness,
    'businessDayConvention': fields.Business,
    'businessDayCalendar': fields.Calendar,
    'callPrice': fields.Price,
    'correlationValue': fields.SingleCorrelation,
    'correlationMatrix': fields.Correlation,
    'dataInstrument': fields.DataInstrument,
    'yieldCurveIndex': fields.DiscountCurve,
    'discountCurveIndex': fields.DiscountCurve,
    'dayCountConvention': fields.DayCount,
    'endDate': fields.Maturity,
    'endRegularDate': fields.LastCouponDate,
    'hullWhiteProcessName': fields.StochasticProcess,
    'swaptionVolatilityProcessName': fields.StochasticProcess,
    'capletVolatilityProcessName': fields.StochasticProcess,
    'fixingDaysPrior': fields.FixingDays,
    'fxRateUri': fields.FxRate,
    'yieldCurveUri': fields.DiscountCurve,
    'index': fields.IRIndex,
    'irSwapIndex1': fields.IRSwapIndex,
    'indexGearing1': fields.GearingPositive,
    'indexGearing2': fields.GearingNegative,
    'forwardIndex': fields.IRIndex,
    'leg': fields.LegNumber,
    'matrix': fields.Surface,
    'nominal': fields.Amount,
    'notional': fields.Amount,
    'optionExpiry': fields.OptionTenor,
    'paymentBusinessDayConvention': fields.Business,
    'paymentFrequency': fields.Tenor,
    'position': fields.SwapPosition,
    'primaryCurrency': fields.BaseCurrency,
    'redemptionFormula': fields.Redemption,
    'schedulePeriods': fields.Schedule(''),
    'secondaryCurrency': fields.QuoteCurrency,
    'secondaryCurve': fields.QuoteCurve,
    'sinking': fields.RedemptionPayment,
    'ssdCall': fields.HasSSDCall,
    'startDate': fields.Issue,
    'startRegularDate': fields.FirstCouponDate,
    'swapIndex': fields.IRSwapIndex,
    'swapIndexSpread': fields.IRSpreadSwapIndex,
    'subType': fields.SubType('')
}

NON_ENGINE_FIELDS: dict[str, TypeKey] = {
    'name': TypeKey(types.Str, 'name'),
    'referenceDateTime': TypeKey(types.Date, 'referenceDateTime'),
    'url': TypeKey(types.Str, 'url'),
    'user': TypeKey(types.Str, 'user'),
    'token': TypeKey(types.Str, 'token'),
    'baseUrl': TypeKey(types.Str, 'baseUrl'),
    'baseCurveName': TypeKey(types.Str, 'baseCurveName'),
    'couponFormula': TypeKey(types.Str, 'couponFormula'),
    'spreadConfiguration': TypeKey(types.SubStorage, 'spreadConfiguration'),
    'bidAskDelta': TypeKey(types.Float, 'bidAskDelta'),
    '$priceClassifier': TypeKey(types.Str, '$priceClassifier'),
    'hullWhiteProcessName': TypeKey(types.Reference, 'hullWhiteProcess'),
    'instrumentFeatures': TypeKey(types.Strs, 'features'),
    'callPutEvents': TypeKey(types.SubStorages, 'olympiaCallSchedule'),  # TODO: remove when Excel is removed
    'single': TypeKey(types.SubStorage, 'event'),
    'american': TypeKey(types.SubStorage, 'event'),
    'callPutEventType': TypeKey(types.Str, 'callPutEventType')
}

MULTIPLE_MAPPED_KEYS: dict[str, list[TypeKey]] = {
    'businessDayConvention': [fields.Business, fields.AccrualBusiness]
}

ALL_GREEKS = [
    'delta',
    'vega',
    'theta',
    'rho',
    'lambda',
    'epsilon',
    'gamma',
    'vanna'
]
GREEK_VALUATION_TYPES = [
    'Analytic',
    'MC',
    'Tree'
]


def check_and_make_greek_type(arg: str) -> Optional[TypeKey]:
    for valuation_type in GREEK_VALUATION_TYPES:
        if valuation_type in arg:
            remaining_arg = arg.replace(valuation_type, '')
            if remaining_arg in ALL_GREEKS:
                return fields.GreekType(remaining_arg, valuation_type)
    return None


# # 2.2 Terms and matrices


class MatrixKeys(KeyCollection):  # pylint: disable=too-few-public-methods

    BucketName: str = 'matrix'
    ColumnHeader: str = 'columnHeader'
    ColumnHeaders: str = 'columnHeaders'
    Content: str = 'points'
    Point: str = 'value'
    RowHeader: str = 'rowHeader'
    RowHeaders: str = 'rowHeaders'


class TermKeys(KeyCollection):  # pylint: disable=too-few-public-methods

    Date: str = 'date'
    Dates: str = 'dates'
    Identifier: str = 'points'
    Value: str = 'value'
    Values: str = 'values'


# 3 Values

# # 3.1 String

Strings: dict[str, str] = {
    'DiscountFactor': 'Discount',
    'FIXED': 'Fixed',
    'FLOATING': 'Floating',
    'Float': 'Floating',
    'SWAP_OPTION': 'Swaption',
    'INTEREST_RATE_SWAP': 'Swap',
    'PAYER': 'Payer',
    'RECEIVER': 'Receiver',
    'FX_FORWARD': 'FxForward',
    'NORMAL': 'Normal',
    'LOG_NORMAL': 'LogNormal',
    'CMS_SPREAD': 'CMSSpread'
}

OLYMPIA_MARKET_DATA_OBJECTS: dict[str, Signature] = {
    'FIXING': signatures.ir_index.base,
    'CMS_FIXING': signatures.ir_swap_index,

    'SWAPTION_VOLATILITY': signatures.swaption_volatility.points,

    'YIELD_CURVE': signatures.yield_curve.zero,

    'SWAPTION_VOLATILITY_PROCESS': signatures.process.swaption_volatility,
    'CAPLET_VOLATILITY_PROCESS': signatures.process.cap_floor_volatility,
    'HULL_WHITE_PROCESS': signatures.process.hull_white_calibration,
    'FX_FORWARD_BUNDLE': signatures.fx_rate.triangle,
    'FIXING_FUNCTION': signatures.function.api_call_fixing_v2,
    'CMS_FIXING_FUNCTION': signatures.function.api_call_cms_fixing_v2,

    'FX_FORWARD': signatures.fx_rate.direct,
    'FX_SPOT': signatures.function.api_call_fx_rate_v2
}

# 4 Schedule Service

SCHEDULE_DATA_REQUIRED = {
    'startDate': fields.Issue,
    'endDate': fields.Maturity,
    'calendar': fields.Calendar,
    'businessDayConvention': fields.Business,
    'frequency': fields.Frequency
}

SCHEDULE_DATA_OPTIONAL = {
    'startRegularDate': fields.FirstCouponDate,
    'endRegularDate': fields.LastCouponDate,
    'endOfMonthRule': fields.EndOfMonth,
    'dateGeneration': fields.DateGeneration
}
