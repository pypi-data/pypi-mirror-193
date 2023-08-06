from __future__ import annotations

from typing import Any, Optional, Union

from daa_utils.excel_io import ExcelIO, SimpleData, StorageData, StorageSheet, TableData, TableSheet
from daa_utils.excel_io.helper import get_object_ranges
from daa_utils.excel_io.sheet import IGNORED
from daa_utils.excel_io.style import STANDARD_HEADER_STYLE

from valuation.global_settings import __type_checking__

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from openpyxl import Workbook
    from openpyxl.worksheet.worksheet import Worksheet


class ExcelRequestReadError(Exception):
    pass


def strip_verbose(header: str) -> str:
    if '(' in header:
        header, _ = header.split('(', 1)
    return header


class TableSheetStripVerboseAndCountLegs(TableSheet):  # type: ignore[misc]

    def __init__(self, sheet_name: str, allow_none: bool = True, case_insensitive_access: bool = False) -> None:
        super().__init__(sheet_name, allow_none=allow_none, case_insensitive_access=case_insensitive_access)
        self._leg_count = 1

    def _read(self, sheet: Worksheet, lean: bool, decimal_sep: str) -> None:
        value2check = sheet['A1'].value
        if not isinstance(value2check, str):
            raise ExcelRequestReadError(f'Value at A1 must be present and of type String in {sheet.title}')
        table_ranges: list[tuple[str, int, int]] = get_object_ranges(sheet, bound_values=IGNORED)
        is_single = self._is_single_table(sheet, table_ranges)
        if is_single:
            header = 'single'
            table_end = table_ranges[-1][-1]
            table = TableDataStripVerbose(allow_none=self._allow_none, case_insensitive_access=self._ignore_case)
            table._specify_range(header, 1, table_end, 1, None)  # pylint: disable=protected-access
            table._read(sheet, lean, decimal_sep)  # pylint: disable=protected-access
            self._data[header] = table
        else:
            for table_header, table_start, table_end in table_ranges:
                table = TableDataStripVerbose(allow_none=self._allow_none, case_insensitive_access=self._ignore_case)
                table._specify_range(table_header, table_start, table_end, 2, None)  # pylint: disable=protected-access
                table._read(sheet, lean, decimal_sep)  # pylint: disable=protected-access
                if 'leg' in table_header:
                    table_header = f'leg_{self._leg_count}'
                    self._leg_count += 1
                self._data[table_header] = table
                if self._ignore_case:
                    self._lower_table_names[table_header.lower()] = table_header


class TableDataStripVerbose(TableData):  # type: ignore[misc]

    def _read_headers(self, sheet: Worksheet, header_row: int, start_column: int, end_column: int) -> None:
        if self._header_positions:
            raise ExcelRequestReadError('Table data cannot be read after data has been added')
        for index, single_tuple in enumerate(sheet.iter_cols(min_row=header_row, max_row=header_row, min_col=start_column, max_col=end_column, values_only=True)):
            content = single_tuple[0]
            if content is None:
                continue
            if not isinstance(content, str):
                raise ExcelRequestReadError(f'Header {content} is not of type string in {sheet.title}')
            content = content.strip()
            content = strip_verbose(content)
            self._header_positions[index] = content
            self._headers_with_styles[content] = STANDARD_HEADER_STYLE
            if self._ignore_case:
                self._lower_key_map[content.lower()] = content


class StorageSheetStripVerbose(StorageSheet):  # type: ignore[misc]

    def _read(self, sheet: Worksheet, lean: bool, decimal_sep: str) -> None:
        right_bound: Optional[int] = self._get_right_bound(sheet)
        storage_data_ranges = get_object_ranges(sheet, horizontal=False, first_cells_ignored=1, max_column=right_bound)
        for _, storage_start, storage_end in storage_data_ranges:
            meta_key, meta_field = self._get_meta_data(sheet, storage_start)
            storage_data = StorageDataStripVerbose(meta_key, meta_field)
            storage_data._read(sheet, storage_start, storage_end, right_bound, lean, decimal_sep)  # pylint: disable=protected-access
            self._append(storage_data)


class StorageDataStripVerbose(StorageData):  # type: ignore[misc]  # pylint: disable=abstract-method

    def __init__(self, meta_key: str, meta_field: str, precision: Optional[int] = None) -> None:
        super().__init__(meta_key, meta_field, precision=precision)
        self._meta_key: str = strip_verbose(self._meta_key)

    def _read_non_structured(self, sheet: Worksheet, raw_key: str, values: list[Any]) -> None:
        if not isinstance(raw_key, str):
            raise ExcelRequestReadError(f'Key {raw_key} is not of type String in sheet {sheet.title}')
        raw_key = strip_verbose(raw_key)
        if not values:
            self._data[raw_key] = None
        else:
            self._data[raw_key] = values if len(values) > 1 else values[0]

    def _read_storage_data(self, sheet: Worksheet, storage_data_key: str, meta_field: str, start_row: int, end_row: int, bound_col: Optional[int], lean: bool, decimal_sep: str) -> None:
        new_storage = StorageDataStripVerbose(storage_data_key, meta_field)
        new_storage._increment_depth(self._key_column - 1)  # pylint: disable=protected-access
        new_storage._read(sheet, start_row, end_row, bound_col, lean, decimal_sep)  # pylint: disable=protected-access
        self._data[new_storage.key] = new_storage

    def _read_simple_data(self, sheet: Worksheet, simple_data_key: str, start_row: int, end_row: int, start_col: int, bound_col: Optional[int], lean: bool, decimal_sep: str) -> None:
        new_simple_storage = SimpleDataStripVerbose(simple_data_key)
        new_simple_storage._read(sheet, start_row, end_row, start_col, bound_col, lean, decimal_sep)  # pylint: disable=protected-access
        self._data[new_simple_storage.key] = new_simple_storage


class SimpleDataStripVerbose(SimpleData):  # type: ignore[misc]

    def __init__(self, key: str, precision: Optional[int] = None) -> None:
        super().__init__(key, precision=precision)
        self._meta_key: str = strip_verbose(self._meta_key)
        self._data = TableDataStripVerbose()


class ExcelIOStripVerbose(ExcelIO):  # type: ignore[misc]

    def _read_work_book(self, workbook: Workbook, decimal_sep: str = '.') -> None:
        sheet_names: list[str] = workbook.sheetnames
        self._sheet_names.extend(sheet_names)
        for sheet_name in sheet_names:
            sheet: Worksheet = workbook[sheet_name]
            if self._is_structure(sheet):
                new_data: Union[TableSheetStripVerboseAndCountLegs, StorageSheetStripVerbose] = StorageSheetStripVerbose(sheet_name)
            else:
                new_data = TableSheetStripVerboseAndCountLegs(sheet_name, allow_none=True, case_insensitive_access=self._ignore_case)
            new_data._read(sheet, self._lean, decimal_sep)  # pylint: disable=protected-access
            self._data[sheet_name] = new_data
            if self._ignore_case:
                self._lower_sheet_names[sheet_name.lower()] = sheet_name
        workbook.close()
