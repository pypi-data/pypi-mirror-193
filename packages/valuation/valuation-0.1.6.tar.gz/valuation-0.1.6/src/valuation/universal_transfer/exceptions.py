from __future__ import annotations

from typing import Any

from valuation.exceptions import DAAException
from valuation.global_settings import __type_checking__

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import TypeKey


class UniversalTransferException(DAAException):
    pass


class TypeDiscrepancyError(UniversalTransferException):
    def __init__(self, type_key: TypeKey, value: Any, supposed_type: type[Any]) -> None:
        super().__init__()
        self._type_key: TypeKey = type_key
        self._value: Any = value
        self._supposed_type: type[Any] = supposed_type
        self.args = (f'{self._type_key}: {self._value} is of type {type(self._value)} and not {self._supposed_type}', )


class UnknownFinancialConstant(UniversalTransferException):
    def __init__(self, type_key: TypeKey, value: Any) -> None:
        super().__init__()
        self._type_key: TypeKey = type_key
        self._value: Any = value
        self.args = (f'{self._type_key}: {self._value} is not in the set of known conventions for {self._type_key.type}', )


class InvalidAccessError(UniversalTransferException):
    def __init__(self, key: Any, accessed_object: Any) -> None:
        super().__init__()
        self._key: Any = key
        self._accessed_object: Any = accessed_object
        self.args = (f'{self._key} not in {self._accessed_object}', )
