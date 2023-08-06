from __future__ import annotations

import datetime
from collections import OrderedDict
from copy import copy
from typing import Any, Optional, Union

from valuation.consts import result
from valuation.exceptions import ProgrammingError
from valuation.utils.input_output import JSONType, to_json

SafeAny = Union[str, int, datetime.date, None]


def remove_none(variable: Any) -> Any:
    return '' if variable is None else variable


class ResultLine:
    _output_key: str = result.OutputKeys.general
    _registered_output_keys: dict[str, str] = {}

    @property
    def output_key(self) -> str:
        return self._registered_output_keys[self.data[result.ResultType]]

    @property
    def signature(self) -> tuple[SafeAny, ...]:
        return tuple(remove_none(self._data[partial_id]) for partial_id in self._ids)

    @property
    def scales(self) -> list[str]:
        return self._scales

    def __init__(self) -> None:
        self._data: dict[str, Any] = OrderedDict()
        self._ids: list[str] = []
        self._aggregates: list[str] = []
        self._scales: list[str] = []
        name: str = self.__class__.__name__.replace('ResultLine', '')
        self.register(result.ResultType, name, is_id=True)
        self.__class__._registered_output_keys[name] = self._output_key
        # TODO : check this line's role with ali also bring up the race condition

    def register(self, key: str, value: Any, is_id: bool = False, aggregates: bool = False,
                 scales: bool = False) -> None:
        assert not is_id or not (aggregates or scales)
        assert key not in self._data
        if is_id:
            self._ids.append(key)
        if aggregates:
            self._aggregates.append(key)
        if scales:
            self._scales.append(key)
        self._data[key] = value

    @property
    def data(self) -> dict[str, Any]:
        return self._data

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __contains__(self, key: str) -> bool:
        return key in self._data

    def copy(self, ids2cancel: tuple[str, ...] = tuple()) -> ResultLine:
        result_line = ResultLine()
        result_line._ids = copy(self._ids)  # pylint: disable=protected-access      # Copy constructor
        result_line._aggregates = copy(self._aggregates)  # pylint: disable=protected-access      # Copy constructor
        result_line._scales = copy(self._scales)  # pylint: disable=protected-access      # Copy constructor
        result_line._data = copy(self._data)  # pylint: disable=protected-access      # Copy constructor
        for id2cancel in ids2cancel:
            if id2cancel in result_line._data:  # pylint: disable=protected-access      # Copy constructor
                result_line._data[id2cancel] = None  # pylint: disable=protected-access      # Copy constructor
        return result_line

    def __add__(self, other: Optional[ResultLine]) -> Optional[ResultLine]:
        if other is None:
            return None
        assert self.signature == other.signature
        result_line: ResultLine = self.copy()
        for entry in self._data:
            if entry in self._ids:
                continue
            if entry in self._aggregates:
                result_line._data[entry] += other._data[entry]
            elif self._data[entry] != other._data[entry]:
                result_line._data[entry] = None
        for entry in other._data:
            if entry not in self._data:
                result_line._data[entry] = other._data[entry]
        for entry in self._data:
            if entry in self._ids:
                continue
            if result_line._data[entry] is not None:
                return result_line
        return None

    def __mul__(self, other: float) -> ResultLine:
        result_line: ResultLine = self.copy()
        for entry in self._data:
            if entry in self._scales:
                result_line._data[entry] *= other
        return result_line

    def str_precision(self, precision: Optional[int] = None) -> str:
        modifier = ''
        if __debug__:
            modifier = '#'
        result_line: list[str] = [
            f'{entry}{modifier}\t{self._data[entry]}' for entry in self._ids
        ]

        for entry in self._data:
            if entry not in self._ids:
                modifier = ''
                if __debug__:  # TODO: check if needs to be changed
                    if entry in self._scales:
                        modifier += '*'
                    if entry in self._aggregates:
                        modifier += '+'
                value = self._data[entry]
                if isinstance(value, float) and precision is not None:
                    value = float(format(self._data[entry], f'.{precision}g'))
                result_line.append(f'{entry}{modifier}\t{value}')
        return '\n'.join(result_line)

    def __str__(self) -> str:
        return self.str_precision()


@to_json.register
def _(arg: ResultLine, precision: Optional[int] = None) -> JSONType:
    return to_json(arg._data, precision)  # pylint: disable=protected-access   # Friend of Resultline


class ResultLineInstrument(ResultLine):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str) -> None:
        super().__init__()
        self.register(result.InstrumentId, instrument_id, is_id=True)
        self.register(result.SubId, sub_id, is_id=True)
        self.register(result.AddedBy, added_by, is_id=True)


class ResultLineMarketData(ResultLine):
    def __init__(self, instrument_id: str, market_data_id: str, fixing_date: datetime.date, data: dict[str, Any]) -> None:
        super().__init__()
        self.register(result.InstrumentId, instrument_id, is_id=True)
        self.register(result.MarketData, market_data_id, is_id=True)
        self.register(result.FixingDate, fixing_date, is_id=True)
        for key, value in data.items():
            if key in (result.MarketData, result.FixingDate):
                raise ProgrammingError()
            self.register(key, value)


class ResultLinePV(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, unit_amount: float, currency: str) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Currency, currency, is_id=True)
        self.register(result.PV, unit_amount, aggregates=True, scales=True)


class ResultLineCleanDirty(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, clean_price: float, dirty_price: float,
                 currency: str) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Currency, currency, is_id=True)
        self.register(result.CleanPrice, clean_price, aggregates=True)
        self.register(result.DirtyPrice, dirty_price, aggregates=True)
        self.register(result.AccruedAmount, dirty_price - clean_price, aggregates=True)


class ResultLineSimpleCashFlow(ResultLineInstrument):
    _output_key: str = result.OutputKeys.cash_flows

    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, unit_amount: float,
                 discount_factor: Optional[float], currency: str, fixing_date: datetime.date,
                 payment_date: datetime.date, settlement_date: datetime.date, cashflow_type: Optional[str]) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.CashFlow, unit_amount, aggregates=True, scales=True)
        if discount_factor is not None:
            self.register(result.DiscountedFactor, discount_factor)
            self.register(result.UndiscountedCashFlow, unit_amount / discount_factor, aggregates=True, scales=True)
        self.register(result.Currency, currency, is_id=True)
        self.register(result.PaymentDate, payment_date, is_id=True)
        self.register(result.SettlementDate, settlement_date, is_id=True)
        self.register(result.FixingDate, fixing_date, is_id=True)
        self.register(result.CashFlowType, cashflow_type, is_id=True)


class ResultLineBondAdditionalInfo(ResultLineSimpleCashFlow):
    _output_key: str = result.OutputKeys.cash_flows

    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, unit_amount: float,
                 discount_factor: Optional[float], currency: str, fixing_date: datetime.date,
                 payment_date: datetime.date, settlement_date: datetime.date, cashflow_type: Optional[str], leg_number: int,
                 start_date: datetime.date, accrual_start: datetime.date,
                 accrual_end: datetime.date, period_length: int, period_year_frac: float, cum_period_length: float,
                 notional: float, sinking_amount: float, rate: float, fixed_rate: float, forward_rate: float,
                 actual_coupon: float, discounted_coupon: float, discounted_sinking_amount: float,
                 risk_free_discount: float, is_fixed: bool
                 ) -> None:
        super().__init__(instrument_id, sub_id, added_by, unit_amount, discount_factor, currency, fixing_date,
                         payment_date, settlement_date, cashflow_type)
        self.register(result.LegNumber, leg_number, is_id=True)
        self.register(result.StartDate, start_date, is_id=True)
        self.register(result.AccrualStart, accrual_start, is_id=True)
        self.register(result.AccrualEnd, accrual_end, is_id=True)
        self.register(result.PeriodLength, period_length)
        self.register(result.PeriodYearFrac, period_year_frac)
        self.register(result.CumPeriodLength, cum_period_length)
        self.register(result.Notional, notional, scales=True)
        self.register(result.SinkingAmount, sinking_amount, scales=True)
        self.register(result.Rate, rate)
        self.register(result.FixedRate, fixed_rate)
        self.register(result.ForwardRate, forward_rate)
        self.register(result.ActualCoupon, actual_coupon)
        self.register(result.DiscountedCoupon, discounted_coupon)
        self.register(result.DiscountedSinkingAmount, discounted_sinking_amount, scales=True)
        self.register(result.RiskFreeDiscount, risk_free_discount)
        self.register(result.IsFixed, is_fixed)


class ResultLineAmount(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, amount: float, currency: str) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Amount, amount)
        self.register(result.Currency, currency, is_id=True)


class ResultLineInfo(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, issue: datetime.date,
                 maturity: datetime.date) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        if 'Unknown' == issue:  # TODO: find another workaround for this fix
            issue = None
        self.register(result.Issue, issue)
        self.register(result.Maturity, maturity)


class ResultLineGreek(ResultLineInstrument):
    _output_key: str = result.OutputKeys.greeks

    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, greek: str, md_id: str, currency: str,
                 headers: list[str], values: list[float], aggregates: bool = True, scales: bool = True) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Greek, greek, is_id=True)
        self.register(result.MarketData, md_id, is_id=True)
        self.register(result.Currency, currency, is_id=True)
        assert len(headers) == len(values)
        for header, value in zip(headers, values):
            self.register(header, value, aggregates=aggregates, scales=scales)


class ResultLineImpliedZSpread(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, implied_z_spread: float) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.ImpliedZSpread, implied_z_spread)


class ResultLineError(ResultLineInstrument):
    _output_key: str = result.OutputKeys.error

    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, error_message: str) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Error, error_message)


class ResultLineRange(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, currency: str, range_type: str,
                 high_range_info: str, high_range_pv: float, low_range_info: str, low_range_pv: float) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Currency, currency, is_id=True)
        self.register(result.RangeType, range_type, is_id=True)
        self.register(result.RangeHighInfo, high_range_info)
        self.register(result.RangeLowInfo, low_range_info)
        self.register(result.RangeHigh, high_range_pv, aggregates=True, scales=True)
        self.register(result.RangeLow, low_range_pv, aggregates=True, scales=True)


class ResultLineFlexible(ResultLineInstrument):
    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, **kwargs: Any) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        for key, value in kwargs.items():
            self.register(key, value)


class ResultLineMarketDataInfo(ResultLineInstrument):
    _output_key: str = result.OutputKeys.market_data

    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, name: str, instance_id: str,
                 data_type: str) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.MarketDataName, name, is_id=True)
        self.register(result.MarketDataId, instance_id, is_id=True)
        self.register(result.MarketDataType, data_type, is_id=True)


class ResultLineRequestInfo(ResultLineInstrument):
    _output_key: str = result.OutputKeys.request

    def __init__(self, instrument_id: str, sub_id: SafeAny, added_by: str, instrument_type: str, valuation_date: str,
                 valuation_type: str, **kwargs) -> None:
        super().__init__(instrument_id, sub_id, added_by)
        self.register(result.Type, instrument_type, is_id=True)
        self.register(result.ValuationDate, valuation_date, is_id=True)
        self.register(result.ValuationType, valuation_type, is_id=True)
        for key, value in kwargs.items():
            self.register(key, value)
