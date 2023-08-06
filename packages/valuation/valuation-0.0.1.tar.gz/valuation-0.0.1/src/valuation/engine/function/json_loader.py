from __future__ import annotations

import json
from typing import Any

from valuations.consts import signatures, types
from valuations.consts import fields
from valuations.global_settings import __type_checking__
from valuations.engine.base_object import single_convert
from valuations.engine.check import ContainedIn
from valuations.engine.exceptions import QLInputError
from valuations.engine.function import QLFunction

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuations.engine import QLObjectDB
    from valuations.universal_transfer import DefaultParameters, Storage


class QLFunctionJson(QLFunction):                   # pylint: disable=abstract-method
    _signature = signatures.function.json

    @property
    def return_type(self) -> str:
        return self._data_type

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._file_name: str = self.data(fields.FileName)
        self._data_type: str = self.data(fields.DataType, check=ContainedIn([types.Float, types.Int, types.Bool, types.Str, types.Date, types.Reference, types.Period, types.DayCount, types.Calendar]))
        self._json_data: dict[str, Any]

    def _post_init(self) -> None:
        with open(self._file_name) as file_handle:
            self._json_data = json.load(file_handle)

    def __call__(self, key: Any) -> Any:
        try:
            value = single_convert(self._data_type, self._json_data[str(key)], None, None, None, None, False)             # type: ignore[arg-type]
        except Exception as exception:
            raise QLInputError(self._file_name) from exception
        return value
