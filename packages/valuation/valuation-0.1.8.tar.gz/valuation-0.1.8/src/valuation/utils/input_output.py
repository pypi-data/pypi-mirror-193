import collections
import datetime
import json
from functools import singledispatch
from typing import Any, Iterable, Optional, TextIO, Union


def list2str(values: Iterable[Any], separator: str = ', ', brackets: str = '({})') -> str:
    return brackets.format(separator.join(str(v) for v in values))


def json_dump(data: Any, file_handle: TextIO, precision: Optional[int] = None) -> None:
    json.dump(to_json(data, precision), file_handle, indent='\t', sort_keys=True)


JSONType = Union[str, bool, int, float, list[Any], dict[str, Any], None]


@singledispatch
def to_json(arg: Any, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return None if arg is None else str(arg)


@singledispatch
def to_olympia_json(arg: Any, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return to_json(arg, precision)


@to_json.register
def _(arg: int, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return arg


@to_json.register  # type: ignore[no-redef]
def _(arg: bool, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return arg


@to_json.register  # type: ignore[no-redef]
def _(arg: float, precision: Optional[int] = None) -> JSONType:
    return arg if precision is None else float(format(arg, f'.{precision}g'))


@to_json.register  # type: ignore[no-redef]
def _(arg: str, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return arg


@to_json.register  # type: ignore[no-redef]
def _(arg: datetime.date, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return str(arg)


@to_json.register(list)  # type: ignore[no-redef]
def _(arg: list[Any], precision: Optional[int] = None) -> JSONType:
    return [to_json(entry, precision) for entry in arg]


@to_json.register(tuple)  # type: ignore[no-redef]
def _(arg: tuple[Any, ...], precision: Optional[int] = None) -> JSONType:
    return [to_json(entry, precision) for entry in arg]


@to_json.register(dict)  # type: ignore[no-redef]
def _(arg: dict[Any, Any], precision: Optional[int] = None) -> JSONType:
    return {str(key): to_json(value, precision) for key, value in arg.items()}


@to_json.register(Exception)  # type: ignore[no-redef]
def _(arg: Exception, precision: Optional[int] = None) -> JSONType:  # pylint: disable=unused-argument
    return f'{arg.__class__.__name__}: {arg}'


@to_json.register(collections.Counter)  # type: ignore[no-redef]
def _(arg: dict[Any, Any], precision: Optional[int] = None) -> JSONType:
    return {str(key): to_json(value, precision) for key, value in arg.items()}


def shorten_list(values: Iterable[Any], stop_at: int = 5, precision: int = 5, hint: bool = True) -> list[JSONType]:
    shortened: list[JSONType] = []
    values_hidden = False
    for count, value in enumerate(values):
        if count < stop_at:
            shortened.append(to_json(value, precision=precision))
        else:
            values_hidden = True
            break
    if hint and values_hidden:
        shortened += ['...']
    return shortened
