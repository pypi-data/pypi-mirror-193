from __future__ import annotations

from dataclasses import dataclass

from valuation.universal_transfer.exceptions import UniversalTransferException


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=False, frozen=True)
class Reference:
    type: str
    id: str  # pylint: disable=invalid-name

    def __post_init__(self) -> None:
        assert isinstance(self.type, str)
        assert isinstance(self.id, str)

    def __str__(self) -> str:
        return f'{self.type}|{self.id}'

    def __hash__(self) -> int:
        return hash(bytes(f'{self.type}{self.id}', 'utf-8'))

    def __eq__(self, other):
        assert isinstance(other, Reference)
        return self.id == other.id and self.type == other.type

    def __gt__(self, other):
        assert isinstance(other, Reference)
        return str(self) > str(other)

    @staticmethod
    def from_str(value: str) -> Reference:
        try:
            object_type, object_id = value.split('|', 1)
        except ValueError as error:
            raise UniversalTransferException(value) from error
        except Exception as error:
            raise error
        return Reference(object_type, object_id)
