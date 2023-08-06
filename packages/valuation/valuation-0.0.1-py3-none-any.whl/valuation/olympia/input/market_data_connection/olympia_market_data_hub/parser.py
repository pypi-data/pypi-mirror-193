from __future__ import annotations

import datetime
from typing import Any
# Do not remove the ignore[import], even if it says unused
import requests  # type: ignore[import]
from daa_utils import Log

from valuation.consts import signatures
from valuation.global_settings import __type_checking__
from valuation.olympia.input.market_data_connection.base_parser import Parser
from valuation.olympia.input.market_data_connection.exception import OlympiaDataConnectionError
from valuation.olympia.input.market_data_connection.source import OLYMPIA, OlympiaSource
from valuation.engine.base_object import classproperty

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.olympia.input.market_data_connection.source import Source  # pylint: disable=ungrouped-imports


class ParserOlympiaHub(Parser):
    _sources = (OLYMPIA, )
    _method_type: str = '/instances/'  # Should be either instances or archetypes
    _human_readable_interface: bool = True

    @classproperty
    def human_readable_interface(self) -> bool:
        """
        There are two kinds of Olympia Interfaces, one is the human readable and the other one
        if made for Olympia itself. While in the first one, the user can enter the names of the desired
        market data and the parser will search for the corresponding entry, the latter mode will just
        receive a reference key to the database of Olympia.
        """
        return self._human_readable_interface

    def __init__(self, source: Source) -> None:  # pylint: disable=unused-argument
        super().__init__(source)
        assert isinstance(source, OlympiaSource), 'Olympia Parser only compatible with OlympiaSource'  # actually always true
        self._valuation_date: str = source.date.isoformat()  # type: ignore[union-attr]
        api_mode, base_url, method = source.location.split('@')
        assert api_mode == 'user', 'Currently, only the "user" mode is supported.'
        self._method_name: str = method
        self._base_url: str = base_url
        self._access_token: str = source.access_token

        self._content: dict[str, Any] = {}

    def _search_call(self, reference_id: str) -> list[dict[str, Any]]:
        """
        search call uses olympias search function to find the instance based on name and date.
        reference id has to be the name of the object on Olympia
        """
        url: str = self._base_url + self._method_type + self._method_name
        params: dict[str, str] = {'date': self._valuation_date,
                                  'name': reference_id}
        response: requests.Response = requests.get(url, params=params, headers=self._headers)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()
        return content

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
            self._content[reference_id] = instance.get('id')
        return self._content[reference_id] is not None

    def get(self, reference_id: str) -> dict[str, Any]:
        instance_id: str = self._content[reference_id]
        url: str = self._base_url + self._method_type + self._method_name + '/' + instance_id
        response: requests.Response = requests.get(url, headers=self._headers)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        initialized = self.initialize_data()
        response_content: dict[str, Any] = response.json()
        initialized.update(response_content)
        initialized['referenceId'] = initialized['id']
        initialized['id'] = initialized['name']
        return initialized

    @property
    def _headers(self) -> dict[str, str]:
        return {'Authorization': f'Basic {self._access_token}'}

    def _load(self) -> None:
        pass


class OParserDiscountCurveBase(ParserOlympiaHub):
    _signature = signatures.empty

    @property
    def sub_type_name(self) -> str:
        curve_types: dict[str, str] = {
            'curves/discount': 'Discount',
            'curves/yield': 'Zero',
        }
        return curve_types[self._method_name]

    def get(self, reference_id: str) -> dict[str, Any]:
        data: dict[str, Any] = super().get(reference_id)
        if 'points' not in data:
            return data
        points: list[dict[str, Any]] = data['points']
        if points[0]['date'] == self._valuation_date:  # fixing potential data issues
            removed_item: dict[str, Any] = points.pop(0)
            Log.warning('Removed item from curve.' + str(removed_item))
        return data


class OParserDiscountCurve(OParserDiscountCurveBase):
    _signature = signatures.yield_curve.discount


class OParserZeroCurve(OParserDiscountCurveBase):
    _signature = signatures.yield_curve.zero


class OParserIndex(ParserOlympiaHub):
    _signature = signatures.ir_index.base
    _method_type = '/archetypes/'

    def check_for(self, reference_id: str) -> bool:
        if reference_id not in self._content:
            content: list[dict[str, Any]] = self._search_call(reference_id)
            if not content:
                instance: dict[str, Any] = {}
            else:
                instance = content[-1]
            self._content[reference_id] = instance
        return self._content[reference_id] is not None

    def get(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        data: dict[str, Any] = self._content[reference_id]
        data['fixingFunction'] = reference_id
        data['discountCurve'] = reference_id
        initialized.update(data)
        initialized['referenceId'] = initialized['id']
        initialized['id'] = initialized['name']
        return initialized


class OParserIRFixing(OParserIndex):
    _signature = signatures.function.api_call_fixing

    @staticmethod
    def _covert_reference_id(reference_id: str) -> str:
        if 'vs' in reference_id:
            currency: str = reference_id[:3]
            period: str = reference_id.split('vs')[1]
            return f'{currency}_CMS_{period}'
        return reference_id

    def _search_call(self, reference_id: str) -> list[dict[str, Any]]:
        url: str = self._base_url + self._method_type + self._method_name
        params: dict[str, str] = {'name': reference_id}
        response: requests.Response = requests.get(url, params=params, headers=self._headers)
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()
        return content

    def check_for(self, reference_id: str) -> bool:
        if reference_id not in self._content:
            oly_reference_id: str = self._covert_reference_id(reference_id)
            self._content[reference_id] = self._search_call(oly_reference_id)
        # Even if not available, we don't want to stop the index initiation. The get function returns an error if not
        # found (same as if a fixing is missing)
        return True

    def _get_empty_fixing_function(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        initialized['subType'] = signatures.function.fixing.sub_type
        initialized['id'] = reference_id
        return initialized

    def _get_fixing_function(self, reference_id: str) -> dict[str, Any]:
        initialized = self.initialize_data()
        data: dict[str, Any] = dict()
        data['id'] = reference_id
        # archetypes were used to check; the function needs to fetch an instance
        data['url'] = f'{self._base_url}/instances/{self._method_name}'
        data['token'] = 'Basic ' + self._access_token
        data['baseCurveName'] = self._covert_reference_id(reference_id)
        initialized.update(data)
        return initialized

    def get(self, reference_id: str) -> dict[str, Any]:
        if self._content[reference_id]:
            return self._get_fixing_function(reference_id)
        return self._get_empty_fixing_function(reference_id)


class OParserZSpreads(ParserOlympiaHub):
    _signature = signatures.z_spread_collection
    reference_id_pattern = '{SPREAD_CURVE_ID}#{BASE_CURVE}'

    def check_for(self, reference_id: str) -> bool:
        if len(ids := reference_id.split('#')) != 2:
            return False
        return super().check_for(ids[0])

    def get(self, reference_id: str) -> dict[str, Any]:
        spread_id, base_curve_id = reference_id.split('#')
        data: dict[str, Any] = super().get(spread_id)
        data['baseCurve'] = base_curve_id
        data['id'] = reference_id
        return data
