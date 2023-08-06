from __future__ import annotations

import math
from typing import Optional, Union

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine import QLObjectBase, QLObjectDB
from valuation.engine.check import ImmDate, ObjectType, Pattern, Range
from valuation.engine.market_data import QLInterestRateIndex, QLYieldCurve
from valuation.engine.utils import period2qlfrequency, period2qlperiod
from valuation.universal_output import result_items
from valuation.universal_transfer import Signature

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObject
    from valuation.engine.mappings import QLBusiness, QLFrequency
    from valuation.universal_transfer import DefaultParameters, Storage, Period


class QLYieldCurveLine(QLObjectBase):               # pylint: disable=abstract-method

    @property
    def curve_point(self) -> Union[ql.OISRateHelper, ql.DepositRateHelper,
                                   ql.FraRateHelper, ql.SwapRateHelper, ql.FuturesRateHelper]:
        return self._curve_point

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._business: QLBusiness = self.data(fields.Business, allow_fallback_to_default_parameters=True)
        self._calendar: ql.Calendar = self.data(fields.Calendar, allow_fallback_to_default_parameters=True)
        self._settlement_days = self.data(fields.SettlementDays,
                                          check=Range(lower=0,
                                                      upper=global_parameters.SettlementDaysMaximum,
                                                      strict=False),
                                          allow_fallback_to_default_parameters=True)
        self._curve_point: Union[ql.OISRateHelper, ql.DepositRateHelper,
                                 ql.FraRateHelper, ql.SwapRateHelper, ql.FuturesRateHelper]


class QLYieldCurveLineCash(QLYieldCurveLine):
    _signature = Signature('Cash')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._rate: float = self.data(fields.FixedRate,
                                      check=Range(lower=global_parameters.InterestRateMinimum,
                                                  upper=global_parameters.InterestRateMaximum))
        self._tenor: Period = self.data(fields.Tenor)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True)

    def _post_init(self) -> None:
        rate: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._rate))
        tenor: ql.Period = period2qlperiod(self._tenor)
        # SWIGs\ratehelpers.i
        # DepositRateHelper (RateHelper)
        # 	DepositRateHelper --> None
        # 		rate	Handle<Quote>
        # 		tenor	Period
        # 		fixingDays	Natural
        # 		calendar	Calendar
        # 		convention	BusinessDayConvention
        # 		endOfMonth	bool
        # 		dayCounter	DayCounter
        self._curve_point = ql.DepositRateHelper(rate,
                                                 tenor,
                                                 self._settlement_days,
                                                 self._calendar,
                                                 self._business,
                                                 False,
                                                 self._daycount)


class QLYieldCurveLineOIS(QLYieldCurveLine):
    _signature = Signature('OIS')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._rate: float = self.data(fields.FixedRate, check=Range(lower=global_parameters.InterestRateMinimum,
                                                                    upper=global_parameters.InterestRateMaximum))
        self._tenor: Period = self.data(fields.Tenor)

    def _post_init(self) -> None:
        rate: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._rate))
        tenor: ql.Period = period2qlperiod(self._tenor)
        empty_yield_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle()
        telescopic_value_dates: bool = False  # No effect
        payment_lag: int = 0  # Effects in the range of 1e-6 for DF
        payment_frequency = ql.Annual  # Effects in the range of 1e-4 for DF
        index: ql.Index = self._master_object.index.ql_index  # type: ignore[union-attr]
        # SWIGs\ratehelpers.i
        # OISRateHelper (RateHelper)
        # 	OISRateHelper --> None
        # 		settlementDays	Natural
        # 		tenor	Period
        # 		rate	Handle<Quote>
        # 		index	<OvernightIndex>
        # 		discountingCurve	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
        # 		telescopicValueDates	bool		(false)
        # 		paymentLag	Natural		(0)
        # 		paymentConvention	BusinessDayConvention		(Following)
        # 		paymentFrequency	Frequency		(Annual)
        # 		paymentCalendar	Calendar		(Calendar ( ))
        # 		forwardStart	Period		(0 * Days)
        # 		overnightSpread	Spread		(0.0)
        self._curve_point = ql.OISRateHelper(self._settlement_days,
                                             tenor,
                                             rate,
                                             index,
                                             empty_yield_curve,
                                             telescopic_value_dates,
                                             payment_lag,
                                             self._business,
                                             payment_frequency,
                                             self._calendar)


class QLYieldCurveLineFRA(QLYieldCurveLine):
    _signature = Signature('FRA')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True)
        self._description: str = self.data(fields.FRADefinition, check=Pattern(r'\d{1,2}x\d{1,2}'))
        self._rate: float = self.data(fields.FixedRate, check=Range(lower=global_parameters.InterestRateMinimum,
                                                                    upper=global_parameters.InterestRateMaximum))

    def _post_init(self) -> None:
        rate: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._rate))
        start_month_as_str, end_month_as_str = self._description.split('x', 1)
        start_month: int = int(start_month_as_str)
        end_month: int = int(end_month_as_str)
        end_of_month: bool = False
        # SWIGs\ratehelpers.i
        # FraRateHelper (RateHelper)
        # 	FraRateHelper --> None
        # 		rate	Handle<Quote>
        # 		monthsToStart	Natural
        # 		monthsToEnd	Natural
        # 		fixingDays	Natural
        # 		calendar	Calendar
        # 		convention	BusinessDayConvention
        # 		endOfMonth	bool
        # 		dayCounter	DayCounter
        # 		pillar	Pillar::Choice		(Pillar::LastRelevantDate)
        # 		customPillarDate	Date		(Date ( ))
        self._curve_point = ql.FraRateHelper(rate,
                                             start_month,
                                             end_month,
                                             self._settlement_days,
                                             self._calendar,
                                             self._business,
                                             end_of_month,
                                             self._daycount)


class QLYieldCurveLineSwap(QLYieldCurveLine):
    _signature = Signature('Swap')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._daycount_fixed: ql.DayCounter = self.data(fields.FixedDayCount, allow_fallback_to_default_parameters=True)
        self._fixed_frequency: Period = self.data(fields.FixedFrequency, allow_fallback_to_default_parameters=True)
        self._tenor: Period = self.data(fields.Tenor)
        self._rate: float = self.data(fields.FixedRate, check=Range(lower=global_parameters.InterestRateMinimum,
                                                                    upper=global_parameters.InterestRateMaximum))

    def _post_init(self) -> None:
        quote: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._rate))
        tenor: ql.Period = period2qlperiod(self._tenor)
        fixed_frequency: QLFrequency = period2qlfrequency(self._fixed_frequency)
        empty_quote: ql.QuoteHandle = ql.QuoteHandle()
        empty_period: ql.Period = ql.Period()
        empty_yield_curve = ql.YieldTermStructureHandle()
        index: ql.Index = self._master_object.index.ql_index  # type: ignore[union-attr]
        # SWIGs\ratehelpers.i
        # SwapRateHelper (RateHelper)
        # 	SwapRateHelper --> None
        # 		rate	Handle<Quote>
        # 		tenor	Period
        # 		calendar	Calendar
        # 		fixedFrequency	Frequency
        # 		fixedConvention	BusinessDayConvention
        # 		fixedDayCount	DayCounter
        # 		index	<IborIndex>
        # 		spread	Handle<Quote>		(Handle<Quote> ( ))
        # 		fwdStart	Period		(0*Days)
        # 		discountingCurve	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
        # 		settlementDays	Natural		(Null<Natural> ( ))
        # 		pillar	Pillar::Choice		(Pillar::LastRelevantDate)
        # 		customPillarDate	Date
        self._curve_point = ql.SwapRateHelper(quote, tenor, self._calendar, fixed_frequency, self._business, self._daycount_fixed, index, empty_quote, empty_period, empty_yield_curve, self._settlement_days)


class QLYieldCurveLineFuture(QLYieldCurveLine):
    _signature = Signature('Future')

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, master_object: Optional[QLObject], data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, master_object, data_only_mode)
        self._valuation_date: ql.Date = self.data(fields.ValuationDate, allow_fallback_to_default_parameters=True)
        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True)
        self._issue: ql.Date = self.data(fields.Issue, check=[Range(lower=self._valuation_date), ImmDate()])
        self._maturity: ql.Date = self.data(fields.Maturity, check=[Range(lower=self._issue), ImmDate()])
        self._mean_reversion: float = self.data(fields.MeanReversion,
                                                check=Range(lower=0, upper=global_parameters.MeanReversionMaximum))
        self._price: float = self.data(fields.Price,
                                       check=Range(lower=global_parameters.FutureMinimum, upper=global_parameters.FutureMaximum))
        self._volatility: float = self.data(fields.VolatilityValue,
                                            check=Range(lower=0.0, upper=global_parameters.VolatilityMaximum))

    def _post_init(self) -> None:
        index: ql.Index = self._master_object.index.ql_index            # type: ignore[union-attr]
        issue_date_adjusted: ql.Date = self._calendar.advance(self._issue, -self._settlement_days, ql.Days)  # pylint: disable=invalid-unary-operand-type
        maturity_date_adjusted: ql.Date = self._calendar.advance(self._maturity, -self._settlement_days, ql.Days)  # pylint: disable=invalid-unary-operand-type
        time2issue: float = self._daycount.yearFraction(self._valuation_date, issue_date_adjusted)
        time2maturity: float = self._daycount.yearFraction(self._valuation_date, maturity_date_adjusted)
        time_difference: float = time2maturity - time2issue
        future_rate: float = (100.0 - self._price) / 100.0
        total_reversion: float = (1.0 - math.exp(-self._mean_reversion * time2issue)) / self._mean_reversion  # pylint: disable=invalid-unary-operand-type
        local_reversion: float = (1.0 - math.exp(-self._mean_reversion * time_difference)) / self._mean_reversion  # pylint: disable=invalid-unary-operand-type
        convexity_adjusted_local_rate: float = (self._volatility * self._volatility / (2.0 * self._mean_reversion)) * local_reversion * (local_reversion * (1 - math.exp(-2.0 * self._mean_reversion * time2issue)) + self._mean_reversion * total_reversion * total_reversion)
        convexity_adjusted_rate: float = (1 - math.exp(-convexity_adjusted_local_rate)) * (future_rate + 1 / time_difference)

        quote_price = ql.QuoteHandle(ql.SimpleQuote(self._price))
        quote_convexity = ql.QuoteHandle(ql.SimpleQuote(convexity_adjusted_rate))

        # SWIGs\ratehelpers.i
        # FuturesRateHelper (RateHelper)
        #   FuturesRateHelper --> None
        # 		price	Handle<Quote>
        # 		iborStartDate	Date
        # 		index	<IborIndex>
        # 		convexityAdjustment	Handle<Quote>		(Handle<Quote> ( ))
        # 		type	Futures::Type		(Futures::IMM)
        self._curve_point = ql.FuturesRateHelper(quote_price, self._issue, index, quote_convexity)


class QLCalibrationCurve(QLYieldCurve):                     # pylint: disable=abstract-method
    _signature = signatures.yield_curve.calibration
    _supported_greeks = (result_items.Rho,)

    @property
    def index(self) -> QLInterestRateIndex:
        return self._index

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self.add_linetype(QLYieldCurveLineCash, fields.InterestRateMarketData)
        self.add_linetype(QLYieldCurveLineOIS, fields.InterestRateMarketData)
        self.add_linetype(QLYieldCurveLineFRA, fields.InterestRateMarketData)
        self.add_linetype(QLYieldCurveLineSwap, fields.InterestRateMarketData)
        self.add_linetype(QLYieldCurveLineFuture, fields.InterestRateMarketData)

        self._index: QLInterestRateIndex = self.data(fields.YieldCurveFreeIRIndex, check=ObjectType(signatures.ir_index.base))

        self._daycount: ql.DayCounter = self.data(fields.DayCount, allow_fallback_to_default_parameters=True)

        self._calendar: ql.Calendar = self.data(fields.Calendar)

        self._currency = self.data(fields.Currency, check=ObjectType(signatures.currency.all))
        self._curve_point_generators = self.data(fields.InterestRateMarketData)

    def _post_init(self) -> None:
        curve_points: list[Union[ql.OISRateHelper, ql.DepositRateHelper,
                                 ql.FraRateHelper, ql.SwapRateHelper, ql.FuturesRateHelper]]\
            = [curve_point_generator.curve_point for curve_point_generator in self._curve_point_generators]

        # SWIGs\piecewiseyieldcurve.i
        # PiecewiseLogLinearDiscount    --> YieldTermStructure
        #   referenceDate   Date
        #   instruments vector<RateHelper>
        #   dayCounter  DayCounter
        #   jumps   vector<Handle<Quote>>       (vector<Handle<Quote>())
        #   jumpDates   vector<Date>        (vector<Date>())
        yield_curve = ql.PiecewiseLogLinearDiscount(self._valuation_date,
                                                    curve_points,
                                                    self._daycount,
                                                    [],
                                                    [])
        self._yc_handle_noshift = ql.YieldTermStructureHandle(yield_curve)  # pylint: disable=attribute-defined-outside-init
        super()._post_init()
