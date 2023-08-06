from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class Signature:
    type: str
    sub_type: str = ''
    ALL: ClassVar[str] = '*'            # pylint: disable=invalid-name

    def __post_init__(self) -> None:
        assert isinstance(self.type, str), f'{self.type} is of type {type(self.type)}'

        assert isinstance(self.sub_type, str), f'{self.sub_type} is of type {type(self.sub_type)}'

    def __str__(self) -> str:
        if self.sub_type == self.ALL:
            return self.type
        return f'{self.type}[{self.sub_type}]'

    def __contains__(self, item: Signature) -> bool:
        if self.sub_type != Signature.ALL:
            return self == item
        return item.type == self.type

    def specify_sub_type(self, sub_type: str) -> Signature:
        assert self.sub_type == self.ALL
        return Signature(self.type, sub_type)

    @staticmethod
    def from_str(value: str) -> Signature:
        if '[' in value:
            object_type, sub_type = value[:-1].split('[')
            return Signature(object_type, sub_type)
        return Signature(value)
