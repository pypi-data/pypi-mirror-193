from __future__ import annotations

from typing import Optional
import QuantLib as ql

from valuation.global_settings import __type_checking__
from valuation.engine.utils import ModelFixedParameters, period2qlperiod
from valuation.engine.volatility_surfaces import QLSwaptionVolatility
from valuation.universal_transfer import Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.market_data import QLInterestRateIndex


def swaption_helper(swaption_expiration: Period,
                    swap_duration: Period,
                    volatility: float,
                    attached_index: QLInterestRateIndex,
                    fixed_leg_daycount: ql.DayCounter,
                    volatility_type: int,
                    strike: float = 0.0,
                    shift: float = 0.0) -> ql.SwaptionHelper:
    # 	SwaptionHelper --> None
    # 		maturity	Period
    # 		length	Period
    # 		volatility	Handle<Quote>
    # 		index	ext::<IborIndex>
    # 		fixedLegTenor	Period
    # 		fixedLegDayCounter	DayCounter
    # 		floatingLegDayCounter	DayCounter
    # 		termStructure	Handle<YieldTermStructure>
    # 		errorType	BlackCalibrationHelper::CalibrationErrorType		(BlackCalibrationHelper::RelativePriceError)
    # 		strike	Real		(Null<Real> ( ))
    # 		nominal	Real		(1.0)
    # 		type	VolatilityType		(ShiftedLognormal)
    # 		shift	Real		(0.0)
    strike_ql = ql.nullDouble() if strike == 0.0 else strike
    helper = ql.SwaptionHelper(
        period2qlperiod(swaption_expiration),
        period2qlperiod(swap_duration),
        ql.QuoteHandle(ql.SimpleQuote(volatility)),
        attached_index.ql_index,
        attached_index.ql_index.tenor(),
        fixed_leg_daycount,
        attached_index.daycount,
        attached_index.yield_curve.handle,
        ql.BlackCalibrationHelper.RelativePriceError,
        strike_ql,
        1.0,
        volatility_type,
        shift
    )
    return helper


def tenors_from_reference_period_diagonal(reference_period_in_years: int, negative_offset: int = 1, positive_offset: int = 1) -> list[tuple[Period, Period]]:
    expiries_and_swap_lengths: list[tuple[Period, Period]] = []
    for reference_step in range(reference_period_in_years - negative_offset, reference_period_in_years + positive_offset + 1):
        for option_expiry in range(1, reference_step):
            swap_length: int = reference_step - option_expiry
            expiries_and_swap_lengths.append((Period(option_expiry, 'Y'), Period(swap_length, 'Y')))
    return expiries_and_swap_lengths


def tenors_and_volatility_standard(surface: QLSwaptionVolatility, reference_period_in_years: Optional[int]) -> list[tuple[Period, Period, float]]:
    expiries_and_swap_lengths: list[tuple[Period, Period, float]] = []
    max_period: Optional[Period] = Period(reference_period_in_years, 'Y') if reference_period_in_years is not None else None
    for calibration_data in surface.calibration_data():
        option_expiry: Period = calibration_data.option_tenor
        swap_length: Period = calibration_data.swap_tenor
        volatility: float = calibration_data.volatility
        if max_period and option_expiry + swap_length > max_period:
            continue
        expiries_and_swap_lengths.append((option_expiry, swap_length, volatility))
    return expiries_and_swap_lengths


def swaption_helpers_diagonal(valuation_date: ql.Date,
                              fixed_parameters: ModelFixedParameters,
                              attached_market_data: QLInterestRateIndex,
                              surface: QLSwaptionVolatility,
                              reference_period: int) -> list[ql.SwaptionHelper]:
    swaption_helpers: list[ql.SwaptionHelper] = []
    tenors: list[tuple[Period, Period]] = tenors_from_reference_period_diagonal(reference_period)
    for tenor in tenors:
        swaption_expiry: Period = tenor[0]
        swap_length: Period = tenor[1]
        expiry_date = valuation_date + period2qlperiod(swaption_expiry)
        handle: ql.SwaptionVolatilityStructureHandle = ql.SwaptionVolatilityStructureHandle(surface.ql_surface)
        volatility: float = handle.volatility(
            expiry_date,
            period2qlperiod(swap_length),
            fixed_parameters.fixed_rate  # This not used for matrices (ql.SwaptionVolatilityMatrix)
        )
        swaption_helpers.append(
            swaption_helper(
                swaption_expiry,
                swap_length,
                volatility,
                attached_market_data,
                fixed_parameters.fixed_daycount,
                surface.ql_surface.volatilityType()
            )
        )
    return swaption_helpers


def swaption_helpers_surface(surface: QLSwaptionVolatility,
                             reference_period: int,
                             attached_market_data: QLInterestRateIndex,
                             fixed_day_count: ql.DayCounter) -> list[ql.SwaptionHelper]:
    swaption_helpers: list[ql.SwaptionHelper] = []
    tenors_and_volatility: list[tuple[Period, Period, float]] = tenors_and_volatility_standard(surface, reference_period)
    for tenor_and_volatility in tenors_and_volatility:
        helper: ql.SwaptionHelper = swaption_helper(
            tenor_and_volatility[0],
            tenor_and_volatility[1],
            tenor_and_volatility[2],
            attached_market_data,
            fixed_day_count,
            surface.ql_surface.volatilityType()
        )
        swaption_helpers.append(helper)
    return swaption_helpers
