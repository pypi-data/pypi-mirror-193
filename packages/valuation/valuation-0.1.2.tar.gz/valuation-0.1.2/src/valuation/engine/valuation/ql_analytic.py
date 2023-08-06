from __future__ import annotations

from typing import Any

from valuation.consts import signatures
from valuation.global_settings import __type_checking__
from valuation.engine.valuation import QLValuation

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.utils import CashFlows, AdditionalBondCfInfo


class QLValuationAnalyticQuantlib(QLValuation):
    _signature = signatures.valuation.analytic_quantlib
    _valuation_type = 'Analytic'

    def pv_and_cashflows(self) -> CashFlows:
        return self._instrument.analytic_ql_evaluate()

    def clean_dirty(self) -> CashFlows:
        return self._instrument.ql_clean_dirty()

    def additional_info(self) -> dict[str, Any]:
        return self._instrument.ql_additional_info()

    def additional_cashflow_info(self) -> list[AdditionalBondCfInfo]:
        return self._instrument.ql_additional_cashflow_info()
