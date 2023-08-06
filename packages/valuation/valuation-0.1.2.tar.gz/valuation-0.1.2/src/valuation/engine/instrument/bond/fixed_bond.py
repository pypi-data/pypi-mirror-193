from __future__ import annotations

from typing import Any

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import defaults
from valuation.engine.check import ObjectType, Range, RangeWarning
from valuation.engine.instrument.bond.base_object import QLBond
from valuation.engine.instrument.schedule import Schedule
from valuation.engine.market_data import QLYieldCurve
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness
    from valuation.universal_transfer import DefaultParameters, Storage, TypeKey, Period


class QLFixedBond(QLBond):  # pylint: disable=abstract-method, too-many-instance-attributes
    _signature = signatures.instrument.fixed_bond
    _pay_off = """
schedule.pay_dates[ALL]:  PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount_curve} := rates[FIXING_INDEX] * schedule.accrual_time[FIXING_INDEX]
schedule.pay_dates[-1]:   PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount_curve} := redemption
    """

    @property
    def tenor(self) -> Period:
        return self._period

    @property
    def schedule(self) -> ql.Schedule:
        return self._schedule

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=ObjectType(signatures.yield_curve.all))
        self._currency = self._discount_curve.currency
        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._business: QLBusiness = self.data(fields.Business, default_value=defaults.business(self._currency.id, coupon_type='fixed', allow_fallback=False))
        self._redemption: float = self.data(
            fields.Redemption,
            default_value=1.0,
            check=[
                Range(lower=0.0, strict=False),
                RangeWarning(upper=global_parameters.RedemptionMaximum, strict=False)
            ]
        )
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=defaults.daycount(self._currency.id, coupon_type='fixed', allow_fallback=False))

        additional_fields: dict[TypeKey, dict[str, Any]] = {
            fields.FixedRate: {
                'check': RangeWarning(
                    lower=global_parameters.InterestRateMinimum,
                    upper=global_parameters.InterestRateMaximum,
                    strict=False
                ),
                'allow_fallback_to_default_parameters': True
            }
        }
        self._schedule = Schedule(self, additional_fields, daycount=self._daycount)             # type: ignore[arg-type]

        self._rates: list[float]
        self._period: Period
        self._instrument: ql.FixedRateBond

    def _post_init(self) -> None:
        self._rates = self._schedule[fields.FixedRate]
        # SWIGs\bonds.i
        # FixedRateBond (Bond)
        # 		settlementDays	Integer
        # 		faceAmount	Real
        # 		schedule	Schedule
        # 		coupons	vector<Rate>
        # 		paymentDayCounter	DayCounter
        # 		paymentConvention	BusinessDayConvention		(QuantLib::Following)
        # 		redemption	Real		(100.0)
        # 		issueDate	Date		(Date ( ))
        # 		paymentCalendar	Calendar		(Calendar ( ))
        # 		exCouponPeriod	Period		(Period ( ))
        # 		exCouponCalendar	Calendar		(Calendar ( ))
        # 		exCouponConvention	BusinessDayConvention		(Unadjusted)
        # 		exCouponEndOfMonth	bool		(false)
        self._instrument = ql.FixedRateBond(self._settlement_days,
                                            1.0,
                                            self._schedule.schedule,
                                            self._rates,
                                            self._daycount,
                                            self._business,
                                            self._redemption * 100.0
                                            )

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        engine, _ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)
        pv: float = self._instrument.NPV()                      # pylint: disable=invalid-name

        cash_flows.add_pv(PVDescriptor(self.currency.reference), pv)
        for cash_flow in self._instrument.cashflows():
            payment_date: ql.Date = cash_flow.date()
            settlement_date: ql.Date = self._schedule.calendar.advance(payment_date, self._settlement_days, ql.Days)                  # pylint: disable=invalid-unary-operand-type
            value = cash_flow.amount() * self._discount_curve[payment_date]
            cash_flows.add(CashFlowDescriptor(self.currency.reference, None, payment_date, settlement_date), value)

        return cash_flows
