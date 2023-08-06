from __future__ import annotations

from typing import Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.engine import QLObjectDB
from valuation.engine.check import RangeWarning
from valuation.engine.instrument.coupons import QLCoupon, SingleQLCashFlow
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument import QLFlexibleSwap, QLFlexibleBond


class QLCouponFixed(QLCoupon):
    _signature = signatures.coupon.fixed
    _pay_off = """
    schedule.pay_dates[ALL]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := life_cycle_payments[FIXING_DATE]
    schedule.pay_dates[-1]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := - life_cycle_payments[FIXING_DATE]
    schedule.pay_dates[ALL]: PAY{FIXING_DATE|FIXING_DATE|PATH[DISCOUNT]|discount} := rates[FIXING_INDEX] * schedule.accrual_time[FIXING_INDEX] * (life_cycle_amounts[FIXING_DATE] / amount)
        """

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,
                 master_object: Union[QLFlexibleSwap, QLFlexibleBond, None] = None, data_only_mode: bool = False,
                 is_swap_leg: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode, is_swap_leg)

        self._rate: float = self.data(
            fields.FixedRate,
            check=RangeWarning(
                global_parameters.InterestRateMinimum,
                global_parameters.InterestRateMaximum,
                strict=False
            )
        )
        self._additional_values.update({fields.FixedRate: self._rate})

        self._rates: list[float] = []
        self._amounts: list[float] = []

    def _post_init(self) -> None:
        super()._post_init()

        # SWIGs\cashflows.i
        # 	FixedRateCoupon --> None
        # 		paymentDate	Date
        # 		nominal	Real
        # 		rate	Rate
        # 		dayCounter	DayCounter
        # 		startDate	Date
        # 		endDate	Date
        # 		refPeriodStart	Date		(Date ( ))
        # 		refPeriodEnd	Date		(Date ( ))
        # 		exCouponDate	Date		(Date ( ))

        for start, end, payment, values in self.schedule_items():
            self._amounts.append(values[fields.Amount])
            self._rates.append(values[fields.FixedRate])
            coupon = ql.FixedRateCoupon(payment,
                                        values[fields.Amount],
                                        values[fields.FixedRate],
                                        self._daycount,
                                        start,
                                        end)
            self._coupons.append(SingleQLCashFlow(coupon.date(), None, self._leg_number, coupon))

    def set_coupon_pricer(self) -> None:
        pass
