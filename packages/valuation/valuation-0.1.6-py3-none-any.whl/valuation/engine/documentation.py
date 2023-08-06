from __future__ import annotations

import json
from copy import copy
from dataclasses import dataclass
from typing import Any, Callable, Generator, Iterable, Optional

from valuation.consts.global_parameters import DummyDate
from valuation.exceptions import ProgrammingError
from valuation.engine.check import Check, CheckMatrix
from valuation.universal_transfer import NoValue, Signature, TypeKey
from valuation.utils.input_output import to_json
from valuation.utils.other import is_ql_null_value

QL_VALUE = '???'
QL_JOIN = '\t&&\t'

ADDITIONAL_CHECK = '__ADDITIONAL_CHECK__'


class DocumentationItem:
    def __init__(self, default_value: Any = '', fall_back_allowed: bool = False, checks: Iterable[Check] = tuple(), value: NoValue = NoValue(), orig_value: NoValue = NoValue(), orig_name: Optional[TypeKey] = None, deleted: bool = False) -> None:
        if is_ql_null_value(default_value):
            default_value = None
        self._default_value: Any = default_value
        self._fall_back_allowed: bool = fall_back_allowed
        self._checks: list[Check] = list(checks)
        self._value: NoValue = value
        self._orig_value: NoValue = orig_value
        self._orig_name: Optional[TypeKey] = orig_name
        self._deleted = deleted

    @property
    def default_value(self) -> Any:
        return self._default_value

    @property
    def fall_back_allowed(self) -> bool:
        return self._fall_back_allowed

    @property
    def original_name(self) -> Optional[TypeKey]:
        return self._orig_name

    @property
    def checks(self) -> list[Check]:
        return self._checks

    def to_string(self, replacement: str) -> str:
        if self._deleted:
            return '<<DELETED>>'

        result: list[str] = []
        if self._orig_name is not None:
            result.append(f'<{self._orig_name}>')

        default_value: str = str(self._default_value)
        if default_value == str(DummyDate):
            default_value = 'date()'
        if self._fall_back_allowed:
            default_value += '*'
        result.append(f'{{{default_value}}}')

        value = str(self._value)

        if str(self._value) != str(self._orig_value):
            substitution_value = str(self._value).replace(replacement, QL_VALUE)
            if self._orig_name:
                substitution_value = substitution_value.replace(f'{{{self._orig_name}}}', QL_VALUE)
            result.append(f'[[{QL_VALUE} --> {substitution_value}]]')
            replacement = f'{self._value}'

        if self._checks:
            checks: str = QL_JOIN.join([check.document().format(value) for check in self._checks])
            result.append(checks.replace(replacement, QL_VALUE))

        return '\t'.join(result)

    def delete(self) -> None:
        self._deleted = True

    def set_original_name(self, orig_name: TypeKey) -> DocumentationItem:
        if self._orig_name is not None:
            raise ProgrammingError('Multiple rename not allowed!')
        self._orig_name = orig_name
        return self

    def set_checks(self, checks: list[Check]) -> DocumentationItem:
        self._checks = checks
        return self

    def apply(self, other: Callable[[Any], Any]) -> DocumentationItem:
        self._value = NoValue.apply(other, self._orig_value)
        return self

    def map(self, map_index: int) -> DocumentationItem:
        self._value = self._value.map(f'Map_{map_index}')
        return self

    def __getitem__(self, item: Any) -> DocumentationItem:
        self._value = self._value[item]
        return self

    def __add__(self, other: Any) -> DocumentationItem:
        self._value = self._value + other
        return self

    def __radd__(self, other: Any) -> DocumentationItem:
        self._value = other + self._value
        return self

    def __sub__(self, other: Any) -> DocumentationItem:
        self._value = self._value - other
        return self

    def __rsub__(self, other: Any) -> DocumentationItem:
        self._value = other - self._value
        return self

    def __neg__(self) -> DocumentationItem:
        self._value = - self._value
        return self

    def __mul__(self, other: Any) -> DocumentationItem:
        self._value = self._value * other
        return self

    def __rmul__(self, other: Any) -> DocumentationItem:
        self._value = other * self._value
        return self

    def __truediv__(self, other: Any) -> DocumentationItem:
        self._value = self._value / other
        return self

    def __rtruediv__(self, other: Any) -> DocumentationItem:
        self._value = other / self._value
        return self

    def __eq__(self, other: Any) -> DocumentationItem:          # type: ignore[override]
        self._value = self._value == other
        return self

    def __lt__(self, other: Any) -> DocumentationItem:
        self._value = self._value < other
        return self

    def __gt__(self, other: Any) -> DocumentationItem:
        self._value = self._value > other
        return self

    def __le__(self, other: Any) -> DocumentationItem:
        self._value = self._value <= other
        return self

    def __ge__(self, other: Any) -> DocumentationItem:
        self._value = self._value >= other
        return self

    def __ne__(self, other: Any) -> DocumentationItem:          # type: ignore[override]
        self._value = self._value != other
        return self

    def __copy__(self) -> DocumentationItem:
        return DocumentationItem(copy(self._default_value), self._fall_back_allowed, self._checks, copy(self._value), copy(self._orig_value), copy(self._orig_name))


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=False, frozen=True)
class MatrixDocumentationItem:
    row_type: str
    col_type: str
    content_type: str
    row_checks: list[Check]
    col_checks: list[Check]
    content_checks: list[Check]
    matrix_checks: list[CheckMatrix]

    def __str__(self) -> str:
        row_checks: str = QL_JOIN.join([check.document().format(QL_VALUE) for check in self.row_checks])
        col_checks: str = QL_JOIN.join([check.document().format(QL_VALUE) for check in self.col_checks])
        content_checks: str = QL_JOIN.join([check.document().format(QL_VALUE) for check in self.content_checks])
        result = [f'{TypeKey(self.row_type, "row")}\t{row_checks}', f'{TypeKey(self.col_type, "col")}\t{col_checks}', f'{TypeKey(self.content_type, "content")}\t{content_checks}']

        if self.matrix_checks:
            matrix_checks: str = QL_JOIN.join([check.document().format(QL_VALUE) for check in self.matrix_checks])
            result.append(f'Matrix\t{matrix_checks}')
        return '\n'.join(result)


class MultiLineDocumentationItem:
    def __init__(self) -> None:
        self._data: dict[Signature, Documentation] = {}

    def add(self, signature: Signature, documentation: Documentation) -> None:
        self._data[signature] = documentation

    def __str__(self) -> str:
        result: list[str] = []
        for signature in sorted(self._data):
            result.extend((str(signature).replace('[]', ''), shift(str(self._data[signature]))))

        return '\n'.join(result)

    def items(self) -> Generator[tuple[Signature, Documentation], None, None]:
        yield from self._data.items()


def shift(string: str, by: str = '\t') -> str:          # pylint: disable=invalid-name
    return by + string.replace('\n', '\n' + by)


class Documentation:
    maps: list[str] = []

    def __init__(self) -> None:
        self._data_standard: dict[TypeKey, DocumentationItem] = {}
        self._data_matrix: dict[TypeKey, MatrixDocumentationItem] = {}
        self._data_multi_line: dict[TypeKey, MultiLineDocumentationItem] = {}

    def __contains__(self, item: Any) -> bool:
        return item in self._data_standard or item in self._data_matrix or item in self._data_multi_line

    @property
    def data_multi_line(self) -> dict[TypeKey, MultiLineDocumentationItem]:
        return self._data_multi_line

    def __iter__(self) -> Generator[TypeKey, Any, Any]:
        yield from self._data_standard

    def items(self) -> Generator[tuple[TypeKey, DocumentationItem], None, None]:
        yield from self._data_standard.items()

    def standard(self, type_key: TypeKey, default_value: Any, fall_back_allowed: bool, checks: list[Check]) -> None:
        if type_key in self:
            if type_key not in self._data_multi_line:
                raise ProgrammingError()
            return

        value = NoValue(f'{{{type_key}}}')

        self._data_standard[type_key] = DocumentationItem(default_value, fall_back_allowed, checks, value=value, orig_value=value)

    def standard_addcheck(self, value: NoValue, check: Check) -> None:
        count = 0
        while TypeKey(ADDITIONAL_CHECK, str(count)) in self._data_standard:
            count += 1
        self._data_standard[TypeKey(ADDITIONAL_CHECK, str(count))] = DocumentationItem(NoValue(), False, [check], value, value)

    def matrix(self, type_key: TypeKey, row_type: str, col_type: str, content_type: str, row_checks: list[Check], col_checks: list[Check], content_checks: list[Check], matrix_checks: list[CheckMatrix]) -> None:
        if type_key not in self._data_standard:
            raise ProgrammingError()
        self._data_standard.pop(type_key)
        self._data_matrix[type_key] = MatrixDocumentationItem(row_type, col_type, content_type, row_checks, col_checks, content_checks, matrix_checks)

    def multi_line(self, type_key: TypeKey, signature: Signature, documentation: Documentation) -> None:
        if type_key in self and type_key not in self._data_multi_line:
            raise ProgrammingError()
        if type_key not in self._data_multi_line:
            self._data_multi_line[type_key] = MultiLineDocumentationItem()
        self._data_multi_line[type_key].add(signature, documentation)

    def __delitem__(self, type_key: TypeKey) -> None:
        if type_key not in self:
            self._data_standard[type_key] = DocumentationItem()
        self._data_standard[type_key].delete()

    def __getitem__(self, type_key: TypeKey) -> DocumentationItem:
        if type_key not in self._data_standard:
            self._data_standard[type_key] = DocumentationItem('', False, [], NoValue(type_key), NoValue(type_key))
        return copy(self._data_standard[type_key])

    def __setitem__(self, type_key: TypeKey, value: DocumentationItem) -> None:
        if type_key not in self._data_standard:
            raise ProgrammingError(type_key)
        self._data_standard[type_key] = value.set_checks(self._data_standard[type_key].checks)

    def __str__(self) -> str:
        result: list[str] = []
        additional_checks = []
        for type_key in sorted(self._data_standard):
            information = self._data_standard[type_key].to_string(f'{{{type_key}}}')
            if type_key.type == ADDITIONAL_CHECK:
                additional_checks.append(information[2:])
            else:
                result.append(f'{type_key}\t{information}')

        result.extend(f'{type_key}\n{shift(str(self._data_matrix[type_key]))}' for type_key in sorted(self._data_matrix))

        result.extend(f'{type_key}\n{shift(str(self._data_multi_line[type_key]))}' for type_key in sorted(self._data_multi_line))

        if additional_checks:
            result.append('Additional Checks:')
            result.extend(sorted(additional_checks))

        return '\n'.join(result)

    def rename(self, old_key: TypeKey, new_key: TypeKey) -> None:
        self._data_standard[old_key] = self._data_standard[new_key].set_original_name(new_key)
        del self._data_standard[new_key]

    def apply_and_rename(self, old_key: TypeKey, new_key: TypeKey, function: Callable[[Any], Any]) -> None:
        self._data_standard[old_key] = self._data_standard[new_key].set_original_name(new_key).apply(function)
        del self._data_standard[new_key]

    def apply(self, type_key: TypeKey, function: Callable[[Any], Any]) -> None:
        self._data_standard[type_key] = self._data_standard[type_key].apply(function)

    def map(self, type_key: TypeKey, mapping: dict[Any, Any]) -> None:
        map_as_str = json.dumps(to_json(mapping), sort_keys=True)
        if map_as_str not in self.maps:
            self.maps.append(map_as_str)
        map_index = self.maps.index(map_as_str)
        self._data_standard[type_key] = self._data_standard[type_key].map(map_index)

    def map_and_rename(self, old_key: TypeKey, new_key: TypeKey, mapping: dict[Any, Any]) -> None:
        map_as_str = json.dumps(to_json(mapping), sort_keys=True)
        if map_as_str not in self.maps:
            self.maps.append(map_as_str)
        map_index = self.maps.index(map_as_str)
        self._data_standard[old_key] = self._data_standard[new_key].set_original_name(new_key).map(map_index)
        del self._data_standard[new_key]

    @staticmethod
    def print_maps() -> str:
        result = [f'Map_{map_index}: {mapping}' for map_index, mapping in enumerate(Documentation.maps)]

        return '\n\n'.join(result)
