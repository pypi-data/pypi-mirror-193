from __future__ import annotations

import datetime
import json
import os
from typing import Any, Generator, Optional

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from daa_utils.daalogging import Log
from valuation.global_settings import __type_checking__
from valuation.olympia.input.exception import OlympiaImportError
from valuation.olympia.input.market_data_connection import get_parsers
from valuation.olympia.input.storage_conversion import InstrumentFinalization, OlympiaStorage, get_generators
from valuation.olympia.input.market_data_connection.olympia_market_data_hub_v2 import market_data_links
from valuation.universal_output import result_items
from valuation.universal_transfer import Reference, Storage, StorageDataBase

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Signature
    from valuation.olympia.input.config import Configuration
    from valuation.olympia.input.market_data_connection.source import SourceDescriptor, Source
    from valuation.olympia.input.market_data_connection.base_parser import Parser
    from valuation.olympia.input.storage_conversion.storage_generation import StorageGeneration
    from valuation.olympia.input.request import Request


class OlympiaDataBaseError(OlympiaImportError):
    pass


class ConfiguredStorageDataBase(StorageDataBase):

    @property
    def valuation_date(self) -> Optional[datetime.date]:
        return self._valuation_date

    @valuation_date.setter
    def valuation_date(self, valuation_date: datetime.date) -> None:
        if self._is_locked:
            raise OlympiaDataBaseError(
                'Valuation date can not be set after default parameters have been provided to the QLObjectDB')
        self._valuation_date = valuation_date

    def __init__(self, configuration: Configuration, log_fails: bool = False, shorten_prints: bool = False) -> None:
        super().__init__()
        self._default_params: Optional[str] = configuration.default_parameters
        self._sources: dict[str, list[Source]] = configuration.sources
        if not self._sources:
            Log.warning('Configuration provided no sources for market data loading')
        self._parsers: dict[SourceDescriptor, type[Parser]] = get_parsers()
        self._storage_generators: dict[str, list[StorageGeneration]] = get_generators()
        self._valuation_date = None  # type: ignore[assignment]
        self._is_locked: bool = False
        self._log_fails: bool = log_fails
        self._shorten_prints: bool = shorten_prints
        self._initialized_parsers: dict[SourceDescriptor, Parser] = {}

    def __getitem__(self, reference: Reference) -> Storage:
        if reference in self:
            return self._data[reference]
        if reference == global_parameters.DefaultParametersReference:
            return self._get_default_params()
        object_type, reference_id = reference.type, reference.id
        storage_from_generator: Optional[Storage] = self._get_generated_storage(object_type, reference_id)
        if storage_from_generator is not None:
            return storage_from_generator
        storage_from_parser: Optional[Storage] = self._get_parsed_object(reference)
        if storage_from_parser is not None:
            return storage_from_parser
        raise OlympiaDataBaseError(f'Could not provide {reference}')

    def _get_default_params(self) -> Storage:
        if self.valuation_date is None:
            raise OlympiaDataBaseError('No valuation date given')
        if self._default_params is None:
            Log.warning('Configuration did not provide default parameters')
            storage = Storage()
            storage[fields.ValuationDate] = self.valuation_date
            storage.assign_reference(global_parameters.DefaultParametersReference)
            storage.make_immutable()
            self.add(storage)
            self._is_locked = True
            return storage
        if not os.path.exists(self._default_params):
            raise OlympiaDataBaseError(
                'Path to default parameters provided by Configuration does not exist: ' + self._default_params)
        with open(self._default_params, mode='r') as json_handle:
            storage = OlympiaStorage(json.load(json_handle))
        storage.assign_reference(global_parameters.DefaultParametersReference)
        storage[fields.ValuationDate] = self.valuation_date
        storage.make_immutable()
        self.add(storage)
        self._is_locked = True
        return storage

    def _get_generated_storage(self, object_type: str, reference_id: str) -> Optional[Storage]:
        if object_type in self._storage_generators:
            candidates = self._storage_generators[object_type]
            for candidate in candidates:
                if candidate.check_for(reference_id):
                    Log.info(f'{reference_id}\t->\t{candidate}')
                    storage = candidate.get(reference_id)
                    storage.make_immutable()
                    self.add(storage)
                    return storage
                if self._log_fails:
                    Log.warning(f'{reference_id}\t!\t{candidate}')
                    continue
        return None

    def _make_storage_from_parsed(self, parsed_content: dict[str, Any]) -> Storage:
        storage = OlympiaStorage(parsed_content, shorten_print=self._shorten_prints)
        storage.make_immutable()
        return storage

    def _get_parsed_object(self, reference: Reference) -> Optional[Storage]:
        assert self._valuation_date is not None, 'Valuation date not set'
        if not self._sources:
            Log.info('No sources provided')
            return None
        for source in self._sources.get(reference.type, []):
            if isinstance(reference,
                          market_data_links.OlympiaMarketDataHubReference):  # todo: change when all references are switched to uri
                if source.descriptor.signature.sub_type != reference.sub_type:
                    continue
            if source.descriptor not in self._initialized_parsers:
                source.resolve(self.valuation_date)  # type: ignore[arg-type]
                if not source.exists:
                    Log.warning(str(source))
                    continue
                new_parser = self._parsers[source.descriptor]
                new_parser_initialized = new_parser(source)
                self._initialized_parsers[source.descriptor] = new_parser_initialized

            initialized_parser = self._initialized_parsers[source.descriptor]
            if initialized_parser.check_for(reference.id):
                Log.info(f'{reference}\t->\t{initialized_parser}')
                storage = self._make_storage_from_parsed(initialized_parser.get(reference.id))
                self.add(storage)
                return storage
            if self._log_fails:
                Log.warning(f'{reference}\t!\t{initialized_parser}')
        if self._log_fails:
            Log.warning(f'No source found in configuration file for object type {reference.type}')
        return None


class RequestDataBase(ConfiguredStorageDataBase):
    _fall_back_valuation_type: Signature = signatures.valuation.analytic_quantlib
    _fall_back_result_types: list[str] = [result_items.Info, result_items.PV, result_items.CashFlows]

    def __init__(self, configuration: Configuration, log_fails: bool = False, shorten_prints: bool = False) -> None:
        super().__init__(configuration, log_fails=log_fails, shorten_prints=shorten_prints)
        self._default_valuations: Optional[dict[str, list[str]]] = self._set_default(configuration.valuations,
                                                                                     'ValuationTypes')
        self._default_result_types: Optional[dict[str, list[str]]] = self._set_default(configuration.result_types,
                                                                                       'ResultTypes')

    def add_request(self, request: Request) -> None:
        self._set_valuation_date(request.valuation_date)

        for valuation_raw in request.valuations():
            self._make_storage_and_add(valuation_raw)
        for instrument_data in request.instruments():
            self._make_instrument_storage_and_add(instrument_data)
        for market_data_raw in request.market_data():
            self._make_storage_and_add(market_data_raw)

        self._load_instrument_reference(request.instrument_references())

    def __getitem__(self, reference: Reference) -> Storage:
        if reference in self:
            return self._data[reference]
        if reference == global_parameters.DefaultParametersReference:
            return self._get_default_params()
        if (pulled_storage := self._pull_data(reference)) is not None:
            return pulled_storage
        raise OlympiaDataBaseError(f'Could not provide {reference}')

    def _set_default(self, path: Optional[str], id_for_log: str) -> Optional[dict[str, list[str]]]:
        if path is None:
            if self._log_fails:
                Log.warning(f'Configuration provided no {id_for_log}')
            return None
        if not os.path.exists(path):
            Log.error(f'Path for {id_for_log} provided by configuration does not exist')
            return None
        with open(path, mode='r') as handle:
            content: dict[str, list[str]] = json.load(handle)
        return content

    def get_generated_storage(self, reference: Reference) -> Optional[Storage]:
        if reference.type in self._storage_generators:
            candidates = self._storage_generators[reference.type]
            for candidate in candidates:
                if candidate.check_for(reference.id):
                    Log.info(f'{reference.id}\t->\t{candidate}')
                    storage = candidate.get(reference.id)
                    storage.make_immutable()
                    return storage
                if self._log_fails:
                    Log.warning(f'{reference.id}\t!\t{candidate}')
                    continue
        return None

    def get_parsed_object(self, reference: Reference) -> Optional[dict[str, Any]]:
        assert self._valuation_date is not None, 'Valuation date not set'
        object_type, reference_id = reference.type, reference.id
        if not self._sources:
            Log.info('No sources provided')
            return None
        for source in self._sources.get(object_type, []):
            if isinstance(reference, market_data_links.OlympiaMarketDataHubReference):  # todo: change when all references are switched to uri
                if source.descriptor.signature.sub_type != reference.sub_type:
                    continue
            if source.descriptor not in self._initialized_parsers:
                source.resolve(self.valuation_date)  # type: ignore[arg-type]
                if not source.exists:
                    Log.warning(str(source))
                    continue
                new_parser = self._parsers[source.descriptor]
                new_parser_initialized = new_parser(source)
                self._initialized_parsers[source.descriptor] = new_parser_initialized

            initialized_parser = self._initialized_parsers[source.descriptor]
            if initialized_parser.check_for(reference_id):
                Log.info(f'{reference}\t->\t{initialized_parser}')
                raw_data: dict[str, Any] = initialized_parser.get(reference_id)
                return raw_data
            if self._log_fails:
                Log.warning(f'{reference}\t!\t{initialized_parser}')
        if self._log_fails:
            Log.warning(f'No source found in configuration file for object type {object_type}')
        return None

    def _pull_data(self, reference: Reference) -> Optional[Storage]:
        storage_from_generator: Optional[Storage] = self.get_generated_storage(reference)
        if storage_from_generator is not None:
            self.add(storage_from_generator)
            return storage_from_generator
        data_from_parser: Optional[dict[str, Any]] = self.get_parsed_object(reference)
        if data_from_parser is None:
            return None
        if reference.type == 'Instrument':
            storage = self._make_instrument_storage_and_add(data_from_parser)
        else:
            storage = self._make_storage_and_add(data_from_parser)
        return storage

    def _set_valuation_date(self, valuation_date: datetime.date) -> None:
        if self.valuation_date is None:
            self.valuation_date = valuation_date
            Log.info(f'Valuation date set to {valuation_date}')
        elif valuation_date != self.valuation_date:
            raise OlympiaDataBaseError(f'Cannot overwrite {self.valuation_date} with {valuation_date}')

    def _make_instrument(self, instrument: Reference, instrument_type: str, instrument_data: dict[str, Any]) -> Storage:
        storage = OlympiaStorage(instrument_data, shorten_print=self._shorten_prints)
        storage.assign_reference(instrument)
        storage[fields.SubType('Instrument')] = instrument_type
        converted = InstrumentFinalization.convert(storage)
        converted.make_immutable()
        return converted

    def _make_market_data(self, market_data_raw: dict[str, Any]) -> Storage:
        storage = OlympiaStorage(market_data_raw, shorten_print=self._shorten_prints)
        storage.make_immutable()
        return storage

    def _make_valuations(self, instrument: Reference, instrument_type: str,
                         valuations: Optional[list[dict[str, Any]]] = None) -> Generator[Storage, None, None]:
        if instrument_type == signatures.instrument.flexible_montecarlo.sub_type:
            valuation = {
                fields.SubType('Valuation').key: 'FinancialProgram',
                fields.ResultTypes.key: (result_items.Info, result_items.PV)
            }
            yield self._make_valuation_storage(instrument.id, valuation)
            return
        if valuations is None:
            final_valuations: list[dict[str, Any]] = []
            if self._default_valuations is None:
                Log.error(
                    f'No ValuationTypes provided by config or request, falling back to (possibly incompatible) {self._fall_back_valuation_type}')
                final_valuations.append({fields.SubType('Valuation').key: self._fall_back_valuation_type.sub_type})
            elif instrument_type not in self._default_valuations:
                Log.error(
                    f'{instrument_type} not found in ValuationTypes provided by config, falling back to (possibly incompatible) {self._fall_back_valuation_type}')
                final_valuations.append({fields.SubType('Valuation').key: self._fall_back_valuation_type.sub_type})
            else:
                final_valuations = [{fields.SubType('Valuation').key: valuation_type} for valuation_type in
                                    self._default_valuations[instrument_type]]
            if self._default_result_types is None:
                Log.error(
                    f'No ResultTypes provided by config or request, falling back to (possibly incompatible) {self._fall_back_result_types}')
                result_types = self._fall_back_result_types
            elif instrument_type not in self._default_result_types:
                Log.error(
                    f'{instrument_type} not found in ResultTypes provided by config, falling back to (possibly incompatible) {self._fall_back_result_types}')
                result_types = self._fall_back_result_types
            else:
                result_types = self._default_result_types[instrument_type]
            for valuation in final_valuations:
                valuation[fields.ResultTypes.key] = result_types
        else:
            final_valuations = valuations
            for valuation in final_valuations:
                for key in (fields.Id.key, fields.Type.key):
                    if key in valuation:
                        del valuation[key]
        for valuation in final_valuations:
            yield self._make_valuation_storage(instrument.id, valuation)

    @staticmethod
    def _make_valuation_storage(instrument_id: str, valuation_data: dict[str, Any]) -> Storage:
        storage = OlympiaStorage(valuation_data)
        sub_type = storage[fields.SubType('Valuation')]
        storage[fields.Type] = 'Valuation'
        storage[fields.Id] = f'{instrument_id}#{sub_type}'
        storage[fields.Instrument] = Reference('Instrument', instrument_id)
        storage.make_immutable()
        return storage

    @staticmethod
    def _create_instrument_storage(instrument_data: dict[str, Any], shorten_prints: bool = False) -> Storage:
        storage = OlympiaStorage(instrument_data, shorten_print=shorten_prints)
        instrument_reference = Reference('Instrument', storage[fields.Id])  # type: ignore[arg-type]
        instrument_sub_type: str = storage[fields.Type]  # type: ignore[assignment]
        storage.assign_reference(instrument_reference)
        storage[fields.SubType('Instrument')] = instrument_sub_type
        converted = InstrumentFinalization.convert(storage)
        converted.make_immutable()
        return converted

    def _load_instrument_reference(self, instrument_references: list[str]) -> None:
        if not instrument_references:
            return
        for instrument_reference in instrument_references:
            try:
                reference = Reference('Instrument', instrument_reference)
                _ = self[reference]
            except OlympiaDataBaseError as error:
                Log.critical(str(error))

    @staticmethod
    def _create_valuation_storage(instrument_id: str, valuation_sub_type: str, result_types: list[str]) -> Storage:
        storage = Storage()
        storage[fields.Type] = 'Valuation'
        storage[fields.SubType('Valuation')] = valuation_sub_type
        storage[fields.ResultTypes] = tuple(result_types)
        storage[fields.Id] = f'{instrument_id}#{valuation_sub_type}'
        storage[fields.Instrument] = Reference('Instrument', instrument_id)
        storage.make_immutable()
        return storage

    def _make_storage_and_add(self, raw_data: dict[str, Any]) -> Optional[Storage]:
        try:
            object_data_id, object_data_type = raw_data[fields.Id.key], raw_data[fields.Type.key]
        except KeyError:
            Log.error('Cannot add data; id and type not found')
            return None
        try:
            storage = OlympiaStorage(raw_data, shorten_print=self._shorten_prints)
            storage.make_immutable()
            self.add(storage)
            return storage
        except Exception as exception:  # pylint: disable=broad-except
            if os.getenv('QL_DEBUGMODE') == '1':
                raise exception
            Log.error(f'Cannot add {Reference(object_data_type, object_data_id)} because of {exception}')
        return None

    def _make_instrument_storage_and_add(self, instrument_data: dict[str, Any]) -> Optional[Storage]:
        instrument_id: str = instrument_data['id']
        instrument_reference: Reference = Reference('Instrument', instrument_id)
        try:
            instrument = self._create_instrument_storage(instrument_data, self._shorten_prints)
            self.add(instrument)
            if not self._has_valuation(instrument):
                self._create_default_valuation(instrument)
            return instrument
        except Exception as exception:  # pylint: disable=broad-except
            Log.critical(f'Cannot add {instrument_reference} because of {exception}')
            self._initiation_errors.append((instrument_reference, str(exception)))
            return None

    def _has_valuation(self, instrument: Storage) -> bool:
        reference: Reference = instrument.reference
        for valuation_ref in self.valuations:
            valuation: Storage = self[valuation_ref]
            if fields.Instrument in valuation and valuation[fields.Instrument] == reference:
                return True
        return False

    def _create_default_valuation(self, instrument: Storage) -> None:
        instrument_type: str = instrument[fields.SubType('Instrument')]  # type: ignore[assignment]
        instrument_id: str = instrument[fields.Id]  # type: ignore[assignment]
        valuations_types: list[str] = self._default_valuations.get(instrument_type, [])
        result_types: list[str] = self._default_result_types.get(instrument_type, [])

        if not valuations_types or not result_types:
            Log.info(f'Instrument Type {instrument_type} has no default result types and/or valuations type.'
                     f'No valuations object was created.')
            return

        for valuation_type in valuations_types:
            self.add(self._create_valuation_storage(instrument_id, valuation_type, result_types))
