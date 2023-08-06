from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Generator, Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from daa_utils import Log
from valuation.engine import QLObject, QLObjectBase, QLObjectDB
from valuation.engine import defaults
from valuation.engine.check import Check, ContainedIn, Equals, ObjectType
from valuation.engine.exceptions import QLInputError
from valuation.engine.mappings import AugmentedDict, DateGeneration, QLDateGeneration, QLSwapPosition, QLSwapPositionType, QLBusiness
from valuation.engine.market_data import QLMarketData, QLYieldCurve
from valuation.engine.process import QLProcess, generate_dummy_process
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, NoValue, Reference, Signature, Storage, StorageTypes, TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QuantlibType
    from valuation.engine.instrument import QLFlexibleBond
    from valuation.engine.instrument.schedule import ScheduleIterator, QLLegScheduleSingleDate
    from valuation.engine.market_data import QLCurrency
    from valuation.universal_transfer import Period


@dataclass(frozen=True)
class SingleQLCashFlow:
    payment_date: ql.Date
    fixing_date: Optional[ql.Date]
    leg_number: int
    ql_obj: ql.Coupon
    payment_type: str = 'Coupon'
    is_fixed: bool = True


@dataclass(frozen=True)
class CouponDescriptor:
    # Todo (2021/03): Probably this would be more handy if separated in data needed for constructing the schedule
    #  and others that are simply describing the coupon section. However that would require some changes in the
    #  construction of pricers.

    signature: Signature
    valuation_date: ql.Date
    currency: QLCurrency
    issue: ql.Date
    maturity: ql.Date
    first_coupon_date: ql.Date
    next_to_last_coupon: ql.Date
    date_generation: QLDateGeneration
    end_of_month: bool
    tenor: ql.Period
    daycount: ql.DayCounter
    business: int
    accrual_business: int
    settlement_days: int
    calendar: ql.Calendar
    leg_number: int
    discount: QLYieldCurve
    payoff: str

    swap_position: Optional[QLSwapPositionType] = None

    def __lt__(self, other: CouponDescriptor) -> bool:
        if not isinstance(other, CouponDescriptor):
            raise ProgrammingError
        return self.maturity <= other.issue  # type: ignore[no-any-return]

    def __gt__(self, other: CouponDescriptor) -> bool:
        if not isinstance(other, CouponDescriptor):
            raise ProgrammingError
        return self.issue >= other.maturity  # type: ignore[no-any-return]

    def is_current(self, date: Optional[ql.Date] = None) -> bool:
        """Return true if valuation date is between issue and maturity date of the leg"""
        return self.issue <= (date or self.valuation_date) <= self.maturity  # type: ignore[no-any-return]

    @property
    def is_active(self) -> bool:
        """Return true if valuation date is before maturity date of the leg"""
        return self.valuation_date <= self.maturity  # type: ignore[no-any-return]


class QLCoupon(QLObjectBase):  # pylint: disable=too-many-instance-attributes, too-many-public-methods
    _admissible_types: tuple[signatures.Signature, ...] = (  # type: ignore[name-defined]
        signatures.instrument.flexible_bond,
        signatures.instrument.callable_flexible_bond,
        signatures.instrument.flexible_swap,
        signatures.instrument.currency_swap
    )

    _market_data_name: Optional[TypeKey] = None
    _market_data_types: list[Signature] = []
    _pay_off: str = ''

    @property
    def reference(self) -> Reference:
        return Reference(self._master_object.reference.type, f'{self._master_object.reference.type}#{self.__class__.__name__}{self._leg_number}')

    @property
    def base_data(self) -> CouponDescriptor:
        return self._descriptor

    @property
    def life_cycle_amounts(self) -> dict[ql.Date, float]:
        return self._life_cycle_amounts

    @property
    def coupons(self) -> list[SingleQLCashFlow]:
        return self._coupons

    @property
    def currency(self) -> QLCurrency:
        return self._currency

    @property
    def current_coupon(self) -> SingleQLCashFlow:
        if len(self._coupons) == 0:
            raise ValueError('No coupons')
        if self.valuation_date < self._coupons[0].ql_obj.accrualStartDate():
            return self._coupons[0]
        for item in self._coupons:
            if item.ql_obj.accrualStartDate() <= self.valuation_date <= item.ql_obj.accrualEndDate():
                return item
        return self._coupons[-1]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Optional[QLFlexibleBond] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        if __debug__ and not self._documentation_mode and master_object is not None and master_object.signature not in self._admissible_types:
            raise ProgrammingError('Master object is not registered for using Coupons.')

        # --- Fetching variables from storages -------------------------------------------------------------------------
        self._currency: QLCurrency = self.data(fields.Currency)
        coupon_type: str = 'fixed' if self.signature in (signatures.Coupon.fixed,) else 'floating'
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True,
                                                  default_value=defaults.daycount(currency=self._currency.id,
                                                                                  coupon_type=coupon_type,
                                                                                  allow_fallback=False))
        self._business: int = self.data(fields.Business, allow_fallback_to_default_parameters=True,
                                        default_value=defaults.business(currency=self._currency.id,
                                                                        coupon_type=coupon_type, allow_fallback=False))
        self._accrual_business: int = self.data(fields.AccrualBusiness, allow_fallback_to_default_parameters=True,
                                                default_value=self._business)

        self._period: Period = self.data(fields.Tenor)
        self._issue: ql.Date = self.data(fields.Issue, allow_fallback_to_default_parameters=True)
        self._maturity: ql.Date = self.data(fields.Maturity, allow_fallback_to_default_parameters=True)
        self._first_coupon_date: ql.Date = self.data(fields.FirstCouponDate, default_value=global_parameters.DummyDate)
        self._next_to_last_coupon: ql.Date = self.data(fields.NextToLastCouponDate,
                                                       default_value=global_parameters.DummyDate)
        self._date_generation: int = self.data(fields.DateGeneration, allow_fallback_to_default_parameters=True,
                                               default_value='Backward', ql_map=DateGeneration)
        self._end_of_month: bool = self.data(fields.EndOfMonth, allow_fallback_to_default_parameters=True,
                                             default_value=False)

        self._amount: float = self.data(fields.Amount, allow_fallback_to_default_parameters=True, default_value=1.0)
        self._settlement_days: int = self.data(fields.SettlementDays, allow_fallback_to_default_parameters=True,
                                               default_value=0)

        self._leg_number: int = self.data(fields.LegNumber, default_value=1)
        self._discount: QLYieldCurve = self.data(fields.DiscountCurve, allow_fallback_to_default_parameters=True)

        if is_swap_leg:
            self._swap_position: Optional[QLSwapPositionType] = self.data(fields.SwapPosition,
                                                                          check=ContainedIn(QLSwapPosition),
                                                                          ql_map=QLSwapPosition)
        else:
            self._swap_position = None

        # --- Process get or create ------------------------------------------------------------------------------------
        # This part is copied from instrument.... TODO: Check if it can be alligned
        self._market_data_objects = set()
        self._process: QLProcess = self.data(fields.StochasticProcess, default_value=None,
                                             check=ObjectType(signatures.process.all))

        if self._market_data_name is not None:
            if self._process is None:
                self._market_data_of_process: QLMarketData = self.data(self._market_data_name,
                                                                       check=ObjectType(self._market_data_types))
                self._process = generate_dummy_process(self._market_data_of_process)
            else:
                attached_market_data = self._process.attached_market_data
                attached_market_data = NoValue.replace(attached_market_data, 'attached_market_data',
                                                       self._market_data_name)
                self._market_data_of_process = self.data(self._market_data_name, default_value=attached_market_data,
                                                         check=[Equals(attached_market_data),
                                                                ObjectType(self._market_data_types)])
        elif self._process is not None:
            self._market_data_of_process = self._process.attached_market_data
            if self._market_data_of_process.supported_greeks:
                self._market_data_objects.add(self._market_data_of_process)
        else:
            self._market_data_of_process = None
            self._process = generate_dummy_process(self)

        self._additional_values: dict[TypeKey, Any] = {}

        # --- Interface provisioning -----------------------------------------------------------------------------------
        if not self._documentation_mode:
            self._life_cycle_amounts: dict[ql.Date, float] = {}
            self._life_cycle_payments: dict[ql.Date, float] = defaultdict(float)
            self._life_cycle_amounts_as_of_fixing: dict[ql.Date, float] = {}
            self._coupons: list[SingleQLCashFlow] = []
            self._schedule: ScheduleIterator
            self._master_object: QLFlexibleBond

            self._additional_values[fields.Amount] = None
            self._additional_values[fields.RedemptionPayment] = None
            self._descriptor = CouponDescriptor(self.signature,
                                                self.valuation_date,
                                                self._currency,
                                                self._issue,
                                                self._maturity,
                                                self._first_coupon_date,
                                                self._next_to_last_coupon,
                                                self._date_generation,
                                                self._end_of_month,
                                                self._period,
                                                self._daycount,
                                                self._business,
                                                self._accrual_business,
                                                master_object.descriptor.settlement_days,  # type: ignore[union-attr]
                                                master_object.descriptor.calendar,  # type: ignore[union-attr]
                                                self._leg_number,
                                                self._discount,
                                                self._pay_off,
                                                self._swap_position)

    def _post_init(self) -> None:
        self._schedule = self._master_object.leg_scheduler.get(self.base_data, self._additional_values)

    def data(self, type_key: TypeKey,
             default_value: Union[QLObject, StorageTypes.GeneralEntry, NoValue, None] = NoValue(),
             check: Union[None, Check, list[Check]] = None, allow_fallback_to_default_parameters: bool = False,
             ql_map: Optional[AugmentedDict[QuantlibType, QuantlibType]] = None,
             ignore_data_only_mode: bool = False) -> QuantlibType:
        value = super().data(type_key, default_value, check, allow_fallback_to_default_parameters, ql_map,
                             ignore_data_only_mode)
        if isinstance(value, QLObject):
            self._master_object.add_market_data(value)
            if value.signature.type == signatures.process.all.type:
                self._master_object.set_process(value)  # type: ignore[arg-type]
        return value

    def schedule_items(self) -> Generator[tuple[ql.Date, ql.Date, Union[dict[TypeKey, Any], QLLegScheduleSingleDate]], None, None]:
        def _secure_division(__dividend: float, __divisor: float) -> float:  # TODO: remove this secure division and add if condition in case of 0
            if __divisor == 0.:
                return 0.0
            return __dividend / __divisor

        past_period_amount: float = 1.0
        current_amount: float = 1.0
        current_amount_absolute: float = self._amount
        for start_date, end_date, values in self._schedule:
            payment = end_date

            if values[fields.RedemptionPayment] is None and values[fields.Amount] is None:
                self._life_cycle_amounts[end_date] = current_amount_absolute
                self._life_cycle_payments[start_date] = 0.0
                self._life_cycle_amounts_as_of_fixing[start_date] = _secure_division(current_amount_absolute,
                                                                                     self._amount)

            if values[fields.Amount] is not None:
                self._life_cycle_amounts[end_date] = values[fields.Amount]
                redemption_payment: float = past_period_amount - _secure_division(values[fields.Amount], self._amount)
                if not math.isclose(self._life_cycle_payments.get(start_date, redemption_payment), redemption_payment):
                    raise QLInputError('Amount and redemption payment contain contrary information')
                self._life_cycle_payments[start_date] = redemption_payment
                self._life_cycle_amounts_as_of_fixing[start_date] = _secure_division(values[fields.Amount], self._amount)
                current_amount = _secure_division(values[fields.Amount], self._amount)
                past_period_amount = _secure_division(values[fields.Amount], self._amount)
            else:
                values[fields.Amount] = current_amount_absolute

            if values[fields.RedemptionPayment] is not None:
                self._life_cycle_amounts[end_date] = values[fields.Amount]
                self._life_cycle_amounts_as_of_fixing[start_date] = current_amount
                current_amount_absolute -= values[fields.RedemptionPayment]
                current_amount = _secure_division(current_amount_absolute, self._amount)
                self._life_cycle_payments[end_date] = _secure_division(values[fields.RedemptionPayment], self._amount)

            yield start_date, end_date, payment, values

        self._life_cycle_payments[self._maturity] = _secure_division(current_amount, self._amount)

    def set_coupon_pricer(self) -> None:
        raise NotImplementedError


def preload_fixing(fixing_date: ql.Date, coupon: ql.FloatingRateCoupon, market_data: QLMarketData,
                   calendar: ql.Calendar, business: QLBusiness, try_past_fixings: bool = False):
    valuation_date: ql.Date = ql.Settings.instance().evaluationDate

    if fixing_date <= valuation_date and (
            try_past_fixings or valuation_date <= coupon.accrualEndDate()):
        try:
            _ = market_data[fixing_date]
        except QLInputError:
            try:
                # only fills gap between fixing date and valuation date on the day after the fixing
                if fixing_date == calendar.advance(valuation_date, -ql.Period(1, ql.Days), business):
                    if not market_data.has_fixing(fixing_date):
                        new_fixing_date = calendar.advance(valuation_date,
                                                           -ql.Period(2, ql.Days),
                                                           business)
                        fixing = market_data[new_fixing_date]
                        Log.warning(f'Missing fixing of {fixing_date}, used {new_fixing_date} instead')
                        market_data.add_fixing(fixing_date, fixing)
            except QLInputError:
                pass
