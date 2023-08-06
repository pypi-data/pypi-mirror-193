from __future__ import annotations

import math
from contextlib import contextmanager
from typing import Generator, Optional, Union

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import ObjectType
from valuation.engine.exceptions import UnsupportedProcessError
from valuation.engine.exceptions import UnsupportedValuationError
from valuation.engine.market_data import QLMarketData
from valuation.engine.process.path import Path, PathDescriptor, SimulatedPath
from valuation.universal_transfer import STORAGE_ID_SEPARATOR, Storage
from valuation.utils.other import listify

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.instrument.coupons.base_object import CouponDescriptor, QLCoupon
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Signature


class QLProcess(QLMarketData):                             # pylint: disable=abstract-method
    _signature = signatures.process.base
    _initializes_past = False
    _market_data_types: list[Signature] = []

    @property
    def attached_market_data(self) -> QLMarketData:
        return self._attached_market_data

    def __getitem__(self, date: ql.Date) -> float:
        return self._attached_market_data[date]

    @contextmanager
    def descriptor(self) -> Generator[PathDescriptor, None, None]:
        try:
            self._descriptor.attach_processes(listify(self._generate_process()))
            yield self._descriptor
        except Exception as exception:
            raise exception
        finally:
            self._descriptor.clear_processes()

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        if self._market_data_types:
            self._attached_market_data: QLMarketData = self.data(fields.MarketData, check=ObjectType(self._market_data_types))
        else:
            self._attached_market_data = self.data(fields.MarketData, default_value=None)
        self._market_data_names: list[str] = ['SingleUnderlying']

        self._descriptor: PathDescriptor

    def _generate_process(self) -> ql.StochasticProcess:
        raise NotImplementedError

    def paths(self, simulation_times: list[float], observation_mask: dict[int, ql.Date], continuous_mask: dict[int, bool], non_observation_dates: dict[ql.Date, float], simulation_time_map: dict[int, float], log_number_of_paths: int, generator_type: str, brownian_bridge: bool, antithetic: bool) -> Generator[Path, None, None]:

        descriptor: PathDescriptor
        with self.descriptor() as descriptor:
            path = Path(observation_mask, continuous_mask, non_observation_dates, simulation_times, simulation_time_map, self, descriptor)
            if len(simulation_times) > 1:
                simulated_path = SimulatedPath(descriptor, path, generator_type, simulation_times, brownian_bridge, antithetic)
                for __ in range(2 ** log_number_of_paths):
                    next(simulated_path)            # type: ignore[call-overload]       # pylint: disable=stop-iteration-return
                    yield path
            else:
                yield path

    def coupon_pricer_analytic(self, ql_object: Union[QLInstrument, CouponDescriptor]) -> ql.FloatingRateCouponPricer:  # pylint: disable=no-self-use
        if ql_object.signature in (signatures.instrument.float_bond, signatures.coupon.floating):
            pricer: ql.IborCouponPricer = ql.BlackIborCouponPricer()
            # SWIGs\volatilities.i
            # 	ConstantOptionletVolatility --> None
            # 		settlementDays	Natural
            # 		cal	Calendar
            # 		bdc	BusinessDayConvention
            # 		volatility	Volatility
            # 		dayCounter	DayCounter
            # 		type	VolatilityType		(ShiftedLognormal)
            # 		shift	Real		(0.0)
            volatility: ql.OptionletVolatilityStructure = \
                ql.ConstantOptionletVolatility(ql_object.settlement_days,  # type: ignore[union-attr]
                                               ql_object.calendar,  # type: ignore[union-attr]
                                               ql_object.business,  # type: ignore[union-attr]
                                               0.0,
                                               ql_object.daycount,
                                               ql.Normal)
            pricer.setCapletVolatility(ql.OptionletVolatilityStructureHandle(volatility))
            return pricer
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_object.signature)

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:       # pylint: disable=no-self-use, unused-argument
        if ql_instrument.signature in (signatures.instrument.zero_bond, signatures.instrument.fixed_bond, signatures.leg_operator):
            return ql.DiscountingBondEngine(ql_instrument.discount_curve.handle), None
        if ql_instrument.signature == signatures.instrument.float_bond:                                                                          # pylint: disable=unidiomatic-typecheck
            engine = ql.DiscountingBondEngine(ql_instrument.discount_curve.handle)
            return engine, self.coupon_pricer_analytic(ql_instrument)
        if ql_instrument.signature == signatures.instrument.vanilla_swap:                                      # pylint: disable=unidiomatic-typecheck
            return ql.DiscountingSwapEngine(ql_instrument.discount_curve.handle), None
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)

    def engine_pricer_tree(self, ql_instrument: QLInstrument, number_time_steps: int) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        raise UnsupportedProcessError(self.signature, signatures.valuation.tree_quantlib, instrument=ql_instrument.signature)

    def _option_engine_pricer_analytic(self, ql_instrument: QLInstrument, vanilla_option: Optional[Signature], continuous_barrier_option: Optional[Signature]) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        if vanilla_option and ql_instrument.signature == vanilla_option:
            if vanilla_option == signatures.instrument.stock_european_option:
                start_value: float = self._attached_market_data[self._valuation_date]
                start_value_stripped: float = self._attached_market_data.stock_dividends.inverse(self._valuation_date, start_value)     # type: ignore[attr-defined]
                if not math.isclose(start_value, start_value_stripped):  # Temporal non-invasive but sufficient test for non zero cash dividends
                    # TODO(2021/11) While the start value of the ql.Process is stripped accordingly of the discounted cumulative cash dividends,
                    #  the successive cash dividend adjustments for date > valuation_date are currently attained only by the FinancialProgram via _attached_market_data.__getitem__(date)
                    raise UnsupportedValuationError(signatures.valuation.analytic_quantlib, ql_instrument.signature, message=f'Cash dividends currently not supported for {self.signature}, use {signatures.valuation.financial_program}')
                # SWIGs\options.i
            # 	AnalyticEuropeanEngine --> None
            # 		[UNKNOWN]	<GeneralizedBlackScholesProcess>
            engine = ql.AnalyticEuropeanEngine(self._generate_process())
            return engine, None
        if continuous_barrier_option and ql_instrument.signature == continuous_barrier_option:
            if continuous_barrier_option == signatures.instrument.stock_continuous_barrier_option:
                start_value = self._attached_market_data[self._valuation_date]
                start_value_stripped = self._attached_market_data.stock_dividends.inverse(self._valuation_date, start_value)        # type: ignore[attr-defined]
                if not math.isclose(start_value, start_value_stripped):
                    raise UnsupportedValuationError(signatures.valuation.analytic_quantlib, ql_instrument.signature, message=f'Cash dividends currently not supported for {self.signature}, use {signatures.valuation.financial_program}')
            if ql_instrument.double_barrier:  # type: ignore[attr-defined]
                # SWIGs\options.i
                # 	AnalyticDoubleBarrierEngine --> None
                # 		process	<GeneralizedBlackScholesProcess>
                # 		series	int		(5)
                # NOTE: the formula holds only when strike is in the barrier range
                engine = ql.AnalyticDoubleBarrierEngine(self._generate_process())
                return engine, None
            # SWIGs\options.i
            #   AnalyticBarrierEngine --> None
            # 		[UNKNOWN]	<GeneralizedBlackScholesProcess>
            engine = ql.AnalyticBarrierEngine(self._generate_process())
            return engine, None
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)


def generate_dummy_process(ql_object: Union[QLMarketData, QLInstrument, QLCoupon]) -> QLProcess:
    dummy_process = Storage()
    dummy_process[fields.Type] = 'Process'
    if ql_object.signature.type not in (
    signatures.instrument.all.type, signatures.coupon.fixed.type, signatures.coupon.floating.type, signatures.coupon.capped_floored.type, signatures.coupon.cms.type):
        dummy_process[fields.MarketData] = ql_object.reference
    dummy_process.make_immutable()
    dummy_process.assign_post_mutable_id(ql_object.reference.id + STORAGE_ID_SEPARATOR + 'DUMMY')
    if dummy_process.reference not in ql_object.ql_db.storage_db:           # type: ignore[operator]
        ql_object.ql_db.storage_db.add(dummy_process)                       # type: ignore[union-attr]
    return ql_object.ql_db[dummy_process.reference]                         # type: ignore[return-value]
