from typing import Any

from google.cloud import secretmanager_v1
from google.api_core.exceptions import PermissionDenied


__all__ = ['get_secret', 'PermissionDenied']


def get_secret(name: str) -> str:
    client = secretmanager_v1.SecretManagerServiceClient()
    response = client.access_secret_version(name=name)
    secret: Any = response.payload.data.decode('UTF-8')
    if not isinstance(secret, str):
        raise PermissionDenied('Something went wrong with getting the secret')  # type: ignore[no-untyped-call]
    return secret
