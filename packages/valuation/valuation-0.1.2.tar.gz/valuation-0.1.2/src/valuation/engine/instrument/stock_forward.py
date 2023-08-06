from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Currency, ObjectType, Range, RangeWarning
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLYieldCurve
    from valuation.universal_transfer import DefaultParameters, Storage


class QLStockForward(QLInstrument):                   # pylint: disable=abstract-method
    _signature = signatures.instrument.stock_forward
    _market_data_name = fields.Stock
    _market_data_types = [signatures.stock]
    _pay_off = 'maturity: PAY{FIXING_DATE|settlement_days|discount_curve} := PATH[VALUE] - strike'

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency = self._market_data_of_process.currency

        with self._market_data_of_process.safe_access_checks_only():
            self._strike: float = self.data(
                fields.Strike,
                check=[
                    Range(lower=0.0, strict=False),
                    RangeWarning(upper=self._market_data_of_process[self._valuation_date] * global_parameters.RelativeStrikeMaximum, strict=False)
                ]
            )
        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._market_data_of_process.currency)])

    def analytic_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)
        pv: float = (self._market_data_of_process[self._maturity] - self._strike) * self._discount_curve[settlement_date]                 # pylint: disable=invalid-name
        if self._maturity > self._valuation_date:
            cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)
        cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, self._maturity, self._maturity, settlement_date), pv)
        return cash_flows
