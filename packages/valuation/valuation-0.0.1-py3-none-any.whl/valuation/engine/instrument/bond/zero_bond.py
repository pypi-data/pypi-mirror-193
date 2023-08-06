from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ObjectType, Range
from valuation.engine.instrument.bond.base_object import QLBond
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLYieldCurve
    from valuation.engine.mappings import QLBusiness
    from valuation.universal_transfer import DefaultParameters, Storage


class QLZeroBond(QLBond):                   # pylint: disable=abstract-method
    _signature = signatures.instrument.zero_bond
    _pay_off = 'maturity: PAY{FIXING_DATE||PATH[DISCOUNT]|discount_curve} := 1.0'

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._business: QLBusiness = self.data(fields.Business)

        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False), default_value=0)
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=ObjectType(signatures.yield_curve.all))

        self._instrument: ql.Instrument

    def _post_init(self) -> None:
        # SWIGs\bonds.i
        # 	ZeroCouponBond --> None
        # 		settlementDays	Natural
        # 		calendar	Calendar
        # 		faceAmount	Real
        # 		maturityDate	Date
        # 		paymentConvention	BusinessDayConvention		(QuantLib::Following)
        # 		redemption	Real		(100.0)
        # 		issueDate	Date		(Date ( ))
        self._instrument = ql.ZeroCouponBond(self._settlement_days,
                                             self._discount_curve.calendar,
                                             1.0,
                                             self._maturity,
                                             self._business)

    def analytic_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        settlement_date: ql.Date = self._maturity
        if self._maturity > self._valuation_date:
            pv: float = self._discount_curve[settlement_date]  # pylint: disable=invalid-name
            cash_flows.add_pv(PVDescriptor(self._currency.reference), pv)
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, self._maturity, settlement_date), pv)
        else:
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, self._maturity, settlement_date), 1.0)
        return cash_flows

    def analytic_ql_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        engine, _ = self.process.engine_pricer_analytic(self)
        self._instrument.setPricingEngine(engine)
        pv: float = self._instrument.NPV()                      # pylint: disable=invalid-name
        if self._instrument.isExpired() or self._instrument.maturityDate() == self._valuation_date:
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, self._instrument.maturityDate(), self._instrument.maturityDate()), 1.0)
        else:
            cash_flows.add_pv(PVDescriptor(self._currency.reference), pv)
            cash_flows.add(CashFlowDescriptor(self._currency.reference, None, self._instrument.maturityDate(), self._instrument.maturityDate()), pv)
        return cash_flows
