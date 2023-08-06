"""
Connection to GCS requires the path of the credentials json file set in the environment variable
    GOOGLE_APPLICATION_CREDENTIALS
"""
from __future__ import annotations

import io
import re
from typing import Optional, Union

from valuation.global_settings import __type_checking__
from valuation.olympia.input.cloud_storage_connectors.base_object import CloudConnectorBase

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from google.cloud import storage  # pylint: disable=import-outside-toplevel
    from valuation.olympia.input.cloud_storage_connectors.base_object import CloudPathHandler


class GoogleConnector(CloudConnectorBase):
    compatible_root = 'gs://'
    _client: Optional[storage.Client] = None
    _project_name: str = 'olympia-quantlib'

    _checked_buckets: set[str] = set()

    @classmethod
    def _check_bucket(cls, bucket: storage.Bucket, raise_if_false: bool = True) -> bool:
        if bucket.name in cls._checked_buckets:
            return True
        if not bucket.exists():
            if raise_if_false:
                raise FileNotFoundError('Bucket does not exist: %s' % bucket.name)
            return False
        cls._checked_buckets.add(bucket.name)
        return True

    @classmethod
    def _initialize(cls) -> None:
        from google.cloud import storage  # pylint: disable=import-outside-toplevel, redefined-outer-name
        cls._client = storage.Client(cls._project_name)

    @classmethod
    def get_file(cls, path: CloudPathHandler) -> io.BytesIO:
        if cls._client is None:
            cls._initialize()
        bucket: storage.Bucket = cls._client.bucket(path.bucket)  # type: ignore[union-attr]
        cls._check_bucket(bucket)
        blob: Optional[storage.Blob] = bucket.get_blob(path.key)
        if blob is None:
            raise FileNotFoundError('File %s not found in bucket %s' % (path.key, path.bucket))
        return io.BytesIO(blob.download_as_bytes())

    @classmethod
    def put_file(cls, path: CloudPathHandler, data: Union[io.BytesIO, bytes], overwrite: bool = False) -> None:
        if path.key.endswith('.json'):
            content_type: str = 'application/json'
        else:
            content_type = 'text/plain'

        if cls._client is None:
            cls._initialize()
        bucket: storage.Bucket = cls._client.bucket(path.bucket)  # type: ignore[union-attr]
        cls._check_bucket(bucket)
        blob = bucket.blob(path.key)
        if not overwrite and blob.exists():
            raise FileExistsError('file %s already exists in bucket %s' % (path.key, path.bucket))
        blob.upload_from_string(data, content_type=content_type)

    @classmethod
    def key_exists(cls, path: CloudPathHandler) -> bool:
        if cls._client is None:
            cls._initialize()
        bucket: storage.Bucket = cls._client.bucket(path.bucket)  # type: ignore[union-attr]
        if not cls._check_bucket(bucket, False):
            return False
        try:
            return len(list(bucket.list_blobs(prefix=path.key))) > 0
        except ValueError:
            return False

    @classmethod
    def glob(cls, path: CloudPathHandler, filename: str) -> list[CloudPathHandler]:
        if cls._client is None:
            cls._initialize()
        if not cls.key_exists(path):
            prefix: str = '/'.join(path.get_prefix_and_filename())
        else:
            prefix, _ = path.get_prefix_and_filename()
        filename = filename.replace(r'*', r'.*')
        result: list[CloudPathHandler] = []
        for item in cls._client.list_blobs(path.bucket, prefix=prefix):  # type: ignore[union-attr]
            file_key: str = item.name
            if bool(re.match(f'^{prefix + filename}$', file_key)):
                result.append(path.replace(path.key, file_key))
        return result
