from __future__ import annotations

import QuantLib as ql

from valuation.global_settings import __type_checking__
from valuation.engine import QLObject
from valuation.universal_transfer import DefaultParameters, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB


class QLOptimize(QLObject):                 # pylint: disable=abstract-method

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._method: ql.OptimizationMethod
        self._end_criteria: ql.EndCriteria

    def method_criteria(self) -> tuple[ql.OptimizationMethod, ql.EndCriteria]:
        return self._method, self._end_criteria
