from __future__ import annotations

from typing import Any, Optional

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ContainedIn, Range
from valuation.engine.valuation import QLValuation

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage
    from valuation.engine.utils import CashFlows


class QLValuationFinancialProgram(QLValuation):         # pylint: disable=abstract-method
    _signature = signatures.valuation.financial_program
    _valuation_type = 'MC'

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._maximal_time_stepping_in_days: float = self.data(fields.MaximalTimeSteppingInDaysMC, check=Range(lower=global_parameters.MaximalTimeSteppingInDaysMCMinimum), allow_fallback_to_default_parameters=True)
        self._continuous_time_stepping_in_days: float = self.data(fields.ContinuousTimeSteppingInDaysMC, check=Range(lower=global_parameters.ContinuousTimeSteppingInDaysMCMinimum), allow_fallback_to_default_parameters=True)
        self._log_number_of_paths: int = self.data(fields.LogNumberOfPaths, check=Range(lower=0, upper=global_parameters.LogNumberOfPathsMaximum, strict=False), allow_fallback_to_default_parameters=True)
        self._generator_type: str = self.data(fields.RandomGeneratorType, check=ContainedIn(('Standard', 'Sobol')), allow_fallback_to_default_parameters=True)
        self._brownian_bridge: bool = self.data(fields.BrownianBridge, allow_fallback_to_default_parameters=True)
        self._antithetic: bool = self.data(fields.Antithetic, allow_fallback_to_default_parameters=True)
        self._tolerance_for_equality: Optional[float] = self.data(fields.ToleranceForEquality, default_value=0.0, check=Range(lower=0.0, upper=global_parameters.ToleranceForEqualityMaximum, strict=False), allow_fallback_to_default_parameters=True) or None
        self._enable_broadie_glassermann: bool = self.data(fields.EnableBroadieGlassermann, default_value=True)

    def pv_and_cashflows(self) -> CashFlows:
        cash_flows = self._instrument.financial_program_evaluate(self._maximal_time_stepping_in_days, self._continuous_time_stepping_in_days, self._log_number_of_paths, self._generator_type, self._brownian_bridge, self._antithetic, self._tolerance_for_equality, self._enable_broadie_glassermann)
        return cash_flows

    def additional_info(self) -> dict[str, Any]:
        return self.additional_info()
