# pylint: disable=invalid-name

from valuation.consts import types
# Fields.Id etc. are also used in UniversalTransfer.storage
# Therefore we need to have a direct import in order to circumvent cycles!
from valuation.universal_transfer.type_key import TypeKey

MatrixRowHeaders: str = 'rowHeaders'
MatrixColumnHeaders: str = 'columnHeaders'
MatrixContent: str = 'content'


def SubType(type_name: str = 'Fill me please correctly; in case that we want to go back to strongly typed subtypes') -> TypeKey:              # pylint: disable=invalid-name, unused-argument
    return TypeKey(types.Str, 'subType')


def GreekType(greek: str, valuation_type: str) -> TypeKey:                  # pylint: disable=invalid-name
    return TypeKey(types.Float, greek + valuation_type)


def Schedule(name_suffix: str) -> TypeKey:                                  # pylint: disable=invalid-name
    return TypeKey(types.SubStorages, f'schedule{name_suffix}') if name_suffix else TypeKey(types.SubStorages, 'schedule')


# Attention!
# All fields should be in camelCaseType
# Before you enter a new combination, please check if there is really nothing which seems to match !!!
# Within the catagories, keep it alphabetically ordered, pls!
Id = TypeKey(types.Str, 'id')
SubId = TypeKey(types.Str, 'subId')
InstanceId = TypeKey(types.Str, 'instanceId')
Type = TypeKey(types.Str, 'type')


# Bools
AdjustPeriodLength = TypeKey('b', 'adjustPeriodLength')
AllowTradeDateMismatch = TypeKey(types.Bool, 'allowTradeDateMismatch')
Antithetic = TypeKey(types.Bool, 'antithetic')
BrownianBridge = TypeKey(types.Bool, 'brownianBridge')
CallOnCouponDate = TypeKey(types.Bool, 'callOnCouponDate')
EarlyRebate = TypeKey(types.Bool, 'earlyRebate')
EnableBroadieGlassermann = TypeKey(types.Bool, 'enableBroadieGlassermann')
EnableExtrapolation = TypeKey(types.Bool, 'enableExtrapolation')
EndOfMonth = TypeKey(types.Bool, 'endOfMonth')
FixingInArrears = TypeKey(types.Bool, 'fixingInArrears')
FixMeanReversion = TypeKey(types.Bool, 'fixMeanReversion')
HasSSDCall = TypeKey(types.Bool, 'hasSSDCall')
SymmetricGreeks = TypeKey(types.Bool, 'symmetricGreeks')
IsAlive = TypeKey(types.Bool, 'isAlive')
IsBaseCurve = TypeKey(types.Bool, 'isBaseCurve')
KnockedIn = TypeKey(types.Bool, 'alreadyKnockedIn')
KnockedOut = TypeKey(types.Bool, 'alreadyKnockedOut')
MakeIndexUnique = TypeKey(types.Bool, 'makeIndexUnique')
NegativePayoutsAllowed = TypeKey(types.Bool, 'negativePayoutsAllowed')
NaturalFloor = TypeKey(types.Bool, 'naturalFloor')
SecondDerivatives = TypeKey(types.Bool, 'secondDerivatives')
SimultaneousCurveShift = TypeKey(types.Bool, 'simultaneousCurveShift')
TryToGetPastFixings = TypeKey(types.Bool, 'tryToGetPastFixings')
# Business:
AccrualBusiness = TypeKey(types.Business, 'accrualBusiness')
Business = TypeKey(types.Business, 'business')
RhoBusiness = TypeKey(types.Business, 'rhoBusiness')

# Calendar:
Calendar = TypeKey(types.Calendar, 'calendar')
RhoCalendar = TypeKey(types.Calendar, 'rhoCalendar')

# Dates
CallDate = TypeKey(types.Date, 'callDate')
ContinuousEnd = TypeKey(types.Date, 'continuousEnd')
ContinuousStart = TypeKey(types.Date, 'continuousStart')
Date = TypeKey(types.Date, 'date')
Dates = TypeKey(types.Dates, 'dates')
DividendDates = TypeKey(types.Dates, 'dividendDates')
ExerciseDates = TypeKey(types.Dates, 'exerciseDates', fall_back_to_single=True)
FirstCouponDate = TypeKey(types.Date, 'firstCouponDate')
FixingDate = TypeKey(types.Date, 'fixingDate')
FixingDates = TypeKey(types.Dates, 'fixingDates')
Issue = TypeKey(types.Date, 'issue')
LastCouponDate = TypeKey(types.Date, 'lastCouponDate')
Maturity = TypeKey(types.Date, 'maturity')
NextToLastCouponDate = TypeKey(types.Date, 'nextToLastCouponDate')
PeriodEnd = TypeKey(types.Date, 'periodEnd')
PeriodStart = TypeKey(types.Date, 'periodStart')
TradeDate = TypeKey(types.Date, 'tradeDate')
ValuationDate = TypeKey(types.Date, 'valuationDate')
ZSpreadSettlementDate = TypeKey(types.Date, 'zSpreadSettlementDate')

# DayCount
DayCount = TypeKey(types.DayCount, 'dayCount')
FixedDayCount = TypeKey(types.DayCount, 'fixedDayCount')
FloatDayCount = TypeKey(types.DayCount, 'floatDayCount')

# Floats
# Coupon --> FixedRate
Accuracy = TypeKey(types.Float, 'accuracy')
AdditiveFactor = TypeKey(types.Float, 'additiveFactor')
Amount = TypeKey(types.Float, 'amount')
BarrierDown = TypeKey(types.Float, 'barrierDown')
BarrierUp = TypeKey(types.Float, 'barrierUp')
CallPrice = TypeKey(types.Float, 'callPrice')
PutPrice = TypeKey(types.Float, 'putPrice')
Cap = TypeKey(types.Float, 'cap')
ContinuousDividendYield = TypeKey(types.Float, 'continuousDividendYield')
ContinuousTimeSteppingInDaysMC = TypeKey(types.Float, 'continuousTimeSteppingInDaysMC')
DividendAbsolute = TypeKey(types.Floats, 'dividendAbsolute')
DividendRelative = TypeKey(types.Floats, 'dividendRelative')
Drift = TypeKey(types.Float, 'drift')
FixedRate = TypeKey(types.Float, 'fixedRate')
Fixing = TypeKey(types.Float, 'fixing')
Fixings = TypeKey(types.Floats, 'fixings')
Floor = TypeKey(types.Float, 'floor')
Gearing = TypeKey(types.Float, 'gearing')
GearingPositive = TypeKey(types.Float, 'gearingPositive')
GearingNegative = TypeKey(types.Float, 'gearingNegative')
GreekSignificanceLowerBound = TypeKey(types.Float, 'greekSignificanceLowerBound')
LongTermVariance = TypeKey(types.Float, 'longTermVariance')
LongTermDrift = TypeKey(types.Float, 'longTermDrift')
LongTermVolatilityValue = TypeKey(types.Float, 'longTermVolatilityValue')
MaximalTimeSteppingInDaysMC = TypeKey(types.Float, 'maximalTimeSteppingInDaysMC')
MeanReversion = TypeKey(types.Float, 'meanReversion')
Price = TypeKey(types.Float, 'price')
Rebate = TypeKey(types.Float, 'rebate')
Redemption = TypeKey(types.Float, 'redemption')  # final redemption
RedemptionPayment = TypeKey(types.Float, 'redemptionPayment')
ReversionRate = TypeKey(types.Float, 'reversionRate')
SingleCorrelation = TypeKey(types.Float, 'correlation')
Spread = TypeKey(types.Float, 'spread')
SpreadCorrelation = TypeKey(types.Float, 'spreadCorrelation')
StdDeviations = TypeKey(types.Float, 'stdDeviations')
Strike = TypeKey(types.Float, 'strike')
ToleranceForEquality = TypeKey(types.Float, 'toleranceForEquality')
Value = TypeKey(types.Float, 'value')
Values = TypeKey(types.Floats, 'values')
VolatilityValue = TypeKey(types.Float, 'volatility')
VolOfVol = TypeKey(types.Float, 'volOfVol')
ZSpreadAccuracy = TypeKey(types.Float, 'zSpreadAccuracy')
ZSpreadGuess = TypeKey(types.Float, 'zSpreadGuess')
ZSpreadPrice = TypeKey(types.Float, 'zSpreadPrice')

# Integers
FixingDays = TypeKey(types.Int, 'fixingDays')
IntegrationSteps = TypeKey(types.Int, 'integrationSteps')
LegNumber = TypeKey(types.Int, 'legNumber')
LogNumberOfPaths = TypeKey(types.Int, 'logNumberOfPaths')
SettlementDays = TypeKey(types.Int, 'settlementDays')
ZSpreadMaxIter = TypeKey(types.Int, 'zSpreadMaxIter')

# Periods
FixedFrequency = TypeKey(types.Period, 'fixedFrequency')
Frequency = TypeKey(types.Period, 'frequency')
IndexTenor = TypeKey(types.Period, 'indexTenor')
Period = TypeKey(types.Period, 'period')
Tenor = TypeKey(types.Period, 'tenor')
Tenors = TypeKey(types.Periods, 'tenors')
MaxCumulativeTime = TypeKey(types.Period, 'maxCumulativeTime')
SwapTenor = TypeKey(types.Period, 'swapTenor')
OptionTenor = TypeKey(types.Period, 'optionTenor')
AmericanCallPutTimeStep = TypeKey(types.Period, 'americanCallPutTimeStep')

# References Currency
BaseCurrency = TypeKey(types.Reference, 'baseCurrency')
BaseRate = TypeKey(types.Reference, 'baseRate')
CorrelationBaseCurrency = TypeKey(types.Reference, 'correlationBaseCurrency')
Currency = TypeKey(types.Reference, 'currency')
QuoteCurrency = TypeKey(types.Reference, 'quoteCurrency')
QuoteRate = TypeKey(types.Reference, 'quoteRate')

# References Curve
BaseCurve = TypeKey(types.Reference, 'baseCurve')
DiscountCurve = TypeKey(types.Reference, 'discountCurve')
QuoteCurve = TypeKey(types.Reference, 'quoteCurve')
RiskFreeCurve = TypeKey(types.Reference, 'riskFreeCurve')
SpreadCurve = TypeKey(types.Reference, 'spreadCurve')

# References Surface
CapFloorVolatility = TypeKey(types.Reference, 'capFloorVolatility')
SwaptionVolatility = TypeKey(types.Reference, 'swaptionVolatility')
SurfaceReference = TypeKey(types.Reference, 'surface')

# Reference MarketData
MarketData = TypeKey(types.Reference, 'marketData')
Stock = TypeKey(types.Reference, 'stock')
LowMarketData = TypeKey(types.Reference, 'lowMarketData')
HighMarketData = TypeKey(types.Reference, 'highMarketData')

# Reference Process
StochasticProcess = TypeKey(types.Reference, 'stochasticProcess')
StochasticProcesses = TypeKey(types.References, 'stochasticProcesses')
ShortRateProcess = TypeKey(types.Reference, 'shortRateProcess')

# Reference InterestRateIndex
IRIndex = TypeKey(types.Reference, 'irIndex')
IRSwapIndex = TypeKey(types.Reference, 'irSwapIndex')
IRSwapIndexShort = TypeKey(types.Reference, 'irSwapIndexShort')
IRSwapIndexLong = TypeKey(types.Reference, 'irSwapIndexLong')
IRSwapIndexPositive = TypeKey(types.Reference, 'irSwapIndexPositive')
IRSwapIndexNegative = TypeKey(types.Reference, 'irSwapIndexNegative')
IRSpreadSwapIndex = TypeKey(types.Reference, 'irSpreadSwapIndex')
YieldCurveFreeIRIndex = TypeKey(types.Reference, 'irIndex', allow_data_only_mode=True)

# Reference IRIndex
FxRate = TypeKey(types.Reference, 'fxRate')

# Reference Instrument
DataInstrument = TypeKey(types.Reference, 'instrument', allow_data_only_mode=True)
Instrument = TypeKey(types.Reference, 'instrument')
Underlying = TypeKey(types.Reference, 'instrument', fall_back_to_storage=True)

# Reference
FixingFunction = TypeKey(types.Reference, 'fixingFunction')
RealObject = TypeKey(types.Reference, 'realObject')

# Reference Optimization
Optimization = TypeKey(types.Reference, 'optimization')

# Strings
BarrierType = TypeKey(types.Str, 'barrierType')
BaseUrl = TypeKey(types.Str, 'baseUrl')
Compounding = TypeKey(types.Str, 'compounding')
CurrencyName = TypeKey(types.Str, 'currencyName')
DataType = TypeKey(types.Str, 'dataType')
DateGeneration = TypeKey(types.Str, 'dateGeneration')
Distribution = TypeKey(types.Str, 'distribution')
FileName = TypeKey(types.Str, 'fileName')
FRADefinition = TypeKey(types.Str, 'fraDefinition')
InterpolationType = TypeKey(types.Str, 'interpolationType')
Model = TypeKey(types.Str, 'model')
OptionType = TypeKey(types.Str, 'optionType')
OptionalInfo = TypeKey(types.Str, 'optionalInfo')
RandomGeneratorType = TypeKey(types.Str, 'randomGeneratorType')
SwapPosition = TypeKey(types.Str, 'swapPosition')
Token = TypeKey(types.Str, 'token')
User = TypeKey(types.Str, 'user')
Url = TypeKey(types.Str, 'url')

# Variable Strings
PayOffDefinitions = TypeKey(types.Strs, 'payOffDefinition', fall_back_to_single=True)

# Tenors
RhoScenarios = TypeKey(types.Periods, 'rhoScenarios')

# Substorages
CallSchedule = TypeKey(types.SubStorages, 'callSchedule')
Legs = TypeKey(types.SubStorages, 'legs')
InterestRateMarketData = TypeKey(types.SubStorages, 'interestRateMarketData')
SwaptionPoints = TypeKey(types.SubStorages, 'swaptionPoints')
UpfrontPayments = TypeKey(types.SubStorages, 'upfrontPayments')
VolaPoints = TypeKey(types.SubStorages, 'volaPoints')

# Storages
SubInstruments = TypeKey(types.Storages, 'subInstruments')

# List of Str
ResultTypes = TypeKey(types.Strs, 'resultTypes')

# Matrices
Surface = TypeKey(types.Matrix, 'surface')
Correlation = TypeKey(types.Matrix, 'correlation')

# LevenbergMarquardt specifics:
LBEndFunctionEpsilon = TypeKey(types.Float, 'endFunctionEpsilon')
LBEndGradientEpsilon = TypeKey(types.Float, 'endGradientEpsilon')
LBEndMaxIteration = TypeKey(types.Int, 'endMaxIteration')
LBEndMaxStationaryIteration = TypeKey(types.Int, 'endMaxStationaryIteration')
LBEndRootEpsilon = TypeKey(types.Float, 'endRootEpsilon')
LBOptFunctionEpsilon = TypeKey(types.Float, 'optFunctionEpsilon')
LBOptToleranceGradient = TypeKey(types.Float, 'optToleranceGradient')
LBOptToleranceVariable = TypeKey(types.Float, 'optToleranceVariable')

# Baskets
MarketDataBasket = TypeKey(types.References, 'marketDataBasket')
