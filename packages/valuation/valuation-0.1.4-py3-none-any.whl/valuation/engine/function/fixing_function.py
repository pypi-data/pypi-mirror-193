from __future__ import annotations

from typing import Any

from valuation.consts import signatures, types
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Length
from valuation.engine.exceptions import QLInputError
from valuation.engine.function import QLFunction
from valuation.engine.utils import date2qldate

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import DefaultParameters, Storage
    from valuation.engine import QLObjectDB
    import QuantLib as ql


class QLFunctionFixing(QLFunction):                             # pylint: disable=abstract-method
    _signature = signatures.function.fixing

    @property
    def return_type(self) -> str:
        return types.Float

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        fixing_dates: list[ql.Date] = self.data(fields.FixingDates, default_value=[])  # type: ignore[arg-type]
        fixing_values: list[float] = self.data(fields.Fixings, check=Length(fixing_dates), default_value=[])  # type: ignore[arg-type]
        self._fixings: dict[ql.Date, float] = dict(zip(fixing_dates, fixing_values))

    def __call__(self, key: Any) -> Any:
        if date2qldate(key) not in self._fixings:
            raise QLInputError(f'No past fixing at {key} available!')
        return self._fixings[date2qldate(key)]


class QLFunctionSwapRateFixing(QLFunctionFixing):
    _signature = signatures.function.swap_rate_fixing
