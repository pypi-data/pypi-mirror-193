from __future__ import annotations

import csv
import datetime
from collections import defaultdict, OrderedDict
from pathlib import Path
from typing import Any, Sequence, Union, Optional

from daa_utils import Log, recursive_glob

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.olympia.input.cloud_storage_connectors import CloudConnector, load_csv_file
from valuation.olympia.input.mappings.request_keys import MatrixKeys
from valuation.olympia.input.market_data_connection.base_parser import Parser
from valuation.olympia.input.market_data_connection.exception import CSVFileParsingError
from valuation.olympia.input.market_data_connection.helpers import german2iso_date
from valuation.olympia.input.market_data_connection.source import CSV, GOOGLE, S3
from valuation.olympia.input.cloud_storage_connectors import CloudPathHandler

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.olympia.input.market_data_connection.source import Source


def local_load(path: str) -> list[list[str]]:
    with open(path, mode='r') as file_handle:
        return list(csv.reader(file_handle, delimiter=';'))


def cloud_storage_load(key: CloudPathHandler) -> list[list[str]]:
    return load_csv_file(key, delimiter=';')


class ParserCSVFileWithHeaders(Parser):  # pylint: disable=abstract-method
    _sources = (CSV, S3, GOOGLE)

    def __init__(self, source: Source) -> None:
        super().__init__(source)
        self._header_row: int = 0

    @staticmethod
    def _load_file(location: Union[str, CloudPathHandler]) -> list[list[str]]:
        if isinstance(location, CloudPathHandler):
            return cloud_storage_load(location)
        return local_load(location)


class ParserCSVConstantContent(ParserCSVFileWithHeaders):  # pylint: disable=abstract-method

    def __init__(self, source: Source) -> None:
        super().__init__(source)
        self._content: list[list[str]] = []
        self._header_indexes: dict[str, int] = {}

    def __contains__(self, item: str) -> bool:
        return item in self._header_indexes

    def check_for(self, reference_id: str) -> bool:
        if not self._content:
            self._load()
        search_id = self._make_search_id(reference_id)
        if search_id in self:
            return True
        Log.warning(f'{self} unsuccessfully checked for {search_id}')
        return False

    def _load(self) -> None:
        self._content = self._load_file(self._source.location)
        self._make_header_indexes()

    def _make_header_indexes(self) -> None:
        self._header_indexes = {name.replace(' ', ''): index for index, name in enumerate(self._content[self._header_row]) if name}


class DiscountFactors(ParserCSVConstantContent):
    _signature = signatures.yield_curve.discount
    reference_id_pattern = '{CCY}{TENOR}'

    def __init__(self, source: Source) -> None:
        super().__init__(source)
        self._header_row: int = 4
        self._first_row: int = 10
        self._date_offset: int = 1
        self._value_offset: int = 2

    def _get_discount_factors(self, reference_id: str) -> tuple[list[str], list[float]]:
        idx: int = self._header_indexes[reference_id]
        dates: list[str] = []
        values: list[float] = []
        for row in self._content[self._first_row:]:
            raw_date: str = row[idx + self._date_offset]
            raw_value: str = row[idx + self._value_offset]
            if raw_date == '' or raw_value == '':
                break
            dates.append(german2iso_date(raw_date))
            values.append(float(raw_value.replace(',', '.')))
        if len(dates) != len(values):
            raise CSVFileParsingError(f'Format issues while accessing {reference_id} in {self._source}. Dates and Discount Factors do not have the same length')
        return dates, values

    def get(self, reference_id: str) -> dict[str, Any]:
        # The following naming convention is assumed <3-digit-ccy><tenor>[<optional suffix>]
        # From the name, the currency and tenor are taken. "OIS" will be changed to "1D", as this is the internal tenor for overnight
        initialized = self.initialize_data()
        object_id = self._make_search_id(reference_id)
        currency: str = object_id[:3]
        period: str = object_id[3:]
        if period == 'OIS':
            period = '1D'
        dates, values = self._get_discount_factors(object_id)
        update: dict[str, Any] = {
            fields.Id.key: object_id,
            'name': object_id,
            'referenceDateTime': global_parameters.DummyDate,
            fields.Currency.key: currency,
            fields.Tenor.key: period,
            fields.Dates.key: dates,
            fields.Values.key: values
        }
        initialized.update(update)
        return initialized

    def _make_search_id(self, reference_id: str) -> str:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        currency = reference_id[:3]
        tenor = reference_id[3:]
        return self.reference_id_pattern.format(CCY=currency, TENOR=tenor)


class RateFixingsBase(ParserCSVConstantContent):
    def __init__(self, source: Source) -> None:
        super().__init__(source)
        self._first_row: int = 1
        # only difference to DiscountFactors is the date index

    def check_for(self, reference_id: str) -> bool:
        if not self._content:
            self._load()
        if reference_id in self:
            return True
        Log.warning(f'{self} unsuccessfully checked for {reference_id}')
        return True

    def _get_fixings(self, reference_id: str) -> tuple[list[str], list[float]]:
        if reference_id not in self:
            return [], []
        idx: int = self._header_indexes[reference_id]
        dates: list[str] = []
        values: list[float] = []
        for row in self._content[self._first_row:]:
            try:
                raw_date: str = row[0]
                raw_value: str = row[idx]
                date: str = german2iso_date(raw_date)
                value: float = float(raw_value.replace(',', '.')) / 100
                dates.append(date)
                values.append(value)
            except ValueError:
                continue
        return dates, values

    def get(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        dates, values = self._get_fixings(reference_id)
        update = {
            fields.Id.key: reference_id,
            fields.FixingDates.key: dates,
            fields.Fixings.key: values
        }
        initialized.update(update)
        return initialized

    def _make_search_id(self, reference_id: str) -> str:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        currency = reference_id[:3]
        tenor = reference_id[3:]
        return self.reference_id_pattern.format(CCY=currency, TENOR=tenor)


class RateFixings(RateFixingsBase):
    _signature = signatures.function.fixing
    reference_id_pattern = '{CCY}{TENOR}'

    def check_for(self, reference_id: str) -> bool:
        if 'vs' in reference_id:
            return False
        return super().check_for(reference_id)


class SwapRateFixings(RateFixingsBase):
    _signature = signatures.function.swap_rate_fixing
    reference_id_pattern = '{INDEX_CCY}{INDEX_FREQUENCY}vs{SWAP_DURATION}'

    def check_for(self, reference_id: str) -> bool:
        if reference_id != reference_id.strip():
            Log.warning(f'Found trailing or leading spaces in {reference_id}')
        if not all((
                'vs' in reference_id,
                len(reference_id) > 3,
                reference_id[reference_id.find('vs') + 2].isnumeric(),
                not reference_id[-1].isnumeric(),
        )):
            return False
        return super().check_for(reference_id)

    def get(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        object_id = self._make_search_id(reference_id)
        dates, values = self._get_fixings(object_id)
        update = {
            fields.Id.key: object_id,
            fields.FixingDates.key: dates,
            fields.Fixings.key: values
        }
        initialized.update(update)
        return initialized

    def _make_search_id(self, reference_id: str) -> str:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        for separator in ('VS', 'vs'):
            try:
                index_name, swap_duration = reference_id.split(separator)
                currency = index_name[:3]
                frequency = index_name[3:]
                return self.reference_id_pattern.format(INDEX_CCY=currency, INDEX_FREQUENCY=frequency, SWAP_DURATION=swap_duration)
            except ValueError:
                continue
        Log.warning(f'{self} could not process {reference_id}')
        return reference_id


class ConstantSpread(ParserCSVConstantContent):
    _signature = signatures.yield_curve.constant_spread

    def __init__(self, source: Source) -> None:
        super().__init__(source)
        self._spread_column: int = 2
        self._header_row: int = 0
        self._first_row: int = 1
        self._base_curve_column: int = 1

    def _make_header_indexes(self) -> None:
        self._header_indexes = {row[self._header_row]: index + self._first_row for index, row in enumerate(self._content[self._first_row:])}

    def _get_spread(self, reference_id: str) -> tuple[str, float]:
        idx: int = self._header_indexes[reference_id]
        return self._content[idx][self._base_curve_column], float(self._content[idx][self._spread_column].replace(',', '.'))

    def get(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        object_id = self._make_search_id(reference_id)
        base_curve, spread = self._get_spread(object_id)
        update = {
            fields.Id.key: object_id,
            'name': object_id,
            fields.BaseCurve.key: base_curve,
            fields.Value.key: spread
        }
        initialized.update(update)
        return initialized


class NoFileFoundError(CSVFileParsingError):
    pass


class InterestRateVolatility(ParserCSVFileWithHeaders):
    _file_pattern = ''
    _normal_distribution_identifier = ''
    _object_type_identifier = ''

    def check_for(self, reference_id: str) -> bool:
        search_id = self._make_search_id(reference_id)
        file_name = self._make_file_name(search_id)
        try:
            _ = self._get_file(file_name)
            return True
        except NoFileFoundError as error:
            Log.warning(str(error))
            return False

    def get(self, reference_id: str) -> dict[str, Any]:
        object_id = self._make_search_id(reference_id)
        content = self._load(reference_id)
        initialized = self.initialize_data()
        currency, tenor, distribution = self._get_params_from_formatted(object_id)
        matrix = self._get_matrix(content, object_id)
        update = {
            fields.Id.key: reference_id,
            fields.Distribution.key: distribution,
            fields.Currency.key: currency,
            fields.Calendar.key: currency,
            fields.Tenor.key: tenor.replace('_', ''),  # todo (2021/10) test if replace is safe, was done for EUR_3M / EUR3M
            MatrixKeys.ColumnHeaders: matrix[MatrixKeys.ColumnHeaders],
            MatrixKeys.RowHeaders: matrix[MatrixKeys.RowHeaders],
            MatrixKeys.Content: matrix[MatrixKeys.Content]
        }
        initialized.update(update)
        return initialized

    def _get_params_from_reference(self, reference_id: str) -> tuple[str, str, str]:
        normal_distribution = self._normal_distribution_identifier
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        stripped_obj_type = reference_id.replace(self._object_type_identifier, '')
        stripped_vol = stripped_obj_type.replace('Vol', '')
        if not stripped_vol.endswith(normal_distribution):
            Log.warning(f'{reference_id} is not of the correct format for {self}')
        stripped_distribution = stripped_vol.replace(normal_distribution, '')
        if stripped_distribution.endswith('Log'):
            distribution = f'Log{self._normal_distribution_identifier}'
            stripped_distribution = stripped_distribution.replace('Log', '')
        else:
            distribution = normal_distribution
        if len(stripped_distribution) not in (5, 6):
            Log.warning(f'{reference_id} is not of the correct format for {self}')
        currency = stripped_distribution[:3]
        tenor = stripped_distribution[3:]
        return currency, tenor, distribution

    @classmethod
    def _get_params_from_formatted(cls, formatted_id: str) -> tuple[str, str, str]:
        stripped_obj_type = formatted_id.strip(cls._object_type_identifier)
        stripped_vol = stripped_obj_type.replace('Vol', '')
        currency, tenor_and_dist = stripped_vol[:3], stripped_vol[3:]
        tenor = tenor_and_dist.replace('Log', '').replace(cls._normal_distribution_identifier, '')
        distribution = tenor_and_dist.replace(tenor, '')
        return currency, tenor, distribution

    def _make_file_name(self, formatted_id: str) -> str:
        currency, _, distribution = self._get_params_from_formatted(formatted_id)
        file_distribution = ' Normal' if distribution == self._normal_distribution_identifier else ''
        pattern_final_space_adjusted = ''.join(self._file_pattern.rsplit(' ', 1))
        return pattern_final_space_adjusted.format(CCY=currency, Normal__or__NONE=file_distribution)

    def _get_file(self, file_name: str) -> Union[str, CloudPathHandler]:
        try:
            if self._source.descriptor.source == CSV:
                files: Sequence[Union[str, CloudPathHandler]] = recursive_glob(self._source.location, f'*{file_name}')
            else:
                files = CloudConnector.glob(self._source.location, f'*{file_name}')
        except Exception as exception:
            raise CSVFileParsingError(f'Error during search for {file_name} in {self._source}') from exception
        if len(files) == 0:
            raise NoFileFoundError(f'{file_name} not found in {self._source}')
        if len(files) > 1:
            file_names = [Path(str(file)).name for file in files]
            raise CSVFileParsingError(f'Multiple files {file_names} found in {self._source}')
        return files[0]

    def _load(self, reference_id: str) -> list[list[str]]:  # type: ignore[override] # pylint: disable=arguments-differ
        search_id = self._make_search_id(reference_id)
        file_name = self._make_file_name(search_id)
        file: Union[str, CloudPathHandler] = self._get_file(file_name)
        return self._load_file(file)

    def _get_matrix(self, content: list[list[str]], object_id: str) -> dict[str, Any]:
        column_indexes = self._make_column_indexes(content)
        row_indexes = self._make_row_indexes(content)
        column_headers = [
            self._finalize_column_header(header) for header in column_indexes
        ]

        row_headers = [self._finalize_row_header(header) for header in row_indexes]
        matrix_items: list[dict[Any, Any]] = []
        for row, row_index in row_indexes.items():
            for column, column_index in column_indexes.items():
                try:
                    matrix_item: dict[Any, Any] = {MatrixKeys.RowHeader: self._finalize_row_header(row), MatrixKeys.ColumnHeader: self._finalize_column_header(column)}
                    value = content[row_index][column_index]
                    matrix_item[MatrixKeys.Point] = self._finalize_value(value)
                except Exception as exception:
                    raise CSVFileParsingError(f'Could not parse value at row: {row}, column: {column} to while generating {object_id} from {self}') from exception
                matrix_items.append(matrix_item)
        return {
            MatrixKeys.ColumnHeaders: column_headers,
            MatrixKeys.RowHeaders: row_headers,
            MatrixKeys.Content: matrix_items
        }

    def _make_row_indexes(self, content: list[list[str]]) -> OrderedDict[str, int]:
        raise NotImplementedError

    def _make_column_indexes(self, content: list[list[str]]) -> OrderedDict[str, int]:
        raise NotImplementedError

    @staticmethod
    def _finalize_column_header(header: str) -> Any:
        return header

    @staticmethod
    def _finalize_row_header(header: str) -> Any:
        return header

    @staticmethod
    def _finalize_value(value: str) -> float:
        raise NotImplementedError


class SwaptionVolatility(InterestRateVolatility):
    _signature = signatures.swaption_volatility.surface
    reference_id_pattern = '{CCY}{FREQUENCY}{LogNormal__or__Normal}Vol'
    _file_pattern = '_SWAPTION Volas {CCY} {Normal__or__NONE}.csv'
    _normal_distribution_identifier = 'Normal'

    def _make_column_indexes(self, content: list[list[str]]) -> OrderedDict[str, int]:
        indexes: OrderedDict[str, int] = OrderedDict()
        for index, swap_duration_raw in enumerate(content[self._header_row][1:]):
            if swap_duration_raw:
                swap_duration = swap_duration_raw.replace(' ', '') + 'Y'
                indexes[swap_duration] = index + 1
        return indexes

    def _make_row_indexes(self, content: list[list[str]]) -> OrderedDict[str, int]:
        indexes: OrderedDict[str, int] = OrderedDict()
        for index, row in enumerate(content[1:]):
            frequency = row[0].strip()
            indexes[frequency] = index + 1
        return indexes

    @staticmethod
    def _finalize_value(value: str) -> float:
        return float(value.replace(',', '.')) / 10000

    def _make_search_id(self, reference_id: str) -> str:
        currency, tenor, distribution = self._get_params_from_reference(reference_id)
        return self.reference_id_pattern.format(CCY=currency, FREQUENCY=tenor, LogNormal__or__Normal=distribution)


class CapFloorVolatility(InterestRateVolatility):
    _signature = signatures.cap_floor_surface
    reference_id_pattern = '{CCY}{FREQUENCY}Cap{LogNor__or__Nor}Vol'
    _file_pattern = '_CAP Volas {CCY} {Normal__or__NONE}.csv'
    _normal_distribution_identifier = 'Nor'
    _object_type_identifier = 'Cap'

    def get(self, reference_id: str) -> dict[str, Any]:
        data = super().get(reference_id)
        del data[fields.Tenor.key]
        distribution_shortened = data[fields.Distribution.key]
        data[fields.Distribution.key] = f'{distribution_shortened}mal'
        return data

    def _load(self, reference_id: str) -> list[list[str]]:  # type: ignore[override]
        raw_content = super()._load(reference_id)
        final_row: int = 0
        for row in raw_content:
            if not any(row):
                break
            final_row += 1
        return raw_content[:final_row]

    def _make_column_indexes(self, content: list[list[str]]) -> OrderedDict[str, int]:
        indexes: OrderedDict[str, int] = OrderedDict()
        for index, atm_strike_raw in enumerate(content[self._header_row]):
            if atm_strike_raw.endswith('%'):
                indexes[atm_strike_raw] = index
        return indexes

    def _make_row_indexes(self, content: list[list[str]]) -> OrderedDict[str, int]:
        indexes: OrderedDict[str, int] = OrderedDict()
        for index, row in enumerate(content[1:]):
            indexes[row[0].strip()] = index + 1
        return indexes

    def _finalize_row_header(self, header: str) -> str:  # type: ignore[override]
        if not header.endswith('Y'):
            try:
                years, months = header.split('Y')
                return str(12 * int(years) + int(months)) + 'M'
            except Exception as exception:
                raise CSVFileParsingError(f'Could parse row header {header} to duration in {self}') from exception
        return header

    def _finalize_column_header(self, header: str) -> float:  # type: ignore[override]
        return self._finalize_value(header)

    @staticmethod
    def _finalize_value(value: str) -> float:
        value = value.replace(',', '.')
        return float(value.replace('%', '')) / 100 if value.endswith('%') else float(value)

    def _make_search_id(self, reference_id: str) -> str:
        currency, tenor, distribution = self._get_params_from_reference(reference_id)
        return self.reference_id_pattern.format(CCY=currency, FREQUENCY=tenor, LogNor__or__Nor=distribution)


class FX(ParserCSVConstantContent):
    reference_id_pattern = '{BASE}/{QUOTE}'
    _csv_high_low_map: dict[str, str] = {}

    def __init__(self, source: Source, automatic_high_low: bool = False) -> None:
        super().__init__(source)
        self._automatic_high_low = automatic_high_low
        self._header_row: int = 0
        self._first_row: int = 1
        self._content_organized: dict[str, list[dict[str, Any]]] = defaultdict(list)

    def _load(self) -> None:
        super()._load()
        self._organize_content()

    @classmethod
    def _is_valid(cls, reference_id: str) -> bool:
        if '/' not in reference_id or not reference_id.isupper():
            return False
        base, quote_plus_high_low = reference_id.split('/', maxsplit=1)
        if len(base) != 3:
            return False
        if '_' in quote_plus_high_low:
            quote, high_low = quote_plus_high_low.split('_', maxsplit=1)
            return len(quote) == 3 and high_low in cls._csv_high_low_map
        return len(quote_plus_high_low) == 3

    def _make_search_id(self, reference_id: str) -> str:
        if '_' in reference_id:
            search_id, _ = reference_id.split('_', maxsplit=1)
        else:
            search_id = reference_id
        return search_id

    @staticmethod
    def _get_parts_from_valid(reference_id: str) -> tuple[str, ...]:
        if '_' in reference_id:
            fx_id, high_low = reference_id.split('_', maxsplit=1)
            base, quote = fx_id.split('/', maxsplit=1)
            return base, quote, high_low
        base, quote = reference_id.split('/', maxsplit=1)
        return base, quote

    def check_for(self, reference_id: str) -> bool:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        if not self._is_valid(reference_id):
            return False
        search_id = self._make_search_id(reference_id)
        if not self._content:
            self._load()
        if search_id not in self._content_organized:
            return False
        return True

    def _organize_content(self) -> None:
        raise NotImplementedError


class FXRateDirect(FX):
    _signature = signatures.fx_rate.direct
    _csv_high_low_map = {
        'BID': 'priceBid',
        'BID_LOW': 'priceBidLow',
        'ASK': 'priceAsk',
        'ASK_HIGH': 'priceAskHigh'
    }

    def __init__(self, source: Source, automatic_high_low: bool = True, high_low_intra_day: bool = True) -> None:
        super().__init__(source, automatic_high_low=automatic_high_low)
        self._high_low_intra = high_low_intra_day

    def _organize_content(self) -> None:
        if self._high_low_intra:
            if 'priceBidLow' not in self._header_indexes:
                Log.warning('BID_LOW/ASH_HIGH only available for calculated outrights (...fx_outrights_calc.csv)')
                self._high_low_intra = False
        for row in self._content[self._first_row:]:
            reference_id: str = row[self._header_indexes['referenceId']]
            content_line: dict[str, Any] = {
                'tenor': row[self._header_indexes['tenor']],
                'priceMid': row[self._header_indexes['priceMid']],
                'tradeDate': row[self._header_indexes['tradeDate']],
            }
            if self._high_low_intra:
                content_line['priceBidLow'] = row[self._header_indexes['priceBidLow']]
                content_line['priceAskHigh'] = row[self._header_indexes['priceAskHigh']]
            else:
                content_line['priceBid'] = row[self._header_indexes['priceBid']]
                content_line['priceAsk'] = row[self._header_indexes['priceAsk']]

            self._content_organized[reference_id].append(content_line)

    def check_for(self, reference_id: str) -> bool:
        if not super().check_for(reference_id):
            return False
        sub_content: list[dict[str, Any]] = self._content_organized[self._make_search_id(reference_id)]
        if sub_content[0]['tenor'] != 'SPOT':
            Log.error(f'Bad data for {reference_id}, no Spot value found')
            return False
        if len(sub_content) <= 1:
            Log.error(f'Bad data for {reference_id}, no Outright values found')
            return False
        return True

    def get(self, reference_id: str) -> dict[str, Any]:
        if not self.check_for(reference_id):
            raise CSVFileParsingError(f'Cannot provide {self._signature.type} {reference_id}')
        initialized: dict[str, Any] = self.initialize_data()
        id_parts: tuple[str, ...] = self._get_parts_from_valid(reference_id)
        base, quote = id_parts[0], id_parts[1]
        if len(id_parts) == 3:
            bid_ask: Optional[str] = id_parts[-1]
        else:
            bid_ask = None
        content: list[dict[str, Any]] = self._content_organized[f'{base}/{quote}']
        tenors, values, oldest_trade_date = self._get_values(reference_id, content, bid_ask=bid_ask)
        initialized[fields.TradeDate.key] = oldest_trade_date
        initialized[fields.BaseCurrency.key] = base
        initialized[fields.QuoteCurrency.key] = quote
        initialized[fields.Id.key] = reference_id
        initialized['tenors'] = tenors
        initialized[fields.Values.key] = values
        if bid_ask is None and self._automatic_high_low:
            id_bid = f'{self._signature.type}|{reference_id}_BID'
            id_ask = f'{self._signature.type}|{reference_id}_ASK'
            if self._high_low_intra:
                id_bid += '_LOW'
                id_ask += '_HIGH'
            initialized[fields.LowMarketData.key] = id_bid
            initialized[fields.HighMarketData.key] = id_ask
        return initialized

    @classmethod
    def _get_values(cls, reference_id: str, sub_content: list[dict[str, Any]], bid_ask: Optional[str]) -> tuple[list[str], list[float], datetime.date]:
        tenors: list[str] = []
        values: list[float] = []
        value_key: str = cls._csv_high_low_map.get(bid_ask, 'priceMid')  # type: ignore[arg-type]
        oldest_trade_date_raw: str = sub_content[0]['tradeDate']
        try:
            oldest_trade_date: datetime.date = datetime.date.fromisoformat(oldest_trade_date_raw)
        except ValueError as error:
            Log.error(f'{reference_id}: tradeDate: {oldest_trade_date_raw} is not iso formatted (YYYY-MM-DD)')
            raise CSVFileParsingError(f'Cannot provide {cls._signature.type} {reference_id}, trade dates could not be parsed') from error
        for index, content_line in enumerate(sub_content):
            tenor: str = content_line['tenor']
            trade_date: datetime.date = datetime.date.fromisoformat(content_line['tradeDate'])
            if trade_date < oldest_trade_date:
                oldest_trade_date = trade_date
            if tenor == 'ERROR':
                Log.warning(f'Bad tenor in {reference_id}, skipping item {index + 1}')
                continue
            value_raw: str = content_line[value_key]
            if not value_raw:
                Log.warning(f'Missing {value_key} value in {reference_id}, skipping item {index + 1}')
                continue
            tenors.append(tenor)
            values.append(float(value_raw.replace(',', '.')))
        if not values:
            raise CSVFileParsingError(f'Cannot provide {cls._signature.type} {reference_id}, no item could be parsed')
        return tenors, values, oldest_trade_date
