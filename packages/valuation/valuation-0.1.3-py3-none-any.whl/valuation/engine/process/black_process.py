from __future__ import annotations

from typing import Callable, Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.consts.pl import PathSeparatedValue, PathValue
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.check import Currency, ObjectType, Range
from valuation.engine.exceptions import UnsupportedProcessError, DAARuntimeException
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, QLPathGenerator, path_generator_factory
from valuation.universal_output import result_items
from valuation.utils.other import is_nan

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.market_data import QLYieldCurve
    from valuation.engine.utils import StockDividends
    from valuation.universal_transfer import DefaultParameters, Storage


class QLBlackProcess(QLProcess):  # pylint: disable=abstract-method
    _signature = signatures.empty
    _supported_greeks = (result_items.Vega,)

    @property
    def volatility(self) -> float:
        return self._volatility

    @property
    def discount(self) -> QLYieldCurve:
        return self._discount

    @property
    def scenario_divisor(self) -> float:
        return self._scenario_divisor

    @property
    def shift_unit(self) -> int:
        return 100

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._volatility: float = self.data(fields.VolatilityValue, check=Range(lower=0.0, upper=global_parameters.VolatilityMaximum))

        if __debug__:
            self._scenario_divisor: float = float('NaN')
            self._original_value: float = float('NaN')

        self._discount: QLYieldCurve
        self._instrument: QLInstrument

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Vega:
            return [result_items.Vega]
        raise ProgrammingError()

    def _initialize_descriptor(self, stock_dividends: Optional[StockDividends] = None) -> None:
        md_name: str = self._attached_market_data.reference.id
        process2generator_factories: list[
            Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
        assignments: dict[Union[int, tuple[int, int]], str] = {0: md_name + PathSeparatedValue}
        aliases: dict[str, str] = {
            md_name: md_name + PathSeparatedValue,
            PathValue: md_name + PathSeparatedValue
        }
        allow_discount: set[str] = set()
        if not stock_dividends:
            stock_modifier: dict[str, StockDividends] = {}
        else:
            # TODO(2021/11) handle stock dividends if possible like in BSMStock
            unsupported_valuations = (signatures.valuation.analytic_quantlib, signatures.valuation.analytic, signatures.valuation.financial_program)
            raise UnsupportedProcessError(self.signature, unsupported_valuations, message=f'Use {signatures.process.black_scholes_merton_stock} with {signatures.valuation.financial_program}')
        summations: dict[str, set[str]] = {}
        self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _generate_process(self) -> ql.StochasticProcess:
        volatility: ql.BlackVolTermStructureHandle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(self._valuation_date, self.discount.calendar, self._volatility, self.discount.daycount))
        forward: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self.attached_market_data[self._instrument.maturity]))
        # SWIGs\stochasticprocess.i
        # BlackProcess (GeneralizedBlackScholesProcess)
        # 	BlackProcess --> None
        # 		s0	Handle<Quote>
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		volTS	Handle<BlackVolTermStructure>
        return ql.BlackProcess(forward, self.discount.handle, volatility)

    def _change_to(self, scenario: str, shift: float) -> None:
        assert is_nan(self._original_value)
        if scenario == result_items.Vega:
            if shift <= -1 * self._volatility * self.shift_unit:
                raise DAARuntimeException(f'Greek/Range calc: Negative {shift = } leads to nonpositive volatility')
            self._scenario_divisor = shift
            self._original_value = self._volatility
            self._volatility += self._scenario_divisor / self.shift_unit
        else:
            raise ProgrammingError()

    def _change_back(self, scenario: str) -> None:
        if scenario == result_items.Vega:
            self._volatility = self._original_value
        else:
            raise ProgrammingError()
        if __debug__:
            self._original_value = float('NaN')
            self._scenario_divisor = float('NaN')


class QLBlackProcessFX(QLBlackProcess):  # pylint: disable=abstract-method
    _signature = signatures.process.black_fx
    _market_data_types = [signatures.fx_rate.standard, signatures.fx_rate.direct_parity, signatures.fx_rate.direct]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        # Black process works with ql.AnalyticBarrierEngine and FinancialProgram also gives similar result compared to BlackScholesMerton, allowing barrier options for now
        self._instrument: QLInstrument = self.data(fields.DataInstrument, check=[ObjectType([signatures.instrument.fx_european_option, signatures.instrument.fx_continuous_barrier_option])])
        self._discount: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self.attached_market_data.quote_currency)])  # type: ignore[attr-defined]
        if not self._documentation_mode:
            self._initialize_descriptor()

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:  # pylint: disable=no-self-use, unused-argument
        return self._option_engine_pricer_analytic(ql_instrument, signatures.instrument.fx_european_option, signatures.instrument.fx_continuous_barrier_option)


class QLBlackProcessStock(QLBlackProcess):  # pylint: disable=abstract-method
    _signature = signatures.process.black_stock
    _market_data_types = [signatures.stock]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._instrument: QLInstrument = self.data(fields.DataInstrument, check=[ObjectType([signatures.instrument.stock_european_option, signatures.instrument.stock_continuous_barrier_option])])
        self._discount: QLYieldCurve = self.attached_market_data.quote_curve        # type: ignore[attr-defined]
        if not self._documentation_mode:
            self._initialize_descriptor()

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:  # pylint: disable=no-self-use, unused-argument
        return self._option_engine_pricer_analytic(ql_instrument, signatures.instrument.stock_european_option, signatures.instrument.stock_continuous_barrier_option)
