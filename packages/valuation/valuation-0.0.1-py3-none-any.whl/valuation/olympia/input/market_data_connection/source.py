import datetime
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, Union

from daa_utils import Log
from valuation.olympia.input.cloud_storage_connectors import CloudPathHandler, CloudConnector
from valuation.olympia.input.market_data_connection.exception import OlympiaDataConnectionError
from valuation.olympia.input.market_data_connection.helpers import replace_date_place_holder
from valuation.olympia.input.market_data_connection.olympia_market_data_hub_v2 import bulk_data_loader
from valuation.olympia.input.market_data_connection.olympia_static_data_connection import bulk_instrument_loader
from valuation.universal_transfer import Reference, Signature


def hide_path(path_or_str: str) -> str:
    path = Path(path_or_str)
    tail = path.name
    if tail == str(path):
        return tail
    if len(path.parts) >= 2:
        return '<BaseDirectory>' + '/' + str(path.parts[-2]) + '/' + tail
    return '<BaseDirectory>' + '/' + tail


EXCEL: str = 'excel'
CSV: str = 'csv'
OLYMPIA: str = 'olympia'
OLYMPIA_V2: str = 'olympia_v2'
OLYMPIA_STATIC: str = 'olympia_static'
GOOGLE: str = 'google'
S3: str = 's3'
LOCAL_SOURCES: tuple[str, str] = (CSV, EXCEL)
CLOUD_SOURCES: tuple[str, str] = (GOOGLE, S3)
SOURCES: tuple[str, ...] = LOCAL_SOURCES + CLOUD_SOURCES + (OLYMPIA, OLYMPIA_STATIC, OLYMPIA_V2)

ReferenceProcessor = Callable[[str, Reference], str]


@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)
class SourceDescriptor:
    signature: Signature
    source: str


SPECIFIC_PROCESSORS: dict[SourceDescriptor, ReferenceProcessor] = {}


# TODO(2021/10) add resolved/unresolved status refinement
class Source:
    _sources: tuple[str, ...] = SOURCES

    @property
    def location(self) -> Union[str, CloudPathHandler]:
        raise NotImplementedError

    @property
    def descriptor(self) -> SourceDescriptor:
        return self._descriptor

    @property
    def exists(self) -> bool:
        if not self._exists:
            return self._check_exists()
        return True

    def __init__(self, signature: Signature, source: str, location: str, no_test: bool = True) -> None:
        assert source.lower() in self._sources, f'{source} not in {self._sources}'
        self._descriptor = SourceDescriptor(signature, source)
        self._location: str = location
        self._exists: bool = False
        self._reference_processor: Optional[ReferenceProcessor] = SPECIFIC_PROCESSORS.get(self._descriptor)
        self._no_test = no_test

    def __str__(self) -> str:
        status = 'OK' if self._exists else 'NOT FOUND'
        location = self._location if self._no_test else hide_path(self._location)
        return f'{self._descriptor.signature} | Source[{self._descriptor.source}] | Status[{status}] | Location[{location}]'

    def resolve(self, valuation_date: datetime.date) -> None:
        self._resolve_date(valuation_date)

    def _check_exists(self) -> bool:
        raise NotImplementedError

    def _resolve_date(self, date: datetime.date) -> None:
        self._location = replace_date_place_holder(self._location, date)


class CloudSource(Source):
    _sources = CLOUD_SOURCES

    @property
    def location(self) -> CloudPathHandler:
        if not self.exists:
            raise OlympiaDataConnectionError(f'{self}')
        return CloudPathHandler(self._location)

    def _check_exists(self) -> bool:
        try:
            if CloudConnector.key_exists(CloudPathHandler(self._location)):
                self._exists = True
                return True
            return False
        except Exception as exception:  # pylint: disable=broad-except
            Log.warning(f'The following exception while searching location for {self}')
            Log.warning(exception)
            return False


class LocalSource(Source):
    _sources = LOCAL_SOURCES

    @property
    def location(self) -> str:
        if not self.exists:
            raise OlympiaDataConnectionError(f'{self}')
        return self._location

    def _check_exists(self) -> bool:
        try:
            if os.path.exists(self._location):
                self._exists = True
                return True
            return False
        except Exception as exception:  # pylint: disable=broad-except
            Log.warning(f'The following exception occurred in {self} while checking for valid location')
            Log.warning(exception)
            return False


class OlympiaSource(Source):
    _access_token_name: str = ''
    _access_token: str = ''
    _sources = (OLYMPIA,)

    @property
    def base_url(self) -> str:
        assert self._base_url is not None, 'Base URL is not defined'
        return self._base_url

    @property
    def method(self) -> str:
        raise NotImplementedError

    @property
    def location(self) -> str:
        if not self.exists:
            raise OlympiaDataConnectionError(f'{self}')
        return self._location

    @property
    def date(self) -> Optional[datetime.date]:
        return self._date

    @property
    def access_token(self) -> str:
        if not self.exists:
            raise OlympiaDataConnectionError(f'{self}')
        return self._access_token  # type: ignore[return-value]

    def __init__(self, signature: Signature, source: str, location: str, base_url: Optional[str],
                 no_test: bool = True) -> None:
        self._base_url: Optional[str] = base_url
        if self._base_url and self._base_url.endswith('/'):
            self._base_url = self._base_url[:-1]

        self._status = ''
        self._date: Optional[datetime.date] = None
        self._access_token: Optional[str] = self._get_access_token()
        super().__init__(signature, source, location, no_test)

    def __str__(self) -> str:
        status = 'OK' if self._exists else self._status
        location = self._location
        return f'{self._descriptor.signature} | Source[{self._descriptor.source}] | Status[{status}] | Location[{location}]'

    def resolve(self, valuation_date: datetime.date) -> None:
        self._date = valuation_date

    def _check_exists(self) -> bool:
        if not self._base_url:
            self._status = 'NO RESOLVABLE base_url* FROM CONFIG'
            Log.warning(str(self))
            return False
        if not self._access_token:
            self._status = f'NO TOKEN <{self._access_token_name}> FOUND IN ENV VARIABLES'
            Log.warning(str(self))
            return False
        self._exists = True
        return True

    def _get_access_token(self) -> Optional[str]:
        access_token: Optional[str] = os.getenv(self._access_token_name)
        return access_token


class OlympiaMarketSource(OlympiaSource):
    _sources = (OLYMPIA, OLYMPIA_V2)
    _access_token_name: str = 'MDH_USER_TOKEN'

    @property
    def method(self) -> str:
        return self._method

    @property
    def user_name(self) -> str:
        assert self._user_name is not None, 'api mode not defined'
        return self._user_name

    def __init__(self, signature: Signature, source: str, location: str, base_url: Optional[str],
                 user_name: Optional[str], no_test: bool = True) -> None:
        self._user_name: Optional[str] = user_name
        self._method: str = location

        new_location: str = f'{user_name}@{base_url}@{location}'
        super().__init__(signature, source, new_location, base_url, no_test)
        bulk_data_loader.BulkDataCache.activate(base_url, user_name, self.access_token)

    def _check_exists(self) -> bool:
        if not self._user_name:
            self._status = 'NO RESOLVABLE user_name* FROM CONFIG'
            Log.warning(str(self))
            return False
        return super()._check_exists()


class OlympiaStaticSource(OlympiaSource):
    _sources = (OLYMPIA_STATIC,)
    _access_token_name: str = 'OLYMPIA_BOND_API_TOKEN'

    @property
    def method(self) -> str:
        return self._method

    @property
    def user_name(self) -> str:
        assert self._user_name is not None, 'api mode not defined'
        return self._user_name

    def __init__(self, signature: Signature, source: str, location: str, base_url: Optional[str],
                 user_name: Optional[str], no_test: bool = True) -> None:
        self._user_name = user_name
        new_location: str = f'{user_name}@{base_url}@{location}'
        self._method: str = location

        super().__init__(signature, source, new_location, base_url, no_test)
        bulk_instrument_loader.BulkInstrumentCache.activate(base_url, self.access_token)
