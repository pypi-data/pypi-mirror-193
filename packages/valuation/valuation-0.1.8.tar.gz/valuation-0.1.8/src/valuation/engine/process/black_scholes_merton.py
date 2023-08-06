from __future__ import annotations

from typing import Callable, Optional, Union

import math
import QuantLib as ql

from daa_utils import Log

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.consts.pl import PathSeparatedRaw, PathSeparatedValue, PathValue
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import UnsupportedProcessError, UnsupportedValuationError, DAARuntimeException
from valuation.engine.check import ContainedIn, Range, ObjectType
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, QLPathGenerator, path_generator_factory
from valuation.universal_output import result_items
from valuation.universal_transfer import Reference
from valuation.utils.other import is_nan

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.universal_transfer import DefaultParameters, Storage
    from valuation.engine.utils import StockDividends
    from valuation.engine.market_data import QLYieldCurve, QLCurrency


# Black Scholes Merton:
# d S(t, S) = (r(t) -q(t) - \sigma^2(t, S) /2 ) S dt + \sigma S dW


class QLBlackScholesMertonProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.empty
    _supported_greeks = (result_items.Vega,)

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
        if __debug__:
            self._scenario_divisor: float = float('NaN')
            self._original_value: float = float('NaN')

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Vega:
            return [result_items.Vega]
        raise ProgrammingError()

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


class QLBlackScholesMertonProcessFX(QLBlackScholesMertonProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.black_scholes_merton_fx
    _market_data_types = [signatures.fx_rate.standard, signatures.fx_rate.direct_parity]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

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

        volatility: ql.BlackVolTermStructureHandle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(self._valuation_date, self._attached_market_data.calendar, self._volatility, self._attached_market_data.daycount))
        start_value: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._attached_market_data[self._valuation_date]))

        # SWIGs\stochasticprocess.i
        # BlackScholesMertonProcess  --> None
        # 		s0	Handle<Quote>
        # 		dividendTS	Handle<YieldTermStructure>
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		volTS	Handle<BlackVolTermStructure>
        return ql.BlackScholesMertonProcess(start_value, self._attached_market_data.base_curve.handle, self._attached_market_data.quote_curve.handle, volatility)       # type: ignore[attr-defined]

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        return self._option_engine_pricer_analytic(ql_instrument, signatures.instrument.fx_european_option, signatures.instrument.fx_continuous_barrier_option)


class QLBlackScholesMertonProcessStock(QLBlackScholesMertonProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.black_scholes_merton_stock
    _market_data_types = [signatures.stock]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        if not self._documentation_mode:
            md_name: str = self._attached_market_data.reference.id
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {0: md_name + PathSeparatedRaw}
            aliases: dict[str, str] = {md_name: md_name + PathSeparatedValue,
                                       PathValue: md_name + PathSeparatedValue}
            allow_discount: set[str] = set()
            stock_modifier: dict[str, StockDividends] = {md_name + PathSeparatedValue: self.attached_market_data.stock_dividends}       # type: ignore[attr-defined]  # guaranteed by market_data_types
            summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _generate_process(self) -> ql.StochasticProcess:

        volatility: ql.BlackVolTermStructureHandle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(self._valuation_date, self._attached_market_data.calendar, self._volatility, self._attached_market_data.daycount))
        start_value_stripped: float = self._attached_market_data.stock_dividends.inverse(self._valuation_date, self._attached_market_data[self._valuation_date])        # type: ignore[attr-defined]
        start_value: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(start_value_stripped))

        # SWIGs\stochasticprocess.i
        # BlackScholesMertonProcess  --> None
        # 		s0	Handle<Quote>
        # 		dividendTS	Handle<YieldTermStructure>
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		volTS	Handle<BlackVolTermStructure>
        return ql.BlackScholesMertonProcess(start_value, self._attached_market_data.dividend_yield_handle, self._attached_market_data.quote_curve.handle, volatility)       # type: ignore[attr-defined]

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        return self._option_engine_pricer_analytic(ql_instrument, signatures.instrument.stock_european_option, signatures.instrument.stock_continuous_barrier_option)


class QLBlackScholesMertonProcessQuanto(QLBlackScholesMertonProcessStock):  # pylint: disable=abstract-method
    # TODO(2021/12) Expand to QLBlackScholesMertonStockAndFX when necessary, proposals:
    #  1) Instrument has to communicate if it is of quanto type (final exchange rate fixed at inception) -> do adjustment to stock drift only in this case
    #  2) Add functionality PATH[VALUE@FX] similar to PATH[VALUE@DISCOUNT] to descriptors and FP?
    _signature = signatures.process.black_scholes_merton_quanto

    @property
    def fx_process(self) -> QLBlackScholesMertonProcessFX:
        return self._fx_rate_process

    @property
    def fx_attached_curve_opposing_stock_attached(self) -> QLYieldCurve:
        if self._attached_market_data.quote_curve.reference == self._fx_rate_process.attached_market_data.base_curve.reference:  # type: ignore[attr-defined]
            return self._fx_rate_process.attached_market_data.quote_curve  # type: ignore[attr-defined, no-any-return]
        return self._fx_rate_process.attached_market_data.base_curve  # type: ignore[attr-defined, no-any-return]

    @property
    def quanto_adjustment(self) -> float:
        return self._volatility * self.fx_process.volatility * self._correlation

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        # Restricting to BlackScholesMertonFX because it checks for the right fx rate market data and to keep it simple
        self._fx_rate_process: QLBlackScholesMertonProcessFX = self.data(fields.StochasticProcess, check=ObjectType(signatures.process.black_scholes_merton_fx))
        self._correlation: float = self.data(fields.SingleCorrelation, check=Range(lower=-1.0, upper=1.0, strict=False))
        admissible_curves: list[Reference] = [self._fx_rate_process.attached_market_data.base_curve.reference, self._fx_rate_process.attached_market_data.quote_curve.reference]  # type: ignore[attr-defined]
        self.check(self._attached_market_data.quote_curve.reference, ContainedIn(admissible_curves))  # type: ignore[attr-defined]
        self._correlation_base_currency: QLCurrency = self.data(
            fields.CorrelationBaseCurrency,
            check=ContainedIn([
                self._fx_rate_process.attached_market_data.base_currency,                                                 # type: ignore[attr-defined]
                self._fx_rate_process.attached_market_data.quote_currency                                                 # type: ignore[attr-defined]
            ])
        )
        log_message_params: tuple[Reference, str, str] = (
            self.attached_market_data.reference,
            self.attached_market_data.quote_curve.currency.reference.id,                                                  # type: ignore[attr-defined]
            self.fx_attached_curve_opposing_stock_attached.currency.reference.id
        )
        if self._correlation_base_currency == self.fx_attached_curve_opposing_stock_attached.currency:
            self._correlation *= -1.0
            message_start = 'Switching to'
        else:
            message_start = 'Using'
        Log.info(f'{message_start} value {self._correlation} for correlation of {log_message_params[0]}({log_message_params[1]}) to {log_message_params[1]}/{log_message_params[2]} ')

    # kwarg is currently switched only in case of analytic option pricer below
    def _generate_process(self, adjust_quanto: bool = True) -> ql.StochasticProcess:  # pylint: disable=arguments-differ
        volatility: ql.BlackVolTermStructureHandle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(self._valuation_date, self._attached_market_data.calendar, self._volatility, self._attached_market_data.daycount))
        start_value_stripped: float = self._attached_market_data.stock_dividends.inverse(self._valuation_date, self._attached_market_data[self._valuation_date])        # type: ignore[attr-defined]
        start_value: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(start_value_stripped))
        if not adjust_quanto:
            # Quantlib wants the instrument(domestic) risk free curve in the BSM process instead of the underlying(foreign) risk free curve
            return ql.BlackScholesMertonProcess(start_value, self.attached_market_data.dividend_yield_handle, self.fx_attached_curve_opposing_stock_attached.handle, volatility)  # type: ignore[attr-defined]
        stock_attached_risk_free: QLYieldCurve = self._attached_market_data.quote_curve  # type: ignore[attr-defined]
        quanto_adjusted_curve: ql.YieldTermStructure = ql.ZeroSpreadedTermStructure(
            stock_attached_risk_free.handle,
            ql.QuoteHandle(
                ql.SimpleQuote(
                    -self.quanto_adjustment
                )
            ),
            ql.Continuous,
        )
        quanto_adjusted_curve_handle: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(quanto_adjusted_curve)
        return ql.BlackScholesMertonProcess(start_value, self._attached_market_data.dividend_yield_handle, quanto_adjusted_curve_handle, volatility)  # type: ignore[attr-defined]

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        if ql_instrument.signature == signatures.instrument.quanto_european_option:
            start_value: float = self._attached_market_data[self._valuation_date]
            start_value_stripped: float = self._attached_market_data.stock_dividends.inverse(self._valuation_date, start_value)  # type: ignore[attr-defined]
            if not math.isclose(start_value, start_value_stripped):
                raise UnsupportedValuationError(signatures.valuation.analytic_quantlib, ql_instrument.signature, message=f'Cash dividends currently not supported for {self.signature}, use {signatures.valuation.financial_program}')
            # SWIGs\options.i
            # 	QuantoEuropeanEngine --> None
            # 		process	ext::<GeneralizedBlackScholesProcess>
            # 		foreignRiskFreeRate	Handle<YieldTermStructure>
            # 		exchangeRateVolatility	Handle<BlackVolTermStructure>
            # 		correlation	Handle<Quote>
            process: ql.StochasticProcess = self._generate_process(adjust_quanto=False)
            stock_attached_risk_free: QLYieldCurve = self._attached_market_data.quote_curve  # type: ignore[attr-defined]
            calendar = stock_attached_risk_free.calendar
            day_count = stock_attached_risk_free.daycount
            volatility: ql.BlackVolTermStructureHandle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(self._valuation_date, calendar, self.fx_process.volatility, day_count))
            correlation: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._correlation))
            return ql.QuantoEuropeanEngine(process, stock_attached_risk_free.handle, volatility, correlation), None
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)
