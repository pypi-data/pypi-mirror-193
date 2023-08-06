from __future__ import annotations

from typing import Any, Optional

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.engine.check import ObjectType, ContainedIn
from valuation.engine.exceptions import ql_require
from valuation.engine.instrument.bond.flexible_bond import QLFlexibleBond
from valuation.engine.instrument.schedule import LegSchedule
from valuation.engine.utils import PVDescriptor, CashFlows
from valuation.global_settings import __type_checking__

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import DefaultParameters, Storage, Reference
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLFXRate
    from valuation.engine.instrument.coupons.leg import SelectedLegOperator


class QLFlexibleSwap(QLFlexibleBond):  # pylint: disable=abstract-method
    _signature = signatures.instrument.flexible_swap
    _is_swap = True

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._ql_pay_leg: ql.Bond
        self._ql_receive_leg: ql.Bond

        if self._documentation_mode:
            return

        ql_require(len(self._leg_operator) > 1, 'Empty swap. A swap needs at least two legs', self.id)

        self._pay_leg: SelectedLegOperator = self._leg_operator.select([('swap_position', ql.VanillaSwap.Payer)])
        self._receive_leg: SelectedLegOperator = self._leg_operator.select([('swap_position', ql.VanillaSwap.Receiver)])
        self._issue = min([self._pay_leg.issue, self._receive_leg.issue])
        self._maturity = max([self._pay_leg.maturity, self._receive_leg.maturity])

    @property
    def calendar(self) -> ql.Calendar:
        return self._calendar

    @property
    def schedule(self) -> LegSchedule:
        return self._leg_scheduler

    def _post_init(self) -> None:
        ql_require(self._pay_leg.current.currency == self._receive_leg.current.currency, 'Currency mismatch.', self.id)
        ql_require(self._receive_leg.current_amount(self._receive_leg.issue) == self._receive_leg.current_amount(
            self._receive_leg.issue), "Differing Amounts", self.id)
        self._currency = self._pay_leg.current.currency
        self._amount = self._receive_leg.current_amount(self._receive_leg.issue)
        self._ql_pay_leg = self._pay_leg.leg
        self._ql_receive_leg = self._receive_leg.leg

    def analytic_ql_evaluate(self) -> CashFlows:
        cash_flows: CashFlows = CashFlows()
        cash_flows.add_discount_curve(self._pay_leg.discount_curve, 'Pay')
        cash_flows.add_discount_curve(self._receive_leg.discount_curve, 'Receive')
        pay_currency = self._pay_leg.discount_curve.currency.reference
        receive_currency = self._receive_leg.discount_curve.currency.reference

        self._pay_leg.set_coupon_pricer()
        self._receive_leg.set_coupon_pricer()

        self._pay_leg.set_pricing_engine()
        self._receive_leg.set_pricing_engine()

        cash_flows.add_pv(PVDescriptor(pay_currency, 'Pay'), - self._get_pv(self._pay_leg))
        cash_flows.add_pv(PVDescriptor(receive_currency, 'Receive'), self._get_pv(self._receive_leg))

        self._discount_curve = self._pay_leg.discount_curve
        self._daycount = self._pay_leg.current.daycount
        cash_flows = self._build_cashflow_report(self._pay_leg, cash_flows, 'Pay', -1, self._settlement_days)
        self._discount_curve = self._receive_leg.discount_curve
        self._daycount = self._receive_leg.current.daycount
        cash_flows = self._build_cashflow_report(self._receive_leg, cash_flows, 'Receive', 1, self._settlement_days)

        return cash_flows

    def _get_pv(self, leg: SelectedLegOperator) -> float:
        pv: float = leg.leg.NPV() / self._amount
        return pv

    def ql_clean_dirty(self) -> CashFlows:
        results: CashFlows = CashFlows(allows_undiscounted_cashflows=False)
        dirty_price: float = self._ql_receive_leg.dirtyPrice()
        clean_price: float = dirty_price - self._ql_receive_leg.accruedAmount(self._ql_pay_leg.settlementDate())
        results.add_clean_and_dirty(PVDescriptor(self._receive_leg.current.currency.reference, 'Receive'),
                                    clean_price / 100.0, dirty_price / 100.0)
        dirty_price = - self._ql_pay_leg.dirtyPrice()
        clean_price = dirty_price + self._ql_pay_leg.accruedAmount(self._ql_pay_leg.settlementDate())
        results.add_clean_and_dirty(PVDescriptor(self._pay_leg.current.currency.reference, 'Pay'), clean_price / 100.0,
                                    dirty_price / 100.0)
        return results

    def _ql_additional_info(self, ql_bond: Optional[ql.Bond] = None, sub_id: str = '') -> dict[str, Any]:
        result: dict[str, Any] = dict()
        self._selected_leg = self._pay_leg
        self._discount_curve = self._pay_leg.discount_curve
        self._daycount = self._pay_leg.current.daycount
        result.update(super()._ql_additional_info(self._ql_pay_leg, 'Pay'))
        self._selected_leg = self._receive_leg
        self._discount_curve = self._receive_leg.discount_curve
        self._daycount = self._receive_leg.current.daycount
        result.update(super()._ql_additional_info(self._ql_receive_leg, 'Receive'))
        return result

    def ql_additional_cashflow_info(self):
        result = []
        result.extend(self._ql_additional_cashflow_info(self._pay_leg))
        result.extend(self._ql_additional_cashflow_info(self._receive_leg))
        return result

    def financial_program_evaluate(self, maximal_time_stepping_in_days: float,
                                   continuous_time_stepping_in_days: Optional[float], log_number_of_paths: int,
                                   generator_type: str, brownian_bridge: bool, antithetic: bool,
                                   tolerance_for_equality: Optional[float],
                                   enable_broadie_glassermann: bool) -> CashFlows:
        pay_payoff, pay_objects = self._pay_leg.generate_payoffs()
        pay_cash_flows = super()._financial_program_evaluate(maximal_time_stepping_in_days,
                                                             continuous_time_stepping_in_days,
                                                             log_number_of_paths,
                                                             generator_type,
                                                             brownian_bridge,
                                                             antithetic,
                                                             tolerance_for_equality,
                                                             enable_broadie_glassermann,
                                                             pay_off_override=pay_payoff,
                                                             base_object=pay_objects)

        ql_require(len(pay_cash_flows.discount_curves) <= 1, 'Multiple currencies defined for one leg')

        receive_payoff, receive_objects = self._receive_leg.generate_payoffs()
        receive_cash_flows = super()._financial_program_evaluate(maximal_time_stepping_in_days,
                                                                 continuous_time_stepping_in_days,
                                                                 log_number_of_paths,
                                                                 generator_type,
                                                                 brownian_bridge,
                                                                 antithetic,
                                                                 tolerance_for_equality,
                                                                 enable_broadie_glassermann,
                                                                 pay_off_override=receive_payoff,
                                                                 base_object=receive_objects)
        ql_require(len(receive_cash_flows.discount_curves) <= 1, 'Multiple currencies defined for one leg')
        cash_flows: CashFlows = receive_cash_flows - pay_cash_flows

        return cash_flows


class QLCrossCurrencySwap(QLFlexibleSwap):  # pylint: disable=abstract-method
    _signature = signatures.instrument.currency_swap

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._fx_rate: QLFXRate = self.data(fields.FxRate, check=ObjectType(signatures.fx_rate.all))
        self._currency = self.data(fields.QuoteCurrency,
                                   check=ContainedIn([self._fx_rate.quote_currency, self._fx_rate.base_currency]))

        # required so that result db aggregation does not destroy the results
        self._amount = 1.0

    def _post_init(self) -> None:
        self._ql_pay_leg = self._pay_leg.leg
        self._ql_receive_leg = self._receive_leg.leg

    def _currency_conversion(self) -> tuple[Reference, Reference, float]:
        pay_leg_currency = self._pay_leg.current.currency
        receive_leg_currency = self._receive_leg.current.currency
        base_currency = pay_leg_currency if pay_leg_currency != self._currency else receive_leg_currency
        rate: float = self._fx_rate.get(self.valuation_date, base_currency, self._currency)
        return base_currency.reference, self._currency.reference, rate

    def analytic_ql_evaluate(self) -> CashFlows:
        start_currency, target_currency, conversion_rate = self._currency_conversion()
        cash_flows = super().analytic_ql_evaluate()
        return cash_flows.adjust_currency(start_currency, target_currency, conversion_rate)

    def ql_clean_dirty(self) -> CashFlows:
        clean_dirty: CashFlows = super().ql_clean_dirty()
        start_currency, target_currency, conversion_rate = self._currency_conversion()
        return clean_dirty.adjust_currency(start_currency, target_currency, conversion_rate)

    def financial_program_evaluate(self, maximal_time_stepping_in_days: float,
                                   continuous_time_stepping_in_days: Optional[float], log_number_of_paths: int,
                                   generator_type: str, brownian_bridge: bool, antithetic: bool,
                                   tolerance_for_equality: Optional[float],
                                   enable_broadie_glassermann: bool) -> CashFlows:
        raise NotImplementedError
