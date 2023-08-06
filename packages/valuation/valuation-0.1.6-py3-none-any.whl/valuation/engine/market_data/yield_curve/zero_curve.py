from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import IsOrdered, Length, ObjectType, Range
from valuation.engine.mappings import Compounding, Frequencies, QLCompounding, QLFrequency
from valuation.engine.market_data import QLYieldCurve
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLZeroCurve(QLYieldCurve):                        # pylint: disable=abstract-method
    _signature = signatures.yield_curve.zero

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._currency = self.data(fields.Currency, check=ObjectType(signatures.currency.all))
        self._curve_dates: list[ql.Date] = self.data(fields.Dates, check=[Range(lower=self._valuation_date,
                                                                                strict=False), IsOrdered()])
        self._zero_rates: list[float] = self.data(fields.Values,
                                                  check=[Range(lower=global_parameters.InterestRateMinimum,
                                                               upper=global_parameters.InterestRateMaximum),
                                                         Length(self._curve_dates)])
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True)
        self._calendar: ql.Calendar = self.data(fields.Calendar, default_value=self._currency.calendar)
        self._compounding: QLCompounding = self.data(fields.Compounding, default_value='Continuous', ql_map=Compounding, allow_fallback_to_default_parameters=True)
        self._frequency: QLFrequency = self.data(fields.Frequency, default_value=Period(1, 'Y'), ql_map=Frequencies)

    def _post_init(self) -> None:
        if self._valuation_date not in self._curve_dates:
            self._curve_dates = [self._valuation_date] + self._curve_dates
            self._zero_rates = [self._zero_rates[0]] + self._zero_rates
        interpolator = ql.Linear()
        # SWIGs\zerocurve.i
        # template(ZeroCurve) InterpolatedZeroCurve<Linear>
        # template <class Interpolator>
        # InterpolatedZeroCurve --> None
        #       dates           vector<Date>
        #       yields          vector<Rate>
        #       dayCounter      DayCounter
        #       calendar        Calendar            (Calendar())
        #       i               Interpolator        (Linear)
        #       compounding     Compounding         (Continuous)
        #       frequency       Frequency           (Annual)
        yield_curve: ql.YieldTermStructure = ql.ZeroCurve(self._curve_dates,
                                                          self._zero_rates,
                                                          self._daycount,
                                                          self._calendar,
                                                          interpolator,
                                                          self._compounding,
                                                          self._frequency)
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()
