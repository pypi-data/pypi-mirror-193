from __future__ import annotations

from math import sqrt
from typing import Callable, Optional, Union

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.consts.pl import PathCMSLong, PathCMSShort, PathDiscount, PathSeparatedDiscount, PathSeparatedSummation, PathSeparatedValue, PathValue
from valuation.global_settings import __type_checking__
from valuation.engine import QLObjectDB
from valuation.engine.check import Equals, ObjectType, Range
from valuation.engine.market_data import QLInterestRateSwapIndex, QLMarketDataBasket
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, QLPathGenerator, path_generator_factory
from valuation.engine.utils import add_tenor
from valuation.engine.volatility_surfaces import QLSwaptionVolatility
from valuation.universal_transfer import DefaultParameters, Period, STORAGE_ID_SEPARATOR, Storage

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.utils import StockDividends
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.process import QLHullWhiteProcessBase


# Hull White Model:
# dr(t) = (R(t) - \alpha r(t)) dt + \sigma dW(t)
# R: Expected interest rate
# \alpha: mean reversion
# \sigma: Volatility

# FB 05/2021:
# Our Model for CMS:
# The following model is very hands-on and needs to be replaced eventually by a better one.
# We assume that we have the following:
#   *   The short rate and the shorter CMS rate are determined as in the CMS case.
#   *   The longer CMS rate is another Hull-White-Process on top.
#       -   I.e. the yield-curve entering needs to be modified!
#       -   The volatility is chosen using the short end volatility of the vol-cube and modified according to the time span by the shorter CMS vol.
#           Vol_long^2 * t_long = Vol_short^2 * t_short + Vol_spread^2 (t_long - t_short)
#           ==>
#           Vol_spread^2 = (Vol_long^2 * t_long - Vol_short^2 * t_short) / (t_long - t_short)
#       -   the mean reversion is copied from the underlying short rate process
# This has the following advantages:
#   *   We have a relatively easy task for calibrating the model, as calibration is performed for the short rate only
#   *   Expected Values will be met
#   *   Volatilities are roughly met
#   ( Todo: Most probably the volatility needs to be changed such that the processes are identical. The above equality just holds for non-mean reverting)
#   *   we do not need to perform a convexity correction
#   *   For the shorter CMS rate, the results are identical to the one in the CMS case, for the longer they should be similar (perhaps after slight modificaiton of the volatility)
# This has the following disadvantages
#   *   Bond pricing or caps and floors will not necessarily fall under the no-arbitrage condition.
#   *   We do not use the full capabilities of the model, as major components are fixed in advance:


class QLCMSSpreadProcess(QLProcess):  # pylint: disable=abstract-method
    _signature = signatures.process.cms_spread

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super(QLProcess, self).__init__(data, ql_db, default_parameters, data_only_mode)  # pylint: disable=bad-super-call

        self._short_rate_process: QLHullWhiteProcessBase = self.data(fields.ShortRateProcess, check=ObjectType(
            [signatures.process.hull_white, signatures.process.hull_white_calibration, signatures.process.hull_white_calibration_no_instrument]))
        self._swap_index_short: QLInterestRateSwapIndex = self.data(fields.IRSwapIndexShort, check=ObjectType(signatures.ir_swap_index))
        self._swap_index_long: QLInterestRateSwapIndex = self.data(fields.IRSwapIndexLong, check=ObjectType(signatures.ir_swap_index))
        self.check(self._short_rate_process.attached_market_data, Equals(self._swap_index_short.ql_index))
        self.check(self._short_rate_process.attached_market_data, Equals(self._swap_index_long.ql_index))
        self.check(self._swap_index_long.period, Range(lower=self._swap_index_short.period))
        self._surface: QLSwaptionVolatility = self.data(fields.SwaptionVolatility, check=ObjectType(signatures.swaption_volatility.surface), exclude_from_greeks=True)
        self._cms_diff_rates_short: ql.YieldTermStructureHandle
        self._cms_volatility_short: float
        self._cms_mean_reversion_short: float
        self._cms_diff_rates_long: ql.YieldTermStructureHandle
        self._cms_volatility_long: float
        self._cms_mean_reversion_long: float

        if not self._documentation_mode:
            self._attached_market_data = generate_dummy_cms_spread_basket(self, self._short_rate_process, self._swap_index_short, self._swap_index_long)
            md_name: str = self._short_rate_process.attached_market_data.reference.id
            cms_name_short: str = self._swap_index_short.reference.id
            cms_name_long: str = self._swap_index_long.reference.id
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory, path_generator_factory,
                                                                                                                                 path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {0: md_name + PathSeparatedValue,
                                                                   1: cms_name_short + PathSeparatedValue,
                                                                   2: cms_name_long + PathSeparatedValue}
            aliases: dict[str, str] = {md_name: md_name + PathSeparatedValue,
                                       PathValue: md_name + PathSeparatedValue,
                                       PathDiscount: md_name + PathSeparatedDiscount,
                                       PathCMSShort: cms_name_short + PathSeparatedSummation,
                                       PathCMSLong: cms_name_long + PathSeparatedSummation}
            allow_discount: set[str] = {md_name + PathSeparatedDiscount}
            stock_modifier: dict[str, StockDividends] = {}
            summations = {cms_name_short + PathSeparatedSummation: {md_name + PathSeparatedValue, cms_name_short + PathSeparatedValue},
                          cms_name_long + PathSeparatedSummation: {md_name + PathSeparatedValue, cms_name_short + PathSeparatedValue, cms_name_long + PathSeparatedValue}}
            self._descriptor = PathDescriptor(process2generator_factories, assignments, aliases, allow_discount, stock_modifier, summations)

    def _post_init(self) -> None:
        curve_dates_short: list[ql.Date] = []
        curve_dates_long: list[ql.Date] = []
        cms_diff_rates_short: list[float] = []
        cms_diff_rates_long: list[float] = []
        calendar = self._swap_index_short.ql_index.calendar
        business = self._swap_index_short.ql_index.business
        # Yearly support points up to 50 years for determining the difference of the cms curve
        # and the underlying short rate curve.
        for year in range(50):
            if year == 0:
                date = add_tenor(self.valuation_date, Period(1, 'D'), calendar, business, 0)
            else:
                date = add_tenor(self.valuation_date, Period(year, 'Y'), calendar, business, 0)
            try:
                cms_diff_rates_short.append(self._swap_index_short[date] - self._short_rate_process[date])
                curve_dates_short.append(date)
            except Exception:  # pylint: disable=broad-except
                break

        # SWIGs\zerocurve.i
        # template(ZeroCurve) InterpolatedZeroCurve<Linear>
        # template <class Interpolator>
        # InterpolatedZeroCurve --> None
        #       dates           vector<Date>
        #       yields          vector<Rate>
        #       dayCounter      DayCounter
        #       calendar        Calendar            (Calendar())
        #       i               Interpolator        (Linear)
        #       compounding     Compounding         (Continuous)
        #       frequency       Frequency           (Annual)
        self._cms_diff_rates_short = ql.YieldTermStructureHandle(ql.ForwardCurve(curve_dates_short, cms_diff_rates_short, self._swap_index_short.ql_index.daycount))  # TODO: check if compounding is used correctly here
        self._cms_volatility_short = self._surface.short_term_swaption_volatility(self._swap_index_short.period)
        self._cms_mean_reversion_short = self._short_rate_process.mean_reversion

        for year in range(50):
            if year == 0:
                date = add_tenor(self.valuation_date, Period(1, 'D'), calendar, business, 0)
            else:
                date = add_tenor(self.valuation_date, Period(year, 'Y'), calendar, business, 0)
            try:
                cms_diff_rates_long.append(self._swap_index_long[date] - self._swap_index_short[date])
                curve_dates_long.append(date)
            except Exception:  # pylint: disable=broad-except
                break
        self._cms_diff_rates_long = ql.YieldTermStructureHandle(ql.ForwardCurve(curve_dates_long, cms_diff_rates_long, self._swap_index_long.ql_index.daycount))
        time_short = self._swap_index_short.period.in_months  # pylint: disable=protected-access
        time_long = self._swap_index_long.period.in_months  # pylint: disable=protected-access
        volatility_long = self._surface.short_term_swaption_volatility(self._swap_index_long.period)
        self._cms_volatility_long = sqrt(
            (volatility_long * volatility_long * time_long - self._cms_volatility_short * self._cms_volatility_short * time_short) / (time_long - time_short))
        self._cms_mean_reversion_long = self._short_rate_process.mean_reversion

    def _generate_process(self) -> ql.StochasticProcess:
        # SWIGs\stochasticprocess.i
        # HullWhiteProcess --> None
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		a	Real
        # 		sigma	Real
        cms_process_short = ql.HullWhiteProcess(self._cms_diff_rates_short, self._cms_mean_reversion_short, self._cms_volatility_short)
        cms_process_long = ql.HullWhiteProcess(self._cms_diff_rates_long, self._cms_mean_reversion_long, self._cms_volatility_long)
        return [self._short_rate_process._generate_process(), cms_process_short, cms_process_long]  # pylint: disable=protected-access

    def engine_pricer_tree(self, ql_instrument: QLInstrument, number_time_steps: int) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        return self._short_rate_process.engine_pricer_tree(ql_instrument, number_time_steps)


def generate_dummy_cms_spread_basket(cms_spread_process: QLCMSSpreadProcess, short_rate_process: QLProcess, swap_index_short: QLInterestRateSwapIndex,
                                     swap_index_long: QLInterestRateSwapIndex) -> QLMarketDataBasket:
    dummy_basket = Storage()
    dummy_basket[fields.Type] = signatures.market_data_basket.type
    dummy_basket[fields.SubType('MarketData')] = signatures.index_and_cms_spread.sub_type
    dummy_basket[fields.MarketDataBasket] = (short_rate_process.attached_market_data.reference, swap_index_short.reference, swap_index_long.reference)
    dummy_basket.make_immutable()
    dummy_basket.assign_post_mutable_id(cms_spread_process.reference.id + STORAGE_ID_SEPARATOR + 'DUMMY')
    cms_spread_process.ql_db.storage_db.add(dummy_basket)  # type: ignore[union-attr]
    return cms_spread_process.ql_db[dummy_basket.reference]  # type: ignore[return-value]
