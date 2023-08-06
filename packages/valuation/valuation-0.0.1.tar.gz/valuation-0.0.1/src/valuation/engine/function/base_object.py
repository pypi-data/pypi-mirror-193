from typing import Any

from valuations.engine import QLObject


class QLFunction(QLObject):                             # pylint: disable=abstract-method

    @property
    def return_type(self) -> str:
        raise NotImplementedError

    def __call__(self, key: Any) -> Any:
        raise NotImplementedError
