"""
Connection to S3 requires the credentials and config file in
    /Users/<username>/.aws/config
    /Users/<username>/.aws/credentials
OR
    setting the environment variables:
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_DEFAULT_REGION
"""
from __future__ import annotations

import csv
import io
import re
from typing import Any, Optional, Union

from valuation.global_settings import __type_checking__
from valuation.olympia.input.cloud_storage_connectors.base_object import CloudConnectorBase

if __type_checking__:
    # pylint: disable=ungrouped-imports
    import boto3
    from valuation.olympia.input.cloud_storage_connectors.base_object import CloudPathHandler


class S3Connector(CloudConnectorBase):
    compatible_root = 's3a://'
    _client: Optional[boto3.resource] = None

    @classmethod
    def _initialize(cls) -> None:
        import boto3  # pylint: disable=import-outside-toplevel, redefined-outer-name
        cls._client = boto3.client('s3')

    @classmethod
    def get_file(cls, path: CloudPathHandler) -> io.BytesIO:
        if cls._client is None:
            cls._initialize()
        s3_obj: dict[str, Any] = cls._client.get_object(Bucket=path.bucket, Key=path.key)  # type: ignore[union-attr]
        return io.BytesIO(s3_obj['Body'].read())

    @classmethod
    def put_file(cls, path: CloudPathHandler, data: Union[io.BytesIO, bytes], overwrite: bool = False) -> None:
        if cls._client is None:
            cls._initialize()
        cls._client.put_object(Bucket=path.bucket, Key=path.key, Body=data)  # type: ignore[union-attr]

    @classmethod
    def key_exists(cls, path: CloudPathHandler) -> bool:
        if cls._client is None:
            cls._initialize()
        return cls._client.list_objects_v2(Bucket=path.bucket, Prefix=path.key, MaxKeys=1)['KeyCount'] > 0  # type: ignore[union-attr, no-any-return]

    @classmethod
    def glob(cls, path: CloudPathHandler, filename: str) -> list[CloudPathHandler]:
        if cls._client is None:
            cls._initialize()
        prefix: str
        prefix = '/'.join(path.get_prefix_and_filename())
        filename = filename.replace(r'*', r'.*')
        response: dict[str, Any] = cls._client.list_objects_v2(Bucket=path.bucket, Prefix=prefix)  # type: ignore[union-attr]
        result: list[CloudPathHandler] = []
        if 'Contents' not in response:
            return []
        for item in response['Contents']:
            file_key: str = item['Key'].replace(prefix, '')
            if file_key.startswith('/'):
                file_key = file_key[1:]
            if bool(re.match(f'^{filename}$', file_key)):
                result.append(path.replace(path.key, item['Key']))
        return result


def load_csv_file(key: CloudPathHandler, **csv_kwargs: Any) -> list[list[Any]]:
    data: io.BytesIO = S3Connector.get_file(key)
    return list(csv.reader(io.StringIO(data.read().decode()), **csv_kwargs))
