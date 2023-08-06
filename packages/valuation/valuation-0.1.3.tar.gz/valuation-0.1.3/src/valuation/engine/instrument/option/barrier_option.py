from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ContainedIn, Currency, ObjectType, Range, RangeWarning
from valuation.engine.exceptions import QLInputError, ql_require
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.mappings import BarrierOptionType, QLBarrierOptionType, QLVanillaOptionType, VanillaOptionType
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor
from valuation.universal_transfer import NoValue

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLCurrency, QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLContinuousBarrierOption(QLInstrument):  # pylint: disable=abstract-method, disable=too-many-instance-attributes
    _pay_off = """
issue:      knock_in_triggered := knocked_in
issue:      STOP := knocked_out
CONTINUOUS: knock_in_triggered := knock_in_triggered OR (PATH[VALUE] << down_in_barrier) OR (PATH[VALUE] >> up_in_barrier)
CONTINUOUS: STOP := (PATH[VALUE] << down_out_barrier) OR (PATH[VALUE] >> up_out_barrier)
CONTINUOUS: IF early_rebate
    THEN    PAYDEAD{FIXING_DATE|settlement_days|discount_curve} := rebate
    ELSE    PAYDEAD{maturity|settlement_days|discount_curve} := rebate
maturity:   IF is_call
    THEN    pay_off := MAX(PATH[VALUE] - strike, 0.0)
    ELSE    pay_off := MAX(strike - PATH[VALUE], 0.0)
maturity:   IF knock_in_triggered:
    THEN    PAY{FIXING_DATE|settlement_days|discount_curve} := pay_off
    ELSE    PAY{FIXING_DATE|settlement_days|discount_curve} := 0.0
"""

    @property
    def double_barrier(self) -> bool:
        return self._double_barrier

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        with self._market_data_of_process.safe_access_checks_only():
            spot: float = self._market_data_of_process[self._valuation_date]
        self._strike: float = self.data(
            fields.Strike,
            check=[
                Range(lower=0.0, strict=False),
                RangeWarning(upper=spot * global_parameters.RelativeStrikeMaximum, strict=False)
            ]
        )
        self._barrier_down: float = self.data(
            fields.BarrierDown,
            default_value=None,
            check=[
                Range(lower=0.0, strict=True),
                RangeWarning(upper=spot * global_parameters.RelativeStrikeMaximum, strict=False)
            ]
        )
        self._barrier_up: float = self.data(
            fields.BarrierUp,
            default_value=None,
            check=[
                Range(lower=0.0, strict=True),
                RangeWarning(upper=spot * global_parameters.RelativeStrikeMaximum, strict=False)
            ]
        )
        self._settlement_days: int = self.data(
            fields.SettlementDays,
            check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False)
        )
        self._option_type = self.data(fields.OptionType, check=ContainedIn(VanillaOptionType))
        self._is_call = self._option_type == 'Call'

        self._barrier_type: str = self.data(fields.BarrierType, check=ContainedIn(BarrierOptionType))

        self._rebate: float = self.data(
            fields.Rebate,
            default_value=0.0,
            check=Range(lower=0.0, upper=1.0, strict=False)
        )
        self._early_rebate: float = self.data(fields.EarlyRebate, default_value=True)

        self._knocked_in: bool = self.data(fields.KnockedIn, default_value=NoValue.is_not_in('In', self._barrier_type))
        self._knocked_out: bool = self.data(fields.KnockedOut, default_value=False)

        self._down_in_barrier: float = - float('inf')  # Needed for financial program, only
        self._down_out_barrier: float = - float('inf')  # Needed for financial program, only
        self._up_in_barrier: float = float('inf')  # Needed for financial program, only
        self._up_out_barrier: float = float('inf')  # Needed for financial program, only

        self._continuous_period = (self._issue, self._maturity)

        self._double_barrier: bool
        self._instrument: ql.Instrument

    def _post_init(self) -> None:
        if self._knocked_out:
            self._is_alive = False  # pylint: disable=attribute-defined-outside-init
        if not self._is_alive:
            return
        self._double_barrier = 'Up' in self._barrier_type and 'Down' in self._barrier_type
        if 'Down' in self._barrier_type and self._barrier_down is None:
            raise QLInputError('Down barrier missing')
        if 'Up' in self._barrier_type and self._barrier_up is None:
            raise QLInputError('Upper barrier missing')

        if 'DownIn' in self._barrier_type:
            self._down_in_barrier = self._barrier_down
            barrier_down = self._barrier_down
        if 'DownOut' in self._barrier_type:
            self._down_out_barrier = self._barrier_down
            barrier_down = self._barrier_down
        if 'UpIn' in self._barrier_type:
            self._up_in_barrier = self._barrier_up
            barrier_up = self._barrier_up
        if 'UpOut' in self._barrier_type:
            self._up_out_barrier = self._barrier_up
            barrier_up = self._barrier_up

        barrier_type: QLBarrierOptionType = BarrierOptionType[self._barrier_type]
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

        if self._double_barrier:
            # SWIGs\options.i
            # 	DoubleBarrierOption --> None
            # 		barrierType	DoubleBarrier::Type
            # 		barrier_lo	Real
            # 		barrier_hi	Real
            # 		rebate	Real
            # 		payoff	<StrikedTypePayoff>
            # 		exercise	<Exercise>
            self._instrument = ql.DoubleBarrierOption(
                barrier_type,
                barrier_down,
                barrier_up,
                self._rebate,
                pay_off,
                exercise
            )
        else:
            barrier = barrier_down if 'Down' in self._barrier_type else barrier_up
            # SWIGs\options.i
            # 	BarrierOption --> None
            # 		barrierType	Barrier::Type
            # 		barrier	Real
            # 		rebate	Real
            # 		payoff	<StrikedTypePayoff>
            # 		exercise	<Exercise>
            self._instrument = ql.BarrierOption(
                barrier_type,
                barrier,
                self._rebate,
                pay_off,
                exercise
            )

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        if self._rebate and not self._early_rebate:
            raise QLInputError('QLAnalytic valuation cannot handle this form of rebate!')
        if self._double_barrier and self._barrier_type == 'DownOutUpOut' and self._rebate:
            raise QLInputError('QLAnalytic valuation cannot handle double knockouts with rebate!')
        if not self._is_alive:
            return cash_flows

        engine, __ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)
        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)

        # Second term is the multi-curve adjustment! See FXVanillaOption.
        discount_factor: float = self._discount_curve[settlement_date]
        if self._maturity > self._valuation_date:
            pv_ql: float = self._instrument.NPV()
            if self.process.signature == signatures.process.black_fx:
                ql_discount_factor: float = self._process.discount[self._maturity]  # type: ignore[attr-defined]
            else:
                ql_discount_factor = self._market_data_of_process.quote_curve[self._maturity]  # type: ignore[attr-defined]
            pv: float = pv_ql * discount_factor / ql_discount_factor  # pylint: disable=invalid-name
            cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)
        else:
            if self._knocked_out and not self._early_rebate:
                pv = self._rebate * discount_factor  # pylint: disable=invalid-name
            elif self._knocked_in:
                ql_require(
                    not self._knocked_out,
                    message=f'{fields.KnockedIn} and {fields.KnockedOut} cannot both be true',
                    object_id=self.id
                )
                payoff_direction: int = 1 if self._is_call else -1
                payoff: float = max(payoff_direction * (self._market_data_of_process[self._maturity] - self._strike), 0)
                pv = payoff * discount_factor  # pylint: disable=invalid-name
            else:
                pv = 0.0  # pylint: disable=invalid-name
            cash_flows.add(
                CashFlowDescriptor(
                    self._discount_curve.currency.reference,
                    self._maturity,
                    self._maturity,
                    settlement_date
                ),
                pv
            )
        return cash_flows


class QLFxContinuousBarrierOption(QLContinuousBarrierOption):  # pylint: disable=abstract-method
    _signature = signatures.instrument.fx_continuous_barrier_option
    _market_data_name = fields.FxRate
    _market_data_types = [signatures.fx_rate.all]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency: QLCurrency = self._market_data_of_process.base_currency  # type: ignore[attr-defined]
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve,
                                                       check=[ObjectType(signatures.yield_curve.all), Currency(
                                                           self._market_data_of_process.quote_currency)])  # type: ignore[attr-defined]


class QLStockContinuousBarrierOption(QLContinuousBarrierOption):  # pylint: disable=abstract-method
    _signature = signatures.instrument.stock_continuous_barrier_option
    _market_data_name = fields.Stock
    _market_data_types = [signatures.stock]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency: QLCurrency = self._market_data_of_process.currency
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve,
                                                       check=[ObjectType(signatures.yield_curve.all),
                                                              Currency(self._currency)])
