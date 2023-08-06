import re

# 1 String

# # 1.1 String -> Date

DATE_SEPARATOR = '-'
IS_DATE: re.Pattern[str] = re.compile(f'^(19|20)[0-9][0-9]{DATE_SEPARATOR}(0[1-9]|1[0-2]){DATE_SEPARATOR}(0[1-9]|1[0-9]|2[0-9]|3[0-1])$')


def is_date(value: str) -> bool:
    return re.match(IS_DATE, value) is not None


# # 1.2 String -> Period

IS_PERIOD: re.Pattern[str] = re.compile('^[1-9][0-9]*[MDYW]$')


def is_period(value: str) -> bool:
    return re.match(IS_PERIOD, value) is not None
