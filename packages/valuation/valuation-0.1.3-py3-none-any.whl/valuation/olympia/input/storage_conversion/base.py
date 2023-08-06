from __future__ import annotations

from typing import Any, Optional, Union

from valuation.consts import types
from valuation.consts import fields
from valuation.consts.fields import MatrixColumnHeaders, MatrixContent, MatrixRowHeaders
from valuation.consts.types import to_single_type
from daa_utils import Log
from valuation.olympia.input.mappings.request_keys import FIELDS, NON_ENGINE_FIELDS, check_and_make_greek_type, \
    MULTIPLE_MAPPED_KEYS, REFERENCES_INFERRED_BY_KEY
from valuation.olympia.input.storage_conversion.conversion.type_key_determination import storage_preparation, type_determination
from valuation.olympia.input.storage_conversion.conversion.value_conversion import value_conversion
from valuation.universal_transfer import Storage, TypeKey
from valuation.utils.other import listify


KNOWN_FIELDS: dict[str, TypeKey] = {value.key: value for _, value in fields.__dict__.items() if isinstance(value, TypeKey)}
MATRIX_KEYS: list[str] = [MatrixRowHeaders, MatrixColumnHeaders, MatrixContent, 'points']


def cast_single_value(type_key: TypeKey, value: Any) -> Any:
    if type_key.type in [types.Str, types.Reference]:
        return str(value)
    if type_key.type == types.Float:
        return float(value)
    if type_key.type == types.Int:
        return int(value)
    if type_key.type == types.Bool:
        if isinstance(value, (int, float)):
            return bool(value)
        return value
    return value


def cast_list_values(type_key: TypeKey, values: Optional[list[Any]]) -> list[Any]:
    single_type = TypeKey.from_str(to_single_type(str(type_key)))
    value_list: list[Any] = listify(values)
    return [cast_single_value(single_type, value) for value in value_list]


class OlympiaStorage(Storage):

    def __init__(self, raw_data: dict[str, Any], shorten_print: bool = False) -> None:
        super().__init__(mutable_substorages=True, shorten_print=shorten_print)
        self._raw_data = raw_data
        self._convert()

    def _convert(self) -> None:
        prepared_content = storage_preparation(self._raw_data)
        typed_content = self._type_key_determination(prepared_content)
        for key, value in typed_content.items():
            new_value = value_conversion(key, value, self._type_key_determination)
            self[key] = new_value

    def _type_key_determination(self, key_or_dict: Union[str, dict[str, Any]], value: Any = None) -> dict[TypeKey, Any]:
        if isinstance(key_or_dict, TypeKey):
            return {key_or_dict: value}
        if isinstance(key_or_dict, dict):
            return dict(type_key_value_pair for typed_key_dict in [self._type_key_determination(key, value) for key, value in key_or_dict.items()] for type_key_value_pair in typed_key_dict.items())
        key: str = key_or_dict
        if isinstance(value, list) and not value:
            return {}

        if key in REFERENCES_INFERRED_BY_KEY:
            value = REFERENCES_INFERRED_BY_KEY[key](str(value))

        if key in KNOWN_FIELDS:
            type_key: Union[TypeKey, list[TypeKey]] = KNOWN_FIELDS[key]
        elif key in FIELDS:
            type_key = FIELDS[key]
        elif key in MULTIPLE_MAPPED_KEYS:
            type_key = MULTIPLE_MAPPED_KEYS[key]
            return self._type_key_determination({tk: value for tk in type_key})
        elif key in MATRIX_KEYS:
            type_key = TypeKey(type_determination(value), key)
        elif key in NON_ENGINE_FIELDS:
            type_key = NON_ENGINE_FIELDS[key]
        elif 'schedule' in key:
            suffix = key.replace('schedule', '')
            type_key = fields.Schedule(suffix)
        else:
            possible_greek_type = check_and_make_greek_type(key)
            if possible_greek_type:
                type_key = possible_greek_type
            else:
                Log.critical(f'Unknown input key "{key}"')
                return {}
        if types.is_list(type_key.type):
            if type_key.fall_back_to_single:
                return {type_key.as_list(): cast_list_values(type_key, value)}
            return {type_key: cast_list_values(type_key, value)}
        if isinstance(value, list):
            return {TypeKey(types.to_list_type(type_key.type), type_key.key): cast_list_values(type_key, value)}
        return {type_key: cast_single_value(type_key, value)}
