from collections import defaultdict
from timeit import default_timer
from typing import Any, TypeVar, Union

import QuantLib as ql

from daa_utils import Log
from valuation.exceptions import ProgrammingError

Serialize = TypeVar('Serialize')
Serialize2nd = TypeVar('Serialize2nd')


def listify(value: Union[None, Serialize, list[Serialize]]) -> list[Serialize]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def zip_listify(value_left: Union[Serialize, list[Serialize]], value_right: Union[Serialize2nd, list[Serialize2nd]]) -> list[tuple[Serialize, Serialize2nd]]:
    if isinstance(value_left, list):
        if isinstance(value_right, list):
            assert len(value_left) == len(value_right)
            return list(zip(value_left, value_right))
        return [(v_left, value_right) for v_left in value_left]
    if isinstance(value_right, list):
        return [(value_left, v_right) for v_right in value_right]
    return [(value_left, value_right)]


def de_listify(value: list[Serialize]) -> Union[Serialize, list[Serialize]]:
    return value[0] if len(value) == 1 else value


def is_nan(value: float) -> bool:
    return value is None or value != value or is_ql_null_value(value)              # pylint: disable=comparison-with-itself


def is_ql_null_value(value: Any) -> bool:
    # todo: (2021/01) potentially we can expand this to all null types in ql (e.g. NullDates, NullCalendar
    #  etc. --> if needed)
    if isinstance(value, (int, float)):
        return value in [ql.nullDouble(), ql.nullInt()]
    return False


class Timer:
    _stack: list[float] = [float('nan')]
    _cumulated_local: dict[Any, list[float]] = defaultdict(list)
    _cumulated_total: dict[Any, list[float]] = defaultdict(list)
    _timer = default_timer

    # The local mode ignores all times measured by timers within ints own context.
    # It the timer is shadowed, this effect for the local mode is countered by this specific timer.
    def __init__(self, identifier: Any, log_local_time: bool = False, log_total_time: bool = False, shadow_timer: bool = False):
        self._identifier: Any = identifier
        self._log_local_time = log_local_time
        self._log_total_time = log_total_time
        self._shadow_timer = shadow_timer
        self._start: float

    def __enter__(self) -> None:
        Timer._stack.append(0.0)
        self._start = Timer._timer()

    def __exit__(self, exc_type, exc_val, exc_tb):          # type: ignore[no-untyped-def]
        overall_time: float = Timer._timer() - self._start
        local_time: float = overall_time - Timer._stack.pop(-1)
        if not self._shadow_timer:
            Timer._stack[-1] += overall_time
        if self._log_local_time:
            Log.info(f'LocalTime\t{self._identifier}:\t{local_time}')
            Timer._cumulated_local[self._identifier].append(local_time)
        if self._log_total_time:
            Log.info(f'TotalTime\t{self._identifier}:\t{overall_time}')
            Timer._cumulated_total[self._identifier].append(overall_time)

    @staticmethod
    def reset() -> None:
        if len(Timer._stack) != 1:
            raise ProgrammingError()
        Timer._cumulated_local = defaultdict(list)
        Timer._cumulated_total = defaultdict(list)

    @staticmethod
    def overall(minimal_reporting_time: float = 0.0, precision: int = 4) -> None:
        for entry in sorted(Timer._cumulated_local):
            result = Timer._cumulated_local[entry]
            average_result = sum(result) / len(result)
            average_result_str = format(average_result, f'.{precision}g')
            if average_result >= minimal_reporting_time:
                Log.info(f'AverageLocalTime\t{entry}:\t{average_result_str}')
        for entry in sorted(Timer._cumulated_total):
            result = Timer._cumulated_total[entry]
            if not result:
                continue
            average_result = sum(result) / len(result)
            average_result_str = format(average_result, f'.{precision}g')
            if average_result >= minimal_reporting_time:
                Log.info(f'AverageTotalTime\t{entry}:\t{average_result_str}')

    @staticmethod
    def show(identifier: str, local: bool, precision: int = 4) -> float:
        if local:
            return float(format(sum(Timer._cumulated_local[identifier]), f'.{precision}g'))
        return float(format(sum(Timer._cumulated_total[identifier]), f'.{precision}g'))
