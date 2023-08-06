from __future__ import annotations

import datetime
from typing import Any, Optional

# Do not remove the ignore[import], even if it says unused
import requests  # type: ignore[import]
import requests.auth
import warnings

from valuation.consts import signatures
from valuation.consts import fields
from daa_utils import Log
from valuation.global_settings import __type_checking__
from valuation.olympia.input.market_data_connection.base_parser import Parser
from valuation.olympia.input.market_data_connection.exception import OlympiaDataConnectionError
from valuation.olympia.input.market_data_connection.olympia_market_data_hub_v2 import bulk_data_loader, object_decoder
from valuation.olympia.input.market_data_connection.source import OLYMPIA_V2, OlympiaMarketSource

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.olympia.input.market_data_connection.source import Source  # pylint: disable=ungrouped-imports


class ParserOlympiaHubV2(Parser):
    _sources = (OLYMPIA_V2,)
    _method_type: str = '/instances/'  # Should be either instances or archetypes
    _default_point_field_name: str = ''
    _expected_links: dict[str, str] = {}

    def __init__(self, source: Source) -> None:  # pylint: disable=unused-argument
        super().__init__(source)
        assert isinstance(source, OlympiaMarketSource), 'Olympia Parser only compatible with OlympiaSource'  # actually always true
        self._valuation_date: str = source.date.isoformat()  # type: ignore[union-attr]
        self._method_name: str = source.method
        self._base_url: str = source.base_url
        self._user_name: str = source.user_name
        self._access_token: str = source.access_token

        self._auth = requests.auth.HTTPBasicAuth(source.user_name, source.access_token)

        self._content: dict[str, Any] = {}
        self._definitions: dict[str, dict[str, Any]] = {}

    def _search_call(self, reference_id: str) -> list[dict[str, Any]]:
        """
        search call uses olympias search function to find the instance based on name and date.
        reference id has to be the name of the object on Olympia
        """
        preloaded_data: Optional[dict[str, Any]] = \
            bulk_data_loader.BulkDataCache.get(reference_id, self._method_type, self._valuation_date)
        if preloaded_data is not None:
            return [preloaded_data]

        url: str = self._base_url + self._method_type
        params: dict[str, str] = {'type': self._method_name,
                                  'date': self._valuation_date,
                                  'name': reference_id}
        response: requests.Response = requests.get(url, params=params, auth=self._auth)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()['data']
        return content

    def _get_point_definition(self, point_definitions_id: str) -> dict[str, Any]:
        if point_definitions_id not in self._definitions:
            url: str = self._base_url + '/pointDefinitions/' + point_definitions_id
            response: requests.Response = requests.get(url, auth=self._auth)
            self._definitions[point_definitions_id] = response.json()['data']
        return self._definitions[point_definitions_id]

    @staticmethod
    def _parse_points(points: list[dict[str, Any]], selected_field: str, new_field: str = 'value',
                      set_type: Optional[str] = None) -> list[dict[str, Any]]:
        new_points: list[dict[str, Any]] = []
        for point in points:
            if selected_field not in point:
                continue
            point[new_field] = point[selected_field]
            if set_type is not None:
                point['type'] = set_type
            new_points.append(point)
        return new_points

    def _parse_links(self, data: dict[str, Any]):
        if not self._expected_links:
            return data
        if 'links' not in data:
            OlympiaDataConnectionError(f'Data body has no links.')
        links: dict[str, str] = data['links']
        for link, target in self._expected_links.items():
            uri: Optional[str] = links.get(link)
            if link is None:
                OlympiaDataConnectionError(f'{link} not in links')
            data[target] = uri
        return data

    def check_for(self, reference_id: str) -> bool:
        """
        check for checks if the object exists on Olympia. The response expected is an instance object, containing
        the instance id of the instance needed. That is used to get the data, which will be done in the .get() methods.

        ! if more than one instance appear for a date, the latest is selected !
        """

        if reference_id not in self._content:
            try:
                content: list[dict[str, Any]] = self._search_call(reference_id)
            except OlympiaDataConnectionError as error:
                Log.error(str(error))
                return False
            if not content:
                instance: dict[str, Any] = {}
            elif len(content) == 1:
                instance = content[0]
            else:
                instance = sorted(content, key=lambda item: datetime.datetime.fromisoformat(item['createdAt'][:19]))[-1]  # cutting microseconds if there
            self._content[reference_id] = instance
        return self._content[reference_id] is not None

    def _decode_object(self, instance: dict[str, Any]) -> dict[str, Any]:
        definition = None
        if object_decoder.POINTS in instance:
            if 'pointDefinitionId' not in instance:
                raise OlympiaDataConnectionError('Object has no pointDefinitionId:', instance)
            definition = self._get_point_definition(instance['pointDefinitionId'])
        return object_decoder.read(instance, definition)

    def get(self, reference_id: str) -> dict[str, Any]:
        instance: dict[str, Any] = self._content[reference_id]
        response_content: dict[str, Any] = self._decode_object(instance)
        if 'type' in response_content:
            response_content['olympiaType'] = response_content['type']
            del response_content['type']
        initialized = self.initialize_data()
        initialized.update(response_content)
        initialized['instanceId'] = initialized['id']
        initialized['id'] = initialized['name']
        return initialized

    def _load(self) -> None:
        pass


class OParserDiscountCurveBaseV2(ParserOlympiaHubV2):
    _signature = signatures.empty

    @staticmethod
    def _parse_points(points: list[dict[str, Any]], selected_field: str, new_field: str = 'value',
                      set_type: Optional[str] = None) -> list[dict[str, Any]]:
        points = ParserOlympiaHubV2._parse_points(points, selected_field, new_field, set_type)
        return sorted(points, key=lambda x: x['date'])

    def get(self, reference_id: str) -> dict[str, Any]:
        data: dict[str, Any] = super().get(reference_id)
        if 'points' not in data:
            return data
        data['points'] = self._parse_points(data['points'], self._default_point_field_name)
        points: list[dict[str, Any]] = data['points']
        if points[0]['date'] == self._valuation_date:  # fixing potential data issues
            removed_item: dict[str, Any] = points.pop(0)
            Log.warning('Removed item from curve.' + str(removed_item))
        return data


class OParserDiscountCurveV2(OParserDiscountCurveBaseV2):
    _signature = signatures.yield_curve.discount
    _default_point_field_name: str = 'DISCOUNT_FACTOR'


class OParserZeroCurve(OParserDiscountCurveBaseV2):
    _signature = signatures.yield_curve.zero
    _default_point_field_name: str = 'YIELD'


class OParserTimeSeriesBaseV2(ParserOlympiaHubV2):
    _signature = signatures.empty
    _expected_links = {}

    def get(self, reference_id: str) -> dict[str, Any]:
        data = super().get(reference_id)
        return self._parse_links(data)

    def _search_call(self, reference_id: str) -> list[dict[str, Any]]:
        url: str = self._base_url + '/archetypes/'
        params: dict[str, str] = {'name': reference_id, 'type': self._method_name}
        response: requests.Response = requests.get(url, params=params, auth=self._auth)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()['data']
        return content

    def _get_fixing_function(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        data: dict[str, Any] = dict()
        data['id'] = reference_id
        # archetypes were used to check; the function needs to fetch an instance
        data['url'] = f'{self._base_url}/instances?type={self._method_name}'
        data['baseUrl'] = f'{self._base_url}'
        data['user'] = self._user_name
        data['token'] = self._access_token
        data['baseCurveName'] = reference_id
        initialized.update(data)
        return initialized


class OPaserIRIndexV2(OParserTimeSeriesBaseV2):
    _signature = signatures.ir_index.base
    _expected_links = {'REL_YIELD_CURVE': fields.DiscountCurve.key}

    def get(self, reference_id: str) -> dict[str, Any]:
        content: dict[str, Any] = super().get(reference_id)
        content[fields.FixingFunction.key] = 'mdh://FIXING_FUNCTION/' + content[fields.Id.key]
        if object_decoder.POINTS in content:
            del content[object_decoder.POINTS]
        return content


class OPaserCMSIndexV2(OParserTimeSeriesBaseV2):
    _signature = signatures.ir_swap_index
    _expected_links = {'REL_YIELD_CURVE': fields.DiscountCurve.key}

    def get(self, reference_id: str) -> dict[str, Any]:
        content: dict[str, Any] = super().get(reference_id)
        content[fields.IRIndex.key] = content[fields.DiscountCurve.key].replace('YIELD_CURVE', 'FIXING')
        del content[fields.DiscountCurve.key]
        content[fields.FixingFunction.key] = 'mdh://CMS_FIXING_FUNCTION/' + content[fields.Id.key]
        content[fields.FixedFrequency.key] = content[fields.Tenor.key]
        content[fields.Period.key] = content[fields.Maturity.key]
        del content[fields.Maturity.key]
        del content[fields.Tenor.key]
        if object_decoder.POINTS in content:
            del content[object_decoder.POINTS]
        return content


class OParserIRFixingV2Base(OParserTimeSeriesBaseV2):
    def get(self, reference_id: str) -> dict[str, Any]:
        content = super().get(reference_id)
        content['url'] = f'{self._base_url}/instances?type={self._method_name}'
        content['baseUrl'] = f'{self._base_url}'
        content['user'] = self._user_name
        content['token'] = self._access_token
        content['baseCurveName'] = reference_id
        return content


class OParserIRFixingV2(OParserIRFixingV2Base):
    _signature = signatures.function.api_call_fixing_v2


class OParserCMSFixingV2(OParserIRFixingV2Base):
    _signature = signatures.function.api_call_cms_fixing_v2

    def get(self, reference_id: str) -> dict[str, Any]:
        content = super().get(reference_id)
        del content[fields.Maturity.key]
        return content


class OParserZSpreadsV2(ParserOlympiaHubV2):
    _signature = signatures.z_spread_collection
    _default_point_field_name = 'MID_SPREAD'
    reference_id_pattern = '{SPREAD_CURVE_ID}#{BASE_CURVE}'

    def check_for(self, reference_id: str) -> bool:
        if len(ids := reference_id.split('#')) != 2:
            return False
        return super().check_for(ids[0])

    def get(self, reference_id: str) -> dict[str, Any]:
        spread_id, base_curve_id = reference_id.split('#')
        data: dict[str, Any] = super().get(spread_id)
        data['points'] = self._parse_points(data['points'], self._default_point_field_name)
        data['baseCurve'] = base_curve_id
        data['id'] = reference_id
        return data


class OParserSwaptionVolV2(ParserOlympiaHubV2):
    _signature = signatures.swaption_volatility.points

    def get(self, reference_id: str) -> dict[str, Any]:
        data: dict[str, Any] = super().get(reference_id)
        if 'distribution' not in data:
            data['distribution'] = 'NORMAL'
            warnings.warn('helper: distribution set to NORMAL')
        if data['distribution'] == 'NORMAL':
            volatility_field: str = 'NORMAL_VOLATILITY'
        else:
            volatility_field: str = 'LOG_NORMAL_VOLATILITY'
        data['volaPoints'] = self._parse_points(data['points'], volatility_field, set_type='SwaptionPoint')
        del data['points']
        return data


class OBundleParserV2(ParserOlympiaHubV2):
    _method_type: str = '/bundles/'
    _expected_links: dict[str, str] = {}

    def _search_call(self, reference_id: str) -> list[dict[str, Any]]:
        url: str = f'{self._base_url}{self._method_type}{self._method_name}/{reference_id}'
        response: requests.Response = requests.get(url, auth=self._auth)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        return [response.json()['data']]

    def get(self, reference_id: str) -> dict[str, Any]:
        data: dict[str, Any] = super().get(reference_id)
        if 'links' not in data:
            OlympiaDataConnectionError(f'Data body has no links ({reference_id})')
        links: dict[str, str] = data['links']
        for link, target in self._expected_links.items():
            uri: Optional[str] = links.get(link)
            if link is None:
                OlympiaDataConnectionError(f'{link} not in links ({reference_id})')
            data[target] = uri
        return data

    def _decode_object(self, instance: dict[str, Any]) -> dict[str, Any]:
        return self._parse_links(instance)


class SwaptionVolBundleBaseParserV2(OBundleParserV2):
    _signature = signatures.empty
    _expected_links = {'REL_FIXING': 'marketData',
                       'REL_SWAPTION_VOLATILITY': 'swaptionVolatility'}


class HullWhiteCalibrationBundleParserV2(SwaptionVolBundleBaseParserV2):
    _signature = signatures.process.hull_white_calibration

    def check_for(self, reference_id: str) -> bool:
        return super().check_for(reference_id.split('#', 1)[0])

    def get(self, reference_id: str) -> dict[str, Any]:
        assert '#' in reference_id, 'reference_id must have pattern: {HULL_WHITE_PROCESS_NAME}#{INSTRUMENT_ID}'
        hull_white_ref, instrument_ref = reference_id.split('#', 1)
        data: dict[str, Any] = super().get(hull_white_ref)
        data['instrument'] = f'Instrument|{instrument_ref}'
        data['optimization'] = 'Optimize|OptimizeLevenbergMarquardtStandard'
        return data


class SwaptionProcessBundleParserV2(SwaptionVolBundleBaseParserV2):
    _signature = signatures.process.swaption_volatility


class FxForwardBundleParserV2(OBundleParserV2):
    _signature = signatures.fx_rate.triangle
    _expected_links = {'REL_BASE_FX_FORWARD': 'baseRate',
                       'REL_QUOTE_FX_FORWARD': 'quoteRate'}

    def get(self, reference_id: str) -> dict[str, Any]:
        data: dict[str, Any] = super().get(reference_id)
        return data


class OParserFxForwardV2(ParserOlympiaHubV2):
    _signature = signatures.fx_rate.direct
    _default_point_field_name = 'MID_SPREAD'

    def get(self, reference_id: str) -> dict[str, Any]:
        data: dict[str, Any] = super().get(reference_id)
        data['fixingFunction'] = data['links']['REL_FX_SPOT']
        if 'points' not in data:
            return data
        data['points'] = self._parse_points(data['points'], self._default_point_field_name)
        return data


class OParserFXRateV2(ParserOlympiaHubV2):
    _signature = signatures.function.api_call_fx_rate_v2

    def _search_call(self, reference_id: str) -> list[dict[str, Any]]:
        url: str = self._base_url + '/archetypes/'
        params: dict[str, str] = {'name': reference_id, 'type': "FX_SPOT"}
        response: requests.Response = requests.get(url, params=params, auth=self._auth)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()['data']
        return content

    def check_for(self, reference_id: str) -> bool:
        if reference_id not in self._content:
            data: list[dict[str, Any]] = self._search_call(reference_id)
            if len(data) == 0:
                return False
            self._content[reference_id] = object_decoder.read(data[0])
        # Even if not available, we don't want to stop the index initiation. The get function returns an error if not
        # found (same as if a fixing is missing)
        return True

    def _get_fixing_function(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        data: dict[str, Any] = dict()
        data['id'] = reference_id
        # archetypes were used to check; the function needs to fetch an instance
        data['url'] = f'{self._base_url}/instances?type={self._method_name}'
        data['baseUrl'] = f'{self._base_url}'
        data['user'] = self._user_name
        data['token'] = self._access_token
        data['baseCurveName'] = reference_id
        initialized.update(data)
        return initialized

    def get(self, reference_id: str) -> dict[str, Any]:
        return self._get_fixing_function(reference_id)
