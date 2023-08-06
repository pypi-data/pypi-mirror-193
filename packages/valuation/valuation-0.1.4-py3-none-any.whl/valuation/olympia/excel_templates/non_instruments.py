from __future__ import annotations

import os
from collections import defaultdict
from typing import Optional, Union

from daa_utils import Log
from daa_utils.excel_io import ExcelIO, SimpleData, StorageData, StorageSheet, TableData, TableSheet

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.olympia.excel_templates.template_generation_base import ExcelField, ExcelFieldSubStorage, QLObjectDocumentationExcel, REVERSED_FIELDS, data_standard2table, get_objects, set_field_style
from valuation.olympia.input.mappings.request_keys import ExcelRequestParams, Keys
from valuation.olympia.input.market_data_connection import get_parsers
from valuation.olympia.input.market_data_connection.file_system_csv.parser import DiscountFactors
from valuation.olympia.input.storage_conversion.storage_generation import HullWhiteCalibrationGeneration, StorageGeneration, SwaptionSurfaceProcessGeneration, get_generators
from valuation.engine.market_data import QLMarketData
from valuation.engine.valuation import QLValuation
from valuation.universal_transfer import TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObject
    from valuation.universal_transfer import Signature
    from valuation.engine.process import QLProcess
    from valuation.olympia.input.market_data_connection.base_parser import Parser


DEFAULT_STRUCTURED = 'default'


def write_structured_one_object(documentation: QLObjectDocumentationExcel, with_types: bool, unique_id_count: int, ignore_rho: bool) -> StorageData:
    object_type = documentation.signature.type
    object_id = f'ID_{object_type}_{unique_id_count}'
    sub_type: Optional[str] = documentation.signature.sub_type or None
    data = StorageData(object_type, object_id)
    if sub_type:
        data[ExcelField(fields.SubType(object_type), False, with_types, allow_fall_back=False).key] = sub_type
    for field in sorted(documentation.data_standard):
        if 'rho' in field.key and ignore_rho:
            continue
        if field.defaults:
            data[field.key] = DEFAULT_STRUCTURED
        elif object_type == 'Valuation' and 'instrument' in field.key.lower():
            data[ExcelField(TypeKey(types.Str, Keys.InstrumentType), False, with_types, allow_fall_back=False).key] = ''
        else:
            data[field.key] = ''
    if documentation.data_sub_storage:
        sub_storage_types: list[str] = [_type for _type, _ in documentation.types_sub_storage]
        sigs: list[str] = [sig for _, sig in documentation.types_sub_storage]
        assert len(set(sub_storage_types)) == 1, 'More than one (O) currently not supported in non-instrument excel templates'
        sub_storage_key = ExcelField(TypeKey(types.SubStorages, sub_storage_types[0]), False, with_types, allow_fall_back=False).key
        signature_key = ExcelField(fields.Type, False, with_types, allow_fall_back=False).key
        simple_data = SimpleData(sub_storage_key)
        for signature in sigs:
            simple_data.append({signature_key: signature})
        set_field_style(simple_data, signature_key, True)
        simple_data = data_standard2table(simple_data, documentation.data_sub_storage)
        data[simple_data.key] = simple_data
    return data


def write_structured(ql_objects: list[type[QLObject]], sheet_name: str, with_types: bool, ignore_rho: bool = True) -> StorageSheet:
    sheet = StorageSheet(sheet_name)
    for count, ql_object in enumerate(ql_objects):
        ql_object_documentation = QLObjectDocumentationExcel(ql_object, with_types)
        storage_data = write_structured_one_object(ql_object_documentation, with_types, count + 1, ignore_rho)
        sheet.append(storage_data)
    return sheet


def add_sub_type_to_field(data2update: list[ExcelFieldSubStorage], object_sub_type: str, new_field: ExcelFieldSubStorage) -> None:
    # Currently, if at least one object per shared field has no default value, the column will be marked as required
    # This also works only with objects that have a subtype
    if new_field in data2update:
        old_item = data2update.pop(data2update.index(new_field))
        if old_item.defaults == new_field.defaults:
            old_item.add_sub_type(object_sub_type)
            data2update.append(old_item)
    else:
        new_field.add_sub_type(object_sub_type)
        data2update.append(new_field)


def write_simple(ql_objects: list[type[QLObject]], sheet_name: str, with_types: bool) -> TableSheet:
    fields_with_reference: list[ExcelFieldSubStorage] = []
    id_field = ExcelField(fields.Id, False, with_types)
    type_field = ExcelField(fields.Type, False, with_types)
    sub_type_field = ExcelField(fields.SubType(''), False, with_types)
    table = TableData()
    for ql_object in ql_objects:
        ql_object_documentation = QLObjectDocumentationExcel(ql_object, with_types)
        object_type = ql_object_documentation.signature.type
        sub_type = ql_object_documentation.signature.sub_type
        table.add_data_line({id_field.key: None, type_field.key: object_type, sub_type_field.key: sub_type})
        date_line: list[ExcelField] = ql_object_documentation.data_standard
        new_fields = [ExcelFieldSubStorage(field.type_key, field.defaults, with_types) for field in date_line]
        for new_field in new_fields:
            add_sub_type_to_field(fields_with_reference, sub_type, new_field)
    number_of_sub_types = len(ql_objects)
    for item in fields_with_reference:
        if len(item.sub_storage_types) == number_of_sub_types:
            item.sub_storage_types = {'All'}
    data_standard2table(table, fields_with_reference)
    set_field_style(table, id_field.key, True)
    set_field_style(table, type_field.key, True)
    set_field_style(table, sub_type_field.key, True)
    sheet = TableSheet(sheet_name)
    sheet.set_single(table)
    return sheet


class NonInstrumentDocumentationFactory:
    _process_exceptions = [signatures.process.basket,
                           signatures.process.uncorrelated_basket,
                           signatures.process.cms,
                           signatures.process.cms_spread,
                           signatures.process.base]  # need basket soon
    _market_data_exceptions = [signatures.index_and_cms, signatures.index_and_cms_spread]

    @property
    def p_market_data(self) -> list[Union[StorageGeneration, type[Parser]]]:
        return self._predefined_market_data

    @property
    def p_processes(self) -> list[Union[StorageGeneration, type[Parser]]]:
        return self._predefined_process

    @property
    def market_data(self) -> list[type[QLMarketData]]:
        return self._market_data

    @property
    def processes(self) -> list[type[QLProcess]]:
        return self._processes

    @property
    def valuations(self) -> list[type[QLValuation]]:
        return self._valuations

    def __init__(self) -> None:
        self._predefined_market_data: list[Union[StorageGeneration, type[Parser]]] = []
        self._predefined_process: list[Union[StorageGeneration, type[Parser]]] = []
        self._valuations: list[type[QLValuation]] = get_objects(QLValuation)  # type: ignore[assignment]
        self._market_data: list[type[QLMarketData]] = []
        self._processes: list[type[QLProcess]] = []
        self._generators: dict[Signature, list[Union[StorageGeneration, type[Parser]]]] = self._initialize_generators_and_parsers()
        self._initialize_objects()

    @staticmethod
    def _initialize_generators_and_parsers() -> dict[Signature, list[Union[StorageGeneration, type[Parser]]]]:
        combined: dict[Signature, list[Union[StorageGeneration, type[Parser]]]] = defaultdict(list)
        parsers = get_parsers()
        generators = get_generators()
        for descriptor, parser in parsers.items():
            combined[descriptor.signature].append(parser)
        for _, generators_per_object in generators.items():
            for generator in generators_per_object:
                combined[generator.signature].append(generator)
        return combined

    def _initialize_objects(self) -> None:
        all_ql_objects = get_objects(QLMarketData, exceptions=self._process_exceptions + self._market_data_exceptions)
        for ql_object in all_ql_objects:
            if ql_object.object_type == 'Process':
                if ql_object.signature in self._generators:
                    self._predefined_process.extend(self._generators[ql_object.signature])
                self._processes.append(ql_object)  # type: ignore[arg-type]
            else:
                if ql_object.signature in self._generators:
                    self._predefined_market_data.extend(self._generators[ql_object.signature])
                self._market_data.append(ql_object)  # type: ignore[arg-type]


def write_predefined(out_dir: str, market_data_generators: list[Union[StorageGeneration, type[Parser]]], process_generators: list[Union[StorageGeneration, type[Parser]]]) -> None:
    try:
        discount = str(TypeKey(types.Reference, REVERSED_FIELDS[fields.DiscountCurve]))
        pattern_discount = DiscountFactors.reference_id_pattern
        replaced_pattern_discount = pattern_discount.format(CCY='EUR', TENOR='6M')
        process = fields.StochasticProcess
        swaption_vol_pattern = SwaptionSurfaceProcessGeneration.reference_id_pattern
        replaced_swaption_vol_pattern = swaption_vol_pattern.format(CCY='EUR', FREQUENCY='6M', LogNormal__or__Normal='Normal')
        pattern_hull_white = HullWhiteCalibrationGeneration.reference_id_pattern
        replaced_pattern_hull_white = pattern_hull_white.format(INSTRUMENT_ID='MyCallableBond', SWAPTION_VOLATILITY_ID=replaced_swaption_vol_pattern)
        help_message = """Fill in for pointers (r) to market data or stochastic process
        Examples:
        Standard discounting with EUR6M:
        {discount} -> Underlying object: YieldCurve[Discount] -> Pattern: {pattern_discount} -> template entry -> {replaced_pattern_discount}
        SwaptionVolatility for EUR CMS leg:
        {process} -> Underlying object: Process[SwaptionVolatility] -> pattern {swaption_vol_pattern} -> template entry -> {replaced_swaption_vol_pattern}
        Stochastic process of type HullWhiteCalibration for a EUR callable bond with {id} MyCallableBond:
        {process} -> Underlying object: Process[HullWhiteCalibration] -> pattern: {pattern_hull_white} -> template entry -> {replaced_pattern_hull_white}""".format(
            discount=discount,
            pattern_discount=pattern_discount,
            replaced_pattern_discount=replaced_pattern_discount,
            process=process,
            swaption_vol_pattern=swaption_vol_pattern,
            replaced_swaption_vol_pattern=replaced_swaption_vol_pattern,
            pattern_hull_white=pattern_hull_white,
            replaced_pattern_hull_white=replaced_pattern_hull_white,
            id=Keys.InstrumentId
        )
    except Exception as exception:  # pylint: disable=broad-except
        Log.error('Cannot write help message because of:')
        Log.error(str(exception))
        help_message = ''
    market_data = []
    processes = []
    previous_sources = ''
    previous_signature: Optional[Signature] = None
    for generator in market_data_generators:
        if isinstance(generator, StorageGeneration):
            market_data.append(f'Generator\t->\t{generator.signature}\t->\tPattern: {generator.reference_id_pattern}')
        else:
            sources = ', '.join(descriptor.source for descriptor in generator.source_descriptors)
            signature = generator.source_descriptors[0].signature
            if sources != previous_sources or signature != previous_signature:
                pattern = generator.reference_id_pattern
                market_data.append(f'Parser({sources})\t->\t{signature}\t->\tPattern: {pattern}')
                previous_sources = sources
                previous_signature = signature
    previous_sources = ''
    previous_signature = None
    for generator in process_generators:
        if isinstance(generator, StorageGeneration):
            processes.append(f'Generator\t->\t{generator.signature}\t->\tPattern: {generator.reference_id_pattern}')
        else:
            sources = ', '.join(descriptor.source for descriptor in generator.source_descriptors)
            signature = generator.source_descriptors[0].signature
            if sources != previous_sources or signature != previous_signature:
                pattern = generator.reference_id_pattern
                processes.append(f'Parser({sources})\t->\t{signature}\t->\tPattern: {pattern}')
                previous_sources = sources
                previous_signature = signature
    final_str = '\n'.join([help_message] + ['Market data:\n'] + sorted(market_data) + ['\nstochasticProcess:\n'] + sorted(processes))
    with open(os.path.join(out_dir, 'Automatic.txt'), mode='w') as handle:
        handle.write(final_str)


def write_non_instrument(out_dir: str, extension: str = 'xlsx', with_types: bool = True) -> None:
    factory = NonInstrumentDocumentationFactory()
    market_data_sheet_name = ExcelRequestParams.MarketDataSheet
    process_sheet_name = ExcelRequestParams.ProcessSheet
    valuations_sheet_name = ExcelRequestParams.ValuationSheet
    valuations_sheet = write_structured(factory.valuations, valuations_sheet_name, with_types, ignore_rho=False)  # type: ignore[arg-type]
    market_data_sheet = write_structured(factory.market_data, market_data_sheet_name, with_types)  # type: ignore[arg-type]
    process_sheet = write_simple(factory.processes, process_sheet_name, with_types)  # type: ignore[arg-type]

    writer = ExcelIO(lean=False, log_io=False)
    writer[process_sheet.name] = process_sheet
    writer[market_data_sheet.name] = market_data_sheet
    writer[valuations_sheet.name] = valuations_sheet
    out_path = os.path.join(out_dir, f'templates.{extension}')
    if extension == 'xlsx':
        writer.to_excel(out_path)
    else:
        for sheet_name in writer.sheet_names:
            writer.to_csv(out_path, sheet_name)
    write_predefined(out_dir, factory.p_market_data, factory.p_processes)
