from __future__ import annotations

import datetime
from typing import Any

# Do not remove the ignore[import], even if it says unused
import requests  # type: ignore[import]
import requests.auth

from valuation.consts import signatures, types
from valuation.consts import fields
from daa_utils.daalogging import Log
from valuation.engine.base_object import single_convert
from valuation.engine.exceptions import QLInputError
from valuation.engine.function import QLFunction
from valuation.global_settings import __type_checking__
from valuation.olympia.input.market_data_connection.olympia_market_data_hub_v2 import object_decoder
from valuation.universal_transfer import TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLFunctionAPICall(QLFunction):  # pylint: disable=abstract-method

    @property
    def return_type(self) -> str:
        return types.Float

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._url: str = self.data(fields.Url)
        self._base_url: str = self.data(fields.BaseUrl)
        user: str = self.data(fields.User)
        token: str = self.data(fields.Token)
        self._auth = requests.auth.HTTPBasicAuth(user, token)

    def _post_init(self) -> None:
        pass

    def _params(self, key: Any) -> dict[str, Any]:
        raise NotImplementedError


class QLFunctionAPICallFixing(QLFunctionAPICall):  # pylint: disable=abstract-method
    _signature = signatures.function.api_call_fixing

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._base_curve_name: str = self.data(TypeKey(types.Str, 'baseCurveName'))

    def _params(self, key: Any) -> dict[str, Any]:
        return {'name': self._base_curve_name,
                'date': key}

    @staticmethod
    def _eval_response(response: requests.Response) -> list[dict[str, Any]]:
        return response.json()

    def __call__(self, key: Any) -> Any:
        response: requests.Response = requests.get(self._url, auth=self._auth, params=self._params(str(key)))
        data = self._eval_response(response)
        if len(data) == 0:
            raise QLInputError('No fixing available for ' + response.url)
        # We use the last element of the retrieved list, as sorted by last edit.
        # So we will always get corrections if made.
        data_point = sorted(data, key=lambda d: datetime.datetime.fromisoformat(d['createdAt'][:19]))[-1]
        value = single_convert(self.return_type, data_point['value'], None, None, None, None, False)  # type: ignore[arg-type]
        Log.info(f'Pulled value {value} from query {response.url}')
        return value


class QLFunctionAPICallV2Base(QLFunctionAPICallFixing):  # pylint: disable=abstract-method
    _signature = signatures.empty
    _field_name: str = ""

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._definitions: dict[str, dict[str, Any]] = {}

    def _eval_response(self, response: requests.Response) -> list[dict[str, Any]]:

        result = []
        for item in response.json()['data']:
            definition = self._get_point_definition(item['pointDefinitionId'])
            obj = object_decoder.read(item, definition)
            for point in obj['points']:
                obj['value'] = point[self._field_name]
            result.append(obj)
        return sorted(result, key=lambda item: item['refDateTime'][:1])  # cutting microseconds if there

    def _get_point_definition(self, point_definitions_id: str) -> dict[str, Any]:
        if point_definitions_id not in self._definitions:
            url: str = self._base_url + '/pointDefinitions/' + point_definitions_id
            response: requests.Response = requests.get(url, auth=self._auth)
            self._definitions[point_definitions_id] = response.json()['data']
        return self._definitions[point_definitions_id]


class QLFunctionAPICallFixingV2(QLFunctionAPICallV2Base):  # pylint: disable=abstract-method
    _signature = signatures.function.api_call_fixing_v2
    _field_name = "FIXING"


class QLFunctionAPICallCMSFixingV2(QLFunctionAPICallV2Base):  # pylint: disable=abstract-method
    _signature = signatures.function.api_call_cms_fixing_v2
    _field_name = "SWAP_RATE"


class QLFunctionAPICallFXRateV2(QLFunctionAPICallV2Base):  # pylint: disable=abstract-method
    _signature = signatures.function.api_call_fx_rate_v2
    _field_name = "MID_PRICE"
