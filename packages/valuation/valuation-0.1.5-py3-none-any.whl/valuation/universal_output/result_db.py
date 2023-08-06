from __future__ import annotations

from typing import Any, Generator, Optional

from valuation.consts import result
from valuation.global_settings import __type_checking__
from valuation.universal_output import ResultLineAmount
from valuation.utils.input_output import JSONType, to_json

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_output import ResultLine, SafeAny


def stringify_signature(signature: tuple[SafeAny, ...]) -> tuple[str, ...]:
    converted: list[str] = [str(item) for item in signature]
    return tuple(converted)


class ResultDB:
    def __init__(self) -> None:
        self._data: dict[tuple[SafeAny, ...], ResultLine] = {}
        self._sortable_keys: dict[tuple[str, ...], tuple[SafeAny, ...]] = {}

    def __contains__(self, result_line: ResultLine) -> bool:
        return result_line.signature in self._sortable_keys

    def __call__(self, result_line: Optional[ResultLine]) -> None:
        if result_line is None:
            return
        signature = result_line.signature
        if signature in self._data:
            self._data[signature] = result_line + self._data[signature]  # type: ignore[assignment, union-attr] # None is ruled out
        else:
            self._data[signature] = result_line
            self._sortable_keys[stringify_signature(signature)] = signature

    def __iter__(self) -> Generator[ResultLine, None, None]:
        for key in sorted(self._sortable_keys):
            yield self._data[self._sortable_keys[key]]

    def __contains__(self, result_line: ResultLine) -> bool:
        return result_line.signature in self._sortable_keys

    def clean(self) -> None:
        for signature in list(self._data):
            if self._data[signature] is None:
                self._data.pop(signature)
                self._sortable_keys.pop(stringify_signature(signature))

    def copy(self, ids2cancel: tuple[str, ...] = tuple()) -> ResultDB:
        new_result_db: ResultDB = ResultDB()
        for new_result in self._data.values():
            new_result_db(new_result.copy(ids2cancel))
        new_result_db.clean()
        return new_result_db

    def adjust_nominal(self) -> ResultDB:
        new_result_db: ResultDB = ResultDB()
        nominals: dict[tuple[str, SafeAny], tuple[float, str]] = {}
        nominal_signature = ResultLineAmount('', None, 'AdjustNominal', float('nan'), '')[result.ResultType]
        for single_result in self._data.values():
            if single_result is None:
                continue
            if single_result[result.ResultType] != nominal_signature:
                continue
            instrument_id: str = single_result[result.InstrumentId]
            sub_id: SafeAny = single_result[result.SubId]
            nominal: float = single_result[result.Amount]
            currency: str = single_result[result.Currency]
            nominals[(instrument_id, sub_id)] = (nominal, currency)
            if (instrument_id, None) not in nominals:
                nominals[(instrument_id, None)] = (nominal, currency)
            if (nominal, currency) != nominals[(instrument_id, None)]:
                nominals[(instrument_id, None)] = None                      # type: ignore[assignment]  # Deliberately made, such that any access triggers an error.
        for single_result in self._data.values():
            if single_result is None:
                continue
            if single_result[result.ResultType] == nominal_signature:
                continue
            if result.Currency not in single_result:
                new_result_db(single_result.copy())
            else:
                instrument_id = single_result[result.InstrumentId]
                sub_id = single_result[result.SubId]
                if (instrument_id, sub_id) in nominals:
                    nominal = nominals[(instrument_id, sub_id)][0]
                else:
                    nominal = nominals[(instrument_id, None)][0]
                new_result: ResultLine = single_result.copy() * nominal
                new_result_db(new_result)
        return new_result_db

    def adjust_portfolio_currency(self, portfolio_currency: str, conversion: dict[str, float]) -> ResultDB:
        new_result_db: ResultDB = ResultDB()
        currencies: dict[tuple[str, SafeAny], str] = {}
        nominal_signature = ResultLineAmount('', None, 'AdjustNominal', float('nan'), '')[result.ResultType]
        for single_result in self._data.values():
            if single_result is None:
                continue
            if single_result[result.ResultType] != nominal_signature:
                continue
            instrument_id: str = single_result[result.InstrumentId]
            sub_id: SafeAny = single_result[result.SubId]
            currencies[(instrument_id, sub_id)] = single_result[result.Currency]
        for single_result in self._data.values():
            if single_result is None:
                continue
            if single_result[result.ResultType] == nominal_signature:
                continue
            if result.Currency not in single_result:
                new_result_db(single_result.copy())
            else:
                currency = single_result[result.Currency]
                factor = conversion[portfolio_currency] / conversion[currency]
                new_result: ResultLine = single_result.copy() * factor
                new_result._data[  # pylint: disable=protected-access
                    result.Currency] = portfolio_currency  # Copy constructor
                new_result_db(new_result)
        return new_result_db

    def str_precision(self, precision: Optional[int] = None) -> str:
        new_result: list[str] = [
            self._data[self._sortable_keys[key]]
            .str_precision(precision)
            .replace('\n', '\t!\t')
            for key in sorted(self._sortable_keys)
        ]

        return '\n'.join(new_result)

    def __str__(self) -> str:
        return self.str_precision()

    def get_list(self) -> list[dict[str, Any]]:
        return [result_line.data for result_line in self]


@to_json.register
def _(arg: ResultDB, precision: Optional[int] = None) -> JSONType:
    return [to_json(result_line, precision) for result_line in arg]
