import datetime

import requests
import requests.auth
from typing import Any, Optional

from valuation.olympia.input.market_data_connection.exception import OlympiaDataConnectionError

MAX_PAGE_SIZE: int = 100  # todo: make that a setting


class BulkDataCache:
    _storage: dict[tuple[str, str, str], Any] = {}
    _archetype_storage: dict[tuple[str, str], Any] = {}
    _bundle_storage: dict[tuple[str, str], Any] = {}
    _url: str = ''
    _auth: Optional[requests.auth.HTTPBasicAuth] = None

    @staticmethod
    def size() -> int:
        return len(BulkDataCache._storage)

    @classmethod
    def activate(cls, base_url: str, user: str, password: str) -> None:
        if not base_url.endswith('/'):
            base_url += '/'
        url: str = base_url

        if cls.is_active():
            if url != cls._url:
                raise RuntimeError(cls.__name__ + ' was already activated with a different url')
            return
        print('logging in with ', base_url, user)

        cls._url = url
        cls._auth = requests.auth.HTTPBasicAuth(user, password)

    @classmethod
    def get_authentication(cls) -> None:
        if not cls.is_active():
            raise RuntimeError(cls.__name__ + ' was never activated and authenticated')
        return cls._auth

    @classmethod
    def is_active(cls) -> bool:
        return cls._auth is not None

    @classmethod
    def get(cls, name: str, data_type: str, val_date: str) -> Optional[dict[str, Any]]:
        return cls._storage.get((name, data_type, val_date))

    @classmethod
    def load(cls, ids: list[str]) -> None:
        data: list[dict[str, Any]] = cls._load_data(ids)
        for item in data:
            if 'name' not in item:
                continue
            if 'type' not in item:
                continue
            if 'refDate' not in item:
                continue
            cls._storage[(item['name'], item['type'], item['refDate'])] = item

    @classmethod
    def search_single_instance(cls, name: str, obj_type: str, valuation_date: str) -> dict[str, Any]:
        if (name, obj_type) not in cls._storage:
            instance: dict[str, Any] = cls._search_call_single_instance(name, obj_type, valuation_date)
            cls._storage[(name, obj_type)] = instance
        return cls._storage[(name, obj_type)]

    @classmethod
    def _search_call_single_instance(cls, name: str, obj_type: str, valuation_date: str) -> dict[str, Any]:
        url: str = cls._url + 'instances/'
        response: requests.Response = requests.get(url,
                                                   params={'type': obj_type, 'date': valuation_date, 'name': name},
                                                   auth=cls.get_authentication())
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()['data']
        if not content:
            raise OlympiaDataConnectionError(f'No instance received for: {obj_type} {name} of {valuation_date}')
        instance = sorted(content, key=lambda item: datetime.datetime.fromisoformat(item['createdAt'][:19]))[-1]  # cutting microseconds if there
        return instance

    @classmethod
    def search_single_archetype(cls, name: str, obj_type: str) -> dict[str, Any]:
        if (name, obj_type) not in cls._archetype_storage:
            instance: dict[str, Any] = cls._search_call_single_archetype(name, obj_type)
            cls._archetype_storage[(name, obj_type)] = instance
        return cls._archetype_storage[(name, obj_type)]

    @classmethod
    def _search_call_single_archetype(cls, name: str, obj_type: str) -> dict[str, Any]:
        url: str = cls._url + 'archetypes/'
        response: requests.Response = requests.get(url,
                                                   params={'type': obj_type, 'name': name},
                                                   auth=cls.get_authentication())
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: list[dict[str, Any]] = response.json()['data']
        if not content:
            raise OlympiaDataConnectionError(f'No archetype received for: {obj_type} {name}')
        return content[0]

    @classmethod
    def search_single_bundle(cls, name: str, obj_type: str) -> dict[str, Any]:
        if (name, obj_type) not in cls._bundle_storage:
            instance: dict[str, Any] = cls._search_call_single_bundle(name, obj_type)
            cls._bundle_storage[(name, obj_type)] = instance
        return cls._bundle_storage[(name, obj_type)]

    @classmethod
    def _search_call_single_bundle(cls, name: str, obj_type: str) -> dict[str, Any]:
        url: str = cls._url + f'bundles/{obj_type}/{name}'
        response: requests.Response = requests.get(url, auth=cls.get_authentication())
        if response.status_code != 200:
            raise OlympiaDataConnectionError(response.text)
        content: dict[str, Any] = response.json()['data']
        if not content:
            raise OlympiaDataConnectionError(f'No bundle received for: {obj_type} {name}')
        return content

    @classmethod
    def _load_data(cls, ids: list[str]) -> list[dict[str, Any]]:
        is_last: bool = False
        result: list[dict[str, Any]] = []
        page: int = 0
        while not is_last:
            is_last, data = cls._single_load(ids, page)
            page += 1
            result.extend(data)
        return result

    @classmethod
    def _single_load(cls, ids: list[str], page_number: int) -> tuple[bool, list[dict[str, Any]]]:
        body: dict[str, Any] = {'ids': ids, 'page': page_number, 'pageSize': MAX_PAGE_SIZE}
        resp: requests.Response = requests.post(cls._url + 'search/instances', json=body, auth=cls.get_authentication())
        if not resp.status_code == 200:
            raise RuntimeError('Error while getting market data: ' + resp.text)
        data: dict[str, Any] = resp.json()
        is_last: bool = data['meta']['page']['isLast']
        items: list[dict[str, Any]] = data['data']
        return is_last, items
