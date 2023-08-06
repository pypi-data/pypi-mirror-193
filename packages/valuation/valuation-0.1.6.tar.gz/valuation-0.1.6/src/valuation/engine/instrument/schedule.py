from __future__ import annotations

from typing import Any, Iterator, Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.engine import QLObjectBase, QLObject
from valuation.engine.check import Range, OneNotNone
from valuation.engine.exceptions import QLInputError
from valuation.engine.mappings import DateGeneration
from valuation.engine.utils import date2year_fraction, period2qlperiod, qldate2date
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import DefaultParameters, NoValue, Signature, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument.coupons.base_object import CouponDescriptor
    from valuation.engine.mappings import QLBusiness
    from valuation.universal_transfer import Period, TypeKey


class QLScheduleGeneralBase(QLObjectBase):  # pylint: disable=abstract-method
    _signature = Signature('General')
    _class_family = signatures.Groups.utility

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self.calendar: ql.Calendar = self.data(fields.Calendar, allow_fallback_to_default_parameters=True)
        self.date_generation = self.data(fields.DateGeneration, allow_fallback_to_default_parameters=True,
                                         default_value='Backward', ql_map=DateGeneration)
        self.end_of_month: bool = self.data(fields.EndOfMonth, allow_fallback_to_default_parameters=True,
                                            default_value=False)


class QLScheduleGeneral(QLScheduleGeneralBase):  # pylint: disable=abstract-method
    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self.tenor: Period = self.data(fields.Tenor, allow_fallback_to_default_parameters=True)
        # TODO(2021/10) Happened in QLVanillaSwap: The VanillaSwap gets its currency from the discount curve and the swap's business convention is defaulted to currency base default.
        #  The line below cannot access this currency based default because it is not present in any storage
        self.business: QLBusiness = self.data(fields.Business, allow_fallback_to_default_parameters=True)
        self.accrual_business: QLBusiness = self.data(fields.AccrualBusiness, allow_fallback_to_default_parameters=True,
                                                      default_value=self.business)


class QLLegScheduleGeneral(QLScheduleGeneralBase):  # pylint: disable=abstract-method
    pass


class QLScheduleSingleDateBase(QLObjectBase):
    _signature = Signature('Single')
    _class_family = signatures.Groups.utility

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self.values: dict[TypeKey, Any] = dict()


class QLScheduleSingleDate(QLScheduleSingleDateBase):  # TODO : create a seperate class that only deals with start and end date (check history)

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self.period_start: Optional[ql.Date] = self.data(fields.Issue, default_value=None)
        self._tenor = self.data(fields.Tenor, allow_fallback_to_default_parameters=True,
                                check=OneNotNone(self.period_start), default_value=None)
        self._calendar = self.data(fields.Calendar, allow_fallback_to_default_parameters=True,
                                   check=OneNotNone(self.period_start), default_value=None)
        self._business = self.data(fields.Business, allow_fallback_to_default_parameters=True,
                                   check=OneNotNone(self.period_start), default_value=None)
        self.period_end: ql.Date = self.data(fields.Maturity)
        if self.period_start is None:
            self.period_start = self._calendar.advance(self.period_end, -period2qlperiod(self._tenor), self._business)


class QLLegScheduleSingleDate(QLScheduleSingleDateBase):

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self.period_start: ql.Date = self.data(fields.PeriodStart)
        self.period_end: ql.Date = self.data(fields.PeriodEnd, check=Range(lower=self.period_start))

        self.leg_number: int = self.data(fields.LegNumber)

    def __setitem__(self, type_key: TypeKey, value: Any) -> None:
        self.values[type_key] = value

    def __getitem__(self, type_key: TypeKey) -> Any:
        return self.values[type_key]

    def get(self, type_key: TypeKey, default: Any) -> Any:
        return self.values.get(type_key, default)

    def __contains__(self, type_key: TypeKey) -> bool:
        return type_key in self.values and not isinstance(self.values[type_key], NoValue) and self.values[
            type_key] is not None


class QLScheduleRollOut(QLObjectBase):
    _signature = Signature('RollOut')
    _class_family = signatures.Groups.utility

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self.issue: ql.Date = self.data(fields.Issue, allow_fallback_to_default_parameters=True)
        self.maturity: ql.Date = self.data(fields.Maturity, check=Range(lower=self.issue),
                                           allow_fallback_to_default_parameters=True)
        self.first_coupon_date: ql.Date = self.data(fields.FirstCouponDate, default_value=global_parameters.DummyDate,
                                                    allow_fallback_to_default_parameters=True)
        self.last_coupon_date: ql.Date = self.data(fields.LastCouponDate, default_value=global_parameters.DummyDate,
                                                   allow_fallback_to_default_parameters=True)
        self.values: dict[TypeKey, Any] = dict()


class LegSchedule:  # pylint: disable=too-few-public-methods
    def __init__(self, ql_object: QLObject, additional_keys: Optional[dict[TypeKey, Optional[dict[str, Any]]]] = None):

        class QLLegScheduleSingleDateTemp(QLLegScheduleSingleDate):

            def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                         master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
                super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
                for type_key in additional_keys or []:
                    self.values[type_key] = self.data(type_key, **(additional_keys[type_key] or dict()))  # type: ignore

        self._documentation_mode = ql_object._documentation_mode

        schedule_type_key = fields.Schedule('')
        ql_object.add_linetype(QLLegScheduleGeneral, schedule_type_key)
        ql_object.add_linetype(QLLegScheduleSingleDateTemp, schedule_type_key)

        schedule_parts = ql_object.data(schedule_type_key, default_value=[])  # type: ignore[arg-type]

        if isinstance(schedule_parts, list) and not schedule_parts:
            self._initialized: bool = False
            general_storage = Storage()
            general_storage[fields.Type] = 'General'

            self._general_parameters = QLLegScheduleGeneral(general_storage,
                                                            ql_object.ql_db,
                                                            [ql_object._data, *ql_object._default_parameters],
                                                            ql_object)

        else:
            self._general_parameters = schedule_parts[0]

        if isinstance(schedule_parts, list) and not schedule_parts:
            return

        self._initialized = True
        self._single_parts: list[QLLegScheduleSingleDate] = schedule_parts[1:]

    def get(self, leg: CouponDescriptor, additional_values: dict[TypeKey, Any]) -> ScheduleIterator:
        if self._initialized:
            leg_number: int = leg.leg_number

            single_parts: list[QLLegScheduleSingleDate] = [part for part in self._single_parts
                                                           if part.leg_number == leg_number]

            if not single_parts:
                raise QLInputError(f'Leg {leg_number} has no schedule entries.')

            last_date = single_parts[0].period_start
            schedule_dates: list[ql.Date] = []

            for single_part in single_parts:
                if last_date != single_part.period_start:
                    raise QLInputError(f'{last_date} != {single_part.period_start}')
                last_date = single_part.period_end

                schedule_dates.append(single_part.period_start)
                for key, value in additional_values.items():
                    if key not in single_part:
                        single_part[key] = value
            schedule_dates.append(single_parts[-1].period_end)
            # SWIGs\scheduler.i
            # Schedule
            # 		[UNKNOWN]	vector<Date>
            # 		calendar	Calendar		(NullCalendar ( ))
            # 		convention	BusinessDayConvention		(Unadjusted)
            # 		terminationDateConvention	optional<BusinessDayConvention>		(none)
            # 		tenor	optional<Period>		(none)
            # 		rule	optional<DateGeneration::Rule>		(none)
            # 		endOfMonth	optional<bool>		(none)
            # 		isRegular	vector<bool>		(vector<bool> ( 0 ))
            schedule = ql.Schedule(schedule_dates,
                                   self._general_parameters.calendar,
                                   leg.accrual_business,
                                   leg.accrual_business,
                                   period2qlperiod(leg.tenor),
                                   self._general_parameters.date_generation,
                                   self._general_parameters.end_of_month,
                                   [True] * (len(schedule_dates) - 1))

            return ScheduleIterator(schedule, single_parts, leg.daycount)  # type: ignore[arg-type]
        # SWIGs\scheduler.i
        # Schedule
        #       effectiveDate	Date
        # 		terminationDate	Date
        # 		tenor	Period
        # 		calendar	Calendar
        # 		convention	BusinessDayConvention
        # 		terminationDateConvention	BusinessDayConvention
        # 		rule	DateGeneration::Rule
        # 		endOfMonth	bool
        # 		firstDate	Date		(Date ( ))
        # 		nextToLastDate	Date		(Date ( ))
        schedule = ql.Schedule(leg.issue,
                               leg.maturity,
                               period2qlperiod(leg.tenor),
                               leg.calendar,
                               leg.accrual_business,
                               leg.accrual_business,
                               leg.date_generation,
                               leg.end_of_month,
                               leg.first_coupon_date,
                               leg.next_to_last_coupon)
        return ScheduleIterator(schedule, [additional_values] * (len(schedule) - 1), leg.daycount)


class ScheduleIterator:
    def __init__(self, schedule: ql.Schedule,
                 schedule_entries: list[Union[dict[TypeKey, Any], QLLegScheduleSingleDate]],
                 daycount: ql.DayCounter) -> None:
        self._schedule: ql.Schedule = schedule
        self._schedule_entries: list[Union[dict[TypeKey, Any], QLLegScheduleSingleDate]] = schedule_entries

        self._fixing_dates = list(self._schedule)[:-1]
        self._pay_dates = list(self._schedule)[1:]
        self._maturity = list(self._schedule)[-1]
        self._accrual_time: list[float] = [date2year_fraction(start_date, end_date, daycount) for
                                           start_date, end_date in zip(self._fixing_dates, self._pay_dates)]

    def __iter__(self) -> Iterator[tuple[ql.Date, ql.Date, Union[dict[TypeKey, Any], QLLegScheduleSingleDate]]]:
        for i, end_date in enumerate(list(self._schedule)[1:]):
            yield self._schedule[i], end_date, self._schedule_entries[i]

    @property
    def schedule(self) -> ql.Schedule:
        return self._schedule

    @property
    def accrual_time(self) -> list[float]:
        return self._accrual_time

    @property
    def calendar(self) -> ql.Calendar:
        return self._schedule.calendar()

    @property
    def tenor(self) -> Period:
        return self._schedule.tenor()  # type: ignore[no-any-return]

    @property
    def maturity(self) -> ql.Date:
        return self._maturity


class Schedule:  # pylint: disable=too-many-instance-attributes

    # TODO(2022/08) Review Schedule class, see below
    # The ql.Schedule should be used to produce accrual start dates and accrual end dates. These dates should be generated with the accrualBusiness(business) field.
    # Fixing dates should be generated by the instruments/coupons by using the correct fixing days offset provided by the index.
    # Payment dates should be generated by the instruments/coupons by using the business(business) field and an optional payment date offset integer (e.g. paymentDelay(i))

    @property
    def start_dates(self) -> list[ql.Date]:
        return self._fixing_dates

    @property
    def end_dates(self) -> list[ql.Date]:
        return self._pay_dates

    @property
    def accrual_time(self) -> list[float]:
        # Warning: Refactoring this name brakes FP Bond payoffs
        return self._accrual_times

    @property
    def calendar(self) -> ql.Calendar:
        return self._calendar

    @property
    def schedule(self) -> ql.Schedule:
        return self._schedule

    @property
    def tenor(self) -> Period:
        return self._tenor

    @property
    def maturity(self) -> ql.Date:
        return self._maturity

    def __init__(self, ql_object: QLObject, additional_keys: Optional[dict[TypeKey, Optional[dict[str, Any]]]] = None,
                 allow_roll_out: bool = True, allow_single: bool = True, daycount: Optional[ql.DayCounter] = None,
                 name_suffix: str = ''):

        class QLScheduleSingleDateTemp(QLScheduleSingleDate):
            _signature = Signature(QLScheduleSingleDate.object_type + name_suffix)

            def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                         master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
                super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
                for type_key in additional_keys or []:
                    self.values[type_key] = self.data(type_key, **(additional_keys[type_key] or dict()))  # type: ignore

        class QLScheduleRollOutTemp(QLScheduleRollOut):
            _signature = Signature(QLScheduleRollOut.object_type + name_suffix)

            def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                         master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
                super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
                for type_key in additional_keys or []:
                    self.values[type_key] = self.data(type_key, **(additional_keys[type_key] or dict()))  # type: ignore

        self._documentation_mode = ql_object._documentation_mode

        self._values: dict[TypeKey, list[Any]] = dict()

        self._aliases: dict[str, TypeKey] = {}
        if additional_keys is not None:
            for type_key in additional_keys:
                if 'alias' in additional_keys[type_key]:  # type: ignore[operator]         # None was excluded
                    alias_name: str = additional_keys[type_key].pop(
                        'alias')  # type: ignore[union-attr]       # None was excluded
                    assert not alias_name.startswith('_')
                    self._aliases[alias_name] = type_key

        schedule_type_key = fields.Schedule(name_suffix)

        ql_object.add_linetype(QLScheduleGeneral, schedule_type_key)
        if allow_single:
            ql_object.add_linetype(QLScheduleSingleDateTemp, schedule_type_key)
        if allow_roll_out:
            ql_object.add_linetype(QLScheduleRollOutTemp, schedule_type_key)

        schedule_parts = ql_object.data(schedule_type_key, default_value=[])  # type: ignore[arg-type]

        if schedule_parts == [] and not isinstance(schedule_parts, NoValue):
            general_storage = Storage()
            general_storage[fields.Type] = 'General'

            roll_out_storage = Storage()
            roll_out_storage[fields.Type] = 'RollOut'

            schedule_parts.append(
                QLScheduleGeneral(general_storage,
                                  ql_object.ql_db,
                                  [ql_object._data, *ql_object._default_parameters],
                                  ql_object)
            )
            schedule_parts.append(
                QLScheduleRollOutTemp(roll_out_storage,
                                      ql_object.ql_db,
                                      [ql_object._data, *ql_object._default_parameters],
                                      ql_object)
            )
        if isinstance(schedule_parts, NoValue):
            return

        if not isinstance(schedule_parts[0], QLScheduleGeneral):
            raise QLInputError('General part must be in front')

        general_parameters: QLScheduleGeneral = schedule_parts[0]
        self._calendar = general_parameters.calendar
        self._tenor: Period = general_parameters.tenor
        if len(schedule_parts) == 2 and isinstance(schedule_parts[1], QLScheduleRollOutTemp):
            # SWIGs\scheduler.i
            # Schedule
            # 		effectiveDate	Date
            # 		terminationDate	Date
            # 		tenor	Period
            # 		calendar	Calendar
            # 		convention	BusinessDayConvention
            # 		terminationDateConvention	BusinessDayConvention
            # 		rule	DateGeneration::Rule
            # 		endOfMonth	bool
            # 		firstDate	Date		(Date ( ))
            # 		nextToLastDate	Date		(Date ( ))
            roll_out: QLScheduleRollOut = schedule_parts[1]

            fst_cpn_date = roll_out.first_coupon_date or ql.Date()
            last_cpn_date = roll_out.last_coupon_date or ql.Date()
            # if not roll_out.first_coupon_date and roll_out.last_coupon_date:
            #     raise QLInputError()
            # if roll_out.first_coupon_date and not roll_out.last_coupon_date:
            #     raise QLInputError()

            self._schedule: Schedule = ql.Schedule(roll_out.issue,
                                                   roll_out.maturity,
                                                   period2qlperiod(general_parameters.tenor),
                                                   general_parameters.calendar,
                                                   general_parameters.accrual_business,
                                                   general_parameters.accrual_business,
                                                   general_parameters.date_generation,
                                                   general_parameters.end_of_month,
                                                   fst_cpn_date,
                                                   last_cpn_date)
            number_dates = len(self._schedule)
            for key, value in roll_out.values.items():
                self._values[key] = [value] * (number_dates - 1)
        else:
            single_parts: list[QLScheduleSingleDate] = schedule_parts[1:]
            # TODO(2021/10) Happened at least in QLVanillaSwap and QLFixedBond: If the schedules provided contain only a single "General" schedule item, the below line will raise an uncaught IndexError: list index out of range
            for key in single_parts[0].values:
                self._values[key] = []
            last_date = single_parts[0].period_start
            schedule_dates: list[ql.Date] = []
            for single_part in single_parts:
                if last_date != single_part.period_start:
                    raise QLInputError
                last_date = single_part.period_end
                schedule_dates.append(single_part.period_start)
                for key, value in single_part.values.items():
                    self._values[key].append(value)
            schedule_dates.append(single_parts[-1].period_end)
            # SWIGs\scheduler.i
            # Schedule
            # 		[UNKNOWN]	vector<Date>
            # 		calendar	Calendar		(NullCalendar ( ))
            # 		convention	BusinessDayConvention		(Unadjusted)
            # 		terminationDateConvention	optional<BusinessDayConvention>		(none)
            # 		tenor	optional<Period>		(none)
            # 		rule	optional<DateGeneration::Rule>		(none)
            # 		endOfMonth	optional<bool>		(none)
            # 		isRegular	vector<bool>		(vector<bool> ( 0 ))
            self._schedule = ql.Schedule(schedule_dates,
                                         general_parameters.calendar,
                                         general_parameters.accrual_business,
                                         general_parameters.accrual_business,
                                         period2qlperiod(general_parameters.tenor),
                                         general_parameters.date_generation,
                                         general_parameters.end_of_month,
                                         [True] * (len(schedule_dates) - 1))

        self._fixing_dates: list[ql.Date] = list(self._schedule)[:-1]  # type: ignore[call-overload]
        self._pay_dates: list[ql.Date] = list(self._schedule)[1:]  # type: ignore[call-overload]
        self._maturity: ql.Date = list(self._schedule)[-1]  # type: ignore[call-overload]
        if daycount is not None:
            self._accrual_times: list[float] = [date2year_fraction(start_date, end_date, daycount) for
                                                start_date, end_date in zip(self.start_dates, self.end_dates)]

    def __getattr__(self, item: str) -> list[Any]:
        if __debug__ and self._documentation_mode:
            return NoValue()  # type: ignore[return-value]
        # Financial Program usage only!
        if not item.startswith('_'):
            raise ProgrammingError()
        return self._values[self._aliases[item[1:]]]

    def __len__(self) -> int:
        return len(self._pay_dates)

    def __getitem__(self, item: TypeKey) -> list[Any]:
        return self._values[item]


class QLSchedule(QLObject):
    _signature = Signature('Schedule')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._daycount: Optional[ql.DayCounter] = self.data(fields.DayCount, default_value=None)
        self._schedule = Schedule(self, daycount=self._daycount)

    def print(self) -> str:
        result: list[str] = [
            str(self),
            f'DayCount:\t{self._daycount}',
            f'Calendar:\t{self._schedule.calendar}',
            f'Tenor:\t{self._schedule.tenor}',
            f'Maturity:\t{self._schedule.maturity}',
            'FixingDate\tPayDate\tAccrualTime'
        ]
        for count, (start, end) in enumerate(zip(self._schedule.start_dates, self._schedule.end_dates)):
            accrual_time = str(self._schedule.accrual_time[count]) if self._daycount else '---'
            result.append(f'{qldate2date(start)}\t{qldate2date(end)}\t{accrual_time}')
        return '\n'.join(result)

    def to_json(self) -> list[dict[str, Any]]:
        json_out: list[dict[str, Any]] = []
        for start, end in zip(self._schedule.start_dates, self._schedule.end_dates):
            json_out.append({
                'fixingDate': qldate2date(start),
                'paymentDate': qldate2date(end)
            })
        return json_out
