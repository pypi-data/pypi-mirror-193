from __future__ import annotations

from collections import OrderedDict
from typing import Any, Generator, Optional

from daa_utils import Log

from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.universal_transfer import Reference
from valuation.universal_transfer.exceptions import InvalidAccessError
from valuation.utils.input_output import JSONType, to_json

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Storage


class StorageDataBase:
    @property
    def initiation_errors(self) -> list[tuple[Reference, str]]:
        return self._initiation_errors

    @property
    def valuations(self) -> list[Reference]:
        return [key for key in self._data if key.type == 'Valuation']

    @property
    def instruments(self) -> list[Reference]:
        return [key for key in self._data if key.type == 'Instrument']

    def __init__(self) -> None:
        self._data: dict[Reference, Storage] = OrderedDict()
        self._initiation_errors: list[tuple[Reference, str]] = []

    def add(self, storage: Storage, overwrite: bool = False) -> None:
        reference: Reference = storage.reference
        assert storage.is_immutable
        if not overwrite and reference in self._data:
            Log.critical(f'No two objects with the same reference allowed: {reference}')
            self._initiation_errors.append((reference, f'No two objects with the same reference allowed: {reference}'))
            return
        self._data[reference] = storage

    def __contains__(self, reference: Reference) -> bool:
        return reference in self._data

    def __delitem__(self, reference: Reference) -> Storage:
        return self._data.pop(reference)

    def __getitem__(self, reference: Reference) -> Storage:
        try:
            return self._data[reference]
        except KeyError as exception:
            raise InvalidAccessError(reference, [str(key) for key in self._data]) from exception
        except Exception as exception:
            raise exception

    def __iter__(self) -> Generator[Reference, None, None]:
        yield from self._data.__iter__()

    def items(self) -> Generator[tuple[Reference, Storage], None, None]:
        yield from self._data.items()

    def get(self, reference: Reference, storage: Optional[Storage]) -> Optional[Storage]:
        return self._data.get(reference, storage)

    def __str__(self) -> str:
        result: list[str] = [
            f'# {reference}\n{storage}\n' for reference, storage in self.items()
        ]

        return '\n'.join(result)

    def __eq__(self, other: Any) -> bool:
        assert isinstance(other, StorageDataBase), f'Comparing different objects {type(self)} and {type(other)}!'
        if set(self) != set(other):
            return False
        return all(value == other[reference] for reference, value in self.items())


@to_json.register
def _(arg: StorageDataBase, precision: Optional[int] = None) -> JSONType:
    result: dict[str, dict[str, JSONType]] = to_json(arg._data, precision)     # type: ignore[assignment]       # pylint: disable=protected-access   # Friend of StorageDataBase
    for storage in result.values():                                            # pylint: disable=no-member
        storage.pop(str(fields.Type))
        storage.pop(str(fields.Id))
    return result
