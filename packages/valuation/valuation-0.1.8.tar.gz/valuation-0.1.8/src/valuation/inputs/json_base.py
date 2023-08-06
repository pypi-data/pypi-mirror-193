from __future__ import annotations

from typing import Any, Optional

from valuation.consts import types
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import Reference, Storage, StorageDataBase

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.inputs.standard import TypeKeyDetermination, ValueConversion


def json2storage_db(data: dict[str, Any], type_key_determination: TypeKeyDetermination, value_conversion: ValueConversion) -> StorageDataBase:
    result: StorageDataBase = StorageDataBase()
    for object_reference, object_description in data.items():
        result.add(json2storage(object_reference, object_description, type_key_determination, value_conversion))
    return result


def json2storage(object_reference_str: Optional[str], object_description: Any, type_key_determination: TypeKeyDetermination, value_conversion: ValueConversion) -> Storage:
    storage: Storage = Storage()
    if object_reference_str is not None:
        storage.assign_reference(Reference.from_str(object_reference_str))
    for key, raw_value in object_description.items():
        for type_key, value in type_key_determination(key, raw_value).items():
            if type_key.type == types.Storage:
                transformed_value: Any = json2storage(None, value, type_key_determination, value_conversion)
            elif type_key.type == types.Storages:
                transformed_value = tuple(json2storage(None, sub_storage_raw, type_key_determination, value_conversion) for sub_storage_raw in value)
            else:
                transformed_value = value_conversion(type_key.type, value, type_key_determination)
            storage[type_key] = transformed_value
    storage.make_immutable()
    return storage
