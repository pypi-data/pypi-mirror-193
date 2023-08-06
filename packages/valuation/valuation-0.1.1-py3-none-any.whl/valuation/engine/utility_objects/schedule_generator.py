from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.engine.check import Range
from valuation.engine.instrument import Schedule
from valuation.engine.mappings import DateGeneration
from valuation.engine.utility_objects import QLUtilityObject

if TYPE_CHECKING:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.mappings import QLBusiness
    from valuation.universal_transfer import Storage, DefaultParameters, Period


class QLScheduleGenerator(QLUtilityObject):
    _signature = signatures.utilities.schedule

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self.business: QLBusiness = self.data(fields.Business, allow_fallback_to_default_parameters=True)
        self.accrual_business: QLBusiness = self.data(fields.AccrualBusiness, allow_fallback_to_default_parameters=True,
                                                      default_value=self.business)

        self.tenor: Period = self.data(fields.Tenor, allow_fallback_to_default_parameters=True)
        self.calendar: ql.Calendar = self.data(fields.Calendar, allow_fallback_to_default_parameters=True)
        self.date_generation = self.data(fields.DateGeneration, allow_fallback_to_default_parameters=True,
                                         default_value='Backward', ql_map=DateGeneration)
        self.end_of_month: bool = self.data(fields.EndOfMonth, allow_fallback_to_default_parameters=True,
                                            default_value=False)

        self.issue: ql.Date = self.data(fields.Issue, allow_fallback_to_default_parameters=True)
        self.maturity: ql.Date = self.data(fields.Maturity, check=Range(lower=self.issue),
                                           allow_fallback_to_default_parameters=True)
        self.first_coupon_date: ql.Date = self.data(fields.FirstCouponDate, default_value=global_parameters.DummyDate)
        self.last_coupon_date: ql.Date = self.data(fields.LastCouponDate, default_value=global_parameters.DummyDate)

        self._schedule = Schedule(self, {}, daycount=ql.Actual360())  # type: ignore[arg-type]

    def get_raw_data(self) -> Union[dict[str, Any], list[dict[str, Any]]]:
        result: list[dict[str, Any]] = []
        dates: list[ql.Date] = list(self._schedule.schedule)
        for start, end in zip(dates[:-1], dates[1:]):
            payment: ql.Date = self.calendar.advance(end, ql.Period(0, ql.Days), self.business)
            result.append({
                'startDate': start.ISO(),
                'endDate': end.ISO(),
                'paymentDate': payment.ISO()
            })
        return result
