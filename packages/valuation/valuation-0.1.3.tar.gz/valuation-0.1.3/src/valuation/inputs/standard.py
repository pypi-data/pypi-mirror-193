import datetime
from collections import defaultdict
from typing import Any, Callable, Union

from valuation.consts import types
from valuation.consts import fields
from valuation.exceptions import DAAException
from valuation.universal_transfer import BusinessConvention, BusinessConventions, Calendar, Calendars, Matrix, Period, Reference, Storage, StorageTypes, TypeKey
from valuation.utils.decorators import serialize_function
from daa_utils import Log

TypeKeyDetermination = Callable[[str, Any], dict[TypeKey, Any]]
ValueConversion = Callable[[str, Any, TypeKeyDetermination], Any]


def standard_type_key_determination(key: str, value: Any) -> dict[TypeKey, Any]:
    if key.startswith('['):
        key = key[1:-1].replace(' ', '')
        result: dict[TypeKey, list[Any]] = defaultdict(list)
        for column, sub_key_raw in enumerate(key.split(',')):
            sub_key: TypeKey = TypeKey.from_str(sub_key_raw)
            for line in value:
                result[sub_key].append(line[column])
        return result
    return {TypeKey.from_str(key): value}


def standard_value_conversion(value_type: str, value: Any, type_key_determination: TypeKeyDetermination) -> Any:
    if types.is_matrix(value_type):
        new_value_type = types.to_list_type(value_type)
        return tuple(standard_value_conversion(new_value_type, line, type_key_determination) for line in value)
    if types.is_single(value_type):
        return standard_value_conversion_single(value_type, value, type_key_determination)
    return tuple(standard_value_conversion_single(types.to_single_type(value_type), entry, type_key_determination) for entry in value)


@serialize_function
def standard_date_converter(value: Union[str, datetime.date]) -> datetime.date:
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    return datetime.datetime.fromisoformat(value).date()


def standard_bool_converter(value: Union[bool, str]) -> Union[bool, str]:
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'ja', 'y', 'j'):
        return True
    if value.lower() in ('no', 'nein', 'n'):
        return False
    return value


def standard_calendar_converter(value: str) -> Calendar:
    if value in Calendars:
        return value
    if value[:3] in Calendars:
        new_value: str = value[:3]
        Log.warning(f'Interpreting calendar {value} as {new_value}')
        return new_value
    return value


def standard_period_converter(value: str) -> Period:
    return Period.from_str(value.upper())


def standard_business_converter(value: str) -> BusinessConvention:
    if value in BusinessConventions:
        return value
    for business in BusinessConventions:
        if business.replace(' ', '').lower() == value.replace(' ', '').lower():
            Log.warning(f'Interpreting business convention {value} as {business}')
            return business
    return value


def standard_matrix_converter(value: dict[str, Any], type_key_determination: TypeKeyDetermination) -> Matrix:
    row_headers: StorageTypes.SimpleList = tuple()
    column_headers: StorageTypes.SimpleList = tuple()
    content: StorageTypes.SimpleMatrix = tuple()
    for key, raw_value in value.items():
        type_key_value: dict[TypeKey, Any] = type_key_determination(key, raw_value)
        assert len(type_key_value) == 1
        type_key, sub_value = next(iter(type_key_value.items()))
        attribute_name = type_key.key
        if attribute_name == fields.MatrixRowHeaders and not row_headers:
            row_header_type: str = type_key.type
            row_headers = standard_value_conversion(row_header_type, sub_value, type_key_determination)
        elif attribute_name == fields.MatrixColumnHeaders and not column_headers:
            column_header_type: str = type_key.type
            column_headers = standard_value_conversion(column_header_type, sub_value, type_key_determination)
        elif attribute_name == fields.MatrixContent and not content:
            content_type = type_key.type
            content = standard_value_conversion(content_type, sub_value, type_key_determination)
        else:
            raise DAAException(f'{sub_value} cannot be converted to matrix!')
    return Matrix(column_headers, row_headers, content, column_header_type, row_header_type, content_type)


def standard_subobject_converter(value: dict[str, Any], type_key_determination: TypeKeyDetermination) -> Storage:
    sub_storage = Storage()
    for key, raw_value in value.items():
        type_key_value: dict[TypeKey, Any] = type_key_determination(key, raw_value)
        assert len(type_key_value) == 1
        type_key, sub_value = next(iter(type_key_value.items()))
        transformed_value = standard_value_conversion(type_key.type, sub_value, type_key_determination)
        sub_storage[type_key] = transformed_value
    sub_storage.make_immutable()
    return sub_storage


def standard_value_conversion_single(value_type: str, value: Any, type_key_determination: TypeKeyDetermination) -> Any:
    advanced_converters = {
        types.SubStorage: standard_subobject_converter,
        types.Matrix: standard_matrix_converter
    }
    converters = {
        types.Date: standard_date_converter,
        types.Reference: Reference.from_str,
        types.Bool: standard_bool_converter,
        types.Business: standard_business_converter,
        types.Calendar: standard_calendar_converter,
        types.Period: standard_period_converter,
    }
    if value_type in advanced_converters:
        return advanced_converters[value_type](value, type_key_determination)
    if value_type in converters:
        return converters[value_type](value)
    return value
