from __future__ import annotations

from typing import Any, Optional

from daa_utils import Log
from daa_utils.excel_io import ExcelIO

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.olympia.input.market_data_connection.base_parser import Parser
from valuation.olympia.input.market_data_connection.exception import ExcelFileParsingError
from valuation.olympia.input.market_data_connection.source import EXCEL

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from daa_utils.excel_io import TableData
    from valuation.olympia.input.market_data_connection.source import LocalSource


class ParserExcelFile(Parser):
    _sources = (EXCEL, )
    reference_id_pattern = '{CCY}{TENOR}'  # Should normally be defined only in non virtual parsers, but in this case it would lead to code duplication

    def __init__(self, source: LocalSource) -> None:
        super().__init__(source)
        self._content: Optional[TableData] = None

    def check_for(self, reference_id: str) -> bool:
        search_id = self._make_search_id(reference_id)
        return search_id in self._source.location  # type: ignore[operator]

    def _load(self) -> None:
        if self._content is None:
            reader = ExcelIO(log_io=False, case_insensitive_access=True)
            reader.from_excel(self._source.location)
            sheet_names = reader.sheet_names
            sheet = reader[sheet_names[0]]
            self._content = sheet.get_single()

    def _parse(self, reference_id: str) -> dict[str, Any]:
        raise NotImplementedError

    def get(self, reference_id: str) -> dict[str, Any]:
        search_id = self._make_search_id(reference_id)
        self._load()
        return self._parse(search_id)

    def _make_search_id(self, reference_id: str) -> str:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        currency = reference_id[:3]
        tenor = reference_id[3:]
        return self.reference_id_pattern.format(CCY=currency, TENOR=tenor)


class ParserDiscountCurve(ParserExcelFile):
    _signature = signatures.yield_curve.discount

    def _parse(self, reference_id: str) -> dict[str, Any]:
        object_id = self._make_search_id(reference_id)
        final_content: dict[str, Any] = self.initialize_data()
        currency: str = object_id[:3].upper()
        raw_tenor: str = object_id[3:]
        dates = []
        values: list[float] = []
        for index, _ in self._content.items():  # type: ignore[union-attr]
            try:
                dates.append(self._content.get_single_content(index, 'date'))  # type: ignore[union-attr]
                values.append(float(self._content.get_single_content(index, 'discountfactor')))  # type: ignore[union-attr]
            except KeyError as error:
                raise ExcelFileParsingError(f'Could not find or parse required column pair ("date", "discountFactor") in input {self._source.location}') from error
        tenor: str = '1D' if raw_tenor.upper() == 'OIS' else raw_tenor.upper()
        final_content[fields.Id.key] = reference_id
        final_content[fields.Currency.key] = currency
        final_content[fields.Tenor.key] = tenor
        final_content[fields.Dates.key] = dates
        final_content[fields.Values.key] = values
        return final_content


class ParserInterestRateIndex(ParserExcelFile):
    _signature = signatures.function.fixing

    def _parse(self, reference_id: str) -> dict[str, Any]:
        final_content: dict[str, Any] = self.initialize_data()
        dates = []
        values: list[float] = []
        for index, _ in self._content.items():  # type: ignore[union-attr]
            try:
                dates.append(self._content.get_single_content(index, 'fixingdate'))  # type: ignore[union-attr]
                values.append(self._content.get_single_content(index, 'fixing'))  # type: ignore[union-attr]
            except KeyError as error:
                raise ExcelFileParsingError(f'Could not find or parse required column pair ("fixingDate", "fixing") in input {self._source.location}') from error
        final_content[fields.Id.key] = reference_id
        final_content[fields.FixingDates.key] = dates
        final_content[fields.Fixings.key] = values
        return final_content
