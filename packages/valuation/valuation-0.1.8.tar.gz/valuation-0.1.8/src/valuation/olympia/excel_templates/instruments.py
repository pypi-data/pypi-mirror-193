from __future__ import annotations

import os
from typing import Generator, Optional

from daa_utils.excel_io import ExcelIO, TableData, TableSheet
from openpyxl import load_workbook
from openpyxl.styles.protection import Protection

from valuation.consts import types
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.olympia.excel_templates.template_generation_base import ExcelField, QLObjectDocumentationExcel, data_standard2table, get_objects, set_field_style
from valuation.olympia.input.mappings.request_keys import ExcelRequestParams, Keys
from valuation.engine.instrument import QLInstrument
from valuation.engine.market_data.yield_curve.spread_curve import QLConstantSpreadCurve
from valuation.universal_transfer import TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Signature
    from valuation.olympia.excel_templates.template_generation_base import ExcelFieldSubStorage


def security_data(table_data: TableData, data_standard: list[ExcelField], requires_schedule: bool, with_types: bool) -> TableData:
    if requires_schedule:
        header = ExcelField(TypeKey(types.Bool, ExcelRequestParams.RequiresScheduleColumn), False, with_types, allow_fall_back=False).key
        table_data.append(header)
        set_field_style(table_data, header, True)
    return data_standard2table(table_data, data_standard)


def leg_data(table_data: TableData, data_standard: list[ExcelField], signature: Signature) -> TableData:
    table_data.append(fields.Type.key, column_data=[signature.type])
    set_field_style(table_data, fields.Type.key, True)
    return data_standard2table(table_data, data_standard)


def request_data(signature: Signature, with_types: bool) -> TableData:
    instrument_id = ExcelField(TypeKey(types.Str, Keys.InstrumentId), False, with_types)
    instrument_type = ExcelField(TypeKey(types.Str, Keys.InstrumentType), False, with_types)
    table_data = TableData()
    table_data.append(instrument_id.key)
    table_data.append(instrument_type.key, column_data=[signature.sub_type])
    set_field_style(table_data, instrument_id.key, True)
    set_field_style(table_data, instrument_type.key, True)
    return table_data


def schedule_data(data_schedule: list[ExcelFieldSubStorage], types_schedule: list[tuple[str, str]], with_types: bool) -> TableData:
    table_data = TableData()
    instrument_id = ExcelField(TypeKey(types.Str, Keys.InstrumentId), False, with_types)
    table_data.append(instrument_id.key)
    set_field_style(table_data, instrument_id.key, True)
    schedule_type = ExcelField(fields.Type, False, with_types)
    schedule_sub_type = ExcelField(fields.SubType('schedule'), False, with_types)
    schedule_types = [schedule_type for schedule_type, _ in types_schedule]
    schedule_sub_types = [schedule_sub_type for _, schedule_sub_type in types_schedule]
    table_data.append(schedule_type.key, column_data=schedule_types)
    table_data.append(schedule_sub_type.key, column_data=schedule_sub_types)
    set_field_style(table_data, schedule_sub_type.key, True)
    set_field_style(table_data, schedule_type.key, True)
    table_data = data_standard2table(table_data, data_schedule)
    return table_data


def valuation_date(with_types: bool, template_version: str) -> TableData:
    valuation_date_field = ExcelField(fields.ValuationDate, False, with_types, allow_fall_back=False).key
    version = ExcelRequestParams.Version
    table_data = TableData()
    table_data.append(valuation_date_field)
    set_field_style(table_data, valuation_date_field, True)
    table_data.add_data_line({version: template_version})
    set_field_style(table_data, version, False)
    return table_data


def spread_curve(with_types: bool) -> TableData:
    documentation = QLObjectDocumentationExcel(QLConstantSpreadCurve, with_types)
    data_no_rho_fields: list[ExcelField] = [
        field
        for field in documentation.data_standard
        if 'rho' not in field.key
    ]

    discount_curve_id = ExcelField(TypeKey(types.Str, ExcelRequestParams.ConstantSpreadCurveId), False, with_types).key
    table_data = TableData()
    table_data.append(discount_curve_id)
    set_field_style(table_data, discount_curve_id, True)
    data_standard2table(table_data, data_no_rho_fields)
    return table_data


def instrument2writer(ql_instrument: type[QLInstrument], with_types: bool, template_version: str) -> Generator[tuple[ExcelIO, Optional[str]], None, None]:
    valuation_date_table = valuation_date(with_types, template_version)
    valuation_date_sheet = TableSheet(ExcelRequestParams.ValuationDateAndVersion)
    valuation_date_sheet.set_single(valuation_date_table)

    spread_curve_table = spread_curve(with_types)
    spread_curve_sheet = TableSheet(ExcelRequestParams.SpreadSheet)
    spread_curve_sheet.set_single(spread_curve_table)

    excel_documentation = QLObjectDocumentationExcel(ql_instrument, with_types)

    request = request_data(excel_documentation.signature, with_types)

    if excel_documentation.data_schedule:
        schedule_table = schedule_data(excel_documentation.data_schedule, excel_documentation.types_schedule, with_types)
        schedule_sheet = TableSheet(ExcelRequestParams.ScheduleSheet)
        schedule_sheet.set_single(schedule_table)
        requires_schedule = True
    else:
        requires_schedule = False
        schedule_sheet = None
    security = security_data(TableData(), excel_documentation.data_standard, requires_schedule, with_types)
    if excel_documentation.data_leg:
        for _, signature_and_items in excel_documentation.data_leg.items():
            for signature, items in signature_and_items.items():
                instrument_sheet = TableSheet(ExcelRequestParams.InstrumentSheet)
                instrument_sheet[ExcelRequestParams.RequestColumn] = request
                instrument_sheet[Keys.Security] = security
                leg_table = leg_data(TableData(), items, signature)
                instrument_sheet[f'{ExcelRequestParams.LegColumns}_1'] = leg_table
                writer = ExcelIO(lean=False, log_io=False)
                writer[valuation_date_sheet.name] = valuation_date_sheet
                writer[instrument_sheet.name] = instrument_sheet
                if requires_schedule:
                    writer[schedule_sheet.name] = schedule_sheet
                writer[spread_curve_sheet.name] = spread_curve_sheet
                yield writer, signature.type

    else:
        instrument_sheet = TableSheet(ExcelRequestParams.InstrumentSheet)
        instrument_sheet[ExcelRequestParams.RequestColumn] = request
        instrument_sheet[Keys.Security] = security
        writer = ExcelIO(lean=False, log_io=False)
        writer[valuation_date_sheet.name] = valuation_date_sheet
        writer[instrument_sheet.name] = instrument_sheet
        if requires_schedule:
            writer[schedule_sheet.name] = schedule_sheet
        writer[spread_curve_sheet.name] = spread_curve_sheet
        yield writer, None


def write_instruments(out_dir: str, template_version: str, extension: str = 'xlsx', with_types: bool = True) -> None:
    instruments: list[type[QLInstrument]] = get_objects(QLInstrument)  # type: ignore[assignment]
    for count, instrument in enumerate(instruments):
        for template_writer, leg_signature in instrument2writer(instrument, with_types, template_version):
            if leg_signature:
                file_name = f'{instrument.signature.sub_type}_{leg_signature}.{extension}'
            else:
                file_name = f'{instrument.signature.sub_type}.{extension}'
            out_path = os.path.join(out_dir, file_name)
            if extension == 'xlsx':
                template_writer.to_excel(out_path)
                re_opened = load_workbook(out_path)
                valuation_date_and_version = re_opened[ExcelRequestParams.ValuationDateAndVersion]
                valuation_date_and_version.protection.sheet = True
                valuation_date_and_version['A2'].protection = Protection(locked=False)
                re_opened.save(out_path)
                re_opened.close()
            else:
                for sheet in template_writer.sheet_names:
                    if count > 0 and sheet in (ExcelRequestParams.SpreadSheet, ExcelRequestParams.ValuationDateAndVersion):
                        continue
                    template_writer.to_csv(out_path, sheet)
