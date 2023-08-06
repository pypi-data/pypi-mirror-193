from __future__ import annotations

import math

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ContainedIn, Currency, Differs, ObjectType
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.instrument.vanilla_swap import QLVanillaSwap
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLSwaption(QLInstrument):                   # pylint: disable=abstract-method
    _signature = signatures.instrument.swaption
    _market_data_name = fields.IRIndex
    _market_data_types = [signatures.ir_index.base, signatures.index_and_cms]
    _pay_off = """
exercise_date: IF underlying_instrument.is_payer
    THEN    STOP := underlying_instrument.rate > PATH[CMS]
    ELSE    STOP := underlying_instrument.rate < PATH[CMS]
underlying_instrument.schedule_float.fixing_dates[ALL]: IF underlying_instrument.is_payer
    THEN    PAY{underlying_instrument.schedule_float.pay_dates[FIXING_INDEX]|underlying_instrument.settlement_days|PATH[DISCOUNT]|underlying_instrument.discount_curve|Pay}     :=   (PATH[VALUE] + underlying_instrument.spread) * underlying_instrument.schedule_float.accrual_time[FIXING_INDEX]
    ELSE    PAY{underlying_instrument.schedule_float.pay_dates[FIXING_INDEX]|underlying_instrument.settlement_days|PATH[DISCOUNT]|underlying_instrument.discount_curve|Receive} := - (PATH[VALUE] + underlying_instrument.spread) * underlying_instrument.schedule_float.accrual_time[FIXING_INDEX]
underlying_instrument.schedule_fixed.fixing_dates[ALL]: IF underlying_instrument.is_payer
    THEN    PAY{underlying_instrument.schedule_fixed.pay_dates[FIXING_INDEX]|underlying_instrument.settlement_days|PATH[DISCOUNT]|underlying_instrument.discount_curve|Receive} := - underlying_instrument.rate * underlying_instrument.schedule_fixed.accrual_time[FIXING_INDEX]
    ELSE    PAY{underlying_instrument.schedule_fixed.pay_dates[FIXING_INDEX]|underlying_instrument.settlement_days|PATH[DISCOUNT]|underlying_instrument.discount_curve|Pay}     :=   underlying_instrument.rate * underlying_instrument.schedule_fixed.accrual_time[FIXING_INDEX]
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._underlying_instrument: QLVanillaSwap = self.data(fields.Underlying, check=ObjectType(signatures.instrument.vanilla_swap))
        self._underlying_instrument.check(self._underlying_instrument.amount, ContainedIn([1.0, self.amount]))

        self._exercise_dates: list[ql.Date] = self.data(fields.ExerciseDates, check=Differs([]))

        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._market_data_of_process.currency)])
        self._currency: QLCurrency = self._discount_curve.currency

        self._instrument: ql.Instrument
        self._exercise_date: ql.Date

    def _post_init(self) -> None:
        if len(self._exercise_dates) == 1:
            # SWIGs\exercise.i
            # 	EuropeanExercise --> None
            # 		date	Date
            exercise: ql.EuropeanExercise = ql.EuropeanExercise(self._exercise_dates[0])
            self._exercise_date = self._exercise_dates[0]
        else:
            # SWIGs\exercise.i
            # 	BermudanExercise --> None
            # 		dates	vector<Date>
            # 		payoffAtExpiry	bool		(false)
            exercise = ql.BermudanExercise(self._exercise_dates)

        # SWIGs\swaption.i
        # 	Swaption --> None
        # 		swap	<VanillaSwap>
        # 		exercise	<Exercise>
        # 		type	Settlement::Type		(Settlement::Physical)
        # 		settlementMethod	Settlement::Method		(Settlement::PhysicalOTC)
        self._instrument = ql.Swaption(self._underlying_instrument.instrument, exercise)

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows(allows_undiscounted_cashflows=False)

        engine, __ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)

        pv = self._instrument.NPV()  # pylint: disable=invalid-name
        if self._maturity > self._valuation_date:
            cash_flows.add_pv(PVDescriptor(self._currency.reference), pv)
        else:
            payment_date: ql.Date = self._maturity
            settlement_date: ql.Date = payment_date
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, payment_date, settlement_date), pv)
        return cash_flows

    def tree_ql_evaluate(self, maximal_time_stepping_in_days: int) -> CashFlows:  # pylint: disable=unused-argument
        number_of_time_steps: int = min(
            100,
            max(10, int(math.ceil(ql.ActualActual().yearFraction(self._valuation_date,
                                                                 self._maturity) * 365.0 / maximal_time_stepping_in_days)))
        )

        cash_flows: CashFlows = CashFlows(allows_undiscounted_cashflows=False)

        engine, __ = self.process.engine_pricer_tree(self, number_of_time_steps)
        self._instrument.setPricingEngine(engine)

        pv = self._instrument.NPV()         # pylint: disable=invalid-name

        if self._maturity > self._valuation_date:
            cash_flows.add_pv(PVDescriptor(self._currency.reference), pv)
        else:
            payment_date: ql.Date = self._maturity
            settlement_date: ql.Date = payment_date
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, payment_date, settlement_date), pv)

        return cash_flows
