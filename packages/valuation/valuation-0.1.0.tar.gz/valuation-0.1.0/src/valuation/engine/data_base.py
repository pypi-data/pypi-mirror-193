from __future__ import annotations

from typing import Optional

import QuantLib as ql

from valuation.consts import fields
from valuation.consts.global_parameters import DefaultParametersReference
from valuation.exceptions import DAAException
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import QLInputError
from valuation.engine.factory import QLFactory
from valuation.engine.utils import date2qldate
from valuation.universal_output import ResultDB
from valuation.universal_transfer import NoValue, Signature
from valuation.utils.other import Timer

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObject
    from valuation.universal_transfer import Reference, Storage, StorageDataBase


class QLObjectDB:

    @property
    def valuation_date(self) -> ql.Date:
        return self._valuation_date

    @property
    def result_db(self) -> ResultDB:
        return self._result_db

    @property
    def storage_db(self) -> Optional[StorageDataBase]:
        return self._storage_db

    def __init__(self, storage_db: Optional[StorageDataBase] = None, time_it: bool = True) -> None:
        self._data: dict[Reference, Optional[QLObject]] = {}
        self._storage_db: Optional[StorageDataBase] = storage_db
        self._valuation_date: ql.Date = NoValue()
        self._aliases: list[Signature] = []
        if storage_db is not None:
            self._default_parameters: Storage = self._storage_db[DefaultParametersReference]        # type: ignore
            self.reset_quantlib()
        else:
            self._default_parameters = None            # type: ignore[assignment]
        self._result_db = ResultDB()
        self._time_it = time_it

    def __contains__(self, reference: Reference) -> bool:
        return self._data.get(reference, False) and self._data[reference].initialization_finished  # type: ignore[return-value, union-attr]

    def reset_quantlib(self) -> None:
        # https://www.quantlib.org/reference/class_quant_lib_1_1_settings.html
        # https://www.quantlib.org/reference/class_quant_lib_1_1_index_manager.html

        self._valuation_date = date2qldate(self._default_parameters[fields.ValuationDate])  # type: ignore[arg-type]

        ql.IndexManager.instance().clearHistories()

        ql.Settings.instance().evaluationDate = self._valuation_date
        ql.Settings.instance().includeReferenceDateEvents = False
        ql.Settings.instance().includeTodaysCashFlows = False
        ql.Settings.instance().enforcesTodaysHistoricFixings = False

    def set_alias(self, reference: Reference, ql_object: QLObject) -> None:
        self._aliases.append(ql_object.signature)
        self._data[reference] = ql_object

    def generate_single_entry(self, storage: Storage, data_only_mode: bool) -> QLObject:
        ql_object_class = QLFactory.assign(storage)

        try:
            if self._time_it:
                with Timer(f'{storage.signature}\t{storage.reference}', log_local_time=True):
                    ql_object: QLObject = ql_object_class(storage, self, self._default_parameters, data_only_mode=data_only_mode)
            else:
                ql_object: QLObject = ql_object_class(storage, self, self._default_parameters, data_only_mode=data_only_mode)  # type: ignore[no-redef]
            if data_only_mode:
                return ql_object
            if ql_object.sub_type != 'Alias':
                self._data[ql_object.reference] = ql_object
            return self._data[ql_object.reference]          # type: ignore[return-value]
        except DAAException as exception:
            try:
                signature = storage.signature
            except Exception:       # pylint: disable=broad-except
                signature = Signature('Signature', 'Not Available')
            try:
                reference = storage.reference
            except Exception:       # pylint: disable=broad-except
                reference = Reference('Reference', 'Not Available')
            exception.set_additional_information(f'{reference}@{signature}')
            raise exception
        except AssertionError as exception:
            new_error = QLInputError(exception)
            try:
                signature = storage.signature
            except Exception:       # pylint: disable=broad-except
                signature = Signature('Signature', 'Not Available')
            try:
                reference = storage.reference
            except Exception:       # pylint: disable=broad-except
                reference = Reference('Reference', 'Not Available')
            new_error.set_additional_information(f'{reference}@{signature}')
            raise new_error from exception
        except Exception as exception:
            raise exception

    def __getitem__(self, reference: Reference) -> QLObject:
        return self.get(reference, False)

    def get(self, reference: Reference, data_only_mode: bool) -> QLObject:
        if reference in self:
            return self._data[reference]            # type: ignore[return-value]
        if not data_only_mode:
            if reference in self._data:
                problematic_references = {
                    key for key, value in self._data.items() if value is None
                }

                for key in problematic_references:
                    del self._data[key]
                raise QLInputError(f'Cycle in references detected: {sorted([str(key) for key in problematic_references])}')
            self._data[reference] = None
        storage: Storage = self._storage_db[reference]              # type: ignore[index]
        return self.generate_single_entry(storage, data_only_mode)

    # Should just be used in rare cases, in order to iron out a detected error!
    def empty_call_stack(self) -> None:
        for key in list(self._data):
            if self._data[key] is None:
                self._data.pop(key)

    def __bool__(self) -> bool:
        return bool(self._data)

    def __str__(self) -> str:
        result: list[str] = [
            f'{reference}: {self._data[reference]}'
            for reference in sorted(self._data)
        ]

        return '\n'.join(result)

    def track(self) -> list[Signature]:
        result: list[Signature] = [
            entry.signature for entry in self._data.values() if entry is not None
        ]

        for entry in self._aliases:
            result.pop(result.index(entry))
            result.append(Signature(entry.type, 'Alias'))
        return result

    if __debug__:
        def given_but_not_requested(self) -> str:
            results: list[str] = []
            for reference, ql_object in self._data.items():
                if ql_object is None:
                    results.extend((str(reference), '\tObject non-existent!!!'))
                elif superfluous_lines := ql_object.given_but_not_requested():
                    results.extend((str(reference), '\t' + '\n\t'.join(superfluous_lines) + '\n'))
            return '\n'.join(results)
