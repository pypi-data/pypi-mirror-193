from __future__ import annotations

from typing import Any, Generator, Optional, cast

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.exceptions import ProgrammingError, daa_warn
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import ql_require
from valuation.engine.instrument.coupons import QLCoupon, SingleQLCashFlow
from valuation.engine.instrument.coupons.base_object import CouponDescriptor
from valuation.engine.market_data import QLCurrency, QLYieldCurve
from valuation.engine.utils import period2qlperiod
from valuation.universal_transfer import Signature

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument import QLFlexibleBond


class _LegOperatorBase:
    """
    Function of this class is to organize the leg structure of a fixed income instrument.

    1) Initialize the LegOperator with the parent instrument and it's admissible leg types. It will collect the
    corresponding coupon constituents from the "Legs" sub-storage.

    2) Use the select method to collect the coupons that construct one leg. Select can filter using key value pairs.

    3) Once selected the constituents will be pre-processed and ready to be converted to a ql.Bond.
    """

    _signature = signatures.leg_operator

    @property
    def signature(self) -> Signature:
        return self._signature

    def __init__(self, ql_object: QLFlexibleBond, coupons: list[QLCoupon]):
        self._master_object: QLFlexibleBond = ql_object
        self._all: list[QLCoupon] = coupons

    def select(self, attribute_values: Optional[list[tuple[str, Any]]] = None) -> SelectedLegOperator:
        """Filters the list of coupons by the attributes of the descriptor"""
        attribute_values = attribute_values or []
        selected_coupons: list[QLCoupon] = [
            coupon
            for coupon in self._all
            if self.__matches_criteria(coupon.base_data, attribute_values)
        ]

        return SelectedLegOperator(self._master_object, selected_coupons)

    @staticmethod
    def __matches_criteria(coupon_data: CouponDescriptor, attribute_values: list[tuple[str, Any]]) -> bool:
        for attribute, value in attribute_values:
            if __debug__ and attribute.startswith('_'):
                raise ProgrammingError('Invalid Access')
            if coupon_data.__getattribute__(attribute) != value:
                return False
        return True

    def __len__(self) -> int:
        return len(self._all)


class LegOperator(_LegOperatorBase):
    def __init__(self, ql_object: QLFlexibleBond, admissible_leg_types: list[type[QLCoupon]]):
        for coupon_class in admissible_leg_types:
            if ql_object.is_swap:
                ql_object.add_linetype(_AsSwapLeg(coupon_class), fields.Legs)  # type: ignore[arg-type]
            else:
                ql_object.add_linetype(coupon_class, fields.Legs)
        all_legs: list[QLCoupon] = sorted(ql_object.data(fields.Legs), key=lambda l: l.base_data)
        super().__init__(ql_object, all_legs)


class SelectedLegOperator(_LegOperatorBase):
    @property
    def issue(self) -> ql.Date:
        return self._issue

    @property
    def maturity(self) -> ql.Date:
        return self._maturity

    @property
    def discount_curve(self) -> QLYieldCurve:
        return self._discount

    @property
    def accrued_days(self) -> int:
        coupon: ql.Coupon = self._all[self._get_current_idx()].current_coupon.ql_obj
        return coupon.dayCounter().dayCount(coupon.accrualStartDate(), self._master_object.valuation_date)

    @property
    def current(self) -> CouponDescriptor:
        return self._all[self.__current].base_data

    @property
    def ql_coupons(self) -> list[SingleQLCashFlow]:
        return list(self._single_ql_coupons.values())

    @property
    def leg(self) -> ql.Bond:
        return self._leg

    def __init__(self, ql_object: QLFlexibleBond, coupons: list[QLCoupon]) -> None:
        super().__init__(ql_object, coupons)
        self.__current: int = self._get_current_idx()

        self._currency: QLCurrency = self.current.currency
        self._discount: QLYieldCurve = self.current.discount
        self._issue: ql.Date = coupons[0].base_data.issue
        self._maturity: ql.Date = coupons[-1].base_data.maturity
        self._single_ql_coupons: dict[ql.Date, SingleQLCashFlow] = {}  # TODO: fix how the dates are passed etc
        self._redemptions: dict[ql.Date, SingleQLCashFlow] = {}

        for coupon in self._all:
            ql_require(coupon.base_data.currency == self._currency, 'Inconsistent Currency within leg.',
                       self._master_object.id)
            ql_require(coupon.base_data.discount == self._discount, 'Inconsistent Discount within leg.',
                       self._master_object.id)
            for cpn in coupon.coupons:
                self._single_ql_coupons[cpn.payment_date] = cpn
        # For each period the change in notional (here: amount) is calculated. If not 0, an amortizing payment is added.
        # The residual amount is added as redemption payment, multiplied with the redemption factor.
        amounts: dict[ql.Date, float] = {}
        for coupon in self._all:
            amounts |= coupon.life_cycle_amounts
        self._sorted_amounts: list[tuple[ql.Date, float]] = sorted(amounts.items(),
                                                                   key=lambda a: a[0])  # type: ignore[no-any-return]

        ql_redemptions: list[ql.CashFlow] = []
        for i, (date, amount) in enumerate(self._sorted_amounts):
            if i == len(self._sorted_amounts) - 1:
                redemption = ql.Redemption(amount * self._master_object.descriptor.redemption, date)
            else:
                amortizing_payment: float = amount - self._sorted_amounts[i + 1][1]
                if amortizing_payment == 0:
                    continue
                redemption = ql.AmortizingPayment(amortizing_payment, date)
            ql_redemptions.append(redemption)
            leg_number: int = self._all[self._get_current_idx(date)].base_data.leg_number
            self._redemptions[date] = SingleQLCashFlow(date, None, leg_number, redemption, 'Redemption')
        ql_coupons = [item.ql_obj for item in self._single_ql_coupons.values()]
        self._leg = ql.Bond(self._master_object.descriptor.settlement_days,
                            self._master_object.descriptor.calendar,
                            self.current_amount(self._master_object.valuation_date),
                            self._maturity,
                            self._issue,
                            cast(list[ql.CashFlow], ql_coupons) + ql_redemptions)

    def __getitem__(self, index: int) -> QLCoupon:
        return self._all[index]

    def _get_current_idx(self, date: Optional[ql.Date] = None) -> int:
        """Returns current coupon or the last one"""
        idx: int = 0
        for idx, coupon in enumerate(self._all):
            if coupon.base_data.is_current(date):
                break
        return idx

    def cash_flows(self) -> Generator[tuple[SingleQLCashFlow, Optional[SingleQLCashFlow]], None, None]:
        for date, single_cashflow in self._single_ql_coupons.items():
            yield single_cashflow, self._redemptions.get(date)

    def current_amount(self, date: ql.Date) -> float:
        return next((value for schedule_date, value in self._sorted_amounts if date < schedule_date), 0.0)

    def set_coupon_pricer(self) -> None:
        for coupon in self._all:
            coupon.set_coupon_pricer()

    def set_pricing_engine(self) -> None:
        self._leg.setPricingEngine(
            self._master_object.process.engine_pricer_analytic(self)[0])  # type: ignore[arg-type]

    def make_schedule(self) -> ql.Schedule:
        daa_warn('make_schedule is a workaround for instruments that are not able to work with single cash flows '
                 '(e.g., the flexible callable bond). Data may be omitted.')

        calendar: ql.Calendar = self._master_object.descriptor.calendar
        dates = []
        for date in sorted([self._issue] + [cf.payment_date for cf in self.ql_coupons]):
            if not calendar.isBusinessDay(date):
                dates.append(calendar.adjust(date, self.current.accrual_business))
            else:
                dates.append(date)

        # SWIGs\scheduler.i
        # Schedule
        # 		[UNKNOWN]	vector<Date>
        # 		calendar	Calendar		(NullCalendar ( ))
        # 		convention	BusinessDayConvention		(Unadjusted)
        # 		terminationDateConvention	optional<BusinessDayConvention>		(none)
        # 		tenor	optional<Period>		(none)
        # 		rule	optional<DateGeneration::Rule>		(none)
        # 		endOfMonth	optional<bool>		(none)
        # 		isRegular	vector<bool>		(vector<bool> ( 0 ))
        return ql.Schedule(dates,
                           calendar,
                           self.current.accrual_business,
                           self.current.accrual_business,
                           period2qlperiod(self.current.tenor),
                           None,
                           self.current.end_of_month)

    def generate_payoffs(self) -> tuple[str, list[QLCoupon]]:
        result: list[str] = []
        for coupon_sequence in self._all:
            payoff: str = coupon_sequence.base_data.payoff
            if not payoff:
                return '', []
            parts: list[str] = payoff.split('\n')
            result.extend(parts)
        result.append(
            f'schedule.pay_dates[-1]:   PAY{{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount}} := {self._master_object.descriptor.redemption} * life_cycle_payments[FIXING_DATE]'
        )

        return '\n'.join(result), [self._all[-1]] * len(
            [item for item in result if item.replace(' ', '').replace('\t', '')])


class _AsSwapLeg:  # pylint: disable=too-few-public-methods

    @property
    def signature(self) -> Signature:
        return Signature(self._object_type, self._sub_type)

    def __init__(self, coupon_class: type[QLCoupon]):
        self._object_type: str = coupon_class.object_type
        self._sub_type: str = coupon_class.sub_type
        self._coupon_class: type[QLCoupon] = coupon_class

    def __call__(self, *args: Any, **kwargs: Any) -> QLCoupon:
        kwargs['is_swap_leg'] = True
        return self._coupon_class(*args, **kwargs)  # TODO: Check if fields.Position in self._coupon_class.base_storage

# might be useful when the behavior of the bond needs to change. For example an customized definition of the
# accrued amount

# class _QLBond(ql.Bond):
#     """
#     Change here, if the behavior of the ql.Bond is not as desired.
#     This change was done to be prepared for changes on the coupon level. E.g.
#     """
#     def __init__(self, settlement_days: int, calendar: ql.Calendar, notional: float, maturity: ql.Date,
#                  issue: ql.Date, cash_flows: list[ql.CashFlow]) -> None:
#         #     Bond(Natural settlementDays,
#         #             const Calendar& calendar,
#         #             Real faceAmount,
#         #             const Date& maturityDate,
#         #             const Date& issueDate = Date(),
#         #             const Leg& cashflows = Leg());
#         super().__init__(settlement_days, calendar, notional, maturity, issue, cash_flows)
#         self._cash_flows: list[ql.CashFlow] = cash_flows
#
#     def accruedAmount(self, *args):
#         return super(_QLBond, self).accruedAmount(*args)
#
#     def _accruedAmount(self, date: Optional[ql.Date] = None) -> float:
#         settlement = date or self.settlementDate()
#         accrued_amount: float = 0.
#         for cash_flow in self._cash_flows:
#             if not isinstance(cash_flow, ql.Coupon):
#                 continue
#             accrued_amount = cash_flow.accruedAmount(settlement) * 100 / self.notional()
#             if cash_flow.accrualEndDate() > settlement:
#                 break
#         return accrued_amount
#
#     def cleanPrice(self, date: Optional[ql.Date] = None) -> float:
#         return self.dirtyPrice() - self.accruedAmount(date)
