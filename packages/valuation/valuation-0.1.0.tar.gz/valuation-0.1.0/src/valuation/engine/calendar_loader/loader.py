import datetime
from pathlib import Path
from functools import lru_cache

import QuantLib as ql

from valuation.engine.exceptions import DAARuntimeException

CALENDAR_DATA_PATH = Path(__file__).parent / 'data'


class CustomizedCalendar(ql.WeekendsOnly):
    def __init__(self, name: str):
        self.name = name.title() + " imported calendar"
        super().__init__()

    def __str__(self):
        return self.name


class _CalendarLoader:
    _cache: dict[str, ql.Calendar] = {}

    @classmethod
    def _load_data(cls, name: str) -> list[str]:
        file_name = CALENDAR_DATA_PATH / f'{name}.csv'
        if not file_name.exists():
            raise DAARuntimeException(f'CalendarLoader has no data for calendar: {name}')
        with open(file_name) as file_handle:
            dates: list[str] = file_handle.read().split('\n')
        return dates

    @classmethod
    @lru_cache()
    def get(cls, name: str) -> ql.Calendar:
        s_dates: list[str] = cls._load_data(name)
        try:
            dates: list[datetime.date] = [datetime.date.fromisoformat(d) for d in s_dates if d]
        except (TypeError, ValueError):
            raise DAARuntimeException(f'Failed to load dates from external calendar: {name}')
        base_calendar = CustomizedCalendar(name)
        for date in dates:
            base_calendar.addHoliday(ql.Date(date.day, date.month, date.year))
        return base_calendar


def get_calendar(name: str) -> ql.Calendar:
    return _CalendarLoader.get(name)
