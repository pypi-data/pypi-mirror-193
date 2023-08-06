from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Range
from valuation.engine.optimization import QLOptimize
from valuation.universal_transfer import DefaultParameters, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB


class QLLevenbergMarquardtBase(QLOptimize):                             # pylint: disable=abstract-method

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._epsfcn: float
        self._xtol: float
        self._gtol: float
        self._max_iteration: int
        self._max_stationary_state_iterations: int
        self._root_epsilon: float
        self._function_epsilon: float
        self._gradient_epsilon: float

    def _post_init(self) -> None:
        # SWIGs\optimizers.i
        # 	LevenbergMarquardt --> None
        # 		epsfcn	Real		(1.0e-8)
        # 		xtol	Real		(1.0e-8)
        # 		gtol	Real		(1.0e-8)
        # 		useCostFunctionsJacobian	bool		(false)
        self._method = ql.LevenbergMarquardt(  # pylint: disable=attribute-defined-outside-init
            self._epsfcn,
            self._xtol,
            self._gtol)
        # SWIGs\optimizers.i
        # 	EndCriteria --> None
        # 		maxIteration	Size
        # 		maxStationaryStateIterations	Size
        # 		rootEpsilon	Real
        # 		functionEpsilon	Real
        # 		gradientNormEpsilon	Real
        self._end_criteria = ql.EndCriteria(  # pylint: disable=attribute-defined-outside-init
            self._max_iteration,
            self._max_stationary_state_iterations,
            self._root_epsilon,
            self._function_epsilon,
            self._gradient_epsilon)


class QLLevenbergMarquardt(QLLevenbergMarquardtBase):                             # pylint: disable=abstract-method
    _signature = signatures.optimize.levenberg_marquardt

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._epsfcn: float = self.data(fields.LBOptFunctionEpsilon, default_value=1e-8, check=Range(lower=0.0))
        self._xtol: float = self.data(fields.LBOptToleranceVariable, default_value=1e-8, check=Range(lower=0.0))
        self._gtol: float = self.data(fields.LBOptToleranceGradient, default_value=1e-8, check=Range(lower=0.0))
        self._max_iteration: int = self.data(fields.LBEndMaxIteration, default_value=10000, check=Range(lower=0))
        self._max_stationary_state_iterations: int = self.data(fields.LBEndMaxStationaryIteration, default_value=100, check=Range(lower=0, upper=self._max_iteration))
        self._root_epsilon: float = self.data(fields.LBEndRootEpsilon, default_value=1e-6, check=Range(lower=0.0))
        self._function_epsilon: float = self.data(fields.LBEndFunctionEpsilon, default_value=1e-8, check=Range(lower=0.0))
        self._gradient_epsilon: float = self.data(fields.LBEndGradientEpsilon, default_value=1e-8, check=Range(lower=0.0))


class QLLevenbergMarquardtFast(QLLevenbergMarquardtBase):  # pylint: disable=abstract-method
    _signature = signatures.optimize.levenberg_marquardt_fast

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._epsfcn: float = self.data(fields.LBOptFunctionEpsilon, default_value=1e-6, check=Range(lower=0.0))
        self._xtol: float = self.data(fields.LBOptToleranceVariable, default_value=1e-6, check=Range(lower=0.0))
        self._gtol: float = self.data(fields.LBOptToleranceGradient, default_value=1e-6, check=Range(lower=0.0))
        self._max_iteration: int = self.data(fields.LBEndMaxIteration, default_value=100, check=Range(lower=0))
        self._max_stationary_state_iterations: int = self.data(fields.LBEndMaxStationaryIteration, default_value=10, check=Range(lower=0))
        self._root_epsilon: float = self.data(fields.LBEndRootEpsilon, default_value=1e-4, check=Range(lower=0.0))
        self._function_epsilon: float = self.data(fields.LBEndFunctionEpsilon, default_value=1e-6, check=Range(lower=0.0))
        self._gradient_epsilon: float = self.data(fields.LBEndGradientEpsilon, default_value=1e-6, check=Range(lower=0.0))
