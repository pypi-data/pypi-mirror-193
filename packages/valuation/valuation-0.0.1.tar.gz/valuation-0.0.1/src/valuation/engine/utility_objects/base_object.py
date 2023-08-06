from __future__ import annotations

from typing import Any, Union

from valuations.consts import signatures
from valuations.engine import QLObject


class QLUtilityObject(QLObject):
    _signature = signatures.empty

    def get_raw_data(self) -> Union[dict[str, Any], list[dict[str, Any]]]:
        raise NotImplementedError
