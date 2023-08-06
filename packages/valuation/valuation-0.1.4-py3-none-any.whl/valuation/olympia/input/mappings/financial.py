# Day counters

DAY_COUNT_MAP = {
    '1_1': '1/1',
    'ACT_ACT': 'ACT/ACT',
    'ACT_ACT_BOND': 'ACT/ACT_BOND',
    'ACT_ACT/BOND': 'ACT/ACT_BOND',
    'ACT/ACT/BOND': 'ACT/ACT_BOND',
    'ACT_360': 'ACT/360',
    'ACT_365': 'ACT/365',
    'ACT_364': 'ACT/364',
    'IACT_ACT': 'IACT/ACT',
    '30_360': '30/360',
    '30_365': '30/365',
    'G30_360': 'G30/360',
    '30_360_ISDA': '30/360_ISDA',
    '30_360/ISDA': '30/360_ISDA',
    '30/360/ISDA': '30/360_ISDA',
    'E30_360_ISDA': '30/360',
    'E30_360': 'E30/360',
    'U30_360': '30U/360',
    '30I_360': '30I/360',
    'BU_252': 'BU/252'
}


def day_count_converter(day_count: str) -> str:
    day_count = day_count.upper()
    if day_count in DAY_COUNT_MAP:
        return DAY_COUNT_MAP[day_count]
    return day_count


# Calendars


CALENDAR_MAP: dict[str, str] = {
    'TARGET': 'EUR',
    'Target': 'EUR',
    'Finland': 'EUR|Finland',
    'Germany': 'EUR|Germany',
    'Italy': 'EUR|Italy',
    'Slovakia': 'EUR|Slovakia',
    'Austria': 'EUR|Austria',
    'Belgium': 'EUR|Belgium',
    'France': 'EUR|France',
    'Greece': 'EUR|Greece',
    'Ireland': 'EUR|Ireland',
    'Luxembourg': 'EUR|Luxembourg',
    'Netherlands': 'EUR|Netherlands',
    'Portugal': 'EUR|Portugal',
    'Spain': 'EUR|Spain',
    'Argentina': 'ARS',
    'Australia': 'AUD',
    'Brazil': 'BRL',
    'Canada': 'CAD',
    'Chile': 'CLP',
    'China': 'CNY',
    'Colombia': 'COP',
    'Croatia': 'HRK',
    'CzechRepublic': 'CZK',
    'Denmark': 'DKK',
    'Hongkong': 'HKD',
    'Hungary': 'HUF',
    'Iceland': 'ISK',
    'India': 'INR',
    'Indonesia': 'IDR',
    'Israel': 'ILS',
    'Japan': 'JPY',
    'Mexico': 'MXN',
    'Morocco': 'MAD',
    'NewZealand': 'NZD',
    'Norway': 'NOK',
    'Peru': 'PEN',
    'Poland': 'PLN',
    'Russia': 'RUB',
    'Romania': 'RON',
    'SaudiArabia': 'SAR',
    'Serbia': 'RSD',
    'Singapore': 'SGD',
    'SouthAfrica': 'ZAR',
    'SouthKorea': 'KRW',
    'Sweden': 'SEK',
    'Switzerland': 'CHF',
    'Taiwan': 'TWD',
    'Thailand': 'THB',
    'Turkey': 'TRY',
    'Ukraine': 'UAH',
    'UnitedKingdom': 'GBP',
    'UnitedStates': 'USD',
    'United States': 'USD',
    'USA': 'USD',
    'Uruguay': 'UYU',
    'AngloAmerica': 'AngloAmerica',
    'WeekendsOnly': 'WeekendsOnly',

}

# Business conventions

# TODO: This map gives the payment business convention, review this
BUSINESS_MAP: dict[str, str] = {
    'ACTUAL': 'Unadjusted',
    'UNADJUSTED': 'Unadjusted',
    'FOLLOWING': 'Following',
    'FOLLOWING_ADJUSTED': 'Following',
    'FOLLOWING_UNADJUSTED': 'Following',
    'MODIFIED_FOLLOWING': 'Modified Following',
    'MODIFIED_FOLLOWING_ADJUSTED': 'Modified Following',
    'MODIFIED_FOLLOWING_UNADJUSTED': 'Modified Following',
    'PRECEDING': 'Preceding',
    'PRECEDING_ADJUSTED': 'Preceding',
    'PRECEDING_UNADJUSTED': 'Preceding',
    'MODIFIED_PRECEDING': 'Modified Preceding',
}

ACCRUAL_BUSINESS_MAP: dict[str, str] = {
    'ACTUAL': 'Unadjusted',
    'UNADJUSTED': 'Unadjusted',
    'FOLLOWING': 'Following',
    'FOLLOWING_ADJUSTED': 'Following',
    'FOLLOWING_UNADJUSTED': 'Unadjusted',
    'MODIFIED_FOLLOWING': 'Modified Following',
    'MODIFIED_FOLLOWING_ADJUSTED': 'Modified Following',
    'MODIFIED_FOLLOWING_UNADJUSTED': 'Unadjusted',
    'PRECEDING': 'Preceding',
    'PRECEDING_ADJUSTED': 'Preceding',
    'PRECEDING_UNADJUSTED': 'Unadjusted',
    'MODIFIED_PRECEDING': 'Modified Preceding',
    'MODIFIED_PRECEDING_ADJUSTED': 'Modified Preceding',
    'MODIFIED_PRECEDING_UNADJUSTED': 'Unadjusted',
}

# Frequencies

PERIOD_MAP: dict[str, str] = {
    'DAILY': '1D',
    'WEEKLY': '1W',
    'MONTHLY': '1M',
    'ONE_MONTH': '1M',
    'QUARTERLY': '3M',
    'THREE_MONTHS': '3M',
    'SEMIANNUAL': '6M',
    'SIX_MONTHS': '6M',
    'ANNUAL': '1Y',
    'ONE_YEAR': '1Y',
}

# Date Generations

DATE_GENERATION_MAP: dict[str, str] = {
    'BACKWARD': 'Backward',
    'CDS': 'CDS',
    'CDS_2015': 'CDS2015',
    'FORWARD': 'Forward',
    'OLD_CDS': 'OldCDS',
    'THIRD_WEDNESDAY': 'ThirdWednesday',
    'TWENTIETH': 'Twentieth',
    'TWENTIETH_IMM': 'TwentiethIMM',
    'ZERO': 'Zero'

}
