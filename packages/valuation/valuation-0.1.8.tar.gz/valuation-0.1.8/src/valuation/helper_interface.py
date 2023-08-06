from __future__ import annotations

from datetime import date
from typing import Any, TYPE_CHECKING
from daa_utils import Log

from valuation.olympia import make_request_database
from valuation.engine import QLObjectDB, QLFactory
from valuation.universal_transfer import Reference
from valuation.utils.input_output import to_json

if TYPE_CHECKING:
    # pylint: disable=ungrouped-imports
    from valuation.olympia import RequestDataBase


# todo 2021/12 before exposing this to an api, this needs to hide the tokens inside the storages
def get_object_from_parser(references: list[tuple[str, str]], valuation_date: str, configuration_path: str,
                           validate_through_ql_obj: bool = True, dump_all: bool = False) -> list[dict[str, Any]]:
    with Log(filename_base=None):
        with QLFactory():
            storage_db: RequestDataBase = make_request_database(date.fromisoformat(valuation_date), configuration_path)
            if validate_through_ql_obj:
                ql_db = QLObjectDB(storage_db)
            result: list[dict[str, Any]] = []
            for ref in references:
                try:
                    reference = Reference(*ref)
                    if validate_through_ql_obj:
                        _ = ql_db[reference]
                    storage_to_add: dict[str, Any] = to_json(storage_db[reference])  # type: ignore[assignment]
                except Exception as exception:  # pylint: disable=broad-except
                    Log.error(f'{type(exception)}: {str(exception)}')
                    storage_to_add = {}
                result.append(storage_to_add)
            print('\n'.join(Log.info_message_list()))
            if dump_all:
                return [to_json(storage_db[item]) for item in storage_db]  # type: ignore[misc]
            return result
