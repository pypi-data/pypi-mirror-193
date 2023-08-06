from __future__ import annotations

import datetime
import io
import os
from timeit import default_timer
from typing import Any, Callable, Optional

from valuation import olympia
from valuation.consts import fields
from daa_utils import Log, LogFormat
from valuation.engine import QLFactory, QLObjectDB
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.inputs import json_base, standard
from valuation.universal_output import ResultLineError, ResultDB
from valuation.utils.input_output import to_json

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import StorageDataBase
    from daa_utils.excel_io import ExcelIO

DEBUG = os.getenv('QL_DEBUDMODE', 0) == '1'
VALUATION_LOG_FORMAT = LogFormat(use_message=True, use_level=True, use_function=False, use_file=False, separator='   ')


def _add_result_error(ql_db: QLObjectDB, instrument_id: str, location: str, error_msg: str) -> QLObjectDB:
    ql_db.result_db(ResultLineError(instrument_id, None, location, error_msg))
    return ql_db


def _run_valuation(storage_db: StorageDataBase, verbose: bool = True) -> ResultDB:
    with QLFactory():
        ql_db = QLObjectDB(storage_db, time_it=False)

        # Adding errors that occurred while parsing the request
        for instrument_id, error_message in storage_db.initiation_errors:
            Log.error(f'{instrument_id}: {error_message}')
            _add_result_error(ql_db, str(instrument_id), 'BeforeInitializeQuantlib', error_message)

        # Evaluate
        valuations = storage_db.valuations
        valuations_count = len(valuations)
        for i, valuation in enumerate(valuations):
            if verbose:
                print(f'[{i + 1}/{valuations_count}] - {valuation}')
            try:
                _ = ql_db[valuation]
            except ProgrammingError as error:
                Log.error(error)
                raise Exception from error
            except Exception as error:  # pylint: disable=broad-except
                if DEBUG:
                    raise error
                Log.error(str(error))
                storage = storage_db[valuation]
                if fields.Instrument in storage:
                    _id: str = storage[fields.Instrument].id
                else:
                    _id = storage[fields.Id]
                _add_result_error(ql_db, _id, str(storage.reference), str(error))  # type: ignore[union-attr]
        return ql_db.result_db.adjust_nominal()


class ResultConverter:
    @property
    def success(self) -> bool:
        return self._success

    def __init__(self, success: bool, result_db: ResultDB, logs: list[str], no_test: bool = True) -> None:
        self._success: bool = success
        self._result_db: ResultDB = result_db
        self._logs: list[str] = logs
        self._no_test: bool = no_test

    def get_logs(self) -> list[str]:
        return self._logs

    def get_raw(self, precision: Optional[int] = None) -> list[dict[str, Any]]:
        return to_json(self._result_db, precision=precision)  # type: ignore[return-value]

    def get_json(self, precision: Optional[int] = None) -> list[dict[str, Any]]:
        return olympia.result_db2json(self._result_db, precision=precision)

    def get_excel(self, precision: Optional[int] = None) -> io.BytesIO:
        return olympia.result_db2excel(self._result_db, precision=precision)

    def test_get_writer(self, precision: Optional[int] = None) -> ExcelIO:
        if self._no_test:
            raise ProgrammingError('test_get_writer is only for testing')
        return olympia.result_db2writer(self._result_db, precision=precision)


def _valuation_handler(storage_db_converter: Callable[..., StorageDataBase], args: tuple[Any, ...],
                       no_test: bool = True) -> ResultConverter:
    with Log(filename_base=None, info_format=VALUATION_LOG_FORMAT):
        try:
            start = default_timer()
            storage_db: StorageDataBase = storage_db_converter(*args)
            result_db: ResultDB = _run_valuation(storage_db)
            end = default_timer()
            if no_test:
                Log.info(f'Time elapsed: {datetime.timedelta(seconds=int(end - start) + 1)}')
            Log.info('Exit program with status SUCCESS')
        except Exception as exception:  # pylint: disable=broad-except
            Log.error('FATAL EXCEPTION')
            Log.error(f'{exception.__class__.__name__}: {exception}')
            Log.info('Exit program after fatal exception with status FAIL')
            return ResultConverter(False, ResultDB(), Log.info_message_list(), no_test)
        return ResultConverter(True, result_db, Log.info_message_list(), no_test)


def evaluate_raw(data: dict[str, Any], no_test: bool = True) -> ResultConverter:
    return _valuation_handler(json_base.json2storage_db,
                              (data, standard.standard_type_key_determination, standard.standard_value_conversion),
                              no_test)


def evaluate_json(data: dict[str, Any], configuration_path: str, no_test: bool = True) -> ResultConverter:
    return _valuation_handler(olympia.json2storage_db, (data, configuration_path), no_test)


def evaluate_excel(data: io.BytesIO, configuration_path: str, no_test: bool = True) -> ResultConverter:
    return _valuation_handler(olympia.excel2storage_db, (data, configuration_path), no_test)
