from __future__ import annotations

from contextlib import contextmanager
from typing import Generator, Optional, Union

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.check import Range
from valuation.engine.exceptions import UnsupportedProcessError
from valuation.engine.mappings import VolatilityType
from valuation.engine.process import QLProcess

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.instrument.coupons.base_object import CouponDescriptor
    from valuation.engine.process.path import PathDescriptor
    from valuation.engine.volatility_surfaces import QLSwaptionVolatility
    from valuation.universal_transfer import DefaultParameters, Storage


class QLSwaptionVolatilityProcess(QLProcess):                             # pylint: disable=abstract-method
    _signature = signatures.process.swaption_volatility
    _market_data_types = [signatures.ir_index.base]

    @property
    def ql_surface(self) -> ql.SwaptionVolatilityMatrix:
        return self._surface.ql_surface

    @contextmanager
    def descriptor(self) -> Generator[PathDescriptor, None, None]:
        raise UnsupportedProcessError(self.signature, (signatures.valuation.financial_program,))  # TODO(2021/20) signatures.valuation.monte_carlo/ql_monte_carlo

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._surface: QLSwaptionVolatility = self.data(fields.SwaptionVolatility)
        self._mean_reversion: float = self.data(fields.MeanReversion, default_value=0.3, check=Range(lower=0.0))
        self._cms_spread_correlation: float = self.data(fields.SpreadCorrelation, default_value=0.2, check=Range(lower=0.0, upper=0.9))

    def coupon_pricer_analytic(self, ql_object: Union[QLInstrument, CouponDescriptor]) -> ql.FloatingRateCouponPricer:
        if ql_object.signature == signatures.coupon.cms:  # pylint: disable=unidiomatic-typecheck

            swaption_volamatrix_handle = ql.SwaptionVolatilityStructureHandle(self._surface.ql_surface)
            if self._surface.enable_extrapolation:
                swaption_volamatrix_handle.enableExtrapolation()

            # SWIGs\cashflows.i
            # 	LinearTsrPricer --> None
            # 		swaptionVol	Handle<SwaptionVolatilityStructure>
            # 		meanReversion	Handle<Quote>
            # 		couponDiscountCurve	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            # 		settings	LinearTsrPricer::Settings		(LinearTsrPricer::Settings ( ))
            pricer = ql.LinearTsrPricer(swaption_volamatrix_handle, ql.QuoteHandle(ql.SimpleQuote(self._mean_reversion)))
            return pricer
        if ql_object.signature == signatures.coupon.cms_spread:
            swaption_volamatrix_handle = ql.SwaptionVolatilityStructureHandle(self._surface.ql_surface)
            if self._surface.enable_extrapolation:
                swaption_volamatrix_handle.enableExtrapolation()

            # SWIGs\cashflows.i
            # 	LinearTsrPricer --> None
            # 		swaptionVol	Handle<SwaptionVolatilityStructure>
            # 		meanReversion	Handle<Quote>
            # 		couponDiscountCurve	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            # 		settings	LinearTsrPricer::Settings		(LinearTsrPricer::Settings ( ))
            cms_pricer = ql.LinearTsrPricer(swaption_volamatrix_handle, ql.QuoteHandle(ql.SimpleQuote(self._mean_reversion)))

            # SWIGs\cashflows.i
            # 	LognormalCmsSpreadPricer --> None
            # 		cmsPricer	ext::<CmsCouponPricer>
            # 		correlation	Handle<Quote>
            # 		couponDiscountCurve	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
            # 		IntegrationPoints	Size		(16)
            # 		volatilityType	optional<VolatilityType>		(none)
            # 		shift1	Real		(Null<Real> ( ))
            # 		shift2	Real		(Null<Real> ( ))

            cms_spread_correlation: ql.QuoteHandle = ql.QuoteHandle(ql.SimpleQuote(self._cms_spread_correlation))

            pricer = ql.LognormalCmsSpreadPricer(
                cms_pricer,
                cms_spread_correlation
            )

            return pricer
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_object.signature)

    def engine_pricer_analytic(self, ql_instrument: QLInstrument) -> tuple[ql.PricingEngine, Optional[ql.FloatingRateCouponPricer]]:
        # There are two possibilities in here, to fill the discount curve field of the engine.
        # Either the discount curve from the instrument (ql_instrument.discount_curve.handle) or
        # the curve from the market data the engine is based on (self._attached_market_data.yield_curve.handle)
        # As the process should be independent of the instrument, the latter was chosen. Corrections can be performed in the
        # Payoff of the instrument.
        if ql_instrument.signature == signatures.instrument.swaption:  # pylint: disable=unidiomatic-typecheck

            swaption_volamatrix_handle = ql.SwaptionVolatilityStructureHandle(self._surface.ql_surface)

            if self._surface.distribution == VolatilityType['Normal']:
                # SWIGs\swaption.i
                # 	BachelierSwaptionEngine --> None
                # 		discountCurve	Handle<YieldTermStructure>
                # 		v	Handle<SwaptionVolatilityStructure>
                return ql.BachelierSwaptionEngine(self._attached_market_data.yield_curve.handle, swaption_volamatrix_handle), None  # type: ignore[attr-defined]
                #
                # SWIGs\swaption.i
                # 	BlackSwaptionEngine --> None
                # 		discountCurve	Handle<YieldTermStructure>
                # 		v	Handle<SwaptionVolatilityStructure>
            return ql.BlackSwaptionEngine(self._attached_market_data.yield_curve.handle, swaption_volamatrix_handle), None  # type: ignore[attr-defined]
        if ql_instrument.signature == signatures.leg_operator:
            return super().engine_pricer_analytic(ql_instrument)
        raise UnsupportedProcessError(self.signature, signatures.valuation.analytic_quantlib, instrument=ql_instrument.signature)
