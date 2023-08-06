from __future__ import annotations

from typing import Any, Optional

import QuantLib as ql

from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.utils import CashFlows, PVDescriptor

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLBond(QLInstrument):  # pylint: disable=abstract-method

    @property
    def _ql_bond(self) -> ql.Bond:
        instrument = self.instrument
        if not isinstance(instrument, ql.Bond):
            raise ProgrammingError('Inheritance of QL bond is not a Bond')
        return instrument

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._instrument: ql.Bond

    def ql_clean_dirty(self) -> CashFlows:
        dirty_price: float = self._ql_bond.dirtyPrice()
        clean_price: float = dirty_price - self._ql_bond.accruedAmount(self._ql_bond.settlementDate())
        result = CashFlows(allows_undiscounted_cashflows=False)
        result.add_clean_and_dirty(PVDescriptor(self.discount_curve.currency.reference), clean_price / 100, dirty_price / 100)
        return result

    def _ql_weighted_average_life(self, redemptions: list[ql.CashFlow]) -> float:
        """
        calculating the WAL as follows: SUM[i-1, n]((P_i / P) * t_i),
        where
        P_i is the principal payment at time i
        P is the total principal paid
        t_i is the year fraction to the payment date
        """
        total_unweighted_redemption: float = 0.
        total_weighted_redemption: float = 0.
        for redemption in redemptions:
            if redemption.date() <= self._valuation_date:
                continue
            total_unweighted_redemption += redemption.amount()
            year_fraction: float = self.daycount.yearFraction(self.valuation_date, redemption.date())
            total_weighted_redemption += redemption.amount() * year_fraction
        if total_unweighted_redemption == 0:
            return .0
        return total_weighted_redemption / total_unweighted_redemption

    def ql_weighted_average_life(self) -> float:
        return self._ql_weighted_average_life(self._ql_bond.redemptions())

    def ql_additional_info(self) -> dict[str, Any]:
        return self._ql_additional_info()

    def _ql_additional_info(self, ql_bond: Optional[ql.Bond] = None, sub_id: str = '') -> dict[str, Any]:
        if ql_bond is None:
            ql_bond = self._ql_bond
        result: dict[str, Any] = dict()
        args = (ql_bond.maturityDate(), self.discount_curve.daycount, ql.Compounded, ql.Annual)
        result['yieldAtMaturity' + sub_id] = self.discount_curve.base_curve_handle_risk_free.zeroRate(*args).rate()
        result['spreadAtMaturity' + sub_id] = self.discount_curve.handle.zeroRate(*args).rate() - result['yieldAtMaturity' + sub_id]
        result['weightedAverageLife' + sub_id] = self.ql_weighted_average_life()
        try:
            result['yieldToMaturity' + sub_id] = ql_bond.bondYield(ql_bond.cleanPrice(), self.daycount, ql.Compounded, ql.Annual)
        except RuntimeError:
            result['yieldToMaturity' + sub_id] = None
        try:
            result['duration' + sub_id] = ql.BondFunctions.duration(ql_bond, result['yieldToMaturity' + sub_id], self.daycount, ql.Compounded, ql.Annual, ql.Duration.Simple)
        except RuntimeError:
            result['duration' + sub_id] = None
        try:
            result['zSpread' + sub_id] = ql.BondFunctions.zSpread(ql_bond, ql_bond.cleanPrice(), self.discount_curve.base_curve_handle_risk_free.currentLink(), self.daycount, ql.Compounded, ql.Annual)
        except RuntimeError:
            result['zSpread' + sub_id] = None
        try:
            result['modifiedDuration' + sub_id] = ql.BondFunctions.duration(ql_bond, result['yieldToMaturity' + sub_id], self.daycount, ql.Compounded, ql.Annual, ql.Duration.Modified)
        except RuntimeError:
            result['modifiedDuration' + sub_id] = None
        return result
