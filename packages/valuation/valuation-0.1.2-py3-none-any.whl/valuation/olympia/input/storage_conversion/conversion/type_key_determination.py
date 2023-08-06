from functools import singledispatch, wraps
from typing import Any, Callable, Union

from valuation.consts import types
from valuation.inputs.standard import standard_bool_converter
from valuation.olympia.input.exception import OlympiaImportError
from valuation.olympia.input.mappings.conversion import is_date, is_period
from valuation.olympia.input.mappings.request_keys import FIELDS, MatrixKeys, TermKeys
from valuation.universal_transfer import TypeKey, Reference


# Todo: (2021/08) There does not seem to be a test case, which covers this part of code.
# Todo: (2021/08) Nested "for" in dictionary comprehension makes this incredibly hard to read and understand. Consider changing.
def serialize_with_dict(func: Callable[[str, Any], dict[Any, TypeKey]]) -> Callable[[tuple[Any, ...]], dict[TypeKey, Any]]:
    """
    Decorator to serialize a function that takes key, value as args and returns a dict
    """
    @wraps(func)
    def helper(*args: Any) -> dict[TypeKey, Any]:
        if len(args) == 1 and isinstance(args[0], dict):
            return dict(item for d in [func(key, val) for key, val in args[0].items()] for item in d.items())
        if len(args) == 2:
            return func(*args)
        raise Exception
    return helper


@serialize_with_dict
def type_key_determination(key_or_dict: Union[str, dict[str, Any]], value: Any = None) -> dict[TypeKey, Any]:
    assert isinstance(key_or_dict, str), str(type(key_or_dict))
    key: str = key_or_dict
    if isinstance(value, list) and not value:
        return {}
    try:
        type_key: TypeKey = FIELDS[key]
        if isinstance(value, list):
            return {TypeKey(types.to_list_type(type_key.type), type_key.key): value}
        return {type_key: value}
    except KeyError as error:
        if __debug__:
            if key_or_dict in MatrixKeys.get_all() + TermKeys.get_all():
                return {TypeKey(type_determination(value), key): value}
            raise OlympiaImportError('Unknown key in request: {}'.format(key)) from error
        return {TypeKey(type_determination(value), key): value}


def storage_preparation(pre_storage: dict[str, Any]) -> dict[str, Any]:
    # check for matrix
    if all(identifier in pre_storage for identifier in (MatrixKeys.RowHeaders, MatrixKeys.ColumnHeaders, MatrixKeys.Content)):
        to_matrix(pre_storage)
    elif any(identifier in pre_storage for identifier in (MatrixKeys.RowHeaders, MatrixKeys.ColumnHeaders)):
        raise OlympiaImportError('Matrix structure requires: {}, {}, and {}'.format(MatrixKeys.RowHeaders, MatrixKeys.ColumnHeaders, MatrixKeys.Content))
    # check for term structure
    if TermKeys.Identifier in pre_storage:
        to_list(pre_storage)
    return pre_storage


def to_matrix(pre_storage: dict[str, Any]) -> None:
    matrix_keys = (MatrixKeys.RowHeaders, MatrixKeys.ColumnHeaders, MatrixKeys.Content)
    pre_storage[MatrixKeys.BucketName] = {key: pre_storage[key] for key in matrix_keys}
    for key in matrix_keys:
        del pre_storage[key]


def to_list(pre_storage: dict[str, Any]) -> None:

    pre_storage[TermKeys.Dates] = []
    pre_storage[TermKeys.Values] = []
    for item in pre_storage[TermKeys.Identifier]:
        pre_storage[TermKeys.Dates].append(item[TermKeys.Date])
        pre_storage[TermKeys.Values].append(item[TermKeys.Value])
    del pre_storage[TermKeys.Identifier]


@singledispatch
def type_determination(arg: Any) -> str:  # pylint: disable=unused-argument
    raise NotImplementedError(arg)


@type_determination.register(str)
def _(arg: str) -> str:  # pylint: disable=unused-argument
    converted = standard_bool_converter(arg)
    if isinstance(converted, bool):
        return types.Bool
    if is_date(arg):
        return types.Date
    if is_period(arg):
        return types.Period
    if '|' in arg:
        try:
            _ = Reference.from_str(arg)
            return types.Reference
        except Exception:
            # TODO: Warn
            return types.Str
    return types.Str


@type_determination.register(int)  # type: ignore[no-redef]
def _(arg: int) -> str:  # pylint: disable=unused-argument
    return types.Int


@type_determination.register(float)  # type: ignore[no-redef]
def _(arg: float) -> str:  # pylint: disable=unused-argument
    return types.Float


@type_determination.register(bool)  # type: ignore[no-redef]
def _(arg: bool) -> str:  # pylint: disable=unused-argument
    return types.Bool


# Todo: (2020/12) Storage/Substorage
#       FB: I am not sure if that would be the right place. Better make a dummy type types.Storage_or_Substorage and handle this later according to content.
@type_determination.register(dict)  # type: ignore[no-redef]
def _(arg: dict[Any, Any]) -> str:  # pylint: disable=unused-argument
    return types.Storage


@type_determination.register(list)  # type: ignore[no-redef]
def _(arg: list[Any]) -> str:
    # a rule for lists should be that they should never be empty. If an empty list is acceptable for the objects it's
    # handed to, the empty list should be defaulted for that object so that in that case no parameter is passed.
    # Otherwise the type determination is not possible.
    if not arg:
        raise OlympiaImportError('No empty lists allowed')
    list_types: list[str] = [type_determination(entry) for entry in arg]
    if len(set(list_types)) != 1:
        raise OlympiaImportError('Inconsistent list types')
    return list_types[0].upper()
