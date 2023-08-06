from __future__ import annotations

from typing import Optional, Union

import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.engine import QLObject, QLObjectBase, QLObjectDB
from valuation.engine.check import OneNotNone, Range, RangeWarning
from valuation.engine.exceptions import QLInputError
from valuation.engine.mappings import QLBusiness
from valuation.universal_transfer import DefaultParameters, Signature, Storage


class QLCallItem(QLObjectBase):
    _signature = signatures.empty

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,  # pylint: disable=unsubscriptable-object
                 master_object: Optional[QLObject] = None, data_only_mode: bool = False) -> None:  # pylint: disable=unsubscriptable-object
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._call_price: Optional[float] = self.data(
            fields.CallPrice,
            default_value=None,
            check=[
                Range(lower=0.0, strict=True),
                RangeWarning(upper=global_parameters.CallPutPriceMaximum, strict=False)
            ]
        )
        self._put_price: Optional[float] = self.data(
            fields.PutPrice,
            default_value=None,
            check=[
                Range(lower=0.0, strict=True),
                RangeWarning(upper=global_parameters.CallPutPriceMaximum, strict=False),
                OneNotNone(self._call_price)
            ]
        )

        if self._call_price is not None:
            self._call_price *= 100.0
        if self._put_price is not None:
            self._put_price *= 100.0

    def resolve(self, calendar: ql.Calendar, business: QLBusiness, payment_schedule: ql.Schedule) -> list[ql.Callability]:
        raise NotImplementedError


class QLSingleCall(QLCallItem):
    _signature = Signature('SingleCall')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,  # pylint: disable=unsubscriptable-object
                 master_object: Optional[QLObject] = None, data_only_mode: bool = False) -> None:  # pylint: disable=unsubscriptable-object
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._call_date: ql.Date = self.data(fields.CallDate)
        self._call_on_coupon_date: bool = self.data(fields.CallOnCouponDate, default_value=True)

    def resolve(self, calendar: ql.Calendar, business: QLBusiness, payment_schedule: ql.Schedule) -> list[ql.Callability]:
        date = self._call_date
        if payment_schedule is not None and self._call_on_coupon_date:
            if calendar.isBusinessDay(self._call_date) and self._call_date not in payment_schedule:
                raise QLInputError(f'Call date does not fall on a coupon date: {self._call_date}')
            if not calendar.isBusinessDay(self._call_date):
                date = calendar.adjust(self._call_date, business)
                if date not in payment_schedule:
                    raise QLInputError('Call date does not fall on coupon date even after adjusting')

        single_calls: list[ql.Callability] = []
        if self._call_price is not None:
            single_calls.append(ql.Callability(ql.BondPrice(self._call_price, ql.BondPrice.Clean), ql.Callability.Call, date))
        if self._put_price is not None:
            single_calls.append(ql.Callability(ql.BondPrice(self._put_price, ql.BondPrice.Clean), ql.Callability.Put, date))
        return single_calls


class QLAmericanCall(QLCallItem):
    _signature = Signature('AmericanCall')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None,  # pylint: disable=unsubscriptable-object
                 master_object: Optional[QLObject] = None, data_only_mode: bool = False) -> None:  # pylint: disable=unsubscriptable-object
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._start_date: ql.Date = self.data(fields.PeriodStart)
        self._end_date: ql.Date = self.data(fields.PeriodEnd)

    def resolve(self, calendar: ql.Calendar, business: QLBusiness, payment_schedule: ql.Schedule) -> list[ql.Callability]:
        if self._start_date == self._end_date:
            temp_schedule: Union[ql.Schedule, list[ql.Date]] = [self._start_date]
        else:
            temp_schedule = ql.Schedule(self._start_date,
                                        self._end_date,
                                        ql.Period(1, ql.Days),
                                        calendar,
                                        business,
                                        business,
                                        ql.DateGeneration.Backward,
                                        False)
        single_calls: list[ql.Callability] = []
        for date in temp_schedule:
            if self._call_price is not None:
                single_calls.append(ql.Callability(ql.BondPrice(self._call_price, ql.BondPrice.Clean), ql.Callability.Call, date))
            if self._put_price is not None:
                single_calls.append(ql.Callability(ql.BondPrice(self._put_price, ql.BondPrice.Clean), ql.Callability.Put, date))
        return single_calls


class SSDCall:
    """
    Call right granted by German law for "Schuldscheindarlehen" (SSD), defined in §489 BGB
    * instruments with floating coupon are always callable with a notice of 3 months
    * instruments with fixed coupon are always callable with a notice of 6 months, 10 years after activation of the
        instrument or after the last call. Even if the 10 years are passed, a regular call would reactive that blocking
        period.
    """
    def __init__(self, call_schedule: ql.CallabilitySchedule, is_float: bool, issue: ql.Date, maturity: ql.Date,
                 valuation_date: ql.Date, calendar: ql.Calendar, business: int):
        self._call_schedule = call_schedule
        self._issue = issue
        self._maturity = maturity
        self._valuation_date = valuation_date
        self._calendar = calendar
        self._business = business

        if is_float:
            self.notice: ql.Period = ql.Period('3M')
            self.time_to_call: ql.Period = ql.Period('0D')
        else:
            self.notice = ql.Period('6M')
            self.time_to_call = ql.Period('10Y')

        self._ssd_call_dates: list[ql.Date] = []
        self._generate_possible_ssd_calls()
        self._clear_notice_period()

    def get(self) -> ql.CallabilitySchedule:
        new_schedule = list(self._call_schedule)
        new_schedule.extend(ql.Callability(ql.BondPrice(100.0, ql.BondPrice.Clean), ql.Callability.Call, date) for date in self._ssd_call_dates)

        return ql.CallabilitySchedule(sorted(new_schedule, key=lambda c: c.date()))  # type: ignore[no-any-return]

    def _advance_block_date(self, date: ql.Date) -> ql.Date:
        return self._calendar.advance(date, self.time_to_call)

    def _submit_dates(self, start_date: ql.Date, end_date: ql.Date) -> None:
        if end_date < self._valuation_date:
            return
        self._ssd_call_dates.extend(list(
            ql.Schedule(max(start_date, self._valuation_date),
                        end_date,
                        ql.Period(1, ql.Days),
                        self._calendar,
                        self._business,
                        self._business,
                        ql.DateGeneration.Backward,
                        False)
        )[:-1])  # excluding the end date as it's already on the schedule

    def _generate_possible_ssd_calls(self) -> None:
        block_end_date: ql.Date = self._advance_block_date(self._issue)

        for single_call in self._call_schedule:
            if single_call.type() != ql.Callability.Call:
                continue
            call_date: ql.Date = single_call.date()
            if call_date > block_end_date:
                self._submit_dates(block_end_date, call_date)
            block_end_date = self._advance_block_date(call_date)

        if block_end_date < self._maturity:
            self._submit_dates(block_end_date, self._maturity)

    def _clear_notice_period(self) -> None:
        notice_end = self._calendar.advance(self._valuation_date, self.notice)
        for date in list(sorted(self._ssd_call_dates)):
            if self._valuation_date <= date <= notice_end:
                self._ssd_call_dates.remove(date)


def generate_call_schedule(call_schedule: list[QLCallItem], payment_schedule: ql.Schedule, calendar: ql.Calendar,
                           business: QLBusiness) -> ql.CallabilitySchedule:
    single_calls: list[ql.Callability] = []
    for schedule_item in call_schedule:
        single_calls.extend(schedule_item.resolve(calendar, business, payment_schedule))
    return ql.CallabilitySchedule(single_calls)
