import requests
import requests.auth
from typing import Any, Optional

MAX_PAGE_SIZE: int = 100  # todo: make that a setting


class BulkInstrumentCache:
    _storage: dict[str, Any] = {}
    _url: str = ''
    _headers: Optional[dict[str, Any]] = None

    @staticmethod
    def size() -> int:
        return len(BulkInstrumentCache._storage)

    @classmethod
    def activate(cls, base_url: str, token: str) -> None:
        if not base_url.endswith('/'):
            base_url += '/'
        url: str = base_url + 'api/v1/instruments/search/bonds'

        if cls.is_active():
            if url != cls._url:
                raise RuntimeError(cls.__name__ + ' was already activated with a different url')
            return
        print('logging in with ', base_url)

        cls._url = url
        cls._headers = {'Authorization': f'Basic {token}'}

    @classmethod
    def get_authentication(cls) -> None:
        if not cls.is_active():
            raise RuntimeError(cls.__name__ + ' was never activated and authenticated')
        return cls._headers

    @classmethod
    def is_active(cls) -> bool:
        return cls._headers is not None

    @classmethod
    def get(cls, name: str) -> Optional[dict[str, Any]]:
        return cls._storage.get(name)

    @classmethod
    def load(cls, ids: list[str]) -> None:
        ids_to_use = [_id.split('#', 1)[0] if '#' in _id else _id for _id in ids]
        data: list[dict[str, Any]] = cls._load_data(ids_to_use)
        for item in data:
            if 'id' not in item:
                continue
            cls._storage[item['id']] = item

    @classmethod
    def _load_data(cls, ids: list[str]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for chunk in divide_chunks(ids):
            data = cls._single_load(chunk)
            result.extend(data)
        return result

    @classmethod
    def _single_load(cls, ids: list[str]) -> list[dict[str, Any]]:
        body: dict[str, Any] = {'ids': ids}
        resp: requests.Response = requests.post(cls._url, json=body, headers=cls.get_authentication())
        if not resp.status_code == 200:
            raise RuntimeError('Error while getting instrument data: ' + resp.text)
        data: list[dict[str, Any]] = resp.json()
        return data


def divide_chunks(iterable: list[Any], chunk_size: int = MAX_PAGE_SIZE) -> list[Any]:
    for position in range(0, len(iterable), chunk_size):
        yield iterable[position:position + chunk_size]
