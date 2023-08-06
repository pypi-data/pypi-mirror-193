from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from valuation.consts import types
from valuation.consts.types import is_list, is_single, to_list_type, to_single_type
from valuation.exceptions import ProgrammingError


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=False, frozen=True)
class TypeKey:
    type: str
    key: str             # pylint: disable=invalid-name
    fall_back_to_single: bool = False
    fall_back_to_storage: bool = False
    allow_data_only_mode: bool = False

    @property
    def flex(self) -> str:
        return f'{self.key}__{self.type}'

    @property
    def is_simple(self) -> bool:
        return not self.fall_back_to_single

    def __post_init__(self) -> None:
        assert not self.fall_back_to_single or is_list(self.type)
        assert not (self.fall_back_to_single and self.fall_back_to_storage)
        assert not (self.allow_data_only_mode and self.type not in (types.Reference, types.References))

    def as_single(self) -> TypeKey:
        assert self.fall_back_to_single
        return TypeKey(to_single_type(self.type), self.key)

    def as_list(self) -> TypeKey:
        assert self.fall_back_to_single
        return TypeKey(self.type, self.key)

    def as_list_or_single(self) -> TypeKey:
        return TypeKey(to_list_type(self.type), self.key) if (is_single(self.type) or is_list(self.type)) else TypeKey('DUMMY', 'DUMMY')

    def as_storage(self) -> TypeKey:
        assert self.fall_back_to_storage
        assert self.type in (types.Reference, types.References)
        if is_list(self.type):
            return TypeKey(types.Storages, self.key)
        return TypeKey(types.Storage, self.key)

    def as_reference(self) -> TypeKey:
        assert self.fall_back_to_storage
        assert self.type in (types.Reference, types.References)
        return TypeKey(self.type, self.key)

    def as_storage_or_reference(self) -> TypeKey:
        if self.type not in (types.References, types.Storages, types.Reference, types.Storage):
            return TypeKey('DUMMY', 'DUMMY')
        if is_list(self.type):
            return TypeKey(types.References, self.key)
        return TypeKey(types.Reference, self.key)

    def __hash__(self) -> int:
        return hash(f'{self.key}({self.type})')

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TypeKey):
            raise ProgrammingError()
        return self.type == other.type and self.key == other.key

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, TypeKey):
            raise ProgrammingError()
        return (self.type, self.key) < (other.type, other.key)

    def __str__(self) -> str:
        if self.fall_back_to_single:
            type_attribute: str = f'{to_single_type(self.type)}|{self.type}'
        else:
            type_attribute = self.type
        if self.fall_back_to_storage:
            if is_list(self.type):
                type_attribute = f'{self.type}|{types.Storages}'
            else:
                type_attribute = f'{self.type}|{types.Storage}'
        return f'{self.key}({type_attribute})'

    def __copy__(self) -> TypeKey:
        return TypeKey(self.type, self.key, self.fall_back_to_single, self.fall_back_to_storage, self.allow_data_only_mode)

    @staticmethod
    def from_str(value: str) -> TypeKey:
        assert value[-1] == ')', f"""TypeKey needs to be of format "{str(TypeKey('<Key>', '<Type>'))}" and not "{value}\""""

        assert value.count('(') == 1, f"""TypeKey needs to be of format "{str(TypeKey('<Key>', '<Type>'))}" and not "{value}\""""

        object_key, object_type = value[:-1].split('(')
        return TypeKey(object_type, object_key)

    @staticmethod
    def from_flex(value: str) -> TypeKey:
        object_key, object_type = value.split('__')
        return TypeKey(object_type, object_key)
