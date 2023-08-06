from __future__ import annotations

from typing import Any

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.function import QLFunction

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import DefaultParameters, Storage
    from valuation.engine import QLObjectDB


class QLFunctionConstant(QLFunction):                             # pylint: disable=abstract-method
    _signature = signatures.function.constant

    @property
    def return_type(self) -> str:
        return types.Float

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._value: float = self.data(fields.Value)

    def __call__(self, key: Any) -> Any:
        return self._value
