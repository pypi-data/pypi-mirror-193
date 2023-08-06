from dataclasses import dataclass

from valuation.olympia.input.exception import OlympiaImportError
from valuation.olympia.input.mappings.request_keys import OLYMPIA_MARKET_DATA_OBJECTS
from valuation.universal_transfer import Reference

MDH_PREFIX_SCHEME: str = 'mdh://'


@dataclass(init=True, repr=True, eq=False, order=False, unsafe_hash=False, frozen=True)
class OlympiaMarketDataHubReference(Reference):
    sub_type: str
    uri: str

    @staticmethod
    def from_str(value: str) -> Reference:  # todo: use regex here instead
        uri: str = value
        seperator: str = '/'
        if not value.startswith(MDH_PREFIX_SCHEME):
            raise OlympiaImportError('Expected Market Data URI (mdh://) but got: ' + value)
        value = value[len(MDH_PREFIX_SCHEME):]
        if seperator not in value:
            raise OlympiaImportError('Expected Market Data URI (mdh://{TYPE}/{NAME}) but got: ' + value)
        md_type, name = value.split('/', 1)
        if md_type not in OLYMPIA_MARKET_DATA_OBJECTS:
            raise OlympiaImportError(f'Unknown market data: {md_type}')
        return OlympiaMarketDataHubReference(OLYMPIA_MARKET_DATA_OBJECTS[md_type].type,
                                             name,
                                             OLYMPIA_MARKET_DATA_OBJECTS[md_type].sub_type,
                                             uri)

    def __str__(self) -> str:
        return f'{self.type}|{self.uri}'
