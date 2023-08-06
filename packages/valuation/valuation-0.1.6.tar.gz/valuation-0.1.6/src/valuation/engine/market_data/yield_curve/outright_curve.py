from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Contains, IsOrdered, Length, ObjectType, Range
from valuation.engine.market_data import QLYieldCurve

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLOutrightCurve(QLYieldCurve):                # pylint: disable=abstract-method
    _signature = signatures.yield_curve.outright

    @property
    def is_base_curve(self) -> bool:
        return False

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency = self.data(fields.Currency, check=ObjectType(signatures.currency.all))
        self._curve_dates: list[ql.Date] = self.data(fields.Dates, check=[Range(lower=self._valuation_date,
                                                                                strict=False),
                                                                          IsOrdered(),
                                                                          Contains(self._valuation_date)])
        self._outright_factors: list[float] = self.data(fields.Values,
                                                        check=[Range(lower=0.0), Length(self._curve_dates)])
        self._comparison_curve: QLYieldCurve = self.data(fields.DiscountCurve, check=ObjectType(signatures.yield_curve.all))
        self._is_base_curve: bool = self.data(fields.IsBaseCurve)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True)
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)

    def _post_init(self) -> None:
        discount_factors: list[float] = []
        for date, unadjusted_outright_factor in zip(self._curve_dates, self._outright_factors):
            discount_factor_other_curve = self._comparison_curve[date]
            outright_factor = unadjusted_outright_factor / self._outright_factors[0]
            if self._is_base_curve:
                discount_factors.append(discount_factor_other_curve / outright_factor)
            else:
                discount_factors.append(discount_factor_other_curve * outright_factor)

        # SWIGs\discountcurve.i
        # DiscountCurve --> None
        #       dates           vector<Date>
        #       discounts       vector<DiscountFactor>
        #       dayCounter      DayCounter
        #       calendar        Calendar            (Calendar())
        #       i               Interpolator        (LogLinear)
        yield_curve: ql.YieldTermStructure = ql.DiscountCurve(self._curve_dates,
                                                              discount_factors,
                                                              self._daycount,
                                                              self._calendar)
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()
