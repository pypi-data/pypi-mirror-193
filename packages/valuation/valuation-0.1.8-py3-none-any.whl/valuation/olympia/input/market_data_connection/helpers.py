import datetime
import re
from datetime import timedelta
from typing import Union

ISO_DATE = '%Y-%m-%d'


def german2iso_date(date_str: str) -> str:
    return datetime.datetime.strptime(date_str, '%d.%m.%Y').strftime(ISO_DATE)


def excel2iso_date(date_number: Union[int, float]) -> str:
    return (datetime.date(1899, 12, 31) + timedelta(days=int(date_number - 1))).strftime(ISO_DATE)


def float_str2float(value: Union[str, float, int], decimal_sep: str = ',') -> float:
    if isinstance(value, str):
        value = value.replace(decimal_sep, '')
        return float(value)
    return float(value)


def list_float_str2float(values: list[Union[str, float, int]], decimal_sep: str = ',') -> list[float]:
    return [float_str2float(value, decimal_sep=decimal_sep) for value in values]


def int_str2int(value: Union[str, float, int], decimal_sep: str = ',') -> int:
    if isinstance(value, str):
        value = value.replace(decimal_sep, '')
        return int(value)
    return int(value)


def list_int_str2int(values: list[Union[str, float, int]], decimal_sep: str = ',') -> list[int]:
    return [int_str2int(value, decimal_sep=decimal_sep) for value in values]


DATE_BRICKS = {
    'YYYY': '%Y',
    'YY': '%y',
    'MMM': '%b',
    'MM': '%m',
    'DD': '%d'
}
PLACE_HOLDER: re.Pattern[str] = re.compile('([$<])([^$><]+)([$>])')


def replace_date_place_holder(path: str, date: datetime.date) -> str:
    place_holders: list[tuple[str, str, str]] = re.findall(PLACE_HOLDER, str(path))
    for left_border, date_str2_replace, right_border in place_holders:
        str2replace = ''.join((left_border, date_str2_replace, right_border))
        for key, value in DATE_BRICKS.items():
            date_str2_replace = date_str2_replace.replace(key, value)
        path = path.replace(str2replace, datetime.date.strftime(date, date_str2_replace))
    return path
