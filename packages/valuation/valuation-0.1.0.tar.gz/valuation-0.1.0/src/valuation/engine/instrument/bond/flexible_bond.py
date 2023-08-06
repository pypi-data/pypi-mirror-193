from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.engine import QLObjectDB
from valuation.engine.base_object import classproperty
from valuation.engine.check import Range, RangeWarning
from valuation.engine.exceptions import ql_require
from valuation.engine.instrument.bond.base_object import QLBond
from valuation.engine.instrument.coupons import QLCoupon, QLCouponCMS, QLCouponCMSSpread, QLCouponCappedFloored, QLCouponFixed, \
    QLCouponFloating
from valuation.engine.instrument.coupons.leg import LegOperator
from valuation.engine.instrument.schedule import LegSchedule
from valuation.engine.market_data import QLYieldCurve
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor, qldate2date, AdditionalBondCfInfo
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, Storage, TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObject
    from valuation.engine.process import QLProcess
    from valuation.engine.instrument.coupons.leg import SelectedLegOperator


@dataclass(frozen=True)
class FlexibleBondDescriptor:
    calendar: ql.Calendar
    settlement_days: int
    redemption: float


class QLFlexibleBond(QLBond):  # pylint: disable=abstract-method, disable=too-many-instance-attributes, # type: ignore[misc]
    _signature = signatures.instrument.flexible_bond
    _admissible_leg_types: list[type[QLCoupon]] = [QLCouponFixed, QLCouponFloating, QLCouponCappedFloored, QLCouponCMS,
                                                   QLCouponCMSSpread]
    _is_swap: bool = False
    _pay_off = "DUMMY"

    @property
    def is_swap(self) -> bool:
        return self._is_swap

    @property
    def descriptor(self) -> FlexibleBondDescriptor:
        return self._descriptor

    @property
    def leg_scheduler(self) -> LegSchedule:
        return self._leg_scheduler

    @classproperty
    def admissible_leg_types(cls) -> list[type[QLCoupon]]:  # pylint: disable=no-self-argument
        return cls._admissible_leg_types

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        # Proprietary Data #############################################################################################
        self._settlement_days: int = self.data(fields.SettlementDays, default_value=0)
        self._calendar: ql.Calendar = self.data(fields.Calendar)
        self._redemption: float = self.data(
            fields.Redemption,
            default_value=1.0,
            check=[
                Range(lower=0.0, strict=False),
                RangeWarning(upper=global_parameters.RedemptionMaximum, strict=False)
            ]
        )
        self._descriptor = FlexibleBondDescriptor(self._calendar, self._settlement_days, self._redemption)
        # Following are the fields that are allowed to be used via the single periods (e.g. the notional in case of an
        # amortizing instrument). The fields are equipped with default of None, as the values may be provided from the
        # legs themselves. This is needed here, as the schedule uses BaseObject classes for each schedule period, which
        # pull the values using the data method in the __init__.
        # TODO(2022/05) Probably no checks done for additional_keys
        additional_keys: dict[TypeKey, Optional[dict[str, Any]]] = {type_key: {'default_value': None} for type_key in
                                                                    [fields.Amount,
                                                                     fields.FixedRate,
                                                                     fields.Spread,
                                                                     fields.Gearing,
                                                                     fields.Cap,
                                                                     fields.Floor,
                                                                     fields.RedemptionPayment]}
        self._leg_scheduler = LegSchedule(self, additional_keys)

        # Legs #########################################################################################################
        self._leg_operator = LegOperator(self, self._admissible_leg_types)

        # Empty Variables ##############################################################################################
        self._maturity: ql.Date
        self._issue: ql.Date

        self._instrument: ql.Bond
        self._discount_curve: QLYieldCurve
        self._selected_leg: SelectedLegOperator

    def _post_init(self) -> None:
        self._selected_leg = self._leg_operator.select()
        ql_require(len(self._selected_leg) > 0, 'Empty bond. A bond needs at least one leg', self.id)

        self._maturity = self._selected_leg.maturity
        self._issue = self._selected_leg.issue
        self._daycount = self._selected_leg.current.daycount
        self._discount_curve = self._selected_leg.discount_curve

        self._instrument = self._selected_leg.leg

    def _ql_additional_info(self, ql_bond: Optional[ql.Bond] = None, sub_id: str = '') -> dict[str, Any]:
        result: dict[str, Any] = super()._ql_additional_info(ql_bond, sub_id)
        result['daysOfAccrual' + sub_id] = self._selected_leg.accrued_days
        result['outstandingAmount' + sub_id] = self._selected_leg.current_amount(self.valuation_date)
        return result

    def add_market_data(self, ql_object: QLObject) -> None:
        if ql_object.supported_greeks:
            self._market_data_objects.add(ql_object)
        self._market_data_objects.update(ql_object.market_data_objects)

    def set_process(self, ql_object: QLProcess) -> None:
        self._process = ql_object
        self._market_data_of_process = self._process.attached_market_data

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        self._selected_leg.set_coupon_pricer()
        self._selected_leg.set_pricing_engine()

        pv: float = self.safe_call(self._instrument.NPV)  # pylint: disable=invalid-name

        cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv / self._amount)
        cash_flows = self._build_cashflow_report(self._selected_leg, cash_flows)
        return cash_flows

    def _ql_additional_cashflow_info(self, leg: SelectedLegOperator) -> list[AdditionalBondCfInfo]:
        cumulative_remaining_period_length: float = 0.0
        additional_cf_info_list = []
        for cash_flow, redemption in leg.cash_flows():
            extra_cf_info = AdditionalBondCfInfo()
            extra_cf_info.sinking_amount = 0.0
            extra_cf_info.discounted_sinking_amount = 0.0
            extra_cf_info.rate = 0.0
            extra_cf_info.forward_rate = 0.0
            try:
                extra_cf_info.notional = cash_flow.ql_obj.nominal() / self.amount
                extra_cf_info.actual_coupon = cash_flow.ql_obj.amount() / extra_cf_info.notional
                extra_cf_info.rate = cash_flow.ql_obj.rate()
                extra_cf_info.forward_rate = cash_flow.ql_obj.rate()
            except RuntimeError:
                continue
            extra_cf_info.leg_number = cash_flow.leg_number
            try:
                discount: float = leg.discount_curve[cash_flow.ql_obj.date()]
                discount_rf: float = leg.discount_curve.base_curve_handle_risk_free.discount(
                    cash_flow.ql_obj.date())
            except RuntimeError:
                discount = 0.0
                discount_rf = 0.0

            if redemption is not None:
                redemption_extra_cf_info = AdditionalBondCfInfo()
                redemption_extra_cf_info.leg_number = cash_flow.leg_number
                redemption_extra_cf_info.sinking_amount = redemption.ql_obj.amount() / self.amount
                redemption_extra_cf_info.discounted_sinking_amount = redemption.ql_obj.amount() / self.amount * discount
                redemption_extra_cf_info.risk_free_discount = discount_rf
                redemption_extra_cf_info.is_fixed = cash_flow.is_fixed
                redemption_extra_cf_info.start_date = qldate2date(cash_flow.ql_obj.accrualStartDate())
                redemption_extra_cf_info.accrual_start = qldate2date(cash_flow.ql_obj.accrualStartDate())
                redemption_extra_cf_info.accrual_end = qldate2date(cash_flow.ql_obj.accrualEndDate())
                redemption_extra_cf_info.period_length = cash_flow.ql_obj.accrualDays()
                redemption_extra_cf_info.period_year_frac = cash_flow.ql_obj.accrualPeriod()

                redemption_extra_cf_info.notional = cash_flow.ql_obj.nominal() / self.amount
                additional_cf_info_list.append(redemption_extra_cf_info)

            if isinstance(cash_flow.ql_obj, ql.FixedRateCoupon):
                extra_cf_info.fixed_rate = cash_flow.ql_obj.rate()
            elif isinstance(cash_flow.ql_obj, ql.FloatingRateCoupon):
                extra_cf_info.fixed_rate = cash_flow.ql_obj.spread()
            else:
                extra_cf_info.fixed_rate = 0.0
            extra_cf_info.discounted_coupon = extra_cf_info.actual_coupon * discount
            extra_cf_info.risk_free_discount = discount_rf

            extra_cf_info.start_date = qldate2date(cash_flow.ql_obj.accrualStartDate())
            extra_cf_info.accrual_start = qldate2date(cash_flow.ql_obj.accrualStartDate())
            extra_cf_info.accrual_end = qldate2date(cash_flow.ql_obj.accrualEndDate())
            extra_cf_info.period_length = cash_flow.ql_obj.accrualDays()
            extra_cf_info.period_year_frac = cash_flow.ql_obj.accrualPeriod()

            if cash_flow.ql_obj.date() > self.valuation_date:
                cumulative_remaining_period_length += \
                    self.daycount.yearFraction(max(cash_flow.ql_obj.accrualStartDate(), self.valuation_date),
                                               cash_flow.ql_obj.accrualEndDate())
            extra_cf_info.cum_period_length = cumulative_remaining_period_length
            extra_cf_info.is_fixed = cash_flow.is_fixed
            additional_cf_info_list.append(extra_cf_info)

        return additional_cf_info_list

    def ql_additional_cashflow_info(self):
        return self._ql_additional_cashflow_info(self._selected_leg)

    def financial_program_evaluate(self, maximal_time_stepping_in_days: float,
                                   continuous_time_stepping_in_days: Optional[float], log_number_of_paths: int,
                                   generator_type: str, brownian_bridge: bool, antithetic: bool,
                                   tolerance_for_equality: Optional[float],
                                   enable_broadie_glassermann: bool) -> CashFlows:
        payoff, objects = self._selected_leg.generate_payoffs()
        return super()._financial_program_evaluate(maximal_time_stepping_in_days,
                                                   continuous_time_stepping_in_days,
                                                   log_number_of_paths,
                                                   generator_type,
                                                   brownian_bridge,
                                                   antithetic,
                                                   tolerance_for_equality,
                                                   enable_broadie_glassermann, pay_off_override=payoff,
                                                   base_object=objects)

    def _build_cashflow_report(self, selected_leg: SelectedLegOperator, cash_flows: CashFlows,
                               sub_id: str = '', factor: int = 1, settlement_days: int = 0) -> CashFlows:

        for cash_flow, redemption in selected_leg.cash_flows():
            payment_date = cash_flow.payment_date
            fixing_date = cash_flow.fixing_date

            if sub_id in ['Receive', 'Pay']:
                settlement_date: ql.Date = self._calendar.advance(payment_date, settlement_days, ql.Days)
            else:
                settlement_date = payment_date
            if redemption is not None:
                if sub_id in ['Receive', 'Pay']:  # TODO : change this fix, talk to Frank and Ali
                    corrected_amount = redemption.ql_obj.amount() / self._amount * self._discount_curve[
                        payment_date] * factor
                else:
                    corrected_amount = redemption.ql_obj.amount() / self._amount * self._discount_curve[
                        settlement_date]

                cash_flows.add(
                    CashFlowDescriptor(self._discount_curve.currency.reference, None, payment_date,
                                       settlement_date, sub_id, 'Redemption'), corrected_amount)

            try:
                amount = cash_flow.ql_obj.amount()
            except RuntimeError:
                continue

            if sub_id in ['Receive', 'Pay']:  # TODO : change this fix, talk to Frank and Ali
                corrected_amount = amount / self._amount * self._discount_curve[payment_date] * factor
            else:
                corrected_amount = amount / self._amount * self._discount_curve[settlement_date]

            cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, fixing_date, payment_date,
                                              settlement_date, sub_id, 'Coupon'), corrected_amount)

        return cash_flows

    def ql_weighted_average_life(self) -> float:
        return self._ql_weighted_average_life([redemption.ql_obj for _, redemption in self._selected_leg.cash_flows()
                                               if redemption is not None])
