from __future__ import annotations

import itertools
import re
from dataclasses import dataclass
from typing import Any, Iterable, Optional, Union

import QuantLib as ql
import numpy as np

from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import QLInputError, QLInputWarning
from valuation.universal_transfer import Matrix, NoValue, Signature, TypeKey
from valuation.utils.other import is_nan, listify

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.market_data import QLCurrency
    import numpy.typing as npt


class Check:
    def __call__(self, value: Any) -> None:
        if is_nan(value):
            return
        entries: list[Any] = listify(value)
        successful: bool = all(self._check_single(entry) for entry in entries)
        if not successful:
            raise QLInputError(f'{self.document().format(value)} failed!')

    def _check_single(self, value: Any) -> bool:
        raise NotImplementedError

    def document(self) -> str:
        raise NotImplementedError


class Length(Check):  # pylint: disable=abstract-method
    def __init__(self, comparison_list_or_int: Union[list[Any], int, str]) -> None:
        if isinstance(comparison_list_or_int, list):
            self._length: Union[int, str] = len(comparison_list_or_int)
        elif isinstance(comparison_list_or_int, int):
            self._length = comparison_list_or_int
        else:
            self._length = f'len({comparison_list_or_int})'

    def __call__(self, value: Any) -> None:
        if not value:
            return
        if len(value) != self._length:
            raise QLInputError(f'{self.document().format(value)} failed!')

    def document(self) -> str:
        result: str = 'len({})' + f' == {self._length}'
        return result


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)  # pylint: disable=abstract-method
class IsOrdered(Check):             # pylint: disable=abstract-method
    ascending: bool = True
    strict: bool = True

    def __call__(self, value: Any) -> None:
        if self.strict and len(set(value)) != len(value):
            raise QLInputError(f'{self.document().format(value)} failed!')
        if self.ascending:
            if any(value[count] > value[count + 1] for count in range(len(value) - 1)):
                raise QLInputError(f'{self.document().format(value)} failed!')
        elif any(value[count] < value[count + 1] for count in range(len(value) - 1)):
            raise QLInputError(f'{self.document().format(value)} failed!')

    def document(self) -> str:
        result: str = '{} is ordered '
        result += 'ascending' if self.ascending else 'descending'
        if self.strict:
            result += ' strictly'
        return result


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class Range(Check):
    lower: Optional[Any] = None
    upper: Optional[Any] = None
    strict: bool = True

    def _check_single(self, value: Any) -> bool:  # pylint: disable=too-many-return-statements
        if self.lower is None and self.upper is None:
            raise ProgrammingError
        if self.strict:
            if self.lower is None:
                return value < self.upper                   # type: ignore[no-any-return]
            if self.upper is None:
                return self.lower < value                   # type: ignore[no-any-return]
            return self.lower < value < self.upper          # type: ignore[no-any-return]
        if self.lower is None:
            return value <= self.upper                      # type: ignore[no-any-return]
        if self.upper is None:
            return self.lower <= value                      # type: ignore[no-any-return]
        return self.lower <= value <= self.upper            # type: ignore[no-any-return]

    def document(self) -> str:
        operator = ' < ' if self.strict else ' <= '
        entries: list[str] = []
        if self.lower is not None:
            entries.append(str(self.lower))
        entries.append('{}')
        if self.upper is not None:
            entries.append((str(self.upper)))
        return operator.join(entries)


class RangeWarning(Range):

    def __call__(self, value: Any) -> None:
        try:
            super().__call__(value)
        except QLInputError as error:
            raise QLInputWarning(', '.join(error.args))  # pylint: disable=raise-missing-from

    def document(self) -> str:
        return f'{super().document()} (Warn only)'


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class ContainedIn(Check):
    entries: Iterable[Any]

    def _check_single(self, value: Any) -> bool:
        return value in self.entries

    def document(self) -> str:
        try:
            entries: Iterable[Any] = sorted(self.entries)
        except TypeError:
            # If self.entries contains instances (e.g. of QLObject) those cannot be sorted
            entries = self.entries
        displayed_entries: list[Any] = []
        for entry in entries:
            if isinstance(entry, (int, float)):
                displayed_entries.append(entry)
            else:
                displayed_entries.append(str(entry))
        return '{}' + f' in {displayed_entries}'


class Contains(Check):            # pylint: disable=abstract-method
    def __init__(self, comparison_list_or_single: Union[list[Any], Any]) -> None:
        self._comparison_list: list[Any] = listify(comparison_list_or_single)

    def __call__(self, value: Any) -> None:
        for entry in self._comparison_list:
            if entry not in value:
                raise QLInputError(f'{self.document().format(value)} failed!')

    def document(self) -> str:
        out_list = [str(entry) for entry in self._comparison_list]
        return ',  '.join(out_list) + ' in ' + '{}'


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class Equals(Check):
    entry: Any

    def _check_single(self, value: Any) -> bool:
        return value == self.entry                      # type: ignore[no-any-return]

    def document(self) -> str:
        return '{}' + f' == {self.entry}'


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class Differs(Check):
    entry: Any

    def _check_single(self, value: Any) -> bool:
        return value != self.entry                      # type: ignore[no-any-return]

    def document(self) -> str:
        return '{}' + f' != {self.entry}'


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class Pattern(Check):
    pattern: str

    def _check_single(self, value: Any) -> bool:
        return re.match(self.pattern, value) is not None

    def document(self) -> str:
        return '{}' + ' matches "{}"'.format(self.pattern.replace('{', '{{').replace('}', '}}'))


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class ObjectType(Check):
    eligible_signatures: Union[Signature, list[Signature]]

    def _check_single(self, value: Any) -> bool:
        return any(
            value.signature in eligible_signature
            for eligible_signature in listify(self.eligible_signatures)
        )

    def document(self) -> str:
        signatures = [
            str(eligible_object_type)
            for eligible_object_type in listify(self.eligible_signatures)
        ]

        if len(signatures) == 1:
            return '{}' + f' matches type with {signatures[0]}'
        return '{}' + f' matches type with one of {signatures}'


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=True, frozen=True)
class Currency(Check):
    currency: QLCurrency

    def _check_single(self, value: Any) -> bool:
        return value.currency.reference == self.currency.reference                      # type: ignore[no-any-return]

    def document(self) -> str:
        if isinstance(self.currency, (NoValue, str, TypeKey)):
            result: Any = self.currency
        else:
            result = self.currency.reference
        return '{}' + f' has {result}'


class ImmDate(Check):
    def _check_single(self, value: ql.Date) -> bool:
        return ql.IMM_isIMMdate(value)          # type: ignore[no-any-return]

    def document(self) -> str:
        return '{} is IMM date'


class CheckMatrix:
    def __call__(self, value: Matrix) -> None:
        if not self._check(value):
            raise QLInputError(f'{self.document().format(value)} failed!')

    def _check(self, value: Matrix) -> bool:
        raise NotImplementedError

    def document(self) -> str:
        raise NotImplementedError


class MatrixIsSymmetric(CheckMatrix):

    def _check(self, value: Matrix) -> bool:
        if value.row_headers != value.column_headers:
            return False

        return all(value[(row_count, column_count)] == value[(column_count, row_count)] for row_count, column_count in itertools.product(range(len(value.row_headers)), range(len(value.row_headers))))

    def document(self) -> str:
        return 'is symmetric'


class MatrixDiagIsOne(CheckMatrix):
    def _check(self, value: Matrix) -> bool:
        if len(value.row_headers) != len(value.column_headers):
            return False

        return all(value[(row_count, row_count)] == 1.0 for row_count in range(len(value.row_headers)))

    def document(self) -> str:
        return 'has unit diagonal'


class MatrixHasPositiveEigenValues(CheckMatrix):

    def __init__(self, strict: bool = True):
        self.strict: bool = strict
        self.eigen_values: Optional[npt.NDArray] = None  # type: ignore[type-arg]

    def _check(self, value: Matrix) -> bool:
        if len(value.row_headers) != len(value.column_headers):
            return False
        matrix: Union[npt.NDArray[np.float64]] = np.array(value.content)
        self.eigen_values = np.linalg.eigvals(matrix)
        if self.strict:
            return bool(np.all(self.eigen_values > 0))
        return bool(np.all(self.eigen_values >= 0))

    def document(self) -> str:
        if self.eigen_values is not None:
            eigen_value_str: str = f'{self.eigen_values} '
        else:
            eigen_value_str = ''
        strict_str = 'strictly ' if self.strict else ''
        return f'Eigenvalues {eigen_value_str}are {strict_str}positive.'


class BothNoneOrGiven(Check):
    def __init__(self, other: Any):
        self._other: Any = other

    def _check_single(self, value: Any) -> bool:
        return (self._other is None) == (value is None)

    def document(self) -> str:
        return '{}' + f' is None IFF {self._other} is None'


class OneNotNone(Check):
    def __init__(self, other: Any):
        self._other: Any = other

    def _check_single(self, value: Any) -> bool:
        return (self._other is not None) | (value is not None)

    def document(self) -> str:
        return '{}' + f' or {self._other} has to be not None'
