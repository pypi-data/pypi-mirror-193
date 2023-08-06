from __future__ import annotations

from typing import Any, Callable, Optional, Union

import math
import QuantLib as ql

from valuation.consts import signatures
from valuation.consts.pl import PathDiscount, PathSeparatedDiscount, PathSeparatedValue, PathValue
from valuation.global_settings import __type_checking__
from valuation.engine.process import QLProcess
from valuation.engine.process.path import PathDescriptor, path_generator_factory
from valuation.engine.exceptions import UnsupportedProcessError
from valuation.engine.process.short_rate.surface_calibration import swaption_helpers_diagonal, swaption_helpers_surface
from valuation.engine.market_data import QLInterestRateIndex

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.volatility_surfaces import QLSwaptionVolatility
    from valuation.engine.utils import StockDividends, ModelFixedParameters
    from valuation.engine.process.path import QLPathGenerator
    from valuation.universal_transfer import DefaultParameters, Storage, Period


class QLShortRateProcessBase(QLProcess):  # pylint: disable=abstract-method
    _signature = signatures.empty
    _market_data_types = [signatures.ir_index.base]

    @property
    def scenario_divisor(self) -> float:
        return self._scenario_divisor

    @property
    def shift_unit(self) -> int:
        # TODO(2022/07) should be 10000 (bps)
        return 100

    def __init__(self, data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._scenario_divisor: float = float('NaN')
        self._original_value: float = float('NaN')

        if not self._documentation_mode:
            md_name: str = self._attached_market_data.reference.id
            process2generator_factories: list[Callable[[str, ql.StochasticProcess, list[float], bool, int], QLPathGenerator]] = [path_generator_factory]
            assignments: dict[Union[int, tuple[int, int]], str] = {0: md_name + PathSeparatedValue}
            aliases: dict[str, str] = {
                md_name: md_name + PathSeparatedValue,
                PathValue: md_name + PathSeparatedValue,
                PathDiscount: md_name + PathSeparatedDiscount
            }
            allow_discount: set[str] = {md_name + PathSeparatedDiscount}
            stock_modifier: dict[str, StockDividends] = {}
            summations: dict[str, set[str]] = {}
            self._descriptor = PathDescriptor(
                process2generator_factories,
                assignments,
                aliases,
                allow_discount,
                stock_modifier,
                summations
            )
        self._model_type_ql: type[ql.ShortRateModel]
        self._process_type_ql: type[ql.StochasticProcess]

    def generate_storage(self) -> Storage:
        raise NotImplementedError

    def _generate_process(self) -> ql.StochasticProcess:
        return self._process_type_ql(*self._get_process_params())

    def _get_process_params(self) -> tuple[Any, ...]:
        raise NotImplementedError

    def _get_model_params(self) -> tuple[Any, ...]:
        raise NotImplementedError

    def engine_pricer_tree(self, ql_instrument: QLInstrument, number_time_steps: int) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        model = self._model_type_ql(*self._get_model_params())
        if ql_instrument.signature == signatures.instrument.swaption:
            # SWIGs\shortratemodels.i
            # 	TreeSwaptionEngine --> None
            # 		model	<ShortRateModel>
            # 		timeSteps	Size
            # 		termStructure	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            return ql.TreeSwaptionEngine(model, number_time_steps, ql_instrument.discount_curve.handle), None
        if ql_instrument.signature == signatures.instrument.cap_floor:
            # TODO(2021/12): Investigate if the error from HW also holds for G2
            raise UnsupportedProcessError(
                self.signature,
                signatures.valuation.tree_quantlib,
                instrument=ql_instrument.signature,
                message='Possible bug in the Quantlib library for this particular instrument'
            )
            # SWIGs\shortratemodels.i
            # 	TreeCapFloorEngine --> None
            # 		model	<ShortRateModel>
            # 		timeSteps	Size
            # 		termStructure	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))

            # with an explicite time grid, it works as expected as long as the valuation_date is before the first fixing_date.
            # However, when the valuation_date is after the first fixing_date, one gets
            #   RuntimeError: negative times not allowed
            # The obvious change, i.e. discarding the negative times leads to
            #   RuntimeError: using inadequate time grid: all nodes are later than the required time t = -0.0027397260274 (earliest node is t1 = 0)
            # The first error occurs exactly in the same cases, if we just give the number of time_steps.
            # This is a clear indication, that we do not face a mere calling error, but that there is a major problem with this model within the QL itself.
        if ql_instrument.signature in [signatures.instrument.callable_fixed_bond, signatures.instrument.callable_flexible_bond]:
            # 	TreeCallableFixedRateBondEngine --> None
            # 		model	ext::<ShortRateModel>
            # 		timeSteps	Size
            # 		termStructure	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            if 'hullwhite' in self.signature.sub_type.lower():
                model = ql.HullWhite(*((ql_instrument.discount_curve.handle, ) + self._get_model_params()[1:]))
            return ql.TreeCallableFixedRateBondEngine(model, number_time_steps, ql_instrument.discount_curve.handle), None
        raise UnsupportedProcessError(self.signature, signatures.valuation.tree_quantlib, instrument=ql_instrument.signature)

    def _reference_period_from_instrument(self, instrument_maturity: ql.Date, day_count: ql.DayCounter) -> int:
        return max(1, int(round(day_count.yearFraction(self.valuation_date, instrument_maturity), 0)))

    def _swaption_helpers_diagonal(self, fixed_parameters: ModelFixedParameters, swaption_surface: QLSwaptionVolatility) -> list[ql.SwaptionHelper]:
        assert isinstance(self._attached_market_data, QLInterestRateIndex)
        reference_period_in_years: int = self._reference_period_from_instrument(fixed_parameters.fixed_maturity, fixed_parameters.fixed_daycount)
        return swaption_helpers_diagonal(self.valuation_date, fixed_parameters, self._attached_market_data, swaption_surface, reference_period_in_years)

    def _swaption_helpers_surface(self, max_cum_time: Period, swaption_surface: QLSwaptionVolatility) -> list[ql.SwaptionHelper]:
        assert isinstance(self._attached_market_data, QLInterestRateIndex)
        max_time_in_years = math.ceil(max_cum_time.in_months / 12)
        return swaption_helpers_surface(swaption_surface, max_time_in_years, self._attached_market_data, swaption_surface.daycount)
