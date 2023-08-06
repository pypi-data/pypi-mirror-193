from __future__ import annotations

from typing import Any, Union

from valuation.consts import signatures
from valuation.engine import QLObject


class QLUtilityObject(QLObject):
    _signature = signatures.empty

    def get_raw_data(self) -> Union[dict[str, Any], list[dict[str, Any]]]:
        raise NotImplementedError
