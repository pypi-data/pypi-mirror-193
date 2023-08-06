from __future__ import annotations

import datetime
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Generator, Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters
from valuation.engine.exceptions import QLInputError
from valuation.engine.mappings import Frequencies, PeriodUnitMap
from valuation.exceptions import ProgrammingError  # pylint: disable=wrong-import-order
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import Reference
from valuation.utils.decorators import serialize_function
from valuation.utils.other import listify

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Period
    from valuation.engine.mappings import QLBusiness, QLFrequency
    from valuation.engine.market_data import QLYieldCurve


def add_tenor(date: ql.Date, tenor: Period, calendar: ql.Calendar, business_convention: QLBusiness, settlement_days: int) -> ql.Date:
    # docs\WebSites\FXConventions\Settlement\MarketTenor (OpenGamma Strata).html
    # For FX, passed business_convention should always be Following
    if settlement_days > 0:
        settlement_date: ql.Date = calendar.advance(date, settlement_days, ql.Days, ql.Following)  # always Following for trade -> settle
    else:
        settlement_date = date
    if tenor.short_term:
        if tenor.short_term == 'SPOT':
            return date
        if tenor.short_term == 'ON':
            return calendar.advance(date, tenor.number, ql.Days, business_convention)
        if tenor.short_term == 'TN':
            return calendar.advance(date, tenor.number, ql.Days, business_convention)
        if tenor.short_term == 'SN':
            return calendar.advance(date, tenor.number + settlement_days, ql.Days, business_convention)
        if tenor.short_term == 'SW':
            return calendar.advance(settlement_date, tenor.number, ql.Weeks, business_convention)
    return calendar.advance(settlement_date, tenor.number, PeriodUnitMap[tenor.unit], business_convention)


def add_tenors(date: ql.Date, tenors: list[Period], calendar: ql.Calendar, business_convention: QLBusiness, settlement_days: int) -> list[ql.Date]:
    return [add_tenor(date, tenor, calendar, business_convention, settlement_days) for tenor in tenors]


@serialize_function
def date2qldate(date: datetime.date) -> ql.Date:
    if date == global_parameters.DummyDate:
        return ql.Date()
    return ql.Date(date.day, date.month, date.year)


@serialize_function
def qldate2date(date: ql.Date) -> datetime.date:
    if date == ql.Date():
        return global_parameters.DummyDate
    if date is None:
        return None  # type: ignore[return-value]
    return datetime.date(date.year(), date.month(), date.dayOfMonth())


@serialize_function
def period2qlperiod(period: Period) -> ql.Period:
    return ql.Period(period.number, PeriodUnitMap[period.unit])


def period2qlfrequency(period: Period) -> QLFrequency:
    return Frequencies[period]  # type: ignore[return-value]


def date2year_fraction(start_date: ql.Date, end_date: ql.Date, daycount: ql.DayCounter) -> float:
    return daycount.yearFraction(start_date, end_date)  # type: ignore[no-any-return]


# Todo: (2020/12) There must be a better solution!
#       Is there a quantlib-function which performs the job? We cannot be the first ones needing this.
#       If not, the search algorithm is very hand made and shaky.
def year_fraction2date(start_date: ql.Date, year_fraction: float, daycount: ql.DayCounter) -> ql.Date:
    counter = 0
    year_fraction_difference = year_fraction
    end_date = start_date
    while year_fraction_difference > 0.99 / 365.0:
        day_difference: int = int(math.floor(year_fraction_difference * 366.000000001))
        if day_difference == 0:
            day_difference = 1 if year_fraction_difference > 0 else -1
        end_date = end_date + day_difference
        year_fraction_difference = year_fraction - date2year_fraction(start_date, end_date, daycount)
        counter += 1
        if counter > 10:
            raise Exception
    return end_date


@dataclass
class ModelFixedParameters:
    fixed_rate: float
    fixed_daycount: ql.DayCounter
    fixed_maturity: ql.Date


class StockDividends:
    _daycount = ql.ActualActual()

    def __init__(self, dates: Union[ql.Date, list[ql.Date]], addons: Union[None, float, list[float]], scalars: Union[None, float, list[float]]) -> None:
        self._dates: list[ql.Date] = listify(dates)
        self._addons: list[float] = listify(addons)
        self._scalars: list[float] = listify(scalars)

        assert not self._addons or len(self._addons) == len(self._dates) - 1
        assert not self._scalars or len(self._scalars) == len(self._dates) - 1

        for index in range(len(self._dates) - 1):
            assert self._dates[index] < self._dates[index + 1]

    def _find_index_and_part(self, date: ql.Date) -> tuple[int, float]:
        if date < self._dates[0]:
            raise QLInputError(f'Date {date} < first given dividend date: {self._dates[0]}')
        if date >= self._dates[-1]:
            index: int = -1
            year_fraction = date2year_fraction(self._dates[index], date, self._daycount)
            year_fraction = year_fraction - int(year_fraction)
            return index, year_fraction

        for index in range(len(self._dates) - 1):
            if self._dates[index + 1] > date:
                year_fraction = date2year_fraction(self._dates[index], date, self._daycount)
                divisor = date2year_fraction(self._dates[index], self._dates[index + 1], self._daycount)
                return index, year_fraction / divisor
        raise ProgrammingError()

    # S_withDividends = S_withoutDividends * scalar + addon
    def affine_modifiers(self, date: ql.Date) -> tuple[float, float]:
        index, part = self._find_index_and_part(date)
        addon = self._addons[index] * part if self._addons else 0.0
        scalar = 1.0 + self._scalars[index] * part if self._scalars else 1.0
        return addon, scalar

    def __call__(self, date: ql.Date, stock_price: float) -> float:
        addon, scalar = self.affine_modifiers(date)
        return stock_price * scalar + addon

    def inverse(self, date: ql.Date, stock_price: float) -> float:
        addon, scalar = self.affine_modifiers(date)
        return (stock_price - addon) / scalar


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class PVDescriptor:
    currency: Reference
    sub_id: str = ''

    @property
    def all(self) -> PVDescriptor:
        return PVDescriptor(self.currency)

    def change_to(self, currency: Reference) -> PVDescriptor:
        assert currency != self.currency, f'New {currency} == old {self.currency}'
        return PVDescriptor(currency, sub_id=self.sub_id)


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class CashFlowDescriptor:
    currency: Reference
    fixing: Optional[ql.Date]  # Date on which the decision regarding the amount of the cash-flow is made
    payment: ql.Date  # Date on which the amount is formally booked out of the instrument. Equals discount date. Payment delays need to be handled outside.
    settlement: ql.Date  # Given until payment delay is handled outside
    sub_id: str = ''
    cashflowtype: str = ''

    @property
    def pv_descriptor(self) -> PVDescriptor:
        return PVDescriptor(self.currency, self.sub_id)

    def change_to(self, currency: Reference) -> CashFlowDescriptor:
        assert currency != self.currency, f'New {currency} == old {self.currency}'
        return CashFlowDescriptor(currency, self.fixing, self.payment, self.settlement, sub_id=self.sub_id)


########################


class CashFlows:

    @property
    def allows_undiscounted_cashflows(self) -> bool:
        return self._allows_undiscounted_cashflows

    @property
    def discount_curves(self) -> dict[tuple[Reference, str], QLYieldCurve]:
        return self._discount_curves

    @staticmethod
    def consolidate(cash_flows: CashFlows, significance_lower_bound: float) -> CashFlows:
        assert cash_flows.finalized
        consolidated_cash_flows = CashFlows()
        for pv_descriptor, amount in cash_flows.pvs():
            if abs(amount) >= significance_lower_bound:
                consolidated_cash_flows.add_pv(pv_descriptor, amount)
            else:
                consolidated_cash_flows.add_pv(pv_descriptor, 0.0)
        return consolidated_cash_flows

    def __init__(self, allows_undiscounted_cashflows: bool = True) -> None:
        self._cash_flows: dict[CashFlowDescriptor, float] = defaultdict(float)
        self._pvs: dict[PVDescriptor, float] = defaultdict(float)
        self._pvs_continuous: dict[PVDescriptor, float] = defaultdict(float)
        self._clean_and_dirty_prices: dict[PVDescriptor, tuple[float, float]] = {}
        # Todo: Remove sub_id and change to the following!
        #       self._discount_curves: dict[Reference, QLYieldCurve] = {}
        self._discount_curves: dict[tuple[Reference, str], QLYieldCurve] = {}
        self._allows_undiscounted_cashflows: bool = allows_undiscounted_cashflows
        self.finalized = False

    def __getitem__(self, item: Union[CashFlowDescriptor, PVDescriptor]) -> float:
        if isinstance(item, CashFlowDescriptor):
            return self._cash_flows.get(item, 0.0)
        return self._pvs.get(item, 0.0) + self._pvs_continuous.get(item, 0.0)

    def add_discount_curve(self, discount_curve: QLYieldCurve, sub_id: str = '') -> None:
        assert self._allows_undiscounted_cashflows
        if (discount_curve.currency.reference, sub_id) in self._discount_curves:
            assert self._discount_curves[(discount_curve.currency.reference, sub_id)] == discount_curve
        else:
            self._discount_curves[(discount_curve.currency.reference, sub_id)] = discount_curve

    def add(self, cashflow_descriptor: CashFlowDescriptor, discounted_amount: float) -> None:
        assert not self.finalized, 'CashFlows have been finalized'
        self._cash_flows[cashflow_descriptor] += discounted_amount

    def add_pv(self, pv_descriptor: PVDescriptor, amount: float) -> None:
        assert not self.finalized, 'CashFlows have been finalized'
        self._pvs[pv_descriptor] += amount

    def add_continuous_pv(self, pv_descriptor: PVDescriptor, amount: float) -> None:
        assert not self.finalized, 'CashFlows have been finalized'
        self._pvs_continuous[pv_descriptor] += amount

    def add_clean_and_dirty(self, pv_descriptor: PVDescriptor, clean_price: float, dirty_price: float) -> None:
        assert not self.finalized, 'CashFlows have been finalized'
        if pv_descriptor in self._clean_and_dirty_prices:
            existing_clean, existing_dirty = self._clean_and_dirty_prices[pv_descriptor]
            self._clean_and_dirty_prices[pv_descriptor] = (existing_clean + clean_price, existing_dirty + dirty_price)
        else:
            self._clean_and_dirty_prices[pv_descriptor] = (clean_price, dirty_price)

    def finalize_pvs(self, valuation_date: ql.Date) -> None:
        assert not self.finalized, 'CashFlows have been finalized'
        if self._cash_flows:
            pvs: dict[PVDescriptor, float] = defaultdict(float)
            pvs_all: dict[PVDescriptor, float] = defaultdict(float)
            for cash_flow_descriptor, discounted_amount in self._cash_flows.items():
                if cash_flow_descriptor.payment > valuation_date:
                    pvs[cash_flow_descriptor.pv_descriptor] += discounted_amount
                    if cash_flow_descriptor.sub_id:
                        pvs_all[cash_flow_descriptor.pv_descriptor.all] += discounted_amount

            for pv_descriptor, pv in pvs_all.items():
                if pv_descriptor in self._pvs:
                    if not math.isclose(pv, self._pvs[pv_descriptor]):
                        raise ProgrammingError()
                    for snd_desciptor in list(pvs):
                        if pv_descriptor.currency == snd_desciptor.currency and snd_desciptor.sub_id:
                            pvs.pop(snd_desciptor)

            for pv_descriptor, pv in pvs.items():
                if pv_descriptor in self._pvs:
                    if not math.isclose(pv, self._pvs[pv_descriptor]):
                        raise ProgrammingError()
                else:
                    self._pvs[pv_descriptor] = pv

        for pv_descriptor, amount in self._pvs_continuous.items():
            self._pvs[pv_descriptor] += amount
        self._pvs_continuous = {}
        self.finalized = True

    def cfs(self, include_discount: bool = False) -> Generator[tuple[CashFlowDescriptor, float, Optional[float]], None, None]:
        if not include_discount or not self._allows_undiscounted_cashflows:
            for cash_flow_descriptor, discounted_amount in self._cash_flows.items():
                yield cash_flow_descriptor, discounted_amount, None
        else:
            for cash_flow_descriptor, discounted_amount in self._cash_flows.items():
                yield cash_flow_descriptor, discounted_amount, self._discount_curves[(cash_flow_descriptor.currency, cash_flow_descriptor.sub_id)][cash_flow_descriptor.payment]

    def pvs(self, extend: bool = False) -> Generator[tuple[PVDescriptor, float], None, None]:
        yield from self._pvs.items()
        if self._pvs or not extend:
            return
        no_pvs = {cash_flow_descriptor.pv_descriptor.all for cash_flow_descriptor in self._cash_flows}

        for pv_descriptor in no_pvs:
            yield pv_descriptor, 0

    def pvs_continuous(self) -> Generator[tuple[PVDescriptor, float], None, None]:
        yield from self._pvs_continuous.items()

    def clean_and_dirty(self) -> Generator[tuple[PVDescriptor, tuple[float, float]], None, None]:
        yield from self._clean_and_dirty_prices.items()

    def sum_pvs(self) -> float:
        self._verify_pv_descriptors()
        return sum(self._pvs.values())

    def sum_clean_and_dirty(self) -> tuple[float, float]:
        self._verify_pv_descriptors()
        result_clean, result_dirty = 0.0, 0.0
        for _, (clean_amount, dirty_amount) in self.clean_and_dirty():
            result_clean += clean_amount
            result_dirty += dirty_amount
        return result_clean, result_dirty

    def adjust_currency(self, start_currency: Reference, target_currency: Reference, conversion: float) -> CashFlows:
        assert isinstance(conversion, float)
        converted_cash_flows: CashFlows = CashFlows(allows_undiscounted_cashflows=False)
        for cash_flow_descriptor, value, _ in self.cfs():
            adjusted_descriptor, adjustment = self._adjust_currency(cash_flow_descriptor, start_currency, target_currency, conversion)
            converted_cash_flows.add(adjusted_descriptor, value * adjustment)  # type: ignore[arg-type]
        for pv_descriptor, value in self.pvs():
            adjusted_descriptor, adjustment = self._adjust_currency(pv_descriptor, start_currency, target_currency, conversion)
            converted_cash_flows.add_pv(adjusted_descriptor, value * adjustment)  # type: ignore[arg-type]
        for pv_descriptor, value in self.pvs_continuous():
            adjusted_descriptor, adjustment = self._adjust_currency(pv_descriptor, start_currency, target_currency, conversion)
            converted_cash_flows.add_continuous_pv(adjusted_descriptor, value * adjustment)  # type: ignore[arg-type]
        for pv_descriptor, (clean_value, dirty_value) in self.clean_and_dirty():
            adjusted_descriptor, adjustment = self._adjust_currency(pv_descriptor, start_currency, target_currency, conversion)
            converted_cash_flows.add_clean_and_dirty(adjusted_descriptor, clean_value * adjustment, dirty_value * adjustment)  # type: ignore[arg-type]
        return converted_cash_flows

    def _verify_pv_descriptors(self) -> None:
        assert self.finalized, 'CashFlows must be finalized'
        descriptors_all_pv: set[PVDescriptor] = {descriptor.all for descriptor in self._pvs}

        descriptors_all_clean_dirty: set[PVDescriptor] = {descriptor.all for descriptor in self._clean_and_dirty_prices}

        assert len(descriptors_all_pv) in {0, 1}, f'Inconsistent PV entries: {descriptors_all_pv}'

        assert len(descriptors_all_clean_dirty) in {0, 1}, f'Inconsistent Clean/Dirty entries: {descriptors_all_clean_dirty}'

    @staticmethod
    def _adjust_currency(descriptor: Union[CashFlowDescriptor, PVDescriptor], start_currency: Reference, target_currency: Reference, conversion: float) -> tuple[Union[CashFlowDescriptor, PVDescriptor], float]:
        if descriptor.currency == start_currency:
            return descriptor.change_to(target_currency), conversion
        return descriptor, 1.0

    def _multiply(self, factor: float) -> CashFlows:
        assert isinstance(factor, (float, int))

        cash_flows_result: CashFlows = CashFlows(self._allows_undiscounted_cashflows)
        for (_, sub_id), discount_curve in self._discount_curves.items():
            cash_flows_result.add_discount_curve(discount_curve, sub_id)

        for cash_flow_descriptor, discounted_amount, _ in self.cfs():
            cash_flows_result.add(cash_flow_descriptor, discounted_amount * factor)
        for pv_descriptor, pv in self.pvs():
            cash_flows_result.add_pv(pv_descriptor, pv * factor)
        for pv_descriptor, pv in self.pvs_continuous():
            cash_flows_result.add_continuous_pv(pv_descriptor, pv * factor)
        for pv_descriptor, (clean_amount, dirty_amount) in self.clean_and_dirty():
            cash_flows_result.add_clean_and_dirty(pv_descriptor, clean_amount * factor, dirty_amount * factor)
        cash_flows_result.finalized = self.finalized
        return cash_flows_result

    def _add(self, summand: CashFlows) -> CashFlows:
        assert self.finalized == summand.finalized
        assert isinstance(summand, CashFlows)

        cash_flows_result: CashFlows = CashFlows(self.allows_undiscounted_cashflows and summand.allows_undiscounted_cashflows)
        for cash_flow_descriptor, discounted_amount, _ in self.cfs():
            cash_flows_result.add(cash_flow_descriptor, discounted_amount)
        for cash_flow_descriptor, discounted_amount, _ in summand.cfs():
            cash_flows_result.add(cash_flow_descriptor, discounted_amount)

        for pv_descriptor, pv in self.pvs():
            cash_flows_result.add_pv(pv_descriptor, pv)
        for pv_descriptor, pv in summand.pvs():
            cash_flows_result.add_pv(pv_descriptor, pv)
        for pv_descriptor, pv in self.pvs_continuous():
            cash_flows_result.add_continuous_pv(pv_descriptor, pv)
        for pv_descriptor, pv in summand.pvs_continuous():
            cash_flows_result.add_continuous_pv(pv_descriptor, pv)

        for pv_descriptor, (clean_amount, dirty_amount) in self.clean_and_dirty():
            cash_flows_result.add_clean_and_dirty(pv_descriptor, clean_amount, dirty_amount)
        for pv_descriptor, (clean_amount, dirty_amount) in summand.clean_and_dirty():
            cash_flows_result.add_clean_and_dirty(pv_descriptor, clean_amount, dirty_amount)

        sub_id: str
        if cash_flows_result.allows_undiscounted_cashflows:
            for (_, sub_id), discount_curve in self.discount_curves.items():
                cash_flows_result.add_discount_curve(discount_curve, sub_id)
            for (_, sub_id), discount_curve in summand.discount_curves.items():
                cash_flows_result.add_discount_curve(discount_curve, sub_id)
        cash_flows_result.finalized = self.finalized
        return cash_flows_result

    def __add__(self, other: CashFlows) -> CashFlows:
        return self._add(other)

    def __radd__(self, other: CashFlows) -> CashFlows:
        return self._add(other)

    def __neg__(self) -> CashFlows:
        return self._multiply(-1.0)

    def __sub__(self, other: CashFlows) -> CashFlows:
        return self._add(-other)

    def __rsub__(self, other: CashFlows) -> CashFlows:
        return other._add(-self)

    def __mul__(self, other: float) -> CashFlows:
        return self._multiply(other)

    def __rmul__(self, other: float) -> CashFlows:
        return self._multiply(other)

    def __truediv__(self, other: float) -> CashFlows:
        return self._multiply(1.0 / other)


@dataclass()
class AdditionalBondCfInfo:
    leg_number: Optional[int] = None
    start_date: Optional[datetime.date] = None
    accrual_start: Optional[datetime.date] = None
    accrual_end: Optional[datetime.date] = None
    period_length: Optional[int] = None
    period_year_frac: Optional[float] = None
    cum_period_length: Optional[float] = None
    notional: Optional[float] = None
    sinking_amount: Optional[float] = None
    rate: Optional[float] = None
    fixed_rate: Optional[float] = None
    forward_rate: Optional[float] = None
    actual_coupon: Optional[float] = None
    discounted_coupon: Optional[float] = None
    discounted_sinking_amount: Optional[float] = None
    risk_free_discount: Optional[float] = None
    is_fixed: Optional[bool] = None
