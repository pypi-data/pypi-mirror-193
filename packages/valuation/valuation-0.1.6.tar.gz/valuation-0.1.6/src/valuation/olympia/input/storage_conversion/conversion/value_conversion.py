from __future__ import annotations

from typing import Any, Callable, Optional, Union

from valuation.consts import types
from valuation.consts import fields
from daa_utils import Log
from valuation.global_settings import __type_checking__
from valuation.inputs.standard import standard_business_converter, standard_calendar_converter, standard_period_converter, standard_value_conversion_single
from valuation.olympia.input.mappings.financial import BUSINESS_MAP, CALENDAR_MAP, PERIOD_MAP, day_count_converter, \
    ACCRUAL_BUSINESS_MAP, DATE_GENERATION_MAP
from valuation.olympia.input.mappings.request_keys import MatrixKeys, OlympiaMappingError, Strings, field2object
from valuation.olympia.input.storage_conversion.conversion.type_key_determination import type_determination
from valuation.universal_transfer import Matrix, Reference, Storage, StorageTypes, TypeKey
from valuation.universal_transfer.finance_types import Calendars
from valuation.olympia.input.market_data_connection.olympia_market_data_hub_v2 import market_data_links

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer.finance_types import Calendar, BusinessConvention
    from valuation.universal_transfer.storage import Period

TypeKeyDetermination = Callable[[Union[str, dict[str, Any]], Optional[Any]], dict[TypeKey, Any]]
ValueConversion = Callable[[TypeKey, Any, TypeKeyDetermination], Any]


def reference_conversion(type_key: TypeKey, value: str) -> Reference:
    if value.startswith(market_data_links.MDH_PREFIX_SCHEME):
        return market_data_links.OlympiaMarketDataHubReference.from_str(value)
    if '|' in value:
        return Reference.from_str(value)
    try:
        object_type: str = field2object(type_key.key)
        return Reference(object_type, value)
    except OlympiaMappingError as exception:
        example_reference = Reference('ObjectType', 'ObjectID')
        if type_key.key.lower() == 'marketdata':
            raise OlympiaMappingError(f'Field value {value} associated to {type_key} is not of the required form {example_reference}')  # pylint: disable=raise-missing-from
        raise OlympiaMappingError(f'Could not generate reference of pattern {example_reference} from field: {type_key} and associated value: {value}') from exception  # pylint: disable=bad-exception-context


def str_conversion(value: str) -> str:
    if value in Strings:
        return Strings[value]
    return value


TARGET_OVERRIDE: bool = True


def calendar_conversion(value: str) -> Calendar:
    if value in Calendars:
        return value
    if value in CALENDAR_MAP:
        return CALENDAR_MAP[value]
    # TODO(2021/10) The following line destroys already valid input like 'EUR' or 'USD' (it returns 'Eur' and 'Usd'). Do we need this?
    value = ''.join([sub_item[0].upper() + sub_item[1:].lower() for sub_item in value.split('_')])
    if value in Calendars:
        return value
    try:
        new_value: str = CALENDAR_MAP[value]
        return standard_calendar_converter(new_value)
    except KeyError as error:
        if TARGET_OVERRIDE:
            Log.warning('Unknown calendar: {}. TARGET applied.'.format(value))
            return CALENDAR_MAP['TARGET']
        raise OlympiaMappingError('Unknown calendar format: {}'.format(value)) from error


def _business_conversion(value: str, mapping: dict[str, str]) -> BusinessConvention:
    try:
        new_value: str = mapping[value]
        return standard_business_converter(new_value)
    except KeyError as error:
        raise OlympiaMappingError('Unknown business convention format: {}'.format(value)) from error


def business_conversion(value: str) -> BusinessConvention:
    return _business_conversion(value, BUSINESS_MAP)


def accrual_business_conversion(value: str) -> BusinessConvention:
    return _business_conversion(value, ACCRUAL_BUSINESS_MAP)


def date_generation_conversion(value: str) -> str:
    try:
        new_value: str = DATE_GENERATION_MAP[value.upper()]
        return standard_business_converter(new_value)
    except KeyError as error:
        raise OlympiaMappingError('Unknown date generation: {}'.format(value)) from error


def day_count_conversion(value: str) -> str:
    return day_count_converter(value)


def period_conversion(value: str) -> Period:
    return standard_period_converter(PERIOD_MAP.get(value.upper(), value))


# Todo (2020/12) The next two functions are almost identical, remove code duplication!
def sub_storage_conversion(value: dict[str, Any], val_conversion: ValueConversion,
                           type_key_determination: TypeKeyDetermination) -> Storage:
    sub_storage = Storage(mutable_substorages=True)
    for key, raw_value in value.items():
        if raw_value is None:
            Log.critical(f'Value for "{key}" is None')
            continue
        type_key_value = type_key_determination(key, raw_value)
        if len(type_key_value) != 1:
            continue
        type_key, sub_value = next(iter(type_key_value.items()))
        transformed_value = val_conversion(type_key, sub_value, type_key_determination)
        sub_storage[type_key] = transformed_value
    return sub_storage


def storage_conversion(value: dict[str, Any], val_conversion: ValueConversion,
                       type_key_determination: TypeKeyDetermination) -> Storage:
    sub_storage = Storage(mutable_substorages=True)
    for key, raw_value in value.items():
        if raw_value is None:
            Log.critical(f'Value for "{key}" is None')
            continue
        type_key_value = type_key_determination(key, raw_value)
        if len(type_key_value) != 1:
            continue
        type_key, sub_value = next(iter(type_key_value.items()))
        transformed_value = val_conversion(type_key, sub_value, type_key_determination)
        sub_storage[type_key] = transformed_value
    return sub_storage


def matrix_points_type_determination(points: list[dict[str, Any]]) -> str:
    single_types: set[str] = {
        type_determination(item[MatrixKeys.Point]) for item in points
    }

    assert len(single_types) == 1
    return types.to_matrix_type(next(iter(single_types)))


def matrix_conversion(value: dict[str, Any], conversion: ValueConversion, type_key_determination: TypeKeyDetermination) -> Matrix:
    data: dict[TypeKey, Any] = type_key_determination(value)  # type: ignore[call-arg]

    column_headers: Optional[StorageTypes.SimpleList] = None
    row_headers: Optional[StorageTypes.SimpleList] = None
    column_header_type: Optional[str] = None
    row_header_type: Optional[str] = None
    matrix_type: Optional[str] = None
    raw_matrix: list[list[Any]] = []
    original_column_headers: Optional[StorageTypes.SimpleList] = None
    original_row_headers: Optional[StorageTypes.SimpleList] = None

    for type_key, raw_value in data.items():
        key: str = type_key.key
        if key == MatrixKeys.RowHeaders:
            row_header_type = type_key.type
            original_row_headers = raw_value
            row_headers = conversion(type_key, raw_value, type_key_determination)
        elif key == MatrixKeys.ColumnHeaders:
            column_header_type = type_key.type
            original_column_headers = raw_value
            column_headers = conversion(type_key, raw_value, type_key_determination)

    # if any(identifier is None for identifier in ())
    def assert_msg(matrix_item: str, msg: str = 'assert not None!') -> str:
        return f'{msg} failed for {matrix_item}'
    assert column_headers is not None, assert_msg(MatrixKeys.ColumnHeaders)
    assert row_headers is not None, assert_msg(MatrixKeys.RowHeaders)
    assert column_header_type is not None, assert_msg(MatrixKeys.ColumnHeader)
    assert row_header_type is not None, assert_msg(MatrixKeys.RowHeader)
    assert original_row_headers is not None, assert_msg(f'Raw {MatrixKeys.RowHeaders}')
    assert original_column_headers is not None, assert_msg(f'Raw {MatrixKeys.ColumnHeaders}')

    for type_key, raw_value in data.items():
        key = type_key.key
        if key == MatrixKeys.Content:
            na_values: dict[str, Any] = {
                types.FloatMatrix: float('nan'),
                types.IntMatrix: float('nan'),
            }
            matrix_type = matrix_points_type_determination(raw_value)
            nan: Any = na_values.get(matrix_type)

            raw_matrix = [[nan for _ in range(len(column_headers))] for _ in range(len(row_headers))]
            try:
                for point in raw_value:
                    row_idx: int = original_row_headers.index(point[MatrixKeys.RowHeader])
                    col_idx: int = original_column_headers.index(point[MatrixKeys.ColumnHeader])
                    raw_matrix[row_idx][col_idx] = point[MatrixKeys.Point]
            except Exception as exception:
                matrix_print = '\n'.join([
                    'first raw row:\t' + '|'.join(str(value) for value in original_row_headers[:1]),
                    f'first converted row ({row_header_type}):\t' + '|'.join(str(value) for value in row_headers[:1]),
                    'first 2 raw columns:\t' + '|'.join(str(value) for value in original_column_headers[:2]),
                    f'first 2 converted columns ({column_header_type}):\t' + '|'.join(str(value) for value in column_headers[:2]),
                    'first 2 raw values: \n' + '\n'.join([str(value) for value in raw_value[:2]])
                ])
                new_exception = OlympiaMappingError(f'Error during generation of matrix:\n{matrix_print}')
                Log.error(str(new_exception))
                raise new_exception from exception
    assert len(raw_matrix) > 1, assert_msg(f'{raw_matrix}', msg='len(raw_matrix_items) > 1')
    assert matrix_type is not None, assert_msg('matrix type')

    return Matrix(
        column_headers, row_headers, tuple(tuple(i for i in row) for row in raw_matrix),
        column_header_type, row_header_type, matrix_type,
    )


def value_conversion(type_key: TypeKey, value: Any, type_key_determination: TypeKeyDetermination) -> Any:

    type_key_dependant_conversions = {
        fields.DateGeneration: date_generation_conversion,
        fields.AccrualBusiness: accrual_business_conversion
    }

    type_dependent_conversions = {
        types.Reference: reference_conversion,
    }

    conversions = {
        types.Str: str_conversion,
        types.Calendar: calendar_conversion,
        types.DayCount: day_count_conversion,
        types.Business: business_conversion,
        types.Period: period_conversion
    }

    advanced_conversions = {
        types.Storage: storage_conversion,
        types.SubStorage: sub_storage_conversion,
        types.Matrix: matrix_conversion
    }

    if types.is_single(type_key.type):
        if type_key in type_key_dependant_conversions:
            return type_key_dependant_conversions[type_key](value)
        if type_key.type in conversions:
            return conversions[type_key.type](value)
        if type_key.type in type_dependent_conversions:
            return type_dependent_conversions[type_key.type](type_key, value)
        if type_key.type in advanced_conversions:
            return advanced_conversions[type_key.type](value, value_conversion, type_key_determination)
        return standard_value_conversion_single(types.to_single_type(type_key.type), value, type_key_determination)
    single_type = TypeKey(types.to_single_type(type_key.type), type_key.key)
    return tuple(value_conversion(single_type, entry, type_key_determination) for entry in value)
