from __future__ import annotations

from typing import Any

import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ContainedIn, Currency, Differs, ObjectType, Range, RangeWarning
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.utils import CashFlowDescriptor, CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLYieldCurve, QLCurrency
    from valuation.universal_transfer import DefaultParameters, Storage


class QLFxForward(QLInstrument):                   # pylint: disable=abstract-method
    _signature = signatures.instrument.fx_forward
    _market_data_name = fields.FxRate
    _market_data_types = [signatures.fx_rate.all]
    _pay_off = """
    maturity:   IF inverted_rate
        THEN    PAY{FIXING_DATE|settlement_days|discount_curve} := 1 / PATH[VALUE] - strike
        ELSE    PAY{FIXING_DATE|settlement_days|discount_curve} := PATH[VALUE] - strike
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency: QLCurrency = self.data(fields.BaseCurrency, default_value=self._market_data_of_process.base_currency, check=[ObjectType(signatures.currency.all), ContainedIn([self._market_data_of_process.quote_currency, self._market_data_of_process.base_currency])])    # type: ignore[attr-defined]
        self._quote_currency: QLCurrency = self.data(fields.QuoteCurrency, default_value=self._market_data_of_process.quote_currency, check=[Differs(self._currency), ObjectType(
            signatures.currency.all), ContainedIn([self._market_data_of_process.quote_currency, self._market_data_of_process.base_currency])])    # type: ignore[attr-defined]

        self._inverted_rate: bool = self._quote_currency != self._market_data_of_process.quote_currency    # type: ignore[attr-defined]

        with self._market_data_of_process.safe_access_checks_only():
            spot_value: float = self._market_data_of_process[self._valuation_date]
        if self._inverted_rate and not self._documentation_mode:
            spot_value = 1 / spot_value

        self._strike: float = self.data(
            fields.Strike,
            check=[
                Range(lower=0.0, strict=False),
                RangeWarning(upper=spot_value * global_parameters.RelativeStrikeMaximum, strict=False)
            ]
        )
        self._settlement_days: int = self.data(fields.SettlementDays, check=Range(lower=0, upper=global_parameters.SettlementDaysMaximum, strict=False))
        self._discount_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=[ObjectType(signatures.yield_curve.all), Currency(self._quote_currency)])

        self._additional_info: dict[str, Any] = {'strike': self._strike}

    def analytic_evaluate(self) -> CashFlows:

        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._discount_curve)

        settlement_date: ql.Date = self._discount_curve.calendar.advance(self._maturity, self._settlement_days, ql.Days)
        fx_rate: float = self._market_data_of_process[self._maturity]
        if self._inverted_rate:
            fx_rate = 1 / fx_rate
            self._additional_info['rateInverted'] = True
        else:
            self._additional_info['rateInverted'] = False
        self._additional_info['fxRate'] = f'{self._currency.id}/{self._quote_currency.id}'

        discount_factor: float = self._discount_curve[settlement_date]
        pv: float = (fx_rate - self._strike) * discount_factor                # pylint: disable=invalid-name     # type: ignore[call-arg]
        if self._maturity > self._valuation_date:
            cash_flows.add_pv(PVDescriptor(self._discount_curve.currency.reference), pv)
        cash_flows.add(CashFlowDescriptor(self._discount_curve.currency.reference, self._maturity, self._maturity, settlement_date), pv)

        self._additional_info['forwardValue'] = fx_rate
        self._additional_info['discountFactor'] = discount_factor

        return cash_flows

    def additional_info(self) -> dict[str, Any]:
        return self._additional_info
