from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import defaults
from valuation.engine.check import IsOrdered, Length, ObjectType, Range
from valuation.engine.market_data import QLYieldCurve

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLDiscountCurve(QLYieldCurve):                # pylint: disable=abstract-method
    _signature = signatures.yield_curve.discount

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency = self.data(fields.Currency, check=ObjectType(signatures.currency.all))
        self._curve_dates: list[ql.Date] = self.data(fields.Dates,
                                                     check=[Range(lower=self._valuation_date, strict=False),
                                                            IsOrdered()])
        self._discount_factors: list[float] = self.data(fields.Values,
                                                        check=[Range(lower=0.0,
                                                                     upper=global_parameters.DiscountFactorMaximum),
                                                               Length(self._curve_dates)])
        self._daycount: ql.DayCounter = self.data(fields.DayCount, default_value=defaults.daycount(self._currency.id))
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)

    def _post_init(self) -> None:
        if self._valuation_date not in self._curve_dates:
            self._curve_dates = [self._valuation_date] + self._curve_dates
            self._discount_factors = [1.0] + self._discount_factors
        # SWIGs\discountcurve.i
        # DiscountCurve --> None
        #       dates           vector<Date>
        #       discounts       vector<DiscountFactor>
        #       dayCounter      DayCounter
        #       calendar        Calendar            (Calendar())
        #       i               Interpolator        (LogLinear)
        yield_curve: ql.YieldTermStructure = ql.DiscountCurve(self._curve_dates,
                                                              self._discount_factors,
                                                              self._daycount,
                                                              self._calendar)
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()
