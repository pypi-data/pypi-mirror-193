from __future__ import annotations

import datetime

import QuantLib as ql

from valuation.consts import signatures, global_parameters
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import QLObject, QLAlias
from valuation.engine.check import Equals, Range, RangeWarning, ObjectType
from valuation.engine.market_data import QLMarketData
from valuation.engine.utils import period2qlperiod
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.market_data import QLInterestRateIndex
    from valuation.universal_transfer import DefaultParameters, Storage


class InterestRateSwapIndex(QLAlias):
    _signature = signatures.ir_swap_index_alias


class QLInterestRateSwapIndex(QLMarketData):  # pylint: disable=abstract-method
    _signature = signatures.ir_swap_index

    @property
    def ql_swap_index(self) -> ql.SwapIndex:
        return self._swap_index

    @property
    def ql_index(self) -> QLInterestRateIndex:
        return self._index

    @property
    def period(self) -> Period:
        return self._period

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._index: QLInterestRateIndex = self.data(fields.IRIndex, check=ObjectType(signatures.ir_index.base))
        self._fixed_leg_tenor: Period = self.data(fields.FixedFrequency)
        self._period: Period = self.data(fields.Period)
        self._enable_extrapolation: bool = self.data(fields.EnableExtrapolation, default_value=True)
        self._calendar = self._index.calendar

        self._swap_index: ql.SwapIndex
        if self._documentation_mode:
            return
        self._set_index()

    def _set_index(self) -> None:
        # SWIGs\indexes.i
        # 	SwapIndex --> None
        # 		familyName	string
        # 		tenor	Period
        # 		settlementDays	Integer
        # 		currency	Currency
        # 		calendar	Calendar
        # 		fixedLegTenor	Period
        # 		fixedLegConvention	BusinessDayConvention
        # 		fixedLegDayCounter	DayCounter
        # 		iborIndex	<IborIndex>

        index_name: str = self.reference.id + '_' + datetime.datetime.now().isoformat()

        self._swap_index = ql.SwapIndex(
            index_name,
            period2qlperiod(self._period),
            self._index.ql_index.fixingDays(),
            self._index.ql_index.currency(),
            self._index.calendar,
            period2qlperiod(self._fixed_leg_tenor),
            ql.Unadjusted,
            self._index.daycount,
            self._index.ql_index
        )

    def _post_init(self) -> None:
        for date, rate in self._fixings.items():
            if not self._calendar.isHoliday(date):
                self._swap_index.addFixing(date, rate)

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        if date <= self._valuation_date:
            rate = super().__getitem__(date)
            if not self._calendar.isHoliday(date):
                self._swap_index.addFixing(date, rate)
        else:
            engine = ql.DiscountingSwapEngine(self._index.yield_curve.handle)
            fixed_leg_tenor = period2qlperiod(self._fixed_leg_tenor)
            swap_tenor = period2qlperiod(self._period)
            forward_start = ql.Period(date - self._valuation_date, ql.Days)

            swap = ql.MakeVanillaSwap(swap_tenor, self._index.ql_index, 0.0, forward_start, fixedLegTenor=fixed_leg_tenor, pricingEngine=engine)
            rate = swap.fairRate()
        return rate


class QLInterestRateSpreadIndex(QLMarketData):  # pylint: disable=abstract-method
    _signature = signatures.ir_spread_index
    _initializes_past = False

    @property
    def ql_spread_index(self) -> QLInterestRateIndex:
        return self._spread_index       # type: ignore[no-any-return]

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._index_positive: QLInterestRateSwapIndex = self.data(fields.IRSwapIndexPositive, check=ObjectType(signatures.ir_swap_index))
        self._index_negative: QLInterestRateSwapIndex = self.data(fields.IRSwapIndexNegative, check=ObjectType(signatures.ir_swap_index))
        self._gearing_positive: float = self.data(
            fields.GearingPositive,
            default_value=1.0,
            check=[
                Range(lower=0.0),
                RangeWarning(upper=global_parameters.GearingMaximum, strict=False)
            ]
        )
        self._gearing_negative: float = self.data(
            fields.GearingNegative,
            default_value=-1.0,
            check=[
                Range(upper=0.0),
                RangeWarning(lower=global_parameters.GearingMinimum, strict=False)
            ]
        )
        self.check(self._index_negative.ql_index, Equals(self._index_positive.ql_index))

        self._spread_index: ql.SwapSpreadIndex

    def _post_init(self) -> None:
        index_name: str = self.reference.id + '_' + datetime.datetime.now().isoformat()
        # SwapSpreadIndex (InterestRateIndex)
        # 		familyName	string
        # 		swapIndex1	ext::<SwapIndex>
        # 		swapIndex2	ext::<SwapIndex>
        # 		gearing1	Real		(1.0)
        # 		gearing2	Real		(-1.0)
        self._spread_index = ql.SwapSpreadIndex(index_name, self._index_positive.ql_swap_index, self._index_negative.ql_swap_index, self._gearing_positive, self._gearing_negative)

    @QLObject.static
    def __getitem__(self, date: ql.Date) -> float:
        return self._index_positive[date] - self._index_negative[date]
