from __future__ import annotations

import os
from collections import OrderedDict, defaultdict
from configparser import ConfigParser
from pathlib import Path
from typing import Optional, Any

from daa_utils.daalogging import Log
from valuation.global_settings import __type_checking__
from valuation.olympia import secrets_manager
from valuation.olympia.input import defaults
from valuation.olympia.input.exception import OlympiaImportError
from valuation.olympia.input.market_data_connection.base_parser import get_parsers
from valuation.olympia.input.market_data_connection.source import CLOUD_SOURCES, CloudSource, LOCAL_SOURCES, LocalSource, OLYMPIA, \
    SOURCES, hide_path, OLYMPIA_STATIC, OLYMPIA_V2, \
    OlympiaMarketSource, OlympiaStaticSource
from valuation.universal_transfer import Signature

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.olympia.input.market_data_connection.source import Source


class OlympiaConfigurationError(OlympiaImportError):
    pass


config_folder = os.environ['CONFIG_NAME']
DEFAULT_OLYMPIA_CONFIG: str = os.path.join(defaults.__path__[0], 'olympia_configs', config_folder)

VALUATION_DEFAULTS = 'VALUATION CONFIGURATION'
BASE_PATHS = 'BASE PATHS'
SECRET_PATHS = 'SECRET PATHS'
SECRETS = 'SECRETS'

SECTIONS = (BASE_PATHS, VALUATION_DEFAULTS, SECRET_PATHS, SECRETS) + tuple((source.upper() for source in SOURCES))

DEFAULT_PARAMETERS = 'DefaultParameters'
VALUATIONS = 'Valuations'
RESULT_TYPES = 'ResultTypes'

SOURCE_BASE = 'Sources'
DEFAULT_BASE = 'Defaults'

DUMMY_IGNORE = 'dummy'

OLYMPIA_BASE_URL = 'base_url*'
OLYMPIA_USER = 'user_name*'
OLYMPIA_MODE = 'api_mode*'


class TestEnv:
    no_test: bool = True
    sources_base_path: Optional[str] = None
    defaults_base_path: Optional[str] = None

    @classmethod
    def _set_no_test(cls, no_test: bool) -> None:
        cls.no_test = no_test

    @classmethod
    def _set_sources_base_path(cls, defaults_base_path: Optional[str]) -> None:
        cls.sources_base_path = defaults_base_path

    @classmethod
    def _set_defaults_base_path(cls, defaults_base_path: Optional[str]) -> None:
        cls.defaults_base_path = defaults_base_path

    def __init__(self, sources_base_path: Optional[str] = None,
                 defaults_base_path: Optional[str] = None):
        self._set_sources_base_path(sources_base_path)
        self._set_defaults_base_path(defaults_base_path)

    def __enter__(self) -> None:
        self._set_no_test(False)

    def __exit__(self, exc_type: Any, exc_value: Any, exc_tb: Any) -> None:
        self._set_no_test(True)
        self._set_sources_base_path(None)
        self._set_defaults_base_path(None)


def get_source_path(path: str, base_path: Optional[str] = None) -> str:
    path = path.replace('\\', '/')
    if base_path is not None:
        base_path = base_path.replace('\\', '/')
    source_path = Path(path)
    if base_path is not None:
        return str(Path(base_path) / source_path)
    return str(source_path)


def get_section_item_pair(key: str, value: Optional[str]) -> tuple[str, Optional[str]]:
    if not value or value.lower() == DUMMY_IGNORE:
        return key, None
    return key, value


class Configuration:

    @property
    def default_parameters(self) -> Optional[str]:
        return self._default_parameters

    @property
    def valuations(self) -> Optional[str]:
        return self._valuations

    @property
    def result_types(self) -> Optional[str]:
        return self._result_types

    @property
    def sources(self) -> dict[str, list[Source]]:
        return self._sources

    @property
    def config_path(self) -> Optional[str]:
        return self._config_path

    def __init__(self, config_file: Optional[str] = None, ) -> None:
        no_test: bool = TestEnv.no_test
        defaults_base_path: Optional[str] = TestEnv.defaults_base_path
        sources_base_path: Optional[str] = TestEnv.sources_base_path
        config_path: str = str(Path(__file__).parent / 'defaults' / 'olympia_configs' / config_file)

        if config_path is None or not os.path.exists(Path(config_path)):
            config_path = os.getenv('DAA_VALUATION_CONFIG')
        if config_path is None:
            raise OlympiaConfigurationError(
                'No path to configuration file given. Use parameter config_path or set env variable DAA_VALUATION_CONFIG')
        if not os.path.exists(Path(config_path)):
            raise OlympiaConfigurationError(f'Config path {config_path} does not exist')
        if sources_base_path is not None and not os.path.exists(sources_base_path):
            raise OlympiaConfigurationError(f'Source base path {sources_base_path} does not exist')
        if defaults_base_path is not None and not os.path.exists(defaults_base_path):
            raise OlympiaConfigurationError(f'Default base path {defaults_base_path} does not exist')
        self._config_path = config_path
        self._sources_base_path = sources_base_path
        self._defaults_base_path = defaults_base_path
        self._config_parser = ConfigParser(allow_no_value=True, dict_type=OrderedDict)
        self._config_parser.optionxform = str  # type: ignore[assignment]
        try:
            self._config_parser.read(Path(config_path))
        except Exception as exception:
            raise OlympiaConfigurationError(f'Cannot read config from path {config_path}') from exception

        self._default_parameters: Optional[str] = None
        self._valuations: Optional[str] = None
        self._result_types: Optional[str] = None
        self._sources: dict[str, list[Source]] = defaultdict(list)
        self._no_test = no_test

        self._read_base_paths()
        self._read_default_params()
        self._read_secrets()
        self._read_sources()

    def __str__(self) -> str:
        lines: list[str] = [f'Configuration[{self._config_path if self._no_test else hide_path(self._config_path)}]',
                            f'\t{BASE_PATHS}',
                            f'\t\t{DEFAULT_BASE}\t{self._print_non_source_file(str(self._defaults_base_path))}',
                            f'\t\t{SOURCE_BASE}\t{self._print_non_source_file(str(self._sources_base_path))}',
                            f'\t{VALUATION_DEFAULTS}',
                            f'\t\t{DEFAULT_PARAMETERS}\t{self._print_non_source_file(str(self._default_parameters))}',
                            f'\t\t{VALUATIONS}\t{self._print_non_source_file(str(self._valuations))}',
                            f'\t\t{RESULT_TYPES}\t{self._print_non_source_file(str(self._result_types))}', '\tSOURCES']

        if self._sources:
            for object_type in self._sources:
                sources = self._sources[object_type]
                for source in sources:
                    lines.append(f'\t\t{object_type}\t{source}')
        else:
            lines.append('\t\tNone')
        return '\n'.join(lines)

    def _read_default_params(self) -> None:
        config_dir: str = defaults.__path__[0]
        self._default_parameters = os.path.join(config_dir, f'{DEFAULT_PARAMETERS}.json')
        self._valuations = os.path.join(config_dir, f'{VALUATIONS}.json')
        self._result_types = os.path.join(config_dir, f'{RESULT_TYPES}.json')
        if VALUATION_DEFAULTS not in self._config_parser.sections():
            return

    def _read_base_paths(self) -> None:
        if BASE_PATHS not in self._config_parser.sections():
            return
        section = self._config_parser[BASE_PATHS]
        for key, value in section.items():
            new_key, new_value = get_section_item_pair(key, value)
            if new_value is not None:
                new_path = get_source_path(new_value)
                if new_key == SOURCE_BASE:
                    self._sources_base_path = new_path
                elif new_key == DEFAULT_BASE:
                    self._defaults_base_path = new_path
                else:
                    raise OlympiaConfigurationError(
                        f'Unknown key {new_key} in section {BASE_PATHS}, possible keys are {(SOURCE_BASE, DEFAULT_BASE)}')

    def _read_secrets(self) -> None:
        if SECRET_PATHS not in self._config_parser.sections() or SECRETS not in self._config_parser:
            return
        for name, secret in self._config_parser[SECRET_PATHS].items():
            if not isinstance(secret, str):
                continue
            try:
                os.environ[name.upper()] = secrets_manager.get_secret(secret)
            except secrets_manager.PermissionDenied:
                Log.error('Could not read Secret: ', secret)
        for name, secret in self._config_parser[SECRETS].items():
            if not isinstance(secret, str):
                continue
            try:
                os.environ[name.upper()] = secret
            except secrets_manager.PermissionDenied:
                Log.error('Could not read Secret: ', secret)

    def _read_sources(self) -> None:
        for section in self._config_parser.sections():
            if section.lower() in SOURCES:
                section_globals: dict[str, str] = {}
                source = section.lower()
                source_section = self._config_parser[section]
                for key, value in source_section.items():
                    if key.endswith('*'):
                        section_globals[key] = value
                        continue
                    new_key, new_value = get_section_item_pair(key, value)
                    if new_value is not None:
                        signature = Signature.from_str(new_key)
                        object_type = signature.type
                        if source in LOCAL_SOURCES:
                            location = get_source_path(new_value, self._sources_base_path)
                            new_source: Source = LocalSource(signature, source, location, no_test=self._no_test)
                        elif source in CLOUD_SOURCES:
                            new_source = CloudSource(signature, source, new_value, no_test=self._no_test)
                        elif source in (OLYMPIA, OLYMPIA_V2):
                            base_url = section_globals.get(OLYMPIA_BASE_URL)
                            user_name = section_globals.get(OLYMPIA_USER)
                            new_source = OlympiaMarketSource(signature, source, value, base_url, user_name,
                                                             no_test=self._no_test)
                        elif source == OLYMPIA_STATIC:
                            base_url = section_globals.get(OLYMPIA_BASE_URL)
                            new_source = OlympiaStaticSource(signature, source, value, base_url, user_name,
                                                             no_test=self._no_test)
                        else:
                            raise NotImplementedError(f'Unknown source defined: {source}')
                        self._sources[object_type].append(new_source)

    def _print_non_source_file(self, file_path: str) -> str:
        status = 'OK' if os.path.exists(file_path) else 'NOT FOUND'
        if not self._no_test:
            file_path = hide_path(file_path)
        return f'{file_path}\t[{status}]'


def write_empty_config(out_dir: str, template_version: str, defaults_base_path: Optional[str] = None) -> None:
    all_descriptors = list(get_parsers())
    version_file_name = template_version.replace('.', '_').replace('-', '_')
    out_file_name = f'{version_file_name}_.config.ini'
    config_writer = ConfigParser(allow_no_value=True, dict_type=OrderedDict)
    config_writer.optionxform = str  # type: ignore[assignment]
    for section in SECTIONS:
        new_section = OrderedDict()
        if section == VALUATION_DEFAULTS:
            for item in (DEFAULT_PARAMETERS, VALUATIONS, RESULT_TYPES):
                new_section[item] = f'{item}.json' if defaults_base_path else ''
        elif section == BASE_PATHS:
            new_section['# Optional'] = None  # type: ignore[assignment]
            new_section[DEFAULT_BASE] = defaults_base_path or ''
            new_section[SOURCE_BASE] = ''
        elif section.lower() in SOURCES:
            new_section[
                '# Delete entries or leave empty if not needed. The complete section may also be deleted it is not needed.'] = None  # type: ignore[assignment]
            source_section = section.lower()
            if source_section == OLYMPIA:
                new_section[OLYMPIA_USER] = 'user'
                new_section[OLYMPIA_BASE_URL] = ''
            for descriptor in all_descriptors:
                if descriptor.source == source_section:
                    new_section[str(descriptor.signature)] = ''
        config_writer[section] = new_section
    with open(os.path.join(out_dir, out_file_name), mode='w') as c_handle:
        config_writer.write(c_handle)
