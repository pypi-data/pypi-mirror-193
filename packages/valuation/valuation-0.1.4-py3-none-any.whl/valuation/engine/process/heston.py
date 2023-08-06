from __future__ import annotations

from math import sqrt
from typing import Callable, Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.consts.pl import PathSeparatedRaw, PathSeparatedValue, PathSeparatedVolatility, PathValue, PathVolatility
from valuation.global_settings import __type_checking__
from valuation.engine.check import Range
from valuation.engine.exceptions import UnsupportedProcessError
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, QLPathGenerator, path_generator_factory
from valuation.universal_output import result_items
from valuation.universal_transfer import NoValue

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.universal_transfer import DefaultParameters, Storage, Signature
    from valuation.engine.utils import StockDividends


# Heston Model:
# dS(t, S) = \mu S dt + \sqrt{v} S dW_1
# dv(t, S) = \kappa (\theta - v) dt + \sigma \sqrt{v} dW_2
# dW_1 dW2 = \rho dt


class QLHestonProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.empty
    _initializes_past = False

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        # SWIGs\stochasticprocess.i
        # 	HestonProcess --> None
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		dividendTS	Handle<YieldTermStructure>
        # 		s0	Handle<Quote>
        # 		v0	Real
        # 		kappa	Real
        # 		theta	Real
        # 		sigma	Real
        # 		rho	Real

        self._volatility: float = self.data(fields.VolatilityValue, check=Range(lower=0.0, upper=global_parameters.VolatilityMaximum))
        self._kappa: float = self.data(fields.ReversionRate)
        self._theta: float = self.data(fields.LongTermVariance, check=Range(lower=0.0, upper=global_parameters.VolatilityMaximum))
        # Feller condition
        # 2 \kappa \theta > \sigma^2
        self._sigma: float = self.data(fields.VolOfVol, check=[Range(lower=0.0, upper=global_parameters.VolatilityMaximum), Range(upper=NoValue.apply(sqrt, 2.0 * self._kappa * self._theta))])
        self._rho: float = self.data(fields.SingleCorrelation, check=Range(lower=-1.0, upper=1.0))

    def _option_engine_pricer_analytic(self, ql_instrument: QLInstrument, vanilla_option: Optional[Signature], continuous_barrier_option: Optional[Signature]) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        if vanilla_option and ql_instrument.signature == vanilla_option:
            # SWIGs\options.i
            # 	HestonModel --> None
            # 		process	<HestonProcess>
            model = ql.HestonModel(self._generate_process())
            # SWIGs\options.i
            # 	AnalyticHestonEngine --> None
            # 		model	<HestonModel>
            # 		integrationOrder	Size		(144)
            engine = ql.AnalyticHestonEngine(model)
            return engine, None
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)


class QLHestonProcessFX(QLHestonProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.heston_fx
    _supported_greeks = (result_items.Vega,)
    _market_data_types = [signatures.fx_rate.standard, signatures.fx_rate.direct_parity]
    _initializes_past = False

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        if not self._documentation_mode:
            md_name: str = self._attached_market_data.reference.id
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {(0, 0): md_name + PathSeparatedValue,
                                                                   (0, 1): md_name + PathSeparatedVolatility}
            aliases: dict[str, str] = {md_name: md_name + PathSeparatedValue,
                                       PathValue: md_name + PathSeparatedValue,
                                       PathVolatility: md_name + PathSeparatedVolatility
                                       }
            allow_discount: set[str] = set()
            stock_modifier: dict[str, StockDividends] = {}
            summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _generate_process(self) -> ql.StochasticProcess:
        start_value: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._attached_market_data[self._valuation_date]))

        # SWIGs\stochasticprocess.i
        # 	HestonProcess --> None
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		dividendTS	Handle<YieldTermStructure>
        # 		s0	Handle<Quote>
        # 		v0	Real
        # 		kappa	Real
        # 		theta	Real
        # 		sigma	Real
        # 		rho	Real
        return ql.HestonProcess(self._attached_market_data.quote_curve.handle,          # type: ignore[attr-defined]
                                self._attached_market_data.base_curve.handle,           # type: ignore[attr-defined]
                                start_value,
                                self._volatility,
                                self._kappa,
                                self._theta,
                                self._sigma,
                                self._rho)

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        return self._option_engine_pricer_analytic(ql_instrument, signatures.instrument.fx_european_option, None)


class QLHestonProcessStock(QLHestonProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.heston_stock
    _supported_greeks = (result_items.Vega,)
    _market_data_types = [signatures.stock]
    _initializes_past = False

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        if not self._documentation_mode:
            md_name: str = self._attached_market_data.reference.id
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {(0, 0): md_name + PathSeparatedRaw,
                                                                   (0, 1): md_name + PathSeparatedVolatility}
            aliases: dict[str, str] = {md_name: md_name + PathSeparatedValue,
                                       PathValue: md_name + PathSeparatedValue,
                                       PathVolatility: md_name + PathSeparatedVolatility}
            allow_discount: set[str] = set()
            stock_modifier: dict[str, StockDividends] = {md_name + PathSeparatedValue: self.attached_market_data.stock_dividends}       # type: ignore[attr-defined]  # guaranteed by market_data_types
            summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _generate_process(self) -> ql.StochasticProcess:

        start_value_stripped: float = self._attached_market_data.stock_dividends.inverse(self._valuation_date, self._attached_market_data[self._valuation_date])        # type: ignore[attr-defined]
        start_value: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(start_value_stripped))

        # SWIGs\stochasticprocess.i
        # 	HestonProcess --> None
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		dividendTS	Handle<YieldTermStructure>
        # 		s0	Handle<Quote>
        # 		v0	Real
        # 		kappa	Real
        # 		theta	Real
        # 		sigma	Real
        # 		rho	Real
        return ql.HestonProcess(self._attached_market_data.quote_curve.handle,          # type: ignore[attr-defined]
                                self._attached_market_data.dividend_yield_handle,       # type: ignore[attr-defined]
                                start_value,
                                self._volatility,
                                self._kappa,
                                self._theta,
                                self._sigma,
                                self._rho)

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        return self._option_engine_pricer_analytic(ql_instrument, signatures.instrument.stock_european_option, None)
