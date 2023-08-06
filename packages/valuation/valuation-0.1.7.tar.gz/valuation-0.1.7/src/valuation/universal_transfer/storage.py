from __future__ import annotations

import datetime
import re
from dataclasses import dataclass, field
from typing import Any, Callable, Generator, Optional, Tuple, Union

from valuation.consts import types, global_parameters
from valuation.consts import fields
from valuation.exceptions import ProgrammingError
from valuation.universal_transfer.exceptions import InvalidAccessError, TypeDiscrepancyError, UnknownFinancialConstant, \
    UniversalTransferException
from valuation.universal_transfer.finance_types import BusinessConvention, BusinessConventions, Calendar, Calendars, DayCount, \
    DayCounts, PeriodPart, PeriodParts
from valuation.universal_transfer.reference import Reference
from valuation.universal_transfer.signature import Signature
from valuation.universal_transfer.type_key import TypeKey
from valuation.utils.input_output import JSONType, list2str, shorten_list, to_json, to_olympia_json

RowColumn = tuple[int, int]

SIMPLE_TYPES = (
    types.Str, types.Bool, types.Int, types.Float, types.Date, types.Period, types.DayCount, types.Business,
    types.Calendar, types.Reference)

STORAGE_ID_SEPARATOR = "#!#"


def check_type(type_key: TypeKey, value: Any) -> None:
    if types.is_list(type_key.type):
        check_list_type(type_key, value)
    else:
        check_single_type(type_key, value)


def check_single_type(type_key: TypeKey, value: Any, variable_type: str = '') -> None:
    single_types: dict[str, type[Any]] = {
        types.Str: str,
        types.Int: int,
        types.Float: float,
        types.Bool: bool,
        types.Date: datetime.date,
        types.Reference: Reference,
        types.SubStorage: Storage,
        types.Storage: Storage,
        types.Period: Period,
        types.Matrix: Matrix
    }
    finance_types: dict[str, list[str]] = {
        types.DayCount: DayCounts,
        types.Business: BusinessConventions,
        types.Calendar: Calendars,
        types.PeriodPart: PeriodParts
    }

    if not variable_type:
        variable_type = type_key.type
    if variable_type in single_types:
        if not isinstance(value, single_types[variable_type]):
            raise TypeDiscrepancyError(type_key, value, single_types[variable_type])
    elif variable_type in finance_types:
        if not isinstance(value, str):
            raise TypeDiscrepancyError(type_key, value, str)
        if value not in finance_types[variable_type]:
            raise UnknownFinancialConstant(type_key, value)
    else:
        raise ProgrammingError(f'Unknown type {type_key.type} in {type_key}: {value}')


def check_list_type(type_key: TypeKey, value: Any) -> None:
    if not isinstance(value, tuple):
        raise TypeDiscrepancyError(type_key, value, tuple)
    if isinstance(value, Matrix):
        raise ProgrammingError(f'Matrices must not be list entries! ({type_key})')
    for entry in value:
        check_single_type(type_key, entry, types.to_single_type(type_key.type))


PERIOD_PATTERN = re.compile('^([0-9]*Y)?([0-9]*M)?([0-9]*W)?([0-9]*D)?$')


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=False, frozen=True)
class Period:
    # todo: REMOVE THIS CLASS. It creates an overhead. Instead simply use strings until we enter ql.
    #    added: -regex to evaluate combined periods (which is supported by ql),
    #           -removed checks that kill processes (days <= 6) (dangerous!)
    #           -if called from_str it will also return the original str, which is passed to ql, this cannot
    #           manipulate the period on the way.
    number: int
    unit: PeriodPart
    short_term: Optional[str] = None
    _original_str: Optional[str] = None

    @property
    def _in_days(self) -> int:
        if self.unit == 'Y':
            return self.number * 360
        if self.unit == 'M':
            return self.number * 30
        if self.unit == 'W':
            if self.number > 3:
                raise ProgrammingError()
            return self.number * 7
        if self.unit == 'D':
            if self.number > 6:
                raise ProgrammingError()
            return self.number
        raise ProgrammingError()

    @property
    def in_months(self) -> int:
        if self.unit == 'Y':
            return self.number * 12
        if self.unit == 'M':
            return self.number
        raise ValueError('Cannot convert periods other than M and Y into months')

    def __post_init__(self) -> None:
        check_single_type(TypeKey(types.Int, 'PeriodInitialization'), self.number)
        check_single_type(TypeKey(types.PeriodPart, 'PeriodInitialization'), self.unit)

    def __str__(self) -> str:
        return self.short_term or f'{self.number}{self.unit}'

    @classmethod
    def from_str(cls, value: str) -> Period:
        short_term_map = ['SPOT', 'ON', 'TN', 'SN', 'SW']
        if value in short_term_map:
            return cls._from_single_str(value)
        components: tuple[str, str, str, str] = re.findall(PERIOD_PATTERN, value)[0]
        period: Optional[Period] = None  # setting None because D, W can't be added......
        for component in components:
            if not component:
                continue
            component_period = cls._from_single_str(component)
            if period is None:
                period = component_period
            else:
                period += component_period
        if period is None:
            raise UniversalTransferException(f'Not a valid Period: {value}')
        return Period(period.number, period.unit, period.short_term)

    @staticmethod
    def _from_single_str(value: str) -> Period:
        if value.upper() == 'SPOT':
            return Period(0, 'D', 'SPOT')
        if value.upper() == 'ON':
            return Period(1, 'D', 'ON')
        if value.upper() == 'TN':
            return Period(2, 'D', 'TN')
        if value.upper() == 'SN':
            return Period(1, 'D', 'SN')
        if value.upper() == 'SW':
            return Period(1, 'W', 'SW')
        number = int(value[:-1])
        period = value[-1]
        return Period(number, period)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Period):
            raise ProgrammingError()
        if self._equals_sn(self, other):
            return True
        return self._in_days == other._in_days and self.short_term == other.short_term

    @staticmethod
    def _equals_sn(period_1: Period, period_2: Period) -> bool:
        # 1D and SN is the same
        for pd_1, pd_2 in ((period_1, period_2), (period_2, period_1)):
            if pd_1.short_term == 'SN' and (not pd_2.short_term and pd_2._in_days == 1):  # pylint: disable=protected-access
                return True
        return False

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Period):
            raise ProgrammingError()
        if self.short_term and other.short_term:
            return global_parameters.ShortTermTenorOrder[self.short_term] < global_parameters.ShortTermTenorOrder[other.short_term]
        return self._in_days < other._in_days

    def __add__(self, other: Period) -> Period:
        return Period(self.in_months + other.in_months, 'M')

    def __hash__(self) -> int:
        return self._in_days


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=True, frozen=True)
class Matrix:
    column_headers: StorageTypes.SimpleList
    row_headers: StorageTypes.SimpleList
    content: StorageTypes.SimpleMatrix
    column_header_type: str
    row_header_type: str
    content_type: str
    searchable_column_headers: list[int] = field(init=False)
    searchable_row_headers: list[int] = field(init=False)

    def __post_init__(self) -> None:
        if types.to_single_type(self.column_header_type) not in SIMPLE_TYPES:
            raise ProgrammingError('Matrix column headers need to be of a simple type!')
        if types.to_single_type(self.row_header_type) not in SIMPLE_TYPES:
            raise ProgrammingError('Matrix row headers need to be of a simple type!')
        check_list_type(TypeKey(self.column_header_type, 'MatrixInitialization'), self.column_headers)
        check_list_type(TypeKey(self.row_header_type, 'MatrixInitialization'), self.row_headers)
        if not types.is_matrix(self.content_type) or types.to_single_type(self.content_type) not in SIMPLE_TYPES:
            raise ProgrammingError('Matrix content needs to be of #<simpletype>#')
        if not isinstance(self.content, tuple):
            raise ProgrammingError('Matrix content needs to be a tuple of tuples')
        for count, row in enumerate(self.content):
            check_list_type(TypeKey(types.to_list_type(self.content_type[1]), f'MatrixRow{count}'), row)
            if len(row) != len(self.column_headers):
                raise ProgrammingError('Row and number of columns do not coincide!')
        if len(self.content) != len(self.row_headers):
            raise ProgrammingError('Column and number of rows do not coincide!')

        super().__setattr__('searchable_column_headers', [hash(entry) for entry in self.column_headers])
        super().__setattr__('searchable_row_headers', [hash(entry) for entry in self.row_headers])

        if len(set(self.searchable_column_headers)) != len(self.column_headers):
            raise ProgrammingError('Column headers need to be unique!')
        if len(set(self.searchable_row_headers)) != len(self.row_headers):
            raise ProgrammingError('Row headers need to be unique!')

    def __getitem__(self, row_column: RowColumn) -> StorageTypes.Simple:
        return self.content[row_column[0]][row_column[1]]

    def __call__(self, row_header: StorageTypes.Simple, column_header: StorageTypes.Simple) -> StorageTypes.Simple:
        check_single_type(TypeKey(types.to_single_type(self.row_header_type), 'MatrixCall'), row_header)
        check_single_type(TypeKey(types.to_single_type(self.column_header_type), 'MatrixCall'), column_header)
        row_hash: int = hash(row_header)
        column_hash: int = hash(column_header)
        if row_hash not in self.searchable_row_headers:
            raise InvalidAccessError(row_header, list2str(self.row_headers))
        if column_hash not in self.searchable_column_headers:
            raise InvalidAccessError(column_header, list2str(self.column_headers))
        row_number: int = self.searchable_row_headers.index(row_hash)
        column_number: int = self.searchable_column_headers.index(column_hash)
        return self[(row_number, column_number)]

    def __str__(self) -> str:
        lines: list[str] = ['\t' + list2str(self.column_headers, separator='\t', brackets='{}')]
        lines.extend(str(row_header) + '\t' + list2str(row, separator='\t', brackets='{}') for row_header, row in zip(self.row_headers, self.content))

        return '\n'.join(lines)

    @property
    def shortened_print(self) -> str:
        stop_at = 5
        lines: list[str] = ['\t' + list2str(shorten_list(self.column_headers, stop_at=stop_at), separator='\t', brackets='{}')]
        for count, (row_header, row) in enumerate(zip(self.row_headers, self.content)):
            if count < stop_at:
                lines.append(str(row_header) + '\t' + list2str(shorten_list(row, stop_at=stop_at, hint=False), separator='\t', brackets='{}'))
            else:
                lines.extend(['.', '.', '.'])
                break
        return '\n'.join(lines)


@to_json.register
def _(arg: Matrix, precision: Optional[int] = None) -> JSONType:
    return to_json({
        TypeKey(arg.row_header_type, fields.MatrixRowHeaders): arg.row_headers,
        TypeKey(arg.column_header_type, fields.MatrixColumnHeaders): arg.column_headers,
        TypeKey(arg.content_type, fields.MatrixContent): arg.content
    }, precision)


class Storage:

    @property
    def is_immutable(self) -> bool:
        return self._immutable

    @property
    def reference(self) -> Reference:
        return Reference(self[fields.Type], self[fields.Id])  # type: ignore[arg-type]

    @property
    def signature(self) -> Signature:
        type_str: str = self[fields.Type]  # type: ignore[assignment]
        if fields.SubType(type_str) in self:
            return Signature(type_str, self[fields.SubType(type_str)])  # type: ignore[arg-type]
        return Signature(type_str)

    def __init__(self, mutable_substorages: bool = False, shorten_print: bool = False) -> None:
        self._data: dict[TypeKey, StorageTypes.GeneralEntry] = {}
        self._immutable = False
        self._mutable_substorages = mutable_substorages
        self._shorten_print = shorten_print

    def assign_reference(self, reference: Reference) -> None:
        self[fields.Id] = reference.id
        self[fields.Type] = reference.type

    def assign_post_mutable_id(self, post_mutable_id: str) -> None:
        assert self._immutable
        assert fields.Id not in self._data
        self._data[fields.Id] = post_mutable_id

    def make_immutable(self) -> Storage:
        if self._mutable_substorages:
            for type_key, value in self._data.items():
                if type_key.type in [types.Storage, types.SubStorage]:
                    value.make_immutable()  # type: ignore[union-attr]
                elif type_key.type in [types.Storages, types.SubStorages]:
                    for sub_value in value:  # type: ignore[union-attr]
                        sub_value.make_immutable()  # type: ignore[union-attr]
        self._immutable = True
        return self

    def __contains__(self, type_key: TypeKey) -> bool:
        if type_key.fall_back_to_single:
            return type_key.as_list() in self._data or type_key.as_single() in self._data
        if type_key.fall_back_to_storage:
            return type_key.as_reference() in self._data or type_key.as_storage() in self._data
        return type_key in self._data

    def __delitem__(self, type_key: TypeKey) -> None:
        assert not self._immutable
        del self._data[type_key]

    def pop(self, type_key: TypeKey) -> StorageTypes.GeneralEntry:
        assert not self._immutable
        return self._data.pop(type_key)

    def __getitem__(self, type_key: TypeKey) -> StorageTypes.GeneralEntry:
        try:
            if type_key.fall_back_to_storage:
                try:
                    return self._data[type_key.as_reference()]
                except KeyError:
                    return self._data[type_key.as_storage()]
            if type_key.fall_back_to_single:
                try:
                    return self._data[type_key.as_list()]
                except KeyError:
                    return self._data[type_key.as_single()],  # type: ignore[return-value]  # pylint: disable=trailing-comma-tuple
            return self._data[type_key]
        except KeyError as exception:
            raise InvalidAccessError(type_key, [str(key) for key in self._data]) from exception
        except Exception as exception:
            raise exception

    def __setitem__(self, type_key: TypeKey, value: StorageTypes.GeneralEntry) -> None:
        assert type_key.is_simple, 'Just simple type_keys can be used for setting!'
        assert not self._immutable, 'Do not assign value to immutable object!'
        if type_key.type == types.Storage:
            assert fields.Id not in value, f'Just storages without {fields.Id} can be attached'  # type: ignore[operator]
        elif type_key.type == types.Storages:
            for storage in value:  # type: ignore[union-attr]
                assert fields.Id not in storage, f'Just storages without {fields.Id} can be attached'  # type: ignore[operator]
        elif type_key == fields.Id:
            assert STORAGE_ID_SEPARATOR not in value, f'{STORAGE_ID_SEPARATOR} is reserved and cannot be part of an {fields.Id}'  # type: ignore[operator]

        if not self._mutable_substorages:
            if type_key.type == types.SubStorage:
                assert value.is_immutable, 'Just immutable substorages can be attached'  # type: ignore[union-attr]
            elif type_key.type == types.SubStorages:
                for sub_storage in value:  # type: ignore[union-attr]
                    assert sub_storage.is_immutable, 'Just immutable substorages can be attached'  # type: ignore[union-attr]
            elif type_key.type == types.Storage:
                assert value.is_immutable, 'Just immutable storages can be attached'  # type: ignore[union-attr]
            elif type_key.type == types.Storages:
                for storage in value:  # type: ignore[union-attr]
                    assert storage.is_immutable, 'Just immutable storages can be attached'  # type: ignore[union-attr]

        check_type(type_key, value)
        self._data[type_key] = value

    def __iter__(self) -> Generator[TypeKey, None, None]:
        yield from self._data.__iter__()

    def items(self) -> Generator[tuple[TypeKey, StorageTypes.GeneralEntry], None, None]:
        yield from self._data.items()

    def get(self, type_key: TypeKey, value: StorageTypes.GeneralEntry) -> StorageTypes.GeneralEntry:
        check_type(type_key, value)
        return self._data.get(type_key, value)

    def __str__(self) -> str:
        hidden_keys: tuple[TypeKey, ...] = (fields.Token,)
        lines: list[str] = []
        for type_key in sorted(self, reverse=True):
            value = self[type_key]
            if type_key in hidden_keys:
                lines.append(f'{type_key}\t-- VALUE REMOVED BY QL ENGINE JSON CONVERTER --')
            elif isinstance(value, tuple):
                if value and isinstance(value[0], Storage):
                    lines.extend('{}\t\t{}'.format(type_key, '\t!\t'.join(str(simple_storage).split('\n'))) for simple_storage in value)
                else:
                    values2print: Union[tuple[Any, ...], list[Any]] = shorten_list(value) if self._shorten_print else value
                    lines.append(f'{type_key}\t' + list2str(values2print, separator='\t', brackets='{}'))
            elif isinstance(value, Matrix):
                matrix_str = value.shortened_print if self._shorten_print else str(value)
                for sub_line in matrix_str.split('\n'):
                    if self._shorten_print and sub_line == '.':
                        lines.append(f'\t{sub_line}')
                    else:
                        lines.append(f'{type_key}\t{sub_line}')
            else:
                lines.append(f'{type_key}\t{value}')
        return '\n'.join(lines)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Storage):
            return False
        if set(self) != set(other):
            return False
        for type_key, value in self.items():
            if isinstance(value, list):
                other_value = other[type_key]
                if len(value) != len(other_value):
                    return False
                for single_value, other_single_value in zip(value, other_value):
                    if single_value != other_single_value:
                        return False
            elif value != other[type_key]:
                return False
        return True

    def __bool__(self) -> bool:
        return bool(self._data)

    def rename(self, old_key: TypeKey, new_key: TypeKey) -> None:
        self[new_key] = self.pop(old_key)

    def apply_and_rename(self, old_key: TypeKey, new_key: TypeKey, function: Callable[[Any], Any]) -> None:
        self[new_key] = function(self.pop(old_key))

    def apply(self, type_key: TypeKey, function: Callable[[Any], Any]) -> None:
        self[type_key] = function(self.pop(type_key))

    def map(self, type_key: TypeKey, mapping: dict[Any, Any]) -> None:
        self[type_key] = mapping[self.pop(type_key)]

    def map_and_rename(self, old_key: TypeKey, new_key: TypeKey, mapping: dict[Any, Any]) -> None:
        self[new_key] = mapping[self.pop(old_key)]


class StorageTypes:
    Simple = Union[bool, int, float, str, datetime.date, Reference, Period, DayCount, Calendar, BusinessConvention]
    SimpleList = Tuple[Simple, ...]  # Todo (2021/11): Bug in Mypy, change to tuple after update
    SimpleMatrix = Tuple[SimpleList, ...]  # Todo (2021/11): Bug in Mypy, change to tuple after update
    FullList = Tuple[Union[Simple, Storage], ...]  # Todo (2021/11): Bug in Mypy, change to tuple after update
    GeneralEntry = Union[Simple, FullList, Matrix, Storage]


@to_json.register  # type: ignore[no-redef]
def _(arg: Storage, precision: Optional[int] = None) -> JSONType:
    return to_json(arg._data, precision)  # pylint: disable=protected-access   # friend of Storage


@to_olympia_json.register  # type: ignore[no-redef]
def _(arg: Storage, precision: Optional[int] = None) -> JSONType:
    return to_olympia_json(arg._data, precision)  # pylint: disable=protected-access   # friend of Storage


@to_olympia_json.register(dict)  # type: ignore[no-redef]
def _(arg: dict[Any, Any], precision: Optional[int] = None) -> JSONType:
    hidden_keys: tuple[str, ...] = ('token',)

    result: dict[Any, Any] = {}
    for key, value in arg.items():
        if isinstance(key, TypeKey):
            dict_key: Any = key.key
        else:
            dict_key = key
        if key in hidden_keys:
            result[dict_key] = '-- VALUE REMOVED BY QL ENGINE JSON CONVERTER --'
        else:
            result[dict_key] = to_olympia_json(value, precision)
    return result


DefaultParameters = Union[None, Storage, list[Storage]]
