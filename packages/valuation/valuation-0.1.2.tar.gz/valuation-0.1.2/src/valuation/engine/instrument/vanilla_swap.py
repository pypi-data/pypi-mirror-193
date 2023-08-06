from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import defaults
from valuation.engine.check import Currency, ObjectType, Range, RangeWarning
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.instrument.schedule import Schedule
from valuation.engine.mappings import QLSwapPosition
from valuation.engine.market_data import QLYieldCurve
from valuation.engine.utils import CashFlowDescriptor, CashFlows, ModelFixedParameters, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness, QLSwapPositionType
    from valuation.universal_transfer import DefaultParameters, Storage

# TODO(21/07) The following to FP lines seem to not return the same results
#  PAY{schedule_fixed.pay_dates[FIXING_INDEX]|settlement_days|discount_curve} := ...
#  PAY{schedule_fixed.pay_dates[FIXING_INDEX]|settlement_days|PATH[DISCOUNT]|discount_curve} := ...


class QLVanillaSwap(QLInstrument):  # pylint: disable=abstract-method, disable=too-many-instance-attributes
    _signature = signatures.instrument.vanilla_swap
    _market_data_name = fields.IRIndex
    _market_data_types = [signatures.ir_index.base]
    _pay_off = """
schedule_float.fixing_dates[ALL]: IF is_payer
    THEN    PAY{schedule_float.pay_dates[FIXING_INDEX]|settlement_days|PATH[DISCOUNT]|discount_curve|Receive}     :=   (PATH[VALUE] + spread) * schedule_float.accrual_time[FIXING_INDEX]
    ELSE    PAY{schedule_float.pay_dates[FIXING_INDEX]|settlement_days|PATH[DISCOUNT]|discount_curve|Pay} := - (PATH[VALUE] + spread) * schedule_float.accrual_time[FIXING_INDEX]
schedule_fixed.fixing_dates[ALL]: IF is_payer
    THEN    PAY{schedule_fixed.pay_dates[FIXING_INDEX]|settlement_days|PATH[DISCOUNT]|discount_curve|Pay} := - rate * schedule_fixed.accrual_time[FIXING_INDEX]
    ELSE    PAY{schedule_fixed.pay_dates[FIXING_INDEX]|settlement_days|PATH[DISCOUNT]|discount_curve|Receive}     :=   rate * schedule_fixed.accrual_time[FIXING_INDEX]
    """

    @property
    def model_calibration_inputs(self) -> ModelFixedParameters:
        return ModelFixedParameters(self._rate - self._spread, self._fixed_daycount, self._maturity)

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._market_data_of_process.currency)])
        self._currency = self._discount_curve.currency

        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._business: QLBusiness = self.data(fields.Business, default_value=defaults.business(self._currency.id, allow_fallback=False))

        self._fixed_daycount: ql.DayCounter = self.data(fields.FixedDayCount, default_value=defaults.daycount(self._currency.id, coupon_type='fixed', allow_fallback=False))
        self._float_daycount: ql.DayCounter = self.data(fields.FloatDayCount, default_value=defaults.daycount(self._currency.id, coupon_type='floating', allow_fallback=False))

        self._swap_type: QLSwapPositionType = self.data(fields.SwapPosition, ql_map=QLSwapPosition)
        self._is_payer: bool = self._swap_type == QLSwapPosition['Payer']  # pylint: disable=unsubscriptable-object
        self._swap_type_factor = 1.0 if self._is_payer else -1.0
        self._spread: float = self.data(
            fields.Spread,
            default_value=0.0,
            check=RangeWarning(
                lower=global_parameters.InterestRateMinimum,
                upper=global_parameters.InterestRateMaximum,
                strict=False
            )
        )
        self._rate: float = self.data(
            fields.FixedRate,
            check=RangeWarning(
                lower=global_parameters.InterestRateMinimum,
                upper=global_parameters.InterestRateMaximum,
                strict=False
            )
        )

        self._schedule_float: Schedule = Schedule(self, daycount=self._float_daycount, name_suffix='Float')
        self._schedule_fixed: Schedule = Schedule(self, daycount=self._fixed_daycount, name_suffix='Fixed')
        self._fixing_dates_raw: list[ql.Date] = list(self._schedule_float.schedule)[:-1]

        if not self._documentation_mode:
            assert self._schedule_float.calendar == self._schedule_fixed.calendar
            assert self._schedule_float.maturity == self._schedule_fixed.maturity

        self._maturity = self._schedule_float.maturity
        self._instrument: ql.Instrument

    def _post_init(self) -> None:
        # SWIGs\swap.i
        # 	VanillaSwap --> None
        # 		type	VanillaSwap::Type
        # 		nominal	Real
        # 		fixedSchedule	Schedule
        # 		fixedRate	Rate
        # 		fixedDayCount	DayCounter
        # 		floatSchedule	Schedule
        # 		index	<IborIndex>
        # 		spread	Spread
        # 		floatingDayCount	DayCounter

        self._instrument = ql.VanillaSwap(
            self._swap_type,
            1.0,
            self._schedule_fixed.schedule,
            self._rate,
            self._fixed_daycount,
            self._schedule_float.schedule,
            self._market_data_of_process.ql_index,           # type: ignore[attr-defined]
            self._spread,
            self._float_daycount
        )

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve, 'Pay')
        cash_flows.add_discount_curve(self._discount_curve, 'Receive')

        engine, __ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)

        pv: float = self.safe_call(self._instrument.NPV)                # pylint: disable=invalid-name
        cash_flows.add_pv(PVDescriptor(self._currency.reference), pv)

        for cash_flow in self._instrument.fixedLeg():
            leg_name: str = 'Pay' if self._swap_type == ql.VanillaSwap.Payer else 'Receive'
            payment_date: ql.Date = cash_flow.date()
            settlement_date: ql.Date = self._market_data_of_process.calendar.advance(payment_date, self._settlement_days, ql.Days)  # pylint: disable=invalid-unary-operand-type
            cf_value = self._swap_type_factor * self.safe_call(cash_flow.amount) * self._discount_curve[payment_date]
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, payment_date, settlement_date, leg_name), -cf_value)

        num_floating_coupon_payments = len(self._fixing_dates_raw)
        for count, cash_flow in enumerate(self._instrument.floatingLeg()):
            leg_name = 'Receive' if self._swap_type == ql.VanillaSwap.Payer else 'Pay'
            payment_date = cash_flow.date()
            if count + 1 > num_floating_coupon_payments:
                fixing_date = None
            else:
                fixing_date = self._market_data_of_process.ql_index.fixingDate(self._fixing_dates_raw[count])       # type: ignore[attr-defined]
            settlement_date = self._market_data_of_process.calendar.advance(payment_date, self._settlement_days, ql.Days)  # pylint: disable=invalid-unary-operand-type
            cf_value = self._swap_type_factor * self.safe_call(cash_flow.amount) * self._discount_curve[payment_date]
            cash_flows.add(CashFlowDescriptor(self._currency.reference, fixing_date, payment_date, settlement_date, leg_name), cf_value)

        return cash_flows
