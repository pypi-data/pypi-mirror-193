from __future__ import annotations

from typing import Any, Optional

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import defaults
from valuation.engine.check import Currency, ObjectType, Range, RangeWarning
from valuation.engine.instrument.bond.base_object import QLBond
from valuation.engine.instrument.schedule import Schedule
from valuation.engine.market_data import QLYieldCurve
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness
    from valuation.universal_transfer import DefaultParameters, Storage, TypeKey, Period


class QLFloatBond(QLBond):  # pylint: disable=abstract-method, disable=too-many-instance-attributes
    _signature = signatures.instrument.float_bond
    _market_data_name = fields.IRIndex
    _market_data_types = [signatures.ir_index.base]
    _pay_off = """
    schedule.fixing_dates[ALL]: IF NOT(fixing_in_arrears)
        THEN    rate := PATH[VALUE] * schedule.gearings[FIXING_INDEX] + schedule.spreads[FIXING_INDEX]
        THEN    PAY{schedule.pay_dates[FIXING_INDEX]|schedule.pay_dates[FIXING_INDEX]|PATH[DISCOUNT]|discount_curve} := rate * schedule.accrual_time[FIXING_INDEX]
    schedule.pay_dates[ALL]: IF fixing_in_arrears:
        THEN    rate := PATH[VALUE] * schedule.gearings[FIXING_INDEX] + schedule.spreads[FIXING_INDEX]
        THEN    PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount_curve} := rate * schedule.accrual_time[FIXING_INDEX]
    schedule.pay_dates[-1]:   PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount_curve} := redemption
        """
    # Todo: Correct settlement dates!

    @property
    def business(self) -> QLBusiness:
        return self._business

    @property
    def calendar(self) -> ql.Calendar:
        return self._calendar

    @property
    def settlement_days(self) -> int:
        return self._settlement_days

    @property
    def tenor(self) -> Period:
        return self._period

    @property
    def schedule(self) -> ql.Schedule:
        return self._schedule

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._market_data_of_process.currency)])
        self._currency = self._discount_curve.currency

        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._fixing_days: int = self.data(fields.FixingDays, check=Range(lower=0, strict=False))
        self._business: QLBusiness = self.data(fields.Business, default_value=defaults.daycount(self._currency.id, coupon_type='floating', allow_fallback=False))
        self._redemption: float = self.data(
            fields.Redemption,
            default_value=1.0,
            check=[
                Range(lower=0.0, strict=False),
                RangeWarning(upper=global_parameters.RedemptionMaximum, strict=False)
            ]
        )
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=defaults.daycount(self._currency.id, coupon_type='floating', allow_fallback=False))

        additional_fields: dict[TypeKey, Optional[dict[str, Any]]] = {
            fields.Spread: {
                'alias': 'spreads',
                'default_value': 0.0,
                'check': RangeWarning(
                    lower=global_parameters.InterestRateMinimum,
                    upper=global_parameters.InterestRateMaximum,
                    strict=False
                ),
                'allow_fallback_to_default_parameters': True
            },
            fields.Gearing: {
                'alias': 'gearings',
                'default_value': 1.0,
                'check': RangeWarning(lower=global_parameters.GearingMinimum, upper=global_parameters.GearingMaximum, strict=False),
                'allow_fallback_to_default_parameters': True
            }
        }

        self._schedule: Schedule = Schedule(self, additional_fields, daycount=self._daycount)
        self._fixing_in_arrears: bool = self.data(fields.FixingInArrears, default_value=False)

        if self._fixing_in_arrears:
            self._fixing_dates_raw: list[ql.Date] = list(self._schedule.schedule)[1:]
        else:
            self._fixing_dates_raw = list(self._schedule.schedule)[:-1]

        self._calendar = self._schedule.calendar

        self._period: Period
        self._instrument: ql.FloatingRateBond

    def _post_init(self) -> None:
        # SWIGs\bonds.i
        # FloatingRateBond
        # 		settlementDays	Size
        # 		faceAmount	Real
        # 		schedule	Schedule
        # 		index	<IborIndex>
        # 		paymentDayCounter	DayCounter
        # 		paymentConvention	BusinessDayConvention		(Following)
        # 		fixingDays	Size		(Null<Size> ( ))
        # 		gearings	vector<Real>		(vector<Real> ( ))
        # 		spreads	vector<Spread>		(vector<Spread> ( ))
        # 		caps	vector<Rate>		(vector<Rate> ( ))
        # 		floors	vector<Rate>		(vector<Rate> ( ))
        # 		inArrears	bool		(false)
        # 		redemption	Real		(100.0)
        # 		issueDate	Date		(Date ( ))

        self._instrument = ql.FloatingRateBond(
            self._settlement_days,
            1.0,
            self._schedule.schedule,
            self._market_data_of_process.ql_index,                           # type: ignore
            self._daycount,
            self._business,
            self._fixing_days,
            self._schedule[fields.Gearing],
            self._schedule[fields.Spread],
            [],
            [],
            self._fixing_in_arrears,
            self._redemption * 100.0
        )

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        engine, pricer = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)
        ql.setCouponPricer(self._instrument.cashflows(), pricer)

        pv: float = self.safe_call(self._instrument.NPV)  # pylint: disable=invalid-name
        cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)
        num_coupon_payments = len(self._fixing_dates_raw)
        for count, cash_flow in enumerate(self._instrument.cashflows()):
            payment_date: ql.Date = cash_flow.date()
            if count + 1 > num_coupon_payments:
                fixing_date = None
            else:
                fixing_date = self._market_data_of_process.ql_index.fixingDate(self._fixing_dates_raw[count])       # type: ignore[attr-defined]
            # settlement_date: ql.Date = self._schedule.calendar.advance(payment_date, self._settlement_days, ql.Days)  # CORRECT
            settlement_date = payment_date  # Todo: Change to the above!
            cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, fixing_date, payment_date, settlement_date), self.safe_call(cash_flow.amount) * self._discount_curve[payment_date])
        return cash_flows
