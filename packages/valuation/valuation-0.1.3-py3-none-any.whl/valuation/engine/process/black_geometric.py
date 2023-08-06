from __future__ import annotations

from typing import Callable, Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.consts.pl import PathSeparatedValue, PathValue
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.check import Range
from valuation.engine.exceptions import UnsupportedProcessError, DAARuntimeException
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, QLPathGenerator, path_generator_factory
from valuation.universal_output import result_items
from valuation.utils.other import is_nan

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.universal_transfer import DefaultParameters, Storage
    from valuation.engine.utils import StockDividends


# Geometric Brownian Motion:
# dS(t, S) = \mu S dt + \sigma S dW


class QLSimpleBlackProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.simple_black
    _supported_greeks = (result_items.Rho, result_items.Vega)
    _market_data_types = [signatures.fx_rate.all]

    @property
    def drift(self) -> float:
        return self._drift

    @property
    def volatility(self) -> float:
        return self._volatility

    @property
    def scenario_divisor(self) -> float:
        return self._scenario_divisor

    @property
    def shift_unit(self) -> int:
        return 100

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._volatility: float = self.data(fields.VolatilityValue, check=Range(lower=0.0, upper=global_parameters.VolatilityMaximum))
        self._drift: float = self.data(fields.Drift, check=Range(lower=global_parameters.InterestRateMinimum, upper=global_parameters.InterestRateMaximum))
        if __debug__:
            self._scenario_divisor: float = float('NaN')
            self._original_value: float = float('NaN')

        if not self._documentation_mode:
            md_name: str = self._attached_market_data.reference.id
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {0: md_name + PathSeparatedValue}
            aliases: dict[str, str] = {md_name: md_name + PathSeparatedValue,
                                       PathValue: md_name + PathSeparatedValue}
            allow_discount: set[str] = set()
            stock_modifier: dict[str, StockDividends] = {}
            summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _generate_process(self) -> ql.StochasticProcess:
        # SWIGs\stochasticprocess.i
        # GeometricBrownianMotionProcess  --> None
        # 		initialValue	Real
        # 		mu	Real
        # 		sigma	Real
        return ql.GeometricBrownianMotionProcess(self._attached_market_data[self._valuation_date], self._drift, self._volatility)

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Rho:
            return ['drift']
        if greek == result_items.Vega:
            return [result_items.Vega]
        raise ProgrammingError()

    def _change_to(self, scenario: str, shift: float) -> None:
        assert is_nan(self._original_value)
        if scenario == 'drift':
            self._scenario_divisor = shift
            self._original_value = self._drift
            self._drift += self._scenario_divisor / self.shift_unit
        elif scenario == result_items.Vega:
            if shift <= -1 * self._volatility * self.shift_unit:
                raise DAARuntimeException(f'Greek/Range calc: Negative {shift = } leads to nonpositive volatility')
            self._scenario_divisor = shift
            self._original_value = self._volatility
            self._volatility += self._scenario_divisor / self.shift_unit
        else:
            raise ProgrammingError()

    def _change_back(self, scenario: str) -> None:
        if scenario == 'drift':
            self._drift = self._original_value
        elif scenario == result_items.Vega:
            self._volatility = self._original_value
        else:
            raise ProgrammingError()
        if __debug__:
            self._original_value = float('NaN')
            self._scenario_divisor = float('NaN')

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        # TODO(2021/11) This part of the code is apparently completely untested as the the ql.GeometricBrownianMotionProcess is no ql.GeneralizedBlackScholesProcess
        #  Raises: Wrong number or type of arguments for overloaded function 'new_AnalyticEuropeanEngine'
        #  Solution: Replace ql.GeometricBrownianMotionProcess by ql.BlackScholesProcess
        #  It is also doubtful if this process can be used for fx options
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib)
        if ql_instrument.signature == signatures.instrument.fx_european_option:  # pylint: disable=unreachable
            # SWIGs\options.i
            # 	AnalyticEuropeanEngine --> None
            # 		[UNKNOWN]	<GeneralizedBlackScholesProcess>
            engine = ql.AnalyticEuropeanEngine(self._generate_process())
            return engine, None
        if ql_instrument.signature == signatures.instrument.fx_continuous_barrier_option:
            if ql_instrument.double_barrier:
                # SWIGs\options.i
                # 	AnalyticDoubleBarrierEngine --> None
                # 		process	<GeneralizedBlackScholesProcess>
                # 		series	int		(5)
                # NOTE: the formula holds only when strike is in the barrier range
                engine = ql.AnalyticDoubleBarrierEngine(self._generate_process())
                return engine, None
            # SWIGs\options.i
            #   AnalyticBarrierEngine --> None
            # 		[UNKNOWN]	<GeneralizedBlackScholesProcess>
            engine = ql.AnalyticBarrierEngine(self._generate_process())
            return engine, None
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)
