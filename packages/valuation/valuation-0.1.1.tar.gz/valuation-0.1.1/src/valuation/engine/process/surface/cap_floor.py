from __future__ import annotations

from contextlib import contextmanager
from typing import Generator, Optional, Union

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import UnsupportedProcessError
from valuation.engine.mappings import VolatilityType
from valuation.engine.process import QLProcess

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.instrument.coupons.base_object import CouponDescriptor
    from valuation.engine.process.path import PathDescriptor
    from valuation.engine.volatility_surfaces import QLCapFloorVolatility
    from valuation.universal_transfer import DefaultParameters, Storage


class QLCapFloorVolatilityProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.cap_floor_volatility
    _market_data_types = [signatures.ir_index.base]

    @contextmanager
    def descriptor(self) -> Generator[PathDescriptor, None, None]:
        raise UnsupportedProcessError(self.signature, (signatures.valuation.financial_program,))  # TODO(2021/20) signatures.valuation.monte_carlo/ql_monte_carlo

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._surface: QLCapFloorVolatility = self.data(fields.CapFloorVolatility)
        self._enable_extrapolation: bool = self.data(fields.EnableExtrapolation, default_value=True)

    def _generate_process(self) -> ql.StochasticProcess:
        raise NotImplementedError

    def _get_vol_handle(self) -> ql.OptionletVolatilityStructureHandle:
        # SWIGs\old_volatility.i
        # 	OptionletStripper1
        # 		parVolSurface	<CapFloorTermVolSurface>
        # 		index	<IborIndex>
        # 		switchStrikes	Rate		(Null<Rate> ( ))
        # 		accuracy	Real		(1.0e-6)
        # 		maxIter	Natural		(100)
        # 		discount	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
        # 		type	VolatilityType		(ShiftedLognormal)
        # 		displacement	Real		(0.0)
        # 		dontThrow	bool		(false)

        optionlet_stripper = ql.OptionletStripper1(
            self._surface.ql_surface,
            self._attached_market_data.ql_index,  # type: ignore[attr-defined]
            type=self._surface.distribution,
            dontThrow=True
        )

        # SWIGs\old_volatility.i
        # 	StrippedOptionletAdapter
        # 		[UNKNOWN]	<StrippedOptionletBase>
        optionlet_adapter = ql.StrippedOptionletAdapter(optionlet_stripper)
        vol_handle = ql.OptionletVolatilityStructureHandle(optionlet_adapter)
        if self._enable_extrapolation:
            vol_handle.enableExtrapolation()
        return vol_handle

    def coupon_pricer_analytic(self, ql_object: Union[QLInstrument, CouponDescriptor]) -> ql.FloatingRateCouponPricer:
        if ql_object.signature in (signatures.instrument.cap_floor, signatures.coupon.capped_floored):  # pylint: disable=unidiomatic-typecheck
            pricer: ql.BlackIborCouponPricer = ql.BlackIborCouponPricer()
            pricer.setCapletVolatility(self._get_vol_handle())
            return pricer
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_object.signature)

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        if ql_instrument.signature == signatures.instrument.cap_floor:
            if self._surface.distribution == VolatilityType['Normal']:
                # SWIGs\capfloor.i
                # 	BachelierCapFloorEngine --> None
                # 		termStructure	Handle<YieldTermStructure>
                # 		vol	Handle<OptionletVolatilityStructure>
                return ql.BachelierCapFloorEngine(ql_instrument.discount_curve.handle, self._get_vol_handle()), None
            # SWIGs\capfloor.i
            # 	BlackCapFloorEngine --> None
            # 		termStructure	Handle<YieldTermStructure>
            # 		vol	Handle<OptionletVolatilityStructure>
            return ql.BlackCapFloorEngine(ql_instrument.discount_curve.handle, self._get_vol_handle()), None
        if ql_instrument.signature == signatures.leg_operator:
            return super().engine_pricer_analytic(ql_instrument)
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)
