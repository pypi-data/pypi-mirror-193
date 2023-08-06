import datetime
import QuantLib as ql

from valuation.universal_transfer import Reference

DefaultParametersReference: Reference = Reference('DefaultParameters', 'DefaultParameters')

SettlementDaysMaximum: int = 15

InterestRateMinimum: float = -0.1
InterestRateMaximum: float = 0.3
DiscountFactorMaximum: float = 1.5
GearingMaximum: float = 10.0
GearingMinimum: float = -GearingMaximum
RedemptionMaximum: float = 2.0
CallPutPriceMaximum: float = 2.0

ContinuousDividendYieldMaximum: float = 0.1  # 10% should be an input unit confusion most of the time
RelativeStrikeMaximum: float = 10

FutureMinimum: float = 90
FutureMaximum: float = 150

VolatilityMaximum: float = 0.5
MeanReversionMaximum: float = 0.5

MaximalTimeSteppingInDaysMCMinimum: float = 0.04
ContinuousTimeSteppingInDaysMCMinimum: float = 0.01
LogNumberOfPathsMaximum: int = 20
ToleranceForEqualityMaximum: float = 1.0

# Dummy date should be well before any possible start date in instruments.
# It is the instruments obligation to operate with non-inputs, i.e. DummyDates.
# The choice is obviously arbitrary, the following is the date of the
#       Universal Delaration of Human Rights
# 10 December 1948, Paris.
DummyDate: datetime.date = datetime.date(1948, 12, 10)
DummyQLDate: ql.Date = ql.Date(10, 12, 1948)

OutputPrecision: int = 9

GreekIsNonZero: float = 1e-6
MarketDataRangeIsNonZero: float = 1e-8


# Needed to pass initial ordering checks on lists, the precise ordering can be determined only after acquiring the settlement days convention
# Since in FX land the settlement days are at least 1, only TN and SN may fall on the same date (in case of settlement days = 1) so technically
# it should be SN >= TN instead of SN > TN like it is done below. However, implementation of this nuance is not required here and it is more
# important to have SN != TN for raw lists of periods. The case of SN = TN must be handled specifically by the QLMarketData object after it has received settlementDays(i).
ShortTermTenorOrder: dict[str, int] = {
    'SPOT': 0,
    'ON': 1,  # exactly 1 day after spot
    'TN': 2,  # exactly 2 days after spot
    'SN': 3,  # settlement days + 1 day after spot
    'SW': 4   # settlement days + 1 week after spot
}
