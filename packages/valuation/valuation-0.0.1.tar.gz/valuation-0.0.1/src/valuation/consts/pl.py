
# Attention:
# All variables in this file need to be mutually different on letter level from major variables, i.e. for no major variable x in this file and no variable in this file it is allowed to hold:
# x in y  if not  x == y.
# Hence the minor variable PAYIFDEAD is not allowed due to the major variable IF
# However PAYDEAD is allowed because PAY is not a major but a minor variable.

# Majors
Branch: str = 'IF'
BranchPositive: str = 'THEN'
BranchNegative: str = 'ELSE'
Continuous: str = 'CONTINUOUS'

# Minors
Stop: str = 'STOP'
Pay: str = 'PAY'
PayIfDead: str = 'PAYDEAD'

All: str = 'ALL'
FixingIndex: str = 'FIXING_INDEX'
FixingDate: str = 'FIXING_DATE'
PayDate: str = 'PAY_DATE'
SettlementDate: str = 'SETTLE_DATE'

PathKey: str = 'PATH'

PathSeparator: str = '@'
PathAll: str = 'ALL'

PathRaw: str = 'RAW'
PathValue: str = 'VALUE'
PathVolatility: str = 'VOL'
PathDiscount: str = 'DISCOUNT'
PathCMS: str = 'CMS'
PathCMSShort: str = 'CMSShort'      # Be careful, that this does not match with the keyword OR
PathCMSLong: str = 'CMSLong'
PathSummation: str = 'SUMMATION'

PathSeparatedRaw: str = PathSeparator + PathRaw
PathSeparatedValue: str = PathSeparator + PathValue
PathSeparatedVolatility: str = PathSeparator + PathVolatility
PathSeparatedDiscount: str = PathSeparator + PathDiscount
PathSeparatedCMS: str = PathSeparator + PathCMS
PathSeparatedCMSShort: str = PathSeparator + PathCMSShort
PathSeparatedCMSLong: str = PathSeparator + PathCMSLong
PathSeparatedSummation: str = PathSeparator + PathSummation

# Internal:

Dummy: str = 'DUMMY'
