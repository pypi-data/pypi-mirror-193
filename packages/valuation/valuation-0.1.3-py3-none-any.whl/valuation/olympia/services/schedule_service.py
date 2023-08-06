from __future__ import annotations

from typing import Any

from valuation.universal_transfer import Period, Storage, Reference, StorageDataBase
from valuation.consts import global_parameters, types
from valuation.consts import fields
from valuation.engine import QLObjectDB, QLFactory

from valuation.olympia.input.mappings.financial import PERIOD_MAP, CALENDAR_MAP, BUSINESS_MAP, DATE_GENERATION_MAP
from valuation.olympia.input.mappings.request_keys import SCHEDULE_DATA_REQUIRED, SCHEDULE_DATA_OPTIONAL
from valuation.olympia.exception import OlympiaException

from valuation.utils import to_json
from valuation.inputs.standard import standard_date_converter

from valuation.global_settings import __type_checking__

# pylint: disable=ungrouped-imports
if __type_checking__:
    from valuation.engine.instrument import QLSchedule
    from valuation.utils import JSONType


class ScheduleServiceMappingException(OlympiaException):
    pass


class ScheduleServiceMissingDataException(OlympiaException):
    pass


def get_accrual_business_convention(convention_raw: str) -> str:
    if 'UNADJUSTED' in convention_raw:
        return BUSINESS_MAP['UNADJUSTED']
    if 'ADJUSTED' in convention_raw:
        business, _ = convention_raw.rsplit('_', maxsplit=1)
        return BUSINESS_MAP[business]
    return BUSINESS_MAP[convention_raw]


def get_period(period_raw: str) -> Period:
    try:
        period_str: str = PERIOD_MAP[period_raw]
        return Period.from_str(period_str)
    except KeyError:
        raise ScheduleServiceMappingException(f'{period_raw} not found in {PERIOD_MAP.keys()}')  # pylint: disable=raise-missing-from


def get_calendar(calendar_raw: str) -> str:
    try:
        return CALENDAR_MAP[calendar_raw]
    except KeyError:
        raise ScheduleServiceMappingException(f'{calendar_raw} not found in {CALENDAR_MAP.keys()}')  # pylint: disable=raise-missing-from


CONVERTERS = {
    types.Date: standard_date_converter,
    types.Period: get_period,
    types.Calendar: get_calendar,
    types.Business: get_accrual_business_convention,
    types.Bool: lambda x: x,
    types.Str: lambda x: DATE_GENERATION_MAP[x]
}


def make_storage_raw(data_raw: dict[str, Any]) -> Storage:
    schedule_raw = Storage()
    schedule_raw.assign_reference(Reference('Schedule', 'ScheduleParameters'))
    missing: list[str] = []
    for key, type_key in SCHEDULE_DATA_REQUIRED.items():
        if key not in data_raw:
            missing.append(key)
        else:
            schedule_raw[type_key] = CONVERTERS[type_key.type](data_raw[key])
    if missing:
        raise ScheduleServiceMissingDataException(', '.join(missing))
    for key, type_key in SCHEDULE_DATA_OPTIONAL.items():
        if key in data_raw and data_raw[key]:
            schedule_raw[type_key] = CONVERTERS[type_key.type](data_raw[key])
    return schedule_raw


def make_schedule_storage(schedule_parameters: Storage) -> Storage:
    schedule: Storage = Storage()
    schedule.assign_reference(Reference('Schedule', 'Schedule'))

    general = Storage()
    general[fields.Type] = 'General'
    general[fields.Business] = schedule_parameters[fields.Business]
    general[fields.Calendar] = schedule_parameters[fields.Calendar]
    general[fields.Tenor] = schedule_parameters[fields.Frequency]
    if fields.DateGeneration in schedule_parameters:
        general[fields.DateGeneration] = schedule_parameters[fields.DateGeneration]
    if fields.EndOfMonth in schedule_parameters:
        general[fields.EndOfMonth] = schedule_parameters[fields.EndOfMonth]
    general.make_immutable()

    roll_out = Storage()
    roll_out[fields.Type] = 'RollOut'
    roll_out[fields.Issue] = schedule_parameters[fields.Issue]
    roll_out[fields.Maturity] = schedule_parameters[fields.Maturity]
    if fields.FirstCouponDate in schedule_parameters:
        roll_out[fields.FirstCouponDate] = schedule_parameters[fields.FirstCouponDate]
    if fields.LastCouponDate in schedule_parameters:
        roll_out[fields.LastCouponDate] = schedule_parameters[fields.LastCouponDate]
    roll_out.make_immutable()

    schedule[fields.Schedule('')] = (general, roll_out)
    schedule.make_immutable()
    return schedule


def format_result(schedule_items: list[dict[str, Any]]) -> JSONType:
    result = []
    for item in schedule_items:
        new_item = {
            'startDate': item['fixingDate'],
            'endDate': item['paymentDate'],
            'paymentDate': item['paymentDate']
        }
        result.append(new_item)
    return to_json(result)


def make_schedule(data_raw: dict[str, Any]) -> JSONType:
    default_params = Storage()
    default_params.assign_reference(global_parameters.DefaultParametersReference)
    default_params[fields.ValuationDate] = global_parameters.DummyDate
    default_params.make_immutable()

    schedule = make_schedule_storage(
        make_storage_raw(
            data_raw
        )
    )

    storage_db = StorageDataBase()
    storage_db.add(default_params)
    storage_db.add(schedule)

    with QLFactory():
        schedule_db: QLObjectDB = QLObjectDB(storage_db)
        schedule_ql: QLSchedule = schedule_db[schedule.reference]  # type: ignore[assignment]
    formatted = format_result(schedule_ql.to_json())
    return formatted


def get_calendars_list() -> list[str]:
    return sorted(list(CALENDAR_MAP.keys()))
