from __future__ import annotations

from typing import Any, Union

import QuantLib as ql

import contextlib
from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Currency, ObjectType, Range, RangeWarning
from valuation.engine.exceptions import QLInputError
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.instrument.schedule import Schedule
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness
    from valuation.engine.market_data import QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage, TypeKey


class QLCapFloor(QLInstrument):                   # pylint: disable=abstract-method
    _signature = signatures.instrument.cap_floor
    _market_data_name = fields.IRIndex
    _market_data_types = [signatures.ir_index.base]
    _pay_off = """
schedule.fixing_dates[ALL]: IF NOT(fixing_in_arrears)
    THEN    cap_payment := MAX(PATH[VALUE] - caps[FIXING_INDEX], 0.0)
    THEN    floor_payment := MAX(floors[FIXING_INDEX] - PATH[VALUE], 0.0)
    THEN    PAY{schedule.pay_dates[FIXING_INDEX]|settlement_days|PATH[DISCOUNT]|discount_curve} :=(cap_payment + floor_payment) * schedule.accrual_time[FIXING_INDEX]
schedule.pay_dates[ALL]: IF fixing_in_arrears:
    THEN    cap_payment := MAX(PATH[VALUE] - caps[FIXING_INDEX], 0.0)
    THEN    floor_payment := MAX(floors[FIXING_INDEX] - PATH[VALUE], 0.0)
    THEN    PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount_curve} := (cap_payment + floor_payment) * schedule.accrual_time[FIXING_INDEX]
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._fixing_days: int = self.data(fields.FixingDays, check=Range(lower=0, strict=False))
        self._business: QLBusiness = self.data(fields.Business)
        self._daycount: ql.DayCounter = self.data(fields.DayCount)

        additional_fields: dict[TypeKey, dict[str, Any]] = {
            fields.Cap: {'default_value': None, 'check': RangeWarning(lower=global_parameters.InterestRateMinimum, upper=global_parameters.InterestRateMaximum, strict=False), 'allow_fallback_to_default_parameters': True},
            fields.Floor: {'default_value': None, 'check': RangeWarning(lower=global_parameters.InterestRateMinimum, upper=global_parameters.InterestRateMaximum, strict=False), 'allow_fallback_to_default_parameters': True},
        }

        self._schedule = Schedule(self, additional_fields, daycount=self._daycount)             # type: ignore[arg-type]
        self._fixing_in_arrears = self.data(fields.FixingInArrears, default_value=False)
        if self._fixing_in_arrears:
            self._fixing_dates_raw: list[ql.Date] = list(self._schedule.schedule)[1:]
        else:
            self._fixing_dates_raw = list(self._schedule.schedule)[:-1]
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._market_data_of_process.currency)])

        self._caps: list[float]
        self._floors: list[float]
        self._instrument: Union[ql.Cap, ql.Floor, ql.Collar]

    def _post_init(self) -> None:
        self._caps = self._schedule[fields.Cap]
        if all(cap is None for cap in self._caps):
            self._caps = [float('inf')] * len(self._caps)
            caps_ql: list[float] = []
        else:
            caps_ql = self._caps
        self._floors = self._schedule[fields.Floor]
        if all(floor is None for floor in self._floors):
            self._floors = [-float('inf')] * len(self._floors)
            floors_ql: list[float] = []
        else:
            floors_ql = self._floors

        for cap, floor in zip(self._caps, self._floors):
            if cap <= floor:
                raise QLInputError('cap > floor fails')

        # SWIGs\cashflows.i
        # IborLeg
        #       nominals    vector<Real>
        #       schedule    Schedule
        #       index   IborIndex
        #       paymentDayCounter   DayCounter  (DayCounter)
        #       paymentConvention   BusinessDayConvention  (Following)
        #       fixingDays  vector<Natural>  (vector<Natural>)
        #       gearings    vector<Real>  (vector<Real>)
        #       spreads vector<Spread>  (vector<Spread>)
        #       caps    vector<Rate>  (vector<Rate>)
        #       floors  vector<Rate>  (vector<Rate>)
        #       isInArrears bool  (false)

        ibor_leg: ql.IborLeg = ql.IborLeg(
            [1.0],
            self._schedule.schedule,
            self._market_data_of_process.ql_index,               # type: ignore[attr-defined]
            self._daycount,
            self._business,
            [self._fixing_days],
            isInArrears=self._fixing_in_arrears
        )

        # SWIGs\capfloor.i
        # Collar (CapFloor)
        # 		leg	vector< <CashFlow> >
        # 		capRates	vector<Rate>
        # 		floorRates	vector<Rate>
        # Cap (CapFloor)
        # 		leg	vector< <CashFlow> >
        # 		capRates	vector<Rate>
        # Floor (CapFloor)
        # 		leg	vector< <CashFlow> >
        # 		floorRates	vector<Rate>
        if caps_ql and floors_ql:
            self._instrument = ql.Collar(
                ibor_leg,
                caps_ql,
                floors_ql
            )
        elif caps_ql:
            self._instrument = ql.Cap(
                ibor_leg,
                caps_ql,
            )
        elif floors_ql:
            self._instrument = ql.Floor(
                ibor_leg,
                floors_ql,
            )
        else:
            raise QLInputError('At least caps or floors need to be given!')

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        engine, _ = self.process.engine_pricer_analytic(self)

        self._instrument.setPricingEngine(engine)
        pv = self.safe_call(self._instrument.NPV)                   # pylint: disable=invalid-name
        cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)

        with contextlib.suppress(Exception):
            optionlet_values = self._instrument.optionletsPrice()
        num_coupon_payments = len(self._fixing_dates_raw)
        for count, cash_flow in enumerate(self._instrument.floatingLeg()):
            payment_date: ql.Date = cash_flow.date()
            if count + 1 > num_coupon_payments:
                fixing_date = None
            else:
                fixing_date = self._market_data_of_process.ql_index.fixingDate(self._fixing_dates_raw[count])       # type: ignore[attr-defined]
            settlement_date: ql.Date = self._market_data_of_process.calendar.advance(payment_date, self._settlement_days, ql.Days)  # pylint: disable=invalid-unary-operand-type
            if payment_date > self._valuation_date:
                cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, fixing_date, payment_date, settlement_date), optionlet_values[count])
            else:
                rate = self._market_data_of_process[payment_date]
                result = max(rate - self._caps[count], 0.0) + max(self._floors[count] - rate, 0.0)
                cash_flows.add(CashFlowDescriptor(self._market_data_of_process.currency.reference, fixing_date, payment_date, settlement_date), result * self._schedule.accrual_time[count] * self._discount_curve[settlement_date])
        return cash_flows
