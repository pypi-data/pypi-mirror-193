from __future__ import annotations

import io
from typing import Any, Optional

from valuation.global_settings import __type_checking__
from valuation.olympia.input.config import Configuration
from valuation.olympia.input.data_base import RequestDataBase
from valuation.olympia.input.request import ExcelRequest, OlympiaRequest
from valuation.olympia.output.result import convert_result_db, result_to_writer
from valuation.utils.input_output import to_json

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from datetime import date
    from daa_utils.excel_io import ExcelIO
    from valuation.olympia.input.request import Request
    from valuation.universal_output import ResultDB


def _make_request_database(request: Request, configuration_path: str) -> RequestDataBase:
    config = Configuration(configuration_path)
    request_db = RequestDataBase(config)
    request_db.add_request(request)
    return request_db


def json2storage_db(data: dict[str, Any], configuration_path: str) -> RequestDataBase:
    request = OlympiaRequest(data)
    return _make_request_database(request, configuration_path)


def excel2storage_db(data: io.BytesIO, configuration_path: str) -> RequestDataBase:
    request = ExcelRequest(data)
    return _make_request_database(request, configuration_path)


def result_db2json(result_db: ResultDB, precision: Optional[int] = None) -> list[dict[str, Any]]:
    return to_json(convert_result_db(result_db), precision=precision)  # type: ignore[return-value]


def result_db2writer(result_db: ResultDB, precision: Optional[int] = None) -> ExcelIO:
    return result_to_writer(convert_result_db(result_db), precision=precision)


def result_db2excel(result_db: ResultDB, precision: Optional[int] = None) -> io.BytesIO:
    return io.BytesIO(result_db2writer(result_db, precision).to_bytes())


def make_request_database(valuation_date: date, configuration_path: str) -> RequestDataBase:
    config = Configuration(configuration_path)
    storage_db = RequestDataBase(config)
    storage_db.valuation_date = valuation_date
    return storage_db
