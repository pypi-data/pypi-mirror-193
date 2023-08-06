from __future__ import annotations

import datetime
import io
import json
import os
import re
from pathlib import Path
from collections import OrderedDict, defaultdict
from functools import singledispatch, singledispatchmethod
from typing import Any, Generator, Optional, Union

from daa_utils import Log
from daa_utils.excel_io import SimpleData, StorageData

from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.inputs.standard import standard_date_converter
from valuation.olympia.excel_templates.non_instruments import DEFAULT_STRUCTURED
from valuation.olympia.excel_templates.request_io import ExcelIOStripVerbose
from valuation.olympia.input.exception import OlympiaImportError
from valuation.olympia.input.mappings.request_keys import BUCKET_TO_OBJECT, ExcelRequestParams, Keys, MarketDataBuckets
from valuation.utils.input_output import to_json

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from daa_utils.excel_io import TableData, StorageSheet
    from io import BytesIO


# todo (2021/05) change structure of json files:
#   - one valuation date
#   - tie instrumentId to instrumentData
#   - tie calculationFunction as type to instrumentData
#   - what to do with market_data?


class ExcelRequestError(OlympiaImportError):
    pass


class OlympiaRequestError(OlympiaImportError):
    pass


class Request:

    def __init__(self) -> None:
        self._valuation_date: Optional[datetime.date] = None
        self._instruments: list[dict[str, Any]] = []
        self._market_data: list[dict[str, Any]] = []
        self._typed_valuations: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._valuations: list[dict[str, Any]] = []
        self._instrument_references: list[str] = []
        self._market_data_references: list[str] = []
        self._initialize()

    def instruments(self) -> Generator[dict[str, Any], None, None]:
        for instrument_data in self._instruments:
            yield instrument_data

    def market_data(self) -> Generator[dict[str, Any], None, None]:
        yield from self._market_data

    def has_valuations(self, instrument_type: str) -> bool:
        return instrument_type in self._valuations

    def valuations(self) -> Generator[dict[str, Any], None, None]:
        for valuation in self._valuations:
            yield valuation
        for instrument_data in self._instruments:
            instrument_id: str = instrument_data[Keys.ObjectId]
            instrument_type: str = instrument_data[Keys.Type]
            for valuation in self._typed_valuations[instrument_type]:
                yield {**{'instrument': instrument_id, 'id': f'{instrument_id}#{valuation[Keys.SubType]}'},
                       **valuation}

    def instrument_references(self) -> list[str]:
        return self._instrument_references

    def market_data_references(self) -> list[str]:
        return self._market_data_references

    @property
    def valuation_date(self) -> datetime.date:
        return self._valuation_date  # type: ignore[return-value] # not None is asserted

    def _initialize(self) -> None:
        raise NotImplementedError

    @singledispatchmethod
    def _finalized_market_data(self, arg: Any, bucket_key: str) -> Generator[dict[str, Any], None, None]:
        raise NotImplementedError(f'arg: {arg} of type: {type(arg)}')

    @_finalized_market_data.register(dict)
    def _(self, arg: dict[str, Any], bucket_key: str) -> Generator[dict[str, Any], None, None]:  # pylint: disable=no-self-use
        if bucket_key == MarketDataBuckets.MarketData:
            yield arg
            return
        signature = BUCKET_TO_OBJECT[bucket_key]
        arg[fields.Type.key] = signature.type
        if signature.sub_type != '':
            arg[fields.SubType(signature.type).key] = signature.sub_type
        yield arg

    @_finalized_market_data.register(list)  # type: ignore[no-redef]
    def _(self, arg: list[dict[str, Any]], bucket_key: str) -> Generator[dict[str, Any], None, None]:
        for item in arg:
            yield from self._finalized_market_data(item, bucket_key)

    def to_json(self) -> dict[str, Any]:

        out_put: dict[str, Any] = OrderedDict()
        if self._valuation_date is not None:
            out_put[Keys.ValuationDate] = self._valuation_date

        instruments: list[dict[str, Any]] = []
        for instrument_data in self.instruments():
            instrument_id: str = instrument_data['id']
            instrument_type: str = instrument_data['type']
            instrument: dict[str, Any] = OrderedDict({'id': instrument_id})
            instrument['type'] = instrument_type
            for data_key in sorted(instrument_data):
                instrument[data_key] = instrument_data[data_key]
            instruments.append(instrument)

        out_put['instrumentData'] = instruments
        if self._market_data:
            out_put['marketData'] = self._market_data
        if self._typed_valuations:
            out_put['valuation'] = [{Keys.InstrumentType: instrument_type, **valuation}
                                     for instrument_type, valuations in self._typed_valuations.items()
                                     for valuation in valuations]
        if self._valuations:
            out_put['valuation'] = out_put.get('valuation', []) + self._valuations
        return to_json(out_put)  # type: ignore[return-value]


class OlympiaRequest(Request):  # pylint: disable=abstract-method

    def __init__(self, data_or_json_path: Union[dict[str, Any], str, bytes, io.BytesIO]) -> None:
        if isinstance(data_or_json_path, str):
            with open(data_or_json_path, mode='r') as json_handle:
                self._data: dict[str, Any] = json.load(json_handle)
        elif isinstance(data_or_json_path, dict):
            self._data = data_or_json_path
        elif isinstance(data_or_json_path, (bytes, io.BytesIO)):
            self._data = json.load(data_or_json_path)  # type: ignore[arg-type]
        else:
            raise OlympiaImportError(
                f'Unknown data format {data_or_json_path} of {type(data_or_json_path)}'
            )

        super().__init__()

    def _initialize(self) -> None:
        self._initialize_valuation_date()
        self._initialize_instrument_data()
        self._initialize_instrument_references()
        self._initialize_market_data()
        self._initialize_market_data_references()
        self._initialize_valuations()

    def _initialize_valuation_date(self) -> None:
        try:
            self._valuation_date = standard_date_converter(self._data[Keys.ValuationDate])  # type: ignore[assignment]
        except KeyError as error:
            raise OlympiaRequestError('Request does not contain a valuation date') from error

    def _initialize_instrument_data(self) -> None:
        raw_instrument_data: Union[list[dict[str, Any]], dict[str, Any]] = self._data.get(Keys.InstrumentData, [])
        if not isinstance(raw_instrument_data, list):
            instrument_data_bucket: list[dict[str, Any]] = [raw_instrument_data]
        else:
            instrument_data_bucket = raw_instrument_data

        instrument: dict[str, Any]
        for instrument in instrument_data_bucket:
            instrument_bucket: dict[str, Any] = {}
            if any(key not in instrument for key in (Keys.ObjectId, Keys.Type)):
                raise OlympiaRequestError(f'Every instrument must contain {Keys.ObjectId} and {Keys.Type}')
            instrument_bucket[Keys.ObjectId] = instrument[Keys.ObjectId]
            instrument_bucket[Keys.Type] = instrument[Keys.Type]
            instrument_data: dict[str, Any] = {}
            for key, value in instrument.items():
                if key == Keys.Security:
                    instrument_data.update(value)
                else:
                    instrument_data[key] = value
            instrument_bucket.update(instrument_data)
            self._instruments.append(instrument_bucket)
        self._valuation_date = standard_date_converter(self._data[Keys.ValuationDate])  # type: ignore[assignment]

    def _initialize_instrument_references(self) -> None:
        overall_price_classifier: str = self._data.get(Keys.PriceClassifier, 'MID')
        raw_references: Union[list[dict[str, Any]], dict[str, Any]] = self._data.get(Keys.InstrumentReferences, [])
        if isinstance(raw_references, dict):
            raw_references = [raw_references]
        elif not isinstance(raw_references, list):
            raise OlympiaRequestError('Bad request')
        for item in raw_references:
            if Keys.ObjectId not in item:
                Log.critical('Instrument item of pricing request has no "id"')
                continue
            price_classifier = item.get(Keys.PriceClassifier, overall_price_classifier)
            self._instrument_references.append(f'{item[Keys.ObjectId]}#{price_classifier}')

    def _initialize_market_data_references(self) -> None:
        raw_references: Union[list[dict[str, Any]], dict[str, Any]] = self._data.get(Keys.MarketDataReferences, [])
        all_ids: set[str] = set()
        if isinstance(raw_references, dict):
            raw_references = [raw_references]
        elif not isinstance(raw_references, list):
            raise OlympiaRequestError('Bad request')
        for item in raw_references:
            if Keys.ObjectId not in item:
                Log.critical('Market data item of pricing request has no "id"')
                continue
            all_ids.add(item[Keys.ObjectId])
        self._market_data_references = list(all_ids)

    def _initialize_market_data(self) -> None:
        market_data_buckets: tuple[Any, ...] = MarketDataBuckets.get_all()
        for bucket_key in market_data_buckets:
            if bucket_key in self._data:
                for market_data in self._finalized_market_data(self._data[bucket_key], bucket_key):
                    self._market_data.append(market_data)

    def _initialize_valuations(self) -> None:
        if Keys.Valuations not in self._data:
            return
        if not isinstance(self._data[Keys.Valuations], list):
            valuation_bucket: list[dict[str, Any]] = [self._data[Keys.Valuations]]
        else:
            valuation_bucket = self._data[Keys.Valuations]
        for valuation_data in valuation_bucket:
            if Keys.InstrumentType not in valuation_data:
                raise OlympiaRequestError(f'Field {Keys.InstrumentType} is missing in valuation: {valuation_data}')
            instrument_type = valuation_data[Keys.InstrumentType]
            del valuation_data[Keys.InstrumentType]
            self._typed_valuations[instrument_type].append(valuation_data)


@singledispatch
def pascal2camel_case(arg: Any) -> Any:
    raise NotImplementedError(f'{arg}, {type(arg)}')


@pascal2camel_case.register(str)
def _(arg: str) -> str:
    cased_arg = arg[:1].lower() + arg[1:]
    if cased_arg != arg:
        Log.warning(f'Please use camelCase for key: {cased_arg} instead of PascalCase: {arg}')
    return cased_arg


@pascal2camel_case.register(dict)  # type: ignore[no-redef]
def _(arg: dict[str, Any]) -> dict[str, Any]:
    return {pascal2camel_case(key): value for key, value in arg.items()}


@pascal2camel_case.register(list)  # type: ignore[no-redef]
def _(arg: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [pascal2camel_case(item) for item in arg]


VERSION_UNDEFINED = 'VERSION_UNDEFINED'
VERSION_PREFIX = '__version__ = '
IS_VERSION_CHECK = re.compile('^v?\\d+\\.')  # searches for: Must start with either v[digits]. or [digits].


def extract_version(line: str) -> str:
    if not line.startswith(VERSION_PREFIX):
        return VERSION_UNDEFINED
    str2check = line.replace(VERSION_PREFIX, '').strip().strip("'").strip('"')
    is_version = re.match(IS_VERSION_CHECK, str2check) is not None
    if is_version:
        return str2check
    return VERSION_UNDEFINED


def get_engine_version() -> str:
    file_path = os.path.join(Path(os.path.dirname(__file__)).parents[1], '__init__.py')
    try:
        with open(file_path, mode='r') as version_file_handle:
            version_line = version_file_handle.readlines()[0]
            test = extract_version(version_line)
            return test
    # Following is broad on purpose so version determination will not crash the request
    except Exception:  # pylint: disable=broad-except
        return VERSION_UNDEFINED


class ExcelRequest(Request):  # pylint: disable=abstract-method

    def __init__(self, request_path_or_bytes: Union[str, BytesIO], check_version: bool = True) -> None:
        self._path = str(request_path_or_bytes)
        self._reader = ExcelIOStripVerbose(lean=False, log_io=False, case_insensitive_access=True)
        try:
            if isinstance(request_path_or_bytes, str):
                self._reader.from_excel(request_path_or_bytes)
                _, self._file_name = os.path.split(request_path_or_bytes)
            else:
                self._reader.from_bytes(request_path_or_bytes)
                self._file_name = str(self._reader)
        except Exception as exception:
            raise ExcelRequestError('Cannot read request') from exception
        self._sheet_names: list[str] = self._reader.sheet_names

        self._schedule_table: Optional[TableData] = None
        self._spread_table: Optional[TableData] = None
        self._process_table: Optional[TableData] = None
        self._market_data_sheet: Optional[StorageSheet] = None
        self._valuations_sheet: Optional[StorageSheet] = None

        self._schedules_found_but_not_used: bool = True
        self._check_version = check_version
        super().__init__()

    def _initialize(self) -> None:
        self._check_version_and_get_valuation_date()
        if ExcelRequestParams.InstrumentSheet not in self._sheet_names:
            raise ExcelRequestError(f'{self._file_name} is missing {ExcelRequestParams.InstrumentSheet}')
        if ExcelRequestParams.ScheduleSheet in self._sheet_names:
            self._schedule_table = self._reader[ExcelRequestParams.ScheduleSheet].get_single()
        if ExcelRequestParams.SpreadSheet in self._sheet_names:
            self._spread_table = self._reader[ExcelRequestParams.SpreadSheet].get_single()
        if ExcelRequestParams.ProcessSheet in self._sheet_names:
            self._process_table = self._reader[ExcelRequestParams.ProcessSheet].get_single()
        if ExcelRequestParams.MarketDataSheet in self._sheet_names:
            self._market_data_sheet = self._reader[ExcelRequestParams.MarketDataSheet]
        if ExcelRequestParams.ValuationSheet in self._sheet_names:
            self._valuations_sheet = self._reader[ExcelRequestParams.ValuationSheet]
        self._read()

    def _check_version_and_get_valuation_date(self) -> None:
        if ExcelRequestParams.ValuationDateAndVersion not in self._sheet_names:
            raise ExcelRequestError(
                f'{self._file_name} does not contain sheet {ExcelRequestParams.ValuationDateAndVersion}, you are using an unsupported/old template version')
        table = self._reader[ExcelRequestParams.ValuationDateAndVersion].get_single()
        if not table.contains(0, fields.ValuationDate.key):
            raise ExcelRequestError(f'{self._file_name} has no valuation date')
        valuation_date: Union[str, datetime.date] = table.get_single_content(0, fields.ValuationDate.key)
        if isinstance(valuation_date, str):
            try:
                date = datetime.date.fromisoformat(valuation_date)
                self._valuation_date = date
            except Exception as exception:
                raise ExcelRequestError(
                    f'Valuation date is not formatted as excel date, could not isoformat-parse it in {self._file_name}') from exception
        elif isinstance(valuation_date, datetime.date):
            self._valuation_date = valuation_date
        else:
            raise ExcelRequestError(f'Cannot read valuation date in {self._file_name}')
        if self._check_version:
            try:
                template_version: str = str(table.get_single_content(0, ExcelRequestParams.Version)).strip()
            except KeyError:
                template_version = VERSION_UNDEFINED
            engine_version: str = get_engine_version()
            if engine_version != template_version or template_version == VERSION_UNDEFINED:
                Log.warning(f'Template version: {template_version} / Engine version: {engine_version}')
            else:
                Log.info(f'Template version: {template_version} / Engine version: {engine_version}')

    def _read(self) -> None:
        instrument_sheet = self._reader[ExcelRequestParams.InstrumentSheet]
        if ExcelRequestParams.RequestColumn not in instrument_sheet:
            raise ExcelRequestError(f'Table {ExcelRequestParams.RequestColumn} not found or empty in {self._file_name}')
        if Keys.Security not in instrument_sheet:
            Log.warning(f'Table {Keys.Security} not found or empty in {self._file_name}')
            security_table: Optional[TableData] = None
        else:
            security_table = instrument_sheet[Keys.Security]
        request_table = instrument_sheet[ExcelRequestParams.RequestColumn]
        if len(instrument_sheet.table_names) > 2:
            leg_tables: Optional[tuple[TableData, ...]] = tuple(
                instrument_sheet[table_name] for table_name in instrument_sheet.table_names[2:])
        else:
            leg_tables = None
        for instrument_row, _ in request_table.items():
            self._instruments.append(
                self._get_single_instrument(instrument_row, request_table, security_table, leg_tables))
        if self._spread_table is not None:
            self._get_spreads()
        if self._process_table is not None:
            self._get_processes()
        if self._market_data_sheet is not None:
            self._get_market_data()
        if self._valuations_sheet is not None:
            self._get_valuations()

    def _get_single_instrument(self, instrument_row: int, request_table: TableData, security_table: Optional[TableData],
                               leg_tables: Optional[tuple[TableData, ...]]) -> dict[str, Any]:
        has_legs: bool = False
        instrument: dict[str, Any] = {}
        if not request_table.contains(instrument_row, Keys.InstrumentType):
            raise ExcelRequestError(
                f'Table {ExcelRequestParams.RequestColumn} is missing {Keys.InstrumentType} at row {instrument_row + 3} in {self._file_name}')
        if not request_table.contains(instrument_row, Keys.InstrumentId):
            raise ExcelRequestError(
                f'Table {ExcelRequestParams.RequestColumn} is missing {Keys.InstrumentId} at row {instrument_row + 3} in {self._file_name}')
        instrument_id = request_table.get_single_content(instrument_row, Keys.InstrumentId)
        if not isinstance(instrument_id, str):
            Log.warning('Instrument Id is not a string. '
                        'That may cause problems in referencing schedules and other objects.')
            instrument_id = str(instrument_id)
        instrument[Keys.ObjectId] = str(request_table.get_single_content(instrument_row, Keys.InstrumentId))
        instrument[Keys.Type] = request_table.get_single_content(instrument_row, Keys.InstrumentType)
        instrument_data: dict[str, Any] = {}
        if security_table is not None and security_table.has_data_at(instrument_row):
            schedule_required, data = self._get_security(instrument_row, security_table.get_data_at(instrument_row))
            instrument_data.update(data)
            if leg_tables:
                legs: list[dict[str, Any]] = []
                for leg_count, leg_table in enumerate(leg_tables):
                    if leg_table.has_data_at(instrument_row):
                        has_legs = True
                        legs.append(self._get_leg(instrument_row, leg_count + 1, leg_table.get_data_at(instrument_row)))
                if has_legs:
                    instrument_data[fields.Legs.key] = legs
            if schedule_required:
                schedule: dict[str, list[dict[str, Any]]] = self._get_schedules(instrument_id, has_legs)
                for schedule_key, schedule_items in schedule.items():
                    instrument_data[schedule_key] = schedule_items
        instrument.update(instrument_data)
        return instrument

    def _get_security(self, instrument_row: int, data: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
        schedule_required: bool = False
        data = pascal2camel_case(data)
        if ExcelRequestParams.RequiresScheduleColumn in data:
            schedule_required = data[ExcelRequestParams.RequiresScheduleColumn]
            if not isinstance(schedule_required, bool):
                raise ExcelRequestError(
                    f'{ExcelRequestParams.RequestColumn} is not of type bool(TRUE/FALSE) at row {instrument_row + 3} in {self._file_name}')
            del data[ExcelRequestParams.RequiresScheduleColumn]
        return schedule_required, data

    def _get_leg(self, instrument_row: int, leg_count: int, data: dict[str, Any]) -> dict[str, Any]:
        legs = {1: 'first', 2: 'second', 3: 'third'}
        data = pascal2camel_case(data)
        if fields.Type.key not in data:
            leg = legs.get(leg_count, f'{leg_count}th')
            raise ExcelRequestError(
                f'Leg type not specified in the {leg} leg at row {instrument_row + 3} in {self._file_name}')
        data[fields.LegNumber.key] = leg_count
        return data

    def _get_schedules(self, instrument_id: str, has_legs: bool) -> dict[str, list[dict[str, Any]]]:
        schedules: dict[str, list[dict[str, Any]]] = defaultdict(list)
        if not self._schedule_table:
            raise ExcelRequestError(
                f'Instrument {instrument_id} requires but request {self._file_name} has no sheet {ExcelRequestParams.ScheduleSheet}')
        items_found = False
        for schedule_row, schedule_items in self._schedule_table.where_is_equal(Keys.InstrumentId, instrument_id):
            items_found = True
            schedule_items = pascal2camel_case(schedule_items)
            schedule_base_type = fields.Type.key
            schedule_sub_type = fields.SubType().key
            if schedule_base_type not in schedule_items:
                raise ExcelRequestError(
                    f'No {schedule_base_type} given at row {schedule_row + 2} in sheet {ExcelRequestParams.ScheduleSheet} in {self._file_name}')
            if schedule_sub_type not in schedule_items:
                raise ExcelRequestError(
                    f'No {schedule_sub_type} given at row {schedule_row + 2} in sheet {ExcelRequestParams.ScheduleSheet} in {self._file_name}')
            schedule_base_key = schedule_items[schedule_base_type]
            schedule_items[fields.Type.key] = schedule_items[schedule_sub_type]
            del schedule_items[schedule_sub_type]
            del schedule_items[Keys.InstrumentId]
            if has_legs and fields.LegNumber.key not in schedule_items and schedule_base_key != fields.CallSchedule.key:
                raise ExcelRequestError(
                    f'Schedule item at row {schedule_row + 2} in sheet {ExcelRequestParams.ScheduleSheet} in {self._file_name} is not assigned to a leg via {fields.LegNumber}')
            schedules[schedule_base_key].append(schedule_items)
        if not items_found:
            raise ExcelRequestError(
                f'No schedule items found for instrument {instrument_id} in sheet {ExcelRequestParams.ScheduleSheet} in {self._file_name}')
        return schedules

    def _get_spreads(self) -> None:
        items: list[dict[str, Any]] = []
        for row, item in self._spread_table.items():  # type: ignore[union-attr]
            try:
                cased_item = pascal2camel_case(item)
                spread_name = cased_item[ExcelRequestParams.ConstantSpreadCurveId]
                del cased_item[ExcelRequestParams.ConstantSpreadCurveId]
            except KeyError:
                raise ExcelRequestError(
                    f'{ExcelRequestParams.ConstantSpreadCurveId} missing in spread sheet at row {row + 2} in sheet {ExcelRequestParams.SpreadSheet} in {self._file_name}')  # pylint: disable=raise-missing-from
            cased_item[fields.Id.key] = spread_name
            items.append(cased_item)
        for finalized in self._finalized_market_data(items, MarketDataBuckets.SpreadCurves):
            self._market_data.append(finalized)

    def _get_processes(self) -> None:
        for row, process_data in self._process_table.items():  # type: ignore[union-attr]
            process_data = pascal2camel_case(process_data)
            if fields.Type.key not in process_data or fields.Id.key not in process_data:
                raise ExcelRequestError(
                    f'{fields.Type.key} and/or {fields.Id.key} missing in item at row {row + 2} in sheet {ExcelRequestParams.ProcessSheet} in {self._file_name}')
            self._market_data.append(process_data)

    def _get_market_data(self) -> None:
        for item in self._market_data_sheet.data:  # type: ignore[union-attr]
            self._market_data.append(self._read_storage_data(item))

    def _get_valuations(self) -> None:
        for item in self._valuations_sheet.data:  # type: ignore[union-attr]
            valuation_data = self._read_storage_data(item)
            if Keys.InstrumentType not in valuation_data:
                raise ExcelRequestError(
                    f'Field {Keys.InstrumentType} is missing in item at row {item.key}|{item.field} in sheet {ExcelRequestParams.ValuationSheet} in {self._file_name}')
            instrument_type = valuation_data[Keys.InstrumentType]
            del valuation_data[Keys.InstrumentType]
            self._typed_valuations[instrument_type].append(valuation_data)

    def _read_storage_data(self, storage_data: StorageData) -> dict[str, Any]:
        possible_camel_case_key = storage_data.key
        capitalized_key = possible_camel_case_key[:1].upper() + possible_camel_case_key[1:]
        storage: dict[str, Any] = {
            fields.Type.key: capitalized_key,
            fields.Id.key: storage_data.field
        }
        for key, value in storage_data.items():
            if isinstance(value, StorageData):
                storage[pascal2camel_case(key)] = self._read_storage_data(value)
            elif isinstance(value, SimpleData):
                storage[pascal2camel_case(key)] = pascal2camel_case(value.data)
            elif isinstance(value, str) and value.strip().lower() == DEFAULT_STRUCTURED.lower():
                continue
            else:
                storage[pascal2camel_case(key)] = value
        return storage
