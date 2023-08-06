"""
Even though, each cloud storage has to be accessed using their individual library,
the behaviour of those is quite similar. Instead of importing all connectors that are
available at places where more than one are applicable, this class can be used. It
decides based on the storage key, which class to use
"""
# todo (2021/05) check if that concept proofs as stable, otherwise move to factory appraoch
#  Proposal: Remove it, reasons: 1) The undesired class factory is simply delegated to the decorator and is therefore generated for every method call 2) It is impossible to annotate reasonably

from __future__ import annotations

import csv
import io
from typing import Any, Callable, Union, TypeVar
from valuation.olympia.input.cloud_storage_connectors import CloudConnectorBase, CloudPathHandler

ReturnType = TypeVar('ReturnType')
CloudMethod = Callable[..., ReturnType]


def dyn_inheritance(cloud_method: CloudMethod[ReturnType]) -> CloudMethod[ReturnType]:
    _factory: dict[str, type[CloudConnectorBase]] = \
        {_class.compatible_root: _class for _class in CloudConnectorBase.__subclasses__()}

    def wrapper(*args: Any, **kwargs: Any) -> ReturnType:
        new_args = list(args)
        new_cloud_method = cloud_method
        for arg in new_args:
            if isinstance(arg, CloudPathHandler):
                _class = _factory[arg.root]
                new_args.pop(0)
                new_cloud_method = getattr(_class, cloud_method.__name__)
                break
        return new_cloud_method(*new_args, *kwargs)
    return wrapper


class CloudConnector(CloudConnectorBase):
    compatible_root = ''

    @classmethod
    def _initialize(cls) -> None:
        raise NotImplementedError

    @classmethod
    @dyn_inheritance
    def get_file(cls, path: CloudPathHandler) -> io.BytesIO:
        raise NotImplementedError

    @classmethod
    @dyn_inheritance
    def put_file(cls, path: CloudPathHandler, data: Union[io.BytesIO, bytes], overwrite: bool = False) -> None:
        raise NotImplementedError

    @classmethod
    @dyn_inheritance
    def key_exists(cls, path: CloudPathHandler) -> bool:
        raise NotImplementedError

    @classmethod
    @dyn_inheritance
    def glob(cls, path: CloudPathHandler, filename: str) -> list[CloudPathHandler]:
        raise NotImplementedError


def load_csv_file(key: CloudPathHandler, **csv_kwargs: Any) -> list[list[Any]]:
    data: io.BytesIO = CloudConnector.get_file(key)
    return list(csv.reader(io.StringIO(data.read().decode()), **csv_kwargs))
