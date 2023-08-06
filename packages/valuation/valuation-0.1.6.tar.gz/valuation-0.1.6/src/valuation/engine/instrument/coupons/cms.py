from __future__ import annotations

from typing import Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.engine import QLObjectDB
from valuation.engine.check import ObjectType, Range, RangeWarning
from valuation.engine.instrument.coupons import QLCoupon, SingleQLCashFlow
from valuation.engine.instrument.coupons.base_object import preload_fixing
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, Storage
from valuation.utils.other import is_ql_null_value

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument import QLFlexibleSwap, QLFlexibleBond
    from valuation.engine.market_data import QLInterestRateSwapIndex, QLInterestRateSpreadIndex


class QLCouponCMSBase(QLCoupon):  # pylint: disable=abstract-method

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)

        natural_floor_default: bool = not master_object.is_swap if not self._documentation_mode else False
        self._fixing_in_arrears: bool = self.data(fields.FixingInArrears, default_value=False)
        if is_swap_leg:
            self._has_natural_floor = False
        else:
            self._has_natural_floor: bool = self.data(fields.NaturalFloor, default_value=False, allow_fallback_to_default_parameters=True)
        self._fixing_days: int = self.data(fields.FixingDays, check=Range(lower=0, strict=False), allow_fallback_to_default_parameters=True)

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
            check=RangeWarning(lower=global_parameters.GearingMinimum, upper=global_parameters.GearingMaximum, strict=False)
        )

        self._cap: float = self.data(
            fields.Cap,
            default_value=ql.nullDouble(),
            check=[
                Range(lower=global_parameters.InterestRateMinimum, strict=False),
                RangeWarning(upper=global_parameters.InterestRateMaximum, strict=False)
            ]
        )
        self._floor: float = self.data(
            fields.Floor,
            default_value=ql.nullDouble(),
            check=[
                Range(upper=global_parameters.InterestRateMaximum, strict=False),
                RangeWarning(lower=global_parameters.InterestRateMinimum, strict=False)
            ]
        )
        self._try_past_fixings: bool = self.data(fields.TryToGetPastFixings, allow_fallback_to_default_parameters=True, default_value=True)
        if not is_ql_null_value(self._floor) and self._has_natural_floor:
            self._floor: float = max(self._floor, 0.0)
        elif self._has_natural_floor:
            self._floor = 0.0

        self._additional_values.update(
            {
                fields.Spread: self._spread,
                fields.Gearing: self._gearing,
                fields.Cap: self._cap,
                fields.Floor: self._floor
            }
        )


class QLCouponCMS(QLCouponCMSBase):
    _signature = signatures.coupon.cms

    _market_data_name = None
    _market_data_types = [signatures.index_and_cms]

    _pay_off = """
    schedule.pay_dates[ALL]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := life_cycle_payments[FIXING_DATE]
    schedule.pay_dates[-1]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := - life_cycle_payments[FIXING_DATE]
    schedule.fixing_dates[ALL]: IF NOT(fixing_in_arrears)
        THEN    rate := MAX(MIN(PATH[CMS] * gearing + spread, cap), floor)
        THEN    PAY{schedule.pay_dates[FIXING_INDEX]|schedule.pay_dates[FIXING_INDEX]|PATH[DISCOUNT]|discount} := rate * schedule.accrual_time[FIXING_INDEX] * life_cycle_amounts_as_of_fixing[FIXING_DATE]
    schedule.pay_dates[ALL]: IF fixing_in_arrears:
        THEN    rate := MAX(MIN(PATH[CMS] * gearing + spread, cap), floor)
        THEN    PAY{FIXING_DATE|settlement_days|PATH[DISCOUNT]|discount} := rate * schedule.accrual_time[FIXING_INDEX] * life_cycle_amounts[FIXING_DATE]
    """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)

        self._swap_index: QLInterestRateSwapIndex = self.data(fields.IRSwapIndex, check=ObjectType(signatures.ir_swap_index))

    def _post_init(self) -> None:
        super()._post_init()

        # SWIGs\cashflows.i
        # 	CappedFlooredCmsCoupon --> None
        # 		paymentDate	Date
        # 		nominal	Real
        # 		startDate	Date
        # 		endDate	Date
        # 		fixingDays	Natural
        # 		index	<SwapIndex>
        # 		gearing	Real		(1.0)
        # 		spread	Spread		(0.0)
        # 		cap	Rate		(Null<Rate> ( ))
        # 		floor	Rate		(Null<Rate> ( ))
        # 		refPeriodStart	Date		(Date ( ))
        # 		refPeriodEnd	Date		(Date ( ))
        # 		dayCounter	DayCounter		(DayCounter ( ))
        # 		isInArrears	bool		(false)

        for start, end, payment, values in self.schedule_items():
            coupon = ql.CappedFlooredCmsCoupon(payment,
                                               values[fields.Amount],
                                               start,
                                               end,
                                               self._fixing_days,
                                               self._swap_index.ql_swap_index,
                                               values[fields.Gearing],
                                               values[fields.Spread],
                                               values[fields.Cap],
                                               values[fields.Floor],
                                               ql.Date(),
                                               ql.Date(),
                                               self._daycount,
                                               self._fixing_in_arrears)
            self._coupons.append(SingleQLCashFlow(coupon.date(), coupon.fixingDate(), self._leg_number, coupon, is_fixed=False))
            preload_fixing(coupon.fixingDate(), coupon, self._swap_index, self._schedule.calendar,
                           self._business, self._try_past_fixings)
        if is_ql_null_value(self._cap):
            self._cap = 1e10
        if is_ql_null_value(self._floor):
            self._floor = - 1e10

    def set_coupon_pricer(self) -> None:
        pricer: ql.FloatingRateCouponPricer = self._process.coupon_pricer_analytic(self._descriptor)
        ql.setCouponPricer([coupon.ql_obj for coupon in self._coupons], pricer)


class QLCouponCMSSpread(QLCouponCMSBase):
    _signature = signatures.coupon.cms_spread

    _market_data_name = fields.IRIndex
    _market_data_types = [signatures.ir_index.base]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)

        self._cms_spread_index: QLInterestRateSpreadIndex = self.data(fields.IRSpreadSwapIndex, check=ObjectType(signatures.ir_spread_index))

    def _post_init(self) -> None:
        super()._post_init()

        # SWIGs\cashflows.i
        # 	CappedFlooredCmsSpreadCoupon (CappedFlooredCoupon)
        # 		paymentDate	Date
        # 		nominal	Real
        # 		startDate	Date
        # 		endDate	Date
        # 		fixingDays	Natural
        # 		index	ext::<SwapSpreadIndex>
        # 		gearing	Real		(1.0)
        # 		spread	Spread		(0.0)
        # 		cap	Rate		(Null<Rate> ( ))
        # 		floor	Rate		(Null<Rate> ( ))
        # 		refPeriodStart	Date		(Date ( ))
        # 		refPeriodEnd	Date		(Date ( ))
        # 		dayCounter	DayCounter		(DayCounter ( ))
        # 		isInArrears	bool		(false)
        # 		exCouponDate	Date		(Date ( ))

        for start, end, payment, values in self.schedule_items():
            coupon = ql.CappedFlooredCmsSpreadCoupon(end,
                                                     values[fields.Amount],
                                                     start,
                                                     end,
                                                     self._fixing_days,
                                                     self._cms_spread_index.ql_spread_index,
                                                     values[fields.Gearing],
                                                     values[fields.Spread],
                                                     values[fields.Cap],
                                                     values[fields.Floor],
                                                     ql.Date(),
                                                     ql.Date(),
                                                     self._daycount,
                                                     self._fixing_in_arrears)
            self._coupons.append(SingleQLCashFlow(coupon.date(), coupon.fixingDate(), self._leg_number, coupon, is_fixed=False))
            preload_fixing(coupon.fixingDate(), coupon, self._cms_spread_index, self._schedule.calendar,
                           self._business, self._try_past_fixings)
        if is_ql_null_value(self._cap):
            self._cap = 1e10
        if is_ql_null_value(self._floor):
            self._floor = - 1e10

    def set_coupon_pricer(self) -> None:
        pricer: ql.FloatingRateCouponPricer = self._process.coupon_pricer_analytic(self._descriptor)
        ql.setCouponPricer([coupon.ql_obj for coupon in self._coupons], pricer)
