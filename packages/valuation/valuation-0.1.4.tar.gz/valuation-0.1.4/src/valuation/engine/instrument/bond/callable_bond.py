from __future__ import annotations

import contextlib
import math
from typing import Any, Optional

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.engine import QLObjectDB
from valuation.engine.exceptions import QLInputError, UnsupportedValuationError, ql_require
from valuation.engine.instrument.bond.call_schedule import QLAmericanCall, QLSingleCall, SSDCall, generate_call_schedule
from valuation.engine.instrument.bond.flexible_bond import QLFlexibleBond
from valuation.engine.instrument.coupons import QLCouponCappedFloored, QLCouponFixed, QLCouponFloating, QLCouponCMS, QLCouponCMSSpread
from valuation.engine.instrument.coupons.floating import QLCouponOvernight
from valuation.engine.mappings import QLBusiness
from valuation.engine.utils import CashFlowDescriptor, CashFlows, ModelFixedParameters, PVDescriptor
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, Storage, Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument.coupons.base_object import CouponDescriptor
    from valuation.engine.instrument.coupons.leg import SelectedLegOperator
    from valuation.engine.market_data import QLYieldCurve
    from valuation.engine.process import QLProcess
    from valuation.engine.instrument.bond.call_schedule import QLCallItem
    from valuation.universal_transfer import Reference


class QLCallableBondBase(QLFlexibleBond):  # pylint: disable=too-many-instance-attributes
    _signature = signatures.empty
    _pay_off = ''
    _admissible_leg_types = [QLCouponFixed, QLCouponFloating, QLCouponCappedFloored, QLCouponOvernight,
                             QLCouponCMS, QLCouponCMSSpread]

    @property
    def _option_price(self) -> float:
        raise NotImplementedError

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        # Call Schedule ################################################################################################
        self.add_linetype(QLSingleCall, fields.CallSchedule)
        self.add_linetype(QLAmericanCall, fields.CallSchedule)

        self._has_ssd_call: bool = self.data(fields.HasSSDCall, default_value=False)
        self._american_time_step: Period = self.data(fields.AmericanCallPutTimeStep, default_value=Period(1, 'D'), allow_fallback_to_default_parameters=True)
        self._call_schedule = \
            self._validate_call_schedule(self.data(fields.CallSchedule, default_value=None), self._has_ssd_call)

        # Proprietary Data #############################################################################################
        if self._documentation_mode:
            return
        ql_require(len(self._leg_operator) > 0, 'Empty bond. A bond needs at least one leg')

        # Hull-White Calibration Data ##################################################################################
        self._selected_leg: SelectedLegOperator = self._leg_operator.select()
        self._selected_leg.set_coupon_pricer()
        self._selected_leg.leg.setPricingEngine(ql.DiscountingBondEngine(self._selected_leg.discount_curve.handle))

        self._rates: list[float] = self._get_rates(self._selected_leg)
        self._avg_rate: float = self._get_avg_rate(self._rates)

        # Empty Variables ##############################################################################################
        self._ql_schedule: ql.Schedule = self._selected_leg.make_schedule()
        self._discount_curve: QLYieldCurve = self._selected_leg.discount_curve
        self._issue: ql.Date = self._selected_leg.issue
        self._maturity: ql.Date = self._selected_leg.maturity
        self._daycount: ql.DayCounter = self._selected_leg.current.daycount
        self._callability_schedule: ql.CallabilitySchedule = self._generate_callability_schedule()
        self._instrument: ql.Instrument

    @staticmethod
    def _get_rates(selected_leg: SelectedLegOperator) -> list[float]:
        rates: list[float] = []
        for coupon in selected_leg.ql_coupons:
            if coupon.ql_obj.hasOccurred():
                try:
                    rates.append(coupon.ql_obj.rate())
                except RuntimeError:
                    rates.append(float('NaN'))
            else:
                rates.append(coupon.ql_obj.rate())
        return rates

    @staticmethod
    def _get_avg_rate(rates: list[float]) -> float:
        rates_for_avg: list[float] = [rate for rate in rates if not math.isnan(rate)]
        return sum(rates_for_avg) / len(rates_for_avg)

    @staticmethod
    def _validate_call_schedule(call_schedule: Optional[list[QLCallItem]], has_ssd_call: bool) -> list[QLCallItem]:
        if call_schedule is None:
            if not has_ssd_call:
                raise QLInputError(f'Empty {fields.CallSchedule} allowed only if {fields.HasSSDCall} is true')
            return []
        else:
            return call_schedule

    def _generate_callability_schedule(self) -> ql.CallabilitySchedule:
        coupon_descriptor: CouponDescriptor = self._selected_leg.current
        if coupon_descriptor.business != coupon_descriptor.accrual_business:
            payment_schedule = _get_payment_schedule(self._ql_schedule,
                                                     self._calendar,
                                                     coupon_descriptor.business)
        else:
            payment_schedule = self._ql_schedule

        callability_schedule: ql.CallabilitySchedule = \
            generate_call_schedule(self._call_schedule, payment_schedule, self._calendar, coupon_descriptor.business)
        if self._has_ssd_call:
            is_floating = any(
                not isinstance(coupon.ql_obj, ql.FixedRateCoupon) for coupon in self._selected_leg.ql_coupons)
            callability_schedule = SSDCall(callability_schedule, is_floating, self._issue, self._maturity,
                                           self._valuation_date, self._calendar, coupon_descriptor.business).get()
        return callability_schedule

    def analytic_ql_evaluate(self) -> CashFlows:
        raise UnsupportedValuationError(signatures.valuation.analytic_quantlib, self.signature)

    def set_process(self, ql_object: QLProcess) -> None:
        pass

    def ql_additional_info(self) -> dict[str, Any]:
        result: dict[str, Any] = super()._ql_additional_info(self._selected_leg.leg)
        clean_price_no_call: float = self._selected_leg.leg.cleanPrice()
        dirty_price_no_call: float = (clean_price_no_call + self._selected_leg.leg.accruedAmount(self._selected_leg.leg.settlementDate()))

        result['zSpread'] = ql.BondFunctions.zSpread(self._selected_leg.leg,
                                                     clean_price_no_call,
                                                     self.discount_curve.base_curve_handle_risk_free.currentLink(),
                                                     self.daycount,
                                                     ql.Compounded,
                                                     ql.Annual)
        result['impYield'] = self._selected_leg.leg.bondYield(self._selected_leg.leg.cleanPrice(),
                                                              self.daycount,
                                                              ql.Compounded,
                                                              ql.Annual)
        result['cleanPriceNoCall'] = clean_price_no_call / 100.0
        result['dirtyPriceNoCall'] = dirty_price_no_call / 100.0
        result['optionPrice'] = self._option_price

        if self.maturity > self.valuation_date:
            cash_flows = CashFlows()
            sub_id = 'UnderlyingBond'
            cash_flows.add_discount_curve(self._discount_curve, sub_id=sub_id)
            self._build_cashflow_report(self._selected_leg, cash_flows, 'UnderlyingBond')
            result['baseInstrumentCashFlows'] = cash_flows
        return result


class QLCallableFlexibleBond(QLFlexibleBond):  # pylint: disable=too-many-instance-attributes, disable=abstract-method
    _signature = signatures.instrument.callable_flexible_bond
    _admissible_leg_types = [QLCouponFixed, QLCouponFloating, QLCouponCappedFloored]
    _pay_off = ''

    @property
    def model_calibration_inputs(self) -> ModelFixedParameters:
        return ModelFixedParameters(self._avg_rate, self._selected_leg.current.daycount, self._selected_leg.maturity)

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        # Call Schedule ################################################################################################
        self.add_linetype(QLSingleCall, fields.CallSchedule)
        self.add_linetype(QLAmericanCall, fields.CallSchedule)
        call_schedule: Optional[list[QLCallItem]] = self.data(fields.CallSchedule, default_value=None)
        self._has_ssd_call: bool = self.data(fields.HasSSDCall, default_value=False)
        if call_schedule is None:
            if not self._has_ssd_call:
                raise QLInputError(f'Empty {fields.CallSchedule} allowed only if {fields.HasSSDCall} is true')
            self._call_schedule: list[QLCallItem] = []
        else:
            self._call_schedule = call_schedule

        # Proprietary Data #############################################################################################
        if self._documentation_mode:
            return
        ql_require(len(self._leg_operator) > 0, 'Empty bond. A bond needs at least one leg')

        # Hull-White Calibration Data ##################################################################################
        self._selected_leg: SelectedLegOperator = self._leg_operator.select()
        self._selected_leg.set_coupon_pricer()
        self._rates: list[float] = []
        for coupon in self._selected_leg.ql_coupons:
            if coupon.ql_obj.hasOccurred():
                try:
                    self._rates.append(coupon.ql_obj.rate())
                except RuntimeError:
                    self._rates.append(float('NaN'))
            else:
                self._rates.append(coupon.ql_obj.rate())
        rates_for_avg: list[float] = [rate for rate in self._rates if not math.isnan(rate)]
        self._avg_rate: float = sum(rates_for_avg) / len(rates_for_avg)
        # Empty Variables ##############################################################################################
        self._ql_schedule: ql.Schedule
        self._callability_schedule: ql.CallabilitySchedule
        self._instrument: ql.CallableFixedRateBond
        self._discount_curve: QLYieldCurve
        self._issue: ql.Date
        self._maturity: ql.Date
        self._daycount: ql.DayCounter

    def _post_init(self) -> None:
        self._discount_curve = self._selected_leg.discount_curve
        self._ql_schedule = self._selected_leg.make_schedule()
        self._issue = self._selected_leg.issue
        self._maturity = self._selected_leg.maturity
        self._daycount = self._selected_leg.current.daycount
        coupon_descriptor: CouponDescriptor = self._selected_leg.current

        if coupon_descriptor.business != coupon_descriptor.accrual_business:
            payment_schedule = _get_payment_schedule(self._ql_schedule,
                                                     self._calendar,
                                                     coupon_descriptor.business)
        else:
            payment_schedule = self._ql_schedule

        self._callability_schedule = generate_call_schedule(self._call_schedule, payment_schedule, self._calendar,
                                                            coupon_descriptor.business)
        if self._has_ssd_call:
            is_floating = any(
                not isinstance(coupon.ql_obj, ql.FixedRateCoupon) for coupon in self._selected_leg.ql_coupons)
            self._callability_schedule = SSDCall(self._callability_schedule, is_floating, self._issue, self._maturity,
                                                 self._valuation_date, self._calendar, coupon_descriptor.business).get()

        # SWIGs\bonds.i
        # 	CallableFixedRateBond --> None
        # 		settlementDays	Integer
        # 		faceAmount	Real
        # 		schedule	Schedule
        # 		coupons	vector<Rate>
        # 		accrualDayCounter	DayCounter
        # 		paymentConvention	BusinessDayConvention
        # 		redemption	Real
        # 		issueDate	Date
        # 		putCallSchedule	vector< <Callability> >
        self._instrument = ql.CallableFixedRateBond(
            self._settlement_days,
            100.0,
            self._ql_schedule,
            self._rates,
            coupon_descriptor.daycount,
            coupon_descriptor.business,
            self._redemption * 100.0,
            self._issue,
            self._callability_schedule)

    def set_process(self, ql_object: QLProcess) -> None:
        pass

    def analytic_ql_evaluate(self) -> CashFlows:
        raise UnsupportedValuationError(signatures.valuation.analytic_quantlib, self.signature)

    def ql_additional_info(self) -> dict[str, Any]:
        result: dict[str, Any] = super().ql_additional_info()
        clean_price_no_call: float = ql.BondFunctions.cleanPrice(self._selected_leg.leg,
                                                                 self.discount_curve.handle.currentLink())
        result['zSpread'] = ql.BondFunctions.zSpread(self._selected_leg.leg, clean_price_no_call,
                                                     self.discount_curve.base_curve_handle_risk_free.currentLink(),
                                                     self.daycount, ql.Compounded, ql.Annual)
        result['impYield'] = self._instrument.bondYield(self._instrument.cleanPrice(), self.daycount, ql.Compounded,
                                                        ql.Annual)
        result['cleanPriceNoCall'] = clean_price_no_call / 100.0

        if self.maturity > self.valuation_date:
            currency: Reference = self._discount_curve.currency.reference
            cash_flows = CashFlows()
            sub_id = 'UnderlyingBond'
            cash_flows.add_discount_curve(self._discount_curve, sub_id=sub_id)
            for cash_flow, redemption in self._selected_leg.cash_flows():
                settlement_date: ql.Date = cash_flow.payment_date
                fixing_date = cash_flow.fixing_date
                if redemption is not None:
                    corrected_amount = redemption.ql_obj.amount() / self._amount * self._discount_curve[
                        settlement_date]
                    if abs(corrected_amount) > 0:
                        cash_flows.add(
                            CashFlowDescriptor(self._discount_curve.currency.reference, None, settlement_date,
                                               settlement_date, sub_id, 'Redemption'), corrected_amount)
                with contextlib.suppress(RuntimeError):
                    amount = cash_flow.ql_obj.amount()
                    if self._amount is not None:
                        amount /= self._amount
                    descriptor = CashFlowDescriptor(currency, fixing_date, settlement_date, settlement_date, sub_id,
                                                    'Coupon')
                    cash_flows.add(descriptor, amount * self._discount_curve[settlement_date])
            result['baseInstrumentCashFlows'] = cash_flows

        return result

    def tree_ql_evaluate(self, maximal_time_stepping_in_days: int) -> CashFlows:  # pylint: disable=unused-argument

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        number_of_time_steps: int = min(
            100,
            max(10, int(math.ceil(ql.ActualActual().yearFraction(self._valuation_date,
                                                                 self._maturity) * 365.0 / maximal_time_stepping_in_days)))
        )
        engine, __ = self.process.engine_pricer_tree(self, number_of_time_steps)
        self._instrument.setPricingEngine(engine)

        pv: float = self._instrument.NPV() / 100.0  # pylint: disable=invalid-name

        currency: Reference = self._discount_curve.currency.reference
        cash_flows.add_pv(PVDescriptor(currency), pv)
        return cash_flows


def _get_payment_schedule(schedule: ql.Schedule, calendar: ql.Calendar, payment_bdc: QLBusiness) -> ql.Schedule:
    payment_schedule = []
    for date in schedule:
        if not calendar.isBusinessDay(date):
            payment_schedule.append(calendar.adjust(date, payment_bdc))
        else:
            payment_schedule.append(date)
    payment_schedule = ql.Schedule(payment_schedule,
                                   calendar,
                                   payment_bdc)
    return payment_schedule
