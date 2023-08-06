from __future__ import annotations

import QuantLib as ql

from valuation.global_settings import __type_checking__
from valuation.consts import signatures
from valuation.consts import fields
from valuation.engine.check import ObjectType, Range
from valuation.engine.volatility_surfaces import QLSwaptionVolatility
from valuation.engine.process.short_rate.base import QLShortRateProcessBase
from valuation.universal_transfer import Storage, Period

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.engine.optimization import QLOptimize
    from valuation.engine.instrument import QLInstrument
    from valuation.universal_transfer import DefaultParameters


class QLG2ProcessBase(QLShortRateProcessBase):  # pylint: disable=abstract-method
    _signature = signatures.empty
    # ToDo(2021/12): Add greeks
    _market_data_types = [signatures.ir_index.base]

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._model_type_ql: type[ql.ShortRateModel] = ql.G2
        self._process_type_ql: type[ql.StochasticProcess] = ql.G2Process
        self._drift: float
        self._volatility: float
        self._long_term_drift: float
        self._long_term_volatility: float
        self._correlation: float

    def generate_storage(self) -> Storage:
        storage: Storage = Storage()
        storage.assign_reference(self.reference)
        storage[fields.SubType(self.signature.type)] = signatures.process.g2.sub_type
        storage[fields.MarketData] = self._attached_market_data.reference
        storage[fields.Drift] = self._drift
        storage[fields.VolatilityValue] = self._volatility
        storage[fields.LongTermDrift] = self._long_term_drift
        storage[fields.LongTermVolatilityValue] = self._long_term_volatility
        storage[fields.SingleCorrelation] = self._correlation
        storage.make_immutable()
        return storage

    def _get_model_params(self) -> tuple[ql.YieldTermStructureHandle, float, float, float, float, float]:
        # SWIGs\shortratemodels.i
        # 	G2 --> None
        # 		termStructure	Handle<YieldTermStructure>
        # 		a	Real		(0.1)
        # 		sigma	Real	(0.01)
        # 		b	Real		(0.1)
        # 		eta	Real		(0.01)
        # 		rho	Real		(-0.75)
        params = (
            self._attached_market_data.yield_curve.handle,  # type: ignore[attr-defined]
            self._drift,
            self._volatility,
            self._long_term_drift,
            self._long_term_volatility,
            self._correlation
        )
        return params

    def _get_process_params(self) -> tuple[float, float, float, float, float]:
        # SWIGs\stochasticprocess.i
        # G2Process --> None
        # 		a	Real
        # 		sigma	Real
        # 		b	Real
        #       eta	Real
        # 		rho	Real
        return self._get_model_params()[1:]


class QLG2Process(QLG2ProcessBase):  # pylint: disable=abstract-method
    _signature = signatures.process.g2

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._drift: float = self.data(fields.Drift, check=Range(lower=0.0))
        self._volatility: float = self.data(fields.VolatilityValue, check=Range(lower=0.0))
        self._long_term_drift: float = self.data(fields.LongTermDrift, check=Range(lower=0.0))
        self._long_term_volatility: float = self.data(fields.LongTermVolatilityValue, check=Range(lower=0.0))
        self._correlation: float = self.data(fields.SingleCorrelation, check=Range(lower=-1.0, upper=1.0, strict=False))


class QLG2ProcessCalibrationBase(QLG2ProcessBase):  # pylint: disable=abstract-method

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:  # pylint: disable=unsubscriptable-object
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._swaption_surface: QLSwaptionVolatility = self.data(
            fields.SwaptionVolatility,
            check=ObjectType(signatures.swaption_volatility.all),
            exclude_from_greeks=True
        )
        self._optimize: QLOptimize = self.data(fields.Optimization, check=ObjectType(signatures.optimize.all))
        # TODO(2021/12) Find good defaults for all values below
        self._drift_start: float = self.data(fields.Drift, default_value=0.1)
        self._volatility_start: float = self.data(fields.VolatilityValue, default_value=0.01)
        self._long_term_drift_start: float = self.data(fields.LongTermDrift, default_value=0.1)
        self._long_term_volatility_start: float = self.data(fields.LongTermVolatilityValue, default_value=0.01)
        self._correlation_start: float = self.data(fields.SingleCorrelation, default_value=-0.75)
        self._std_deviations: float = self.data(fields.StdDeviations, default_value=4.0)
        self._integration_steps: int = self.data(fields.IntegrationSteps, default_value=4)
        self._swaption_helpers: list[ql.SwaptionHelper] = []

    def _post_init(self) -> None:
        model_params = self._calibrate(
            self._swaption_helpers,
            self._optimize,
            self._drift_start,
            self._volatility_start,
            self._long_term_drift_start,
            self._long_term_volatility_start,
            self._correlation_start,
            self._std_deviations,
            self._integration_steps
        )
        self._drift = model_params[0]
        self._volatility = model_params[1]
        self._long_term_drift = model_params[2]
        self._long_term_volatility = model_params[3]
        self._correlation = model_params[4]

    def _calibrate(self,
                   swaption_helpers: list[ql.SwaptionHelper],
                   optimizer: QLOptimize,
                   drift: float,
                   volatility: float,
                   drift_long: float,
                   volatility_long: float,
                   correlation: float,
                   std_deviations: float,
                   integration_steps: int) -> tuple[float, float, float, float, float]:
        model: ql.G2 = self._model_type_ql(
            self._attached_market_data.yield_curve.handle,  # type: ignore[attr-defined]
            drift,
            volatility,
            drift_long,
            volatility_long,
            correlation
        )
        optimization_method, end_criteria = optimizer.method_criteria()
        # 	G2SwaptionEngine --> None
        # 		model	Date
        # 		range	Real
        # 		intervals	Size
        for helper in swaption_helpers:
            helper.setPricingEngine(ql.G2SwaptionEngine(model, std_deviations, integration_steps))
        model.calibrate(swaption_helpers, optimization_method, end_criteria)
        return model.params()  # type: ignore[no-any-return]


class QLG2ProcessCalibration(QLG2ProcessCalibrationBase):  # pylint: disable=abstract-method
    _signature = signatures.process.g2_calibration

    def __init__(self, data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:  # pylint: disable=unsubscriptable-object
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        underlying_instrument: QLInstrument = self.data(
            fields.DataInstrument,
            exclude_from_greeks=True,
            check=ObjectType(
                [
                    signatures.instrument.vanilla_swap,
                    signatures.instrument.callable_fixed_bond,
                    signatures.instrument.callable_flexible_bond
                ]
            )
        )
        if not self._documentation_mode:
            self._swaption_helpers = self._swaption_helpers_diagonal(
                underlying_instrument.model_calibration_inputs,  # type: ignore[attr-defined]
                self._swaption_surface
            )


class QLG2CalibrationNoInstrument(QLG2ProcessCalibrationBase):  # pylint: disable=abstract-method
    _signature = signatures.process.g2_calibration_no_instrument

    def __init__(self,
                 data: Storage, ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        max_time: Period = self.data(fields.MaxCumulativeTime, default_value=Period.from_str('101Y'))
        if not self._documentation_mode:
            self._swaption_helpers = self._swaption_helpers_surface(max_time, self._swaption_surface)
