from __future__ import annotations

from typing import Any, Optional
# Do not remove the ignore[import], even if it says unused
import requests  # type: ignore[import]
import requests.auth
from daa_utils.daalogging import Log
from valuation.consts import signatures
from valuation.global_settings import __type_checking__
from valuation.olympia.input.market_data_connection.base_parser import Parser
from valuation.olympia.input.market_data_connection.olympia_static_data_connection import bulk_instrument_loader
from valuation.olympia.input.market_data_connection.source import OLYMPIA_STATIC, OlympiaStaticSource

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.olympia.input.market_data_connection.source import Source  # pylint: disable=ungrouped-imports


class ParserOlympiaStaticData(Parser):
    _sources = (OLYMPIA_STATIC, )
    _signature = signatures.instrument.all

    def __init__(self, source: Source) -> None:  # pylint: disable=unused-argument
        super().__init__(source)

        assert isinstance(source, OlympiaStaticSource), 'Olympia Parser only compatible with OlympiaSource'  # actually always true

        self._method_name: str = source.method
        self._base_url: str = source.base_url
        self._user_name: str = source.user_name
        self._access_token: str = source.access_token
        self._auth = requests.auth.HTTPBasicAuth(source.user_name, source.access_token)
        self._content: dict[str, Any] = {}

    def _search_call(self, reference_id: str) -> Optional[dict[str, Any]]:
        preloaded_data: Optional[dict[str, Any]] = \
            bulk_instrument_loader.BulkInstrumentCache.get(reference_id)
        if preloaded_data is not None:
            return preloaded_data

        base_url: str = self._base_url
        if not base_url.endswith('/'):
            base_url += '/'
        url: str = base_url + self._method_name + reference_id
        response: requests.Response = requests.get(url, auth=self._auth)
        if response.status_code != 200:
            Log.error("could not fetch response, the code for request is: " + str(response.status_code))
            return None
        content: dict[str, Any] = response.json()
        return content

    def check_for(self, reference_id: str) -> bool:
        reference_id = reference_id.split('#', 1)[0]  # remove potential price classifier
        if reference_id not in self._content:
            self._content[reference_id] = self._search_call(reference_id)
        return self._content[reference_id] is not None

    def get(self, reference_id: str) -> dict[str, Any]:
        classifier: Optional[str] = None
        if '#' in reference_id:
            reference_id, classifier = reference_id.split('#', 1)

        data: dict[str, Any] = self._content[reference_id].copy()
        data['type'] = data['instrumentType']
        data.update(data['security'])

        # this is an unclean workaround since the concept of the price classifier does not really get along with the
        # structure of this project. Bigger changes would be needed.
        if classifier is not None:
            if not data.get('spreadConfiguration'):
                Log.critical('A price classifier was passed but instrument has no spread config.')
                try:
                    del data['spreadConfiguration']
                except:
                    pass
            else:
                data['spreadConfiguration']['$priceClassifier'] = classifier
            data['id'] = f'{reference_id}#{classifier}'

        return data

    @property
    def _headers(self) -> dict[str, str]:
        return {'Authorization': f'Basic {self._access_token}'}

    def _load(self) -> None:
        pass
