from __future__ import annotations

from typing import Any

from valuation.consts import signatures
from valuation.global_settings import __type_checking__
from valuation.engine.valuation import QLValuation

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.utils import CashFlows


class QLValuationAnalytic(QLValuation):     # pylint: disable=abstract-method
    _signature = signatures.valuation.analytic
    _valuation_type = 'Analytic'

    def pv_and_cashflows(self) -> CashFlows:
        return self._instrument.analytic_evaluate()

    def additional_info(self) -> dict[str, Any]:
        return self._instrument.additional_info()
