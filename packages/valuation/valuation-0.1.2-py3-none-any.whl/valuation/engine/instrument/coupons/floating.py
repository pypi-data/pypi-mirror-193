from __future__ import annotations

from typing import Union

import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.engine import QLObjectDB
from valuation.engine.check import Range, RangeWarning
from valuation.engine.exceptions import QLInputError
from valuation.engine.instrument.coupons import QLCoupon, SingleQLCashFlow
from valuation.engine.instrument.coupons.base_object import preload_fixing
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, Storage
from valuation.utils.other import is_ql_null_value

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument import QLFlexibleSwap, QLFlexibleBond


class QLCouponFloatingBase(QLCoupon):
    _market_data_name = fields.IRIndex
    _market_data_types = [signatures.ir_index.base]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)

        self._fixing_in_arrears: bool = self.data(fields.FixingInArrears, default_value=False)
        if is_swap_leg:
            self._has_natural_floor = False
        else:
            self._has_natural_floor = self.data(fields.NaturalFloor,
                                                default_value=False,
                                                allow_fallback_to_default_parameters=True)  # TODO : do we need this for bonds with floor 0?
        self._fixing_days: int = self.data(
            fields.FixingDays,
            check=Range(lower=0, strict=False),
            allow_fallback_to_default_parameters=True
        )
        self._try_past_fixings: bool = self.data(fields.TryToGetPastFixings, allow_fallback_to_default_parameters=True,
                                                 default_value=True)
        self._spread: float = self.data(
            fields.Spread,
            default_value=0.0,
            check=RangeWarning(
                lower=global_parameters.InterestRateMinimum,
                upper=global_parameters.InterestRateMaximum,
                strict=False
            )
        )
        self._gearing: float = self.data(
            fields.Gearing,
            default_value=1.0,
            check=RangeWarning(lower=global_parameters.GearingMinimum, upper=global_parameters.GearingMaximum,
                               strict=False)
        )

        self._additional_values.update(
            {
                fields.Spread: self._spread,
                fields.Gearing: self._gearing
            }
        )

        self._spreads: list[float] = []
        self._gearings: list[float] = []

    def _make_single_floating_coupon(self, payment: ql.Date, start: ql.Date, end: ql.Date,
                                     values) -> ql.FloatingRateCoupon:
        raise NotImplementedError

    def _post_init(self) -> None:
        super()._post_init()

        # SWIGs\cashflows.i
        # 	IborCoupon --> None
        # 		paymentDate	Date
        # 		nominal	Real
        # 		startDate	Date
        # 		endDate	Date
        # 		fixingDays	Integer
        # 		index	<IborIndex>
        # 		gearing	Real		(1.0)
        # 		spread	Spread		(0.0)
        # 		refPeriodStart	Date		(Date ( ))
        # 		refPeriodEnd	Date		(Date ( ))
        # 		dayCounter	DayCounter		(DayCounter ( ))

        for start, end, payment, values in self.schedule_items():
            self._spreads.append(values[fields.Spread])
            self._gearings.append(values[fields.Gearing])
            coupon = self._make_single_floating_coupon(payment, start, end, values)
            self._coupons.append(SingleQLCashFlow(coupon.date(), coupon.fixingDate(), self._leg_number, coupon, is_fixed=False))

            preload_fixing(coupon.fixingDate(), coupon, self._market_data_of_process, self._schedule.calendar,
                           self._business, self._try_past_fixings)

    def set_coupon_pricer(self) -> None:
        pricer: ql.FloatingRateCouponPricer = self._process.coupon_pricer_analytic(self.base_data)
        ql.setCouponPricer([coupon.ql_obj for coupon in self._coupons], pricer)


class QLCouponFloating(QLCouponFloatingBase):
    _signature = signatures.coupon.floating

    _pay_off = """
schedule.pay_dates[ALL]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := life_cycle_payments[FIXING_DATE]
schedule.pay_dates[-1]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := - life_cycle_payments[FIXING_DATE]
schedule.fixing_dates[ALL]: IF NOT(fixing_in_arrears)
    THEN    rate := PATH[VALUE] * gearings[FIXING_INDEX] + spreads[FIXING_INDEX]
    THEN    PAY{schedule.pay_dates[FIXING_INDEX]|schedule.pay_dates[FIXING_INDEX]|PATH[DISCOUNT]|discount} := MAX(rate, fp_floor) * schedule.accrual_time[FIXING_INDEX] * life_cycle_amounts_as_of_fixing[FIXING_DATE]
schedule.pay_dates[ALL]: IF fixing_in_arrears:
    THEN    rate := PATH[VALUE] * gearings[FIXING_INDEX] + spreads[FIXING_INDEX]
    THEN    PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount} := MAX(rate, fp_floor) * schedule.accrual_time[FIXING_INDEX] * life_cycle_amounts[FIXING_DATE]
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)
        self._fp_floor = .0 if self._has_natural_floor else -1e10

    def _make_single_floating_coupon(self, payment: ql.Date, start: ql.Date, end: ql.Date,
                                     values) -> ql.FloatingRateCoupon:
        coupon = ql.IborCoupon(payment,
                               values[fields.Amount],
                               start,
                               end,
                               self._fixing_days,
                               self._market_data_of_process.ql_index,  # type: ignore[attr-defined]
                               values[fields.Gearing],
                               values[fields.Spread],
                               ql.Date(),
                               ql.Date(),
                               self._daycount,
                               self._fixing_in_arrears)
        if self._has_natural_floor:
            coupon = ql.CappedFlooredCoupon(
                coupon,
                cap=ql.nullDouble(),
                floor=0.0
            )
        return coupon


class QLCouponCappedFloored(QLCouponFloating):
    _signature = signatures.coupon.capped_floored
    # todo (2021/04) @contextmanager "descriptor" of CapFloor Process missing
    _pay_off = """
schedule.pay_dates[ALL]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := life_cycle_payments[FIXING_DATE]
schedule.pay_dates[-1]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := - life_cycle_payments[FIXING_DATE]
schedule.fixing_dates[ALL]: IF NOT(fixing_in_arrears)
    THEN    rate := PATH[VALUE] * gearings[FIXING_INDEX] + spreads[FIXING_INDEX]
    THEN    PAY{schedule.pay_dates[FIXING_INDEX]|schedule.pay_dates[FIXING_INDEX]|PATH[DISCOUNT]|discount} := MAX(MIN(cap, rate), floor) * schedule.accrual_time[FIXING_INDEX] * life_cycle_amounts_as_of_fixing[FIXING_DATE]
schedule.pay_dates[ALL]: IF fixing_in_arrears:
    THEN    rate := PATH[VALUE] * gearings[FIXING_INDEX] + spreads[FIXING_INDEX]
    THEN    PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount} := MAX(MIN(cap, rate), floor) * schedule.accrual_time[FIXING_INDEX] * life_cycle_amounts[FIXING_DATE]
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)

        self._cap: float = self.data(
            fields.Cap,
            default_value=ql.nullDouble(),
            check=RangeWarning(
                lower=global_parameters.InterestRateMinimum,
                upper=global_parameters.InterestRateMaximum,
                strict=False
            )
        )
        self._floor: float = self.data(
            fields.Floor,
            check=RangeWarning(
                lower=global_parameters.InterestRateMinimum,
                upper=global_parameters.InterestRateMaximum,
                strict=False
            ),
            default_value=ql.nullDouble()
        )
        if not is_ql_null_value(self._floor) and self._has_natural_floor:
            self._floor = max(self._floor, 0.)
        elif self._has_natural_floor:
            self._floor = 0.

        self._additional_values.update({fields.Cap: self._cap, fields.Floor: self._floor})

    def _make_single_floating_coupon(self, payment: ql.Date, start: ql.Date, end: ql.Date,
                                     values) -> ql.FloatingRateCoupon:
        # SWIGs\cashflows.i
        # 	CappedFlooredIborCoupon --> None
        # 		paymentDate	Date
        # 		nominal	Real
        # 		startDate	Date
        # 		endDate	Date
        # 		fixingDays	Integer
        # 		index	ext::<IborIndex>
        # 		gearing	Real		(1.0)
        # 		spread	Spread		(0.0)
        # 		cap	Rate		(Null<Rate> ( ))
        # 		floor	Rate		(Null<Rate> ( ))
        # 		refPeriodStart	Date		(Date ( ))
        # 		refPeriodEnd	Date		(Date ( ))
        # 		dayCounter	DayCounter		(DayCounter ( ))
        # 		isInArrears	bool		(false)
        # 		exCouponDate	Date		(Date ( ))
        return ql.CappedFlooredIborCoupon(
            payment,
            values[fields.Amount],
            start,
            end,
            self._fixing_days,
            self._market_data_of_process.ql_index,  # type: ignore[attr-defined]
            values[fields.Gearing],
            values[fields.Spread],
            values[fields.Cap],
            values[fields.Floor],
            ql.Date(),
            ql.Date(),
            self._daycount,
            self._fixing_in_arrears
        )

    def _post_init(self) -> None:
        super()._post_init()

        if is_ql_null_value(self._cap):
            self._cap = 1e10
        if is_ql_null_value(self._floor):
            self._floor = - 1e10


class QLCouponOvernight(QLCouponFloating):
    _signature = signatures.coupon.overnight
    _pay_off = """"""

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)
        if not self._documentation_mode:
            if not self._market_data_of_process.is_overnight_index:  # type: ignore[attr-defined]
                raise QLInputError('Index is not an Overnight Index.')

    def _post_init_(self) -> None:
        # OvernightIndexedCoupon (FloatingRateCoupon)
        # 	OvernightIndexedCoupon --> None
        # 		paymentDate	Date
        # 		nominal	Real
        # 		startDate	Date
        # 		endDate	Date
        # 		overnightIndex	ext::<OvernightIndex>
        # 		gearing	Real		(1.0)
        # 		spread	Spread		(0.0)
        # 		refPeriodStart	Date		(Date ( ))
        # 		refPeriodEnd	Date		(Date ( ))
        # 		dayCounter	DayCounter		(DayCounter ( ))
        # 		telescopicValueDates	bool		(false)
        #       averagingMethod RateAveraging::Type (RateAveraging::Compound)
        for start, end, payment, values in self.schedule_items():
            self._spreads.append(values[fields.Spread])
            self._gearings.append(values[fields.Gearing])
            coupon = ql.OvernightIndexedCoupon(
                payment,
                values[fields.Amount],
                start,
                end,
                self._market_data_of_process.ql_index,  # type: ignore[attr-defined]
                values[fields.Gearing],
                values[fields.Spread],
                ql.Date(),
                ql.Date(),
                self._daycount,
                False,
                ql.RateAveraging.Compound
            )
            self._coupons.append(
                SingleQLCashFlow(coupon.date(), coupon.fixingDate(), self._leg_number, coupon, is_fixed=False)
            )
            for fixing_date in coupon.fixingDates():
                preload_fixing(fixing_date, coupon, self._market_data_of_process, self._schedule.calendar,
                               self._business)

    def set_coupon_pricer(self) -> None:
        pass
