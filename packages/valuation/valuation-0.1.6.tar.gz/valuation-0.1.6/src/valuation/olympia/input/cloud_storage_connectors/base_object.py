from __future__ import annotations

import io
from copy import deepcopy
from typing import Union


class CloudConnectorBase:
    compatible_root = ''

    @classmethod
    def _initialize(cls) -> None:
        raise NotImplementedError

    @classmethod
    def get_file(cls, path: CloudPathHandler) -> io.BytesIO:
        raise NotImplementedError

    @classmethod
    def put_file(cls, path: CloudPathHandler, data: Union[io.BytesIO, bytes], overwrite: bool = False) -> None:
        raise NotImplementedError

    @classmethod
    def key_exists(cls, path: CloudPathHandler) -> bool:
        raise NotImplementedError

    @classmethod
    def glob(cls, path: CloudPathHandler, filename: str) -> list[CloudPathHandler]:
        raise NotImplementedError


class CloudPathHandler:
    """
    Path structures
    ---------------
    S3            :  s3a://<bucket_name>/<prefix>/<filename>
    GCS           :  gs://<bucket_name>/<prefix>/<filename>
    For differing structures, override the _evaluate method
    """

    @property
    def root(self) -> str:
        return self._root + '//'

    @property
    def bucket(self) -> str:
        return self._bucket

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: str) -> None:
        self._key = key

    def __init__(self, path: str) -> None:
        self._root: str = ''
        self._key = ''
        self._bucket: str = ''
        self._evaluate(path)

    def _evaluate(self, path: str) -> None:
        self._root, bucket_and_key = path.split('//')
        self._bucket, self._key = bucket_and_key.split('/', 1)

    def get_prefix_and_filename(self) -> tuple[str, str]:
        prefix: str
        filename: str
        items: list[str] = self._key.rsplit('/', 1)
        if len(items) == 2:
            prefix, filename = items
        else:
            prefix = items[0]
            filename = ''
        return prefix, filename

    def replace(self, __old: str, __new: str) -> CloudPathHandler:
        cls: CloudPathHandler = deepcopy(self)
        cls.key = cls.key.replace(__old, __new)
        return cls

    def __str__(self) -> str:
        return f'{self._root}//{self._bucket}/{self._key}'

    def __repr__(self) -> str:
        return self.__str__()
