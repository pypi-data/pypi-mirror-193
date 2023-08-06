from __future__ import annotations

import QuantLib as ql

from valuations.global_settings import __type_checking__
from valuations.consts import signatures
from valuations.exceptions import ProgrammingError
from valuations.engine.exceptions import DAARuntimeException
from valuations.engine.market_data import QLMarketData
from valuations.universal_output import result_items

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuations.engine import QLObjectDB
    from valuations.engine.mappings import QLVolatilityType
    from valuations.universal_transfer import DefaultParameters, Storage, Signature


class QLVolatility(QLMarketData):  # pylint: disable=abstract-method
    _signature = signatures.empty
    _supported_greeks = (result_items.Vega,)
    _initializes_past = False
    _market_data_types: list[Signature] = []

    @property
    def scenario_divisor(self) -> float:
        return self._scenario_divisor

    @property
    def shift_unit(self) -> int:
        return 10000

    @property
    def distribution(self) -> QLVolatilityType:
        return self._distribution

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters = None, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode=data_only_mode)

        self._vol_surface: list[list[ql.SimpleQuote]]
        self._distribution: QLVolatilityType

        if __debug__:
            self._scenario_divisor: float = float('NaN')
            self._original_value: list[list[float]] = []

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Vega:
            return [result_items.Vega]
        raise ProgrammingError(f'Unsupported greek {greek}')

    def _change_to(self, scenario: str, shift: float) -> None:  # pylint: disable=arguments-differ
        assert not self._original_value
        if scenario != result_items.Vega:
            raise ProgrammingError(f'Unsupported scenario {scenario}')

        self._scenario_divisor = shift
        self._original_value = self._vol_surface
        self._vol_surface = []
        for line in self._original_value:
            entry_line: list[float] = []
            for entry in line:
                shifted_entry = entry + self._scenario_divisor / self.shift_unit
                if shifted_entry <= 0.0:
                    raise DAARuntimeException(f'Greek/Range calc: Negative {shift = } leads to nonpositive volatility')
                entry_line.append(shifted_entry)
            self._vol_surface.append(entry_line)
        self._post_init()

    def _change_back(self, scenario: str) -> None:
        if scenario != result_items.Vega:
            raise ProgrammingError(f'Unsupported scenario {scenario}')
        self._vol_surface = self._original_value
        self._post_init()
        if __debug__:
            self._original_value = []
            self._scenario_divisor = float('NaN')
