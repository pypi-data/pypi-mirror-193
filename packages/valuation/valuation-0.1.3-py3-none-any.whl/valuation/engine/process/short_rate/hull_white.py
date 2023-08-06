from __future__ import annotations

import QuantLib as ql

from valuation.consts import global_parameters, signatures
from valuation.consts import fields
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.check import ObjectType, Range
from valuation.engine.volatility_surfaces import QLSwaptionVolatility
from valuation.engine.process.short_rate.base import QLShortRateProcessBase
from valuation.engine.exceptions import DAARuntimeException
from valuation.universal_output import result_items
from valuation.universal_transfer import Storage, Period
from valuation.utils.other import is_nan

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import DefaultParameters
    from valuation.engine import QLObjectDB
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.optimization import QLOptimize


class QLHullWhiteProcessBase(QLShortRateProcessBase):  # pylint: disable=abstract-method
    _signature = signatures.empty
    _supported_greeks = (result_items.Vega,)
    _market_data_types = [signatures.ir_index.base]

    @property
    def mean_reversion(self) -> float:
        return self._mean_reversion

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._model_type_ql: type[ql.ShortRateModel] = ql.HullWhite
        self._process_type_ql: type[ql.StochasticProcess] = ql.HullWhiteProcess
        self._volatility: float
        self._mean_reversion: float

    def scenarios(self, greek: str) -> list[str]:
        super().scenarios(greek)
        if greek == result_items.Vega:
            return [result_items.Vega]
        raise ProgrammingError()

    def generate_storage(self) -> Storage:
        storage: Storage = Storage()
        storage.assign_reference(self.reference)
        storage[fields.SubType(self.signature.type)] = signatures.process.hull_white.sub_type
        storage[fields.MarketData] = self._attached_market_data.reference
        storage[fields.MeanReversion] = self._mean_reversion
        storage[fields.VolatilityValue] = self._volatility
        storage.make_immutable()
        return storage

    def _get_model_params(self) -> tuple[ql.YieldTermStructureHandle, float, float]:
        # SWIGs\shortratemodels.i
        # 	HullWhite --> None
        # 		termStructure	Handle<YieldTermStructure>
        # 		a	Real		(0.1)
        # 		sigma	Real		(0.01)
        params = (
            self._attached_market_data.yield_curve.handle,  # type: ignore[attr-defined]
            self._mean_reversion,
            self._volatility
        )
        return params

    def _get_process_params(self) -> tuple[ql.YieldTermStructureHandle, float, float]:
        # SWIGs\stochasticprocess.i
        # HullWhiteProcess --> None
        # 		riskFreeTS	Handle<YieldTermStructure>
        # 		a	Real
        # 		sigma	Real
        return self._get_model_params()

    def _change_to(self, scenario: str, shift: float) -> None:  # pylint: disable=arguments-differ
        assert is_nan(self._original_value)  # type: ignore[has-type]
        if scenario == result_items.Vega:
            if shift <= -self._volatility * self.shift_unit:
                raise DAARuntimeException(f'Greek/Range calc: Negative {shift = } leads to nonpositive volatility')
            self._scenario_divisor = shift
            self._original_value = self._volatility
            self._volatility += self._scenario_divisor / self.shift_unit
        else:
            raise ProgrammingError()

    def _change_back(self, scenario: str) -> None:
        if scenario == result_items.Vega:
            self._volatility = self._original_value
        else:
            raise ProgrammingError()
        self._original_value = float('NaN')
        self._scenario_divisor = float('NaN')


class QLHullWhiteProcess(QLHullWhiteProcessBase):  # pylint: disable=abstract-method
    _signature = signatures.process.hull_white

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:  # pylint: disable=unsubscriptable-object
        super().__init__(data, ql_db, default_parameters, data_only_mode)
        self._volatility: float = self.data(
            fields.VolatilityValue,
            check=Range(
                lower=0.0,
                upper=global_parameters.VolatilityMaximum,
                strict=False
            )
        )
        self._mean_reversion: float = self.data(fields.MeanReversion, check=Range(lower=0.0))


class QLHullWhiteProcessCalibrationBase(QLHullWhiteProcessBase):  # pylint: disable=abstract-method

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        self._swaption_surface: QLSwaptionVolatility = self.data(
            fields.SwaptionVolatility,
            check=ObjectType(signatures.swaption_volatility.all),
            exclude_from_greeks=True
        )
        self._mean_reversion_start: float = self.data(fields.MeanReversion, default_value=0.03, check=Range(lower=0.0))
        self._optimize: QLOptimize = self.data(fields.Optimization, check=ObjectType(signatures.optimize.all))
        self._fix_mean_reversion: bool = self.data(
            fields.FixMeanReversion,
            allow_fallback_to_default_parameters=True,
            default_value=True
        )
        self._swaption_helpers: list[ql.SwaptionHelper] = []

    def _post_init(self) -> None:
        self._mean_reversion, self._volatility = self._calibrate(
            self._swaption_helpers,
            self._optimize,
            self._fix_mean_reversion,
            self._mean_reversion_start
        )
        super()._post_init()

    def _calibrate(self,
                   swaption_helpers: list[ql.SwaptionHelper],
                   optimizer: QLOptimize,
                   fix_mean_reversion: bool,
                   mean_reversion_start: float,
                   volatility_start: float = 0.000001) -> tuple[float, float]:
        model: ql.HullWhite = self._model_type_ql(
            self._attached_market_data.yield_curve.handle,  # type: ignore[attr-defined]
            mean_reversion_start,
            volatility_start
        )
        optimization_method, end_criteria = optimizer.method_criteria()
        # 	JamshidianSwaptionEngine --> None
        # 		model	ext::<OneFactorAffineModel>
        # 		termStructure	Handle<YieldTermStructure>		(Handle<YieldTermStructure> ( ))
        for helper in swaption_helpers:
            helper.setPricingEngine(ql.JamshidianSwaptionEngine(model))
        if not fix_mean_reversion:
            model.calibrate(
                swaption_helpers,
                optimization_method,
                end_criteria,
                ql.NoConstraint(),
                [],
                [False, False])
        model.calibrate(
            swaption_helpers,
            optimization_method,
            end_criteria,
            ql.NoConstraint(),
            [],
            [True, False])
        return model.params()  # type: ignore[no-any-return]


class QLHullWhiteProcessCalibration(QLHullWhiteProcessCalibrationBase):  # pylint: disable=abstract-method
    _signature = signatures.process.hull_white_calibration

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:
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


class QLHullWhiteProcessCalibrationNoInstrument(QLHullWhiteProcessCalibrationBase):  # pylint: disable=abstract-method
    _signature = signatures.process.hull_white_calibration_no_instrument

    def __init__(self,
                 data: Storage,
                 ql_db: QLObjectDB,
                 default_parameters: DefaultParameters,
                 data_only_mode: bool = False) -> None:

        super().__init__(data, ql_db, default_parameters, data_only_mode)
        max_time: Period = self.data(fields.MaxCumulativeTime, default_value=Period.from_str('101Y'))
        if not self._documentation_mode:
            self._swaption_helpers = self._swaption_helpers_surface(max_time, self._swaption_surface)
