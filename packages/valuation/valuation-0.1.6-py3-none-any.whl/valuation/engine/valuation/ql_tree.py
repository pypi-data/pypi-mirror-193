from __future__ import annotations

from typing import Any

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Range
from valuation.engine.valuation import QLValuation

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage
    from valuation.engine.utils import CashFlows, AdditionalBondCfInfo


class QLValuationTreeQuantlib(QLValuation):
    _signature = signatures.valuation.tree_quantlib
    _valuation_type = 'Tree'

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._maximal_time_stepping_in_days = self.data(fields.MaximalTimeSteppingInDaysMC, check=Range(lower=global_parameters.MaximalTimeSteppingInDaysMCMinimum), allow_fallback_to_default_parameters=True)

    def pv_and_cashflows(self) -> CashFlows:
        cash_flows = self._instrument.tree_ql_evaluate(self._maximal_time_stepping_in_days)
        return cash_flows

    def clean_dirty(self) -> CashFlows:
        return self._instrument.ql_clean_dirty()

    def additional_info(self) -> dict[str, Any]:
        return self._instrument.ql_additional_info()

    def additional_cashflow_info(self) -> list[AdditionalBondCfInfo]:
        return self._instrument.ql_additional_cashflow_info()
