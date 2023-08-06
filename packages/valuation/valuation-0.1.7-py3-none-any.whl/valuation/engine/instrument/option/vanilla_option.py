from __future__ import annotations

import math

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ContainedIn, Currency, ObjectType, Range, RangeWarning
from valuation.engine.exceptions import UnsupportedProcessError
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.mappings import QLVanillaOptionType, VanillaOptionType
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLEuropeanOption(QLInstrument):             # pylint: disable=abstract-method
    _pay_off = """
maturity: IF is_call
THEN    PAY{FIXING_DATE|settlement_days|discount_curve} := MAX(PATH[VALUE] - strike, 0.0)
ELSE    PAY{FIXING_DATE|settlement_days|discount_curve} := MAX(strike - PATH[VALUE], 0.0)
"""

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)

        with self._market_data_of_process.safe_access_checks_only():
            self._strike: float = self.data(
                fields.Strike,
                check=[
                    Range(lower=0.0, strict=False),
                    RangeWarning(upper=self._market_data_of_process[self._valuation_date] * global_parameters.RelativeStrikeMaximum, strict=False)
                ]
            )
        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._option_type = self.data(fields.OptionType, check=ContainedIn(VanillaOptionType))
        self._is_call = self._option_type == 'Call'
        self._instrument: ql.Instrument

    def _post_init(self) -> None:
        option_type: QLVanillaOptionType = VanillaOptionType[self._option_type]

        # SWIGs\payoffs.i
        # 	PlainVanillaPayoff --> None
        # 		type	Option::Type
        # 		strike	Real
        pay_off: ql.Payoff = ql.PlainVanillaPayoff(option_type, self._strike)

        # SWIGs\exercise.i
        # 	EuropeanExercise --> None
        # 		date	Date
        exercise: ql.Exercise = ql.EuropeanExercise(self._maturity)

        # SWIGs\options.i
        # 	EuropeanOption --> None
        # 		payoff	<StrikedTypePayoff>
        # 		exercise	<Exercise>
        self._instrument = ql.VanillaOption(pay_off, exercise)

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        engine, __ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)
        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)

        # There is no option provided by QuantLib to use a discount curve other than the one used in the process. Thus
        # we do an adjustment here, that allows the described. Note: if the curves for the process and for discounting
        # are identical, there is no change compared to the original result provided by QuantLib.
        # If the BlackProcessFX is used, we take the curve directly from the process instead of its MarketData.
        if self._maturity > self._valuation_date:
            if self.process.signature == signatures.process.black_fx:
                pv: float = self._instrument.NPV() * self._discount_curve[settlement_date] / self._process.discount[self._maturity]  # type: ignore[attr-defined]    # pylint: disable=invalid-name
            else:
                pv = self._instrument.NPV() * self._discount_curve[settlement_date] / self._market_data_of_process.quote_curve[self._maturity]  # type: ignore[attr-defined]    # pylint: disable=invalid-name

            cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)
        else:
            if self._is_call:
                pv = max(self._market_data_of_process[self._maturity] - self._strike, 0) * self._discount_curve[settlement_date]        # pylint: disable=invalid-name
            else:
                pv = max(self._strike - self._market_data_of_process[self._maturity], 0) * self._discount_curve[settlement_date]        # pylint: disable=invalid-name
            cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, self._maturity, self._maturity, settlement_date), pv)
        return cash_flows

    def analytic_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        # Black-Scholes formula/Black formula
        #
        # Case SimpleBlack(Geometric brownian motion)
        #   d_1 = 1 / (\sigma * sqrt(delta_t)) * (log(s_0/strike) + (drift + 1 / 2 * \sigma^2) * delta_t)
        #   d_2 = d_1 - \sigma * sqrt(delta_t)
        #       Call: C = \Phi(d_1) * s_0 - \Phi(d_2) * strike * exp(-drift * delta_t)
        #       Put: P = \Phi(-d_2) * strike * exp(-drift * delta_t) - \Phi(-d_1) * s_0
        #
        # Case Black
        #   d_1 = 1 / (\sigma * sqrt(delta_t)) * (log(forward_price/strike) + 1 / 2 * \sigma^2 * delta_t)
        #   d_2 = d_1 - \sigma * sqrt(delta_t)
        #       Call: C = process.discount * (forward_price * Phi(d_1) - strike * Phi(d_2))
        #       Put: P = process.discount * (strike * Phi(-d_2) - forward_price * Phi(-d_1))
        #
        # Case BlackScholesMerton
        #   d_1 = 1 / (\sigma * sqrt(delta_t)) * (log(s_0/strike) + (risk_free - cont_div_yield_OR_foreign_risk_free + 1 / 2 * \sigma^2) * delta_t)
        #   d_2 = d_1 - \sigma * sqrt(delta_t)
        #       Call: C = risk_free.discount * (F * Phi(d_1) - strike * Phi(d_2))
        #       Put: P = risk_free.discount * (strike * Phi(-d_2) - F * Phi(-d_1)),
        #       where F := cont_div_yield_OR_foreign_risk_free.discount / risk_free.discount * s_0

        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)
        if self.maturity > self._valuation_date:
            # TODO(2021/10) SimpleBlack may not apply for fx, move to StockOption
            if self.process.signature == signatures.process.simple_black:
                day_count: ql.DayCounter = self.process.attached_market_data.daycount
                zero_rate: float = self.process.drift  # type: ignore[attr-defined]
                discount_curve_from_zero: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(ql.FlatForward(self.valuation_date, ql.QuoteHandle(ql.SimpleQuote(zero_rate)), day_count))
                discount_factor: float = discount_curve_from_zero.discount(self._maturity)
                forward_adjustment: float = 1.0 / discount_factor
                s_0: float = self._market_data_of_process[self._valuation_date]
            elif self.process.signature in (signatures.process.black_scholes_merton_fx, signatures.process.black_scholes_merton_stock):
                day_count = self._market_data_of_process.quote_curve.daycount  # type: ignore[attr-defined]
                risk_free_rate: float = self._market_data_of_process.quote_curve.zero_rate(self._maturity, day_count)  # type: ignore[attr-defined]
                discount_factor = self._market_data_of_process.quote_curve[self._maturity]  # type: ignore[attr-defined]
                if self.process.signature == signatures.process.black_scholes_merton_fx:
                    foreign_risk_free: QLYieldCurve = self.process.attached_market_data.base_curve  # type: ignore[attr-defined]
                    zero_rate = risk_free_rate - foreign_risk_free.zero_rate(self._maturity, day_count)
                    forward_adjustment = foreign_risk_free[self._maturity] / discount_factor
                else:
                    zero_rate = risk_free_rate - self.process.attached_market_data.dividend_yield  # type: ignore[attr-defined]
                    forward_adjustment = self.process.attached_market_data.dividend_yield_handle.discount(self._maturity) / discount_factor  # type: ignore[attr-defined]
                s_0 = self._market_data_of_process[self._valuation_date]
            elif self.process.signature in (signatures.process.black_fx, signatures.process.black_stock):
                day_count = self.process.discount.daycount  # type: ignore[attr-defined]
                zero_rate = 0.0
                forward_adjustment = 1.0
                s_0 = self.process.attached_market_data[self.maturity]
            else:
                raise UnsupportedProcessError(self.process.signature, signatures.valuation.analytic, instrument=self.signature)
            s_0_adjusted = s_0 * forward_adjustment
            delta_t = day_count.yearFraction(self.valuation_date, self._maturity)
            volatility = self.process.volatility  # type: ignore[attr-defined]
            d_1_erf = 1.0 / (volatility * math.sqrt(delta_t * 2)) * (math.log(s_0 / self._strike) + (zero_rate + volatility ** 2 / 2) * delta_t)
            d_2_erf = d_1_erf - volatility * math.sqrt(delta_t / 2)
            if self._is_call:
                expected_payoff: float = 1 / 2 * ((1 + math.erf(d_1_erf)) * s_0_adjusted - (1 + math.erf(d_2_erf)) * self._strike)
            else:
                expected_payoff = 1 / 2 * ((1 + math.erf(-d_2_erf)) * self._strike - (1 + math.erf(-d_1_erf)) * s_0_adjusted)
            settlement_adjustment_result = self._discount_curve[settlement_date] * expected_payoff
            cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), settlement_adjustment_result)
            return cash_flows
        if self._is_call:
            pv = max(self._market_data_of_process[self._maturity] - self._strike, 0) * self._discount_curve[settlement_date]  # pylint: disable=invalid-name
        else:
            pv = max(self._strike - self._market_data_of_process[self._maturity], 0) * self._discount_curve[settlement_date]  # pylint: disable=invalid-name
        cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, self._maturity, self._maturity, settlement_date), pv)
        return cash_flows


class QLFxEuropeanOption(QLEuropeanOption):  # pylint: disable=abstract-method
    _signature = signatures.instrument.fx_european_option
    _market_data_name = fields.FxRate
    _market_data_types = [signatures.fx_rate.all]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)

        self._currency: QLCurrency = self._market_data_of_process.base_currency  # type: ignore[attr-defined]
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._market_data_of_process.quote_currency)])        # type: ignore[attr-defined]


class QLStockEuropeanOption(QLEuropeanOption):  # pylint: disable=abstract-method
    _signature = signatures.instrument.stock_european_option
    _market_data_name = fields.Stock
    _market_data_types = [signatures.stock]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)

        self._currency: QLCurrency = self._market_data_of_process.currency
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._currency)])


class QLQuantoEuropeanOption(QLEuropeanOption):  # pylint: disable=abstract-method
    _signature = signatures.instrument.quanto_european_option
    _market_data_name = fields.Stock
    _market_data_types = [signatures.stock]
    _pay_off = """
    maturity: IF is_call
    THEN    PAY{FIXING_DATE|settlement_days|discount_curve} := fixed_rate * MAX(PATH[VALUE] - strike, 0.0)
    ELSE    PAY{FIXING_DATE|settlement_days|discount_curve} := fixed_rate * MAX(strike - PATH[VALUE], 0.0)
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)
        self.check(self.process, ObjectType(signatures.process.black_scholes_merton_quanto))  # For now, could do this for other instruments that require certain processes as well?
        self._discount_curve: QLYieldCurve = self.data(
            fields.DiscountCurve,
            check=[
                ObjectType(signatures.yield_curve.all),
                Currency(self.process.fx_attached_curve_opposing_stock_attached.currency)  # type: ignore[attr-defined]
            ],
            default_value=self.process.fx_attached_curve_opposing_stock_attached  # type: ignore[attr-defined]
        )
        self._fixed_rate: float = self.data(fields.FixedRate, check=Range(lower=0.0, strict=True))

    def _post_init(self) -> None:
        option_type: QLVanillaOptionType = VanillaOptionType[self._option_type]

        # SWIGs\payoffs.i
        # 	PlainVanillaPayoff --> None
        # 		type	Option::Type
        # 		strike	Real
        pay_off: ql.Payoff = ql.PlainVanillaPayoff(option_type, self._strike)

        # SWIGs\exercise.i
        # 	EuropeanExercise --> None
        # 		date	Date
        exercise: ql.Exercise = ql.EuropeanExercise(self._maturity)

        # SWIGs\options.i
        # 	QuantoVanillaOption --> None
        # 		payoff	ext::<StrikedTypePayoff>
        # 		exercise	ext::<Exercise>
        self._instrument = ql.QuantoVanillaOption(pay_off, exercise)

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        engine, __ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)
        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)
        if self._maturity > self._valuation_date:
            pv = self._fixed_rate * self._instrument.NPV() * self._discount_curve[settlement_date] / self.process.fx_attached_curve_opposing_stock_attached[self._maturity]  # type: ignore[attr-defined]    # pylint: disable=invalid-name
            cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)
        else:
            if self._is_call:
                pv = self._fixed_rate * max(self._market_data_of_process[self._maturity] - self._strike, 0) * self._discount_curve[settlement_date]        # pylint: disable=invalid-name
            else:
                pv = self._fixed_rate * max(self._strike - self._market_data_of_process[self._maturity], 0) * self._discount_curve[settlement_date]        # pylint: disable=invalid-name
            cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, self._maturity, self._maturity, settlement_date), pv)
        return cash_flows

    def analytic_evaluate(self) -> CashFlows:

        # Haug, The Complete Guide To Option Pricing Formulas, 2nd edition, p. 228
        #   d_1 = 1 / (\sigma * sqrt(delta_t)) * (log(s_0/strike) + (adjusted_risk_free + 1 / 2 * \sigma^2) * delta_t)
        #   where adjusted_risk_free := underlying.risk_free - dividend_yield - quanto_adjustment
        #   d_2 = d_1 - \sigma * sqrt(delta_t)
        #       Call: C = domestic_risk_free.discount * fixed_rate * (exp(adjusted_risk_free * delta_t) * s_0 * Phi(d_1) - strike * Phi(d_2))
        #       Put: P = domestic_risk_free.discount * fixed_rate * (strike * Phi(-d_2) - exp(adjusted_risk_free * delta_t) * s_0 * Phi(-d_1))

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)
        if self.maturity > self._valuation_date:
            if self.process.signature in signatures.process.black_scholes_merton_quanto:
                day_count: ql.DayCounter = self._market_data_of_process.quote_curve.daycount  # type: ignore[attr-defined]
                foreign_risk_free: float = self._market_data_of_process.quote_curve.zero_rate(self._maturity, day_count)  # type: ignore[attr-defined]
                adjusted_risk_free: float = foreign_risk_free - self._market_data_of_process.dividend_yield - self.process.quanto_adjustment  # type: ignore[attr-defined]
                s_0: float = self._market_data_of_process[self._valuation_date]
                delta_t: float = day_count.yearFraction(self.valuation_date, self._maturity)
                volatility: float = self.process.volatility  # type: ignore[attr-defined]
                d_1_erf: float = 1.0 / (volatility * math.sqrt(delta_t * 2)) * (math.log(s_0 / self._strike) + (adjusted_risk_free + volatility ** 2 / 2) * delta_t)
                d_2_erf: float = d_1_erf - volatility * math.sqrt(delta_t / 2)
                if self._is_call:
                    expected_payoff: float = self._fixed_rate * 1 / 2 * ((1 + math.erf(d_1_erf)) * s_0 * math.exp(adjusted_risk_free * delta_t) - (1 + math.erf(d_2_erf)) * self._strike)
                else:
                    expected_payoff = self._fixed_rate * 1 / 2 * ((1 + math.erf(-d_2_erf)) * self._strike - (1 + math.erf(-d_1_erf)) * s_0 * math.exp(adjusted_risk_free * delta_t))
                settlement_adjustment_result: float = self._discount_curve[settlement_date] * expected_payoff
                cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), settlement_adjustment_result)
                return cash_flows
            raise UnsupportedProcessError(self.process.signature, signatures.valuation.analytic, instrument=self.signature)
        if self._is_call:
            pv = self._fixed_rate * max(self._market_data_of_process[self._maturity] - self._strike, 0) * self._discount_curve[settlement_date]  # pylint: disable=invalid-name
        else:
            pv = self._fixed_rate * max(self._strike - self._market_data_of_process[self._maturity], 0) * self._discount_curve[settlement_date]  # pylint: disable=invalid-name
        cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, self._maturity, self._maturity, settlement_date), pv)
        return cash_flows
