from __future__ import annotations
from collections import defaultdict
from datetime import date
from daa_utils import Log
from valuation.consts import signatures
from valuation.consts import fields
from valuation.universal_transfer import Storage, Reference, Period, finance_types


class StorageGeneration:
    signature = signatures.empty
    reference_id_pattern: str = '{ID}'

    def check_for(self, reference_id: str) -> bool:
        raise NotImplementedError

    def get(self, reference_id: str) -> Storage:
        raise NotImplementedError

    def __str__(self) -> str:
        return f'Generator: {self.signature} | Pattern: {self.reference_id_pattern}'

    def _initialize(self) -> Storage:
        initialized_and_mutable = Storage()
        initialized_and_mutable[fields.Type] = self.signature.type
        if self.signature.sub_type != '':
            initialized_and_mutable[fields.SubType(self.signature.type)] = self.signature.sub_type
        return initialized_and_mutable


class CurrencyStandardGeneration(StorageGeneration):
    signature = signatures.currency.standard
    reference_id_pattern = '{CCY}'

    def check_for(self, reference_id: str) -> bool:
        return len(reference_id) == 3

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = reference_id
        if reference_id not in finance_types.Currencies:
            initialized[fields.CurrencyName] = 'EmptyFallback'
            Log.warning(f'No existing currency object for {initialized.reference}, using empty Currency instead.')
        if initialized.reference.id not in finance_types.Calendars:
            initialized[fields.Calendar] = 'WeekendsOnly'
            Log.warning(f'No holiday calendar supported for {initialized.reference}, using WeekendsOnly holiday calendar.')
        return initialized


class OptimizerGeneration(StorageGeneration):
    signature = signatures.optimize.levenberg_marquardt
    reference_id_pattern: str = 'OptimizeLevenbergMarquardtStandard'

    def check_for(self, reference_id: str) -> bool:
        return reference_id == self.reference_id_pattern

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = self.reference_id_pattern
        return initialized


class SurfaceProcessGeneration(StorageGeneration):  # pylint: disable=abstract-method
    _normal_distribution_identifier = ''
    _object_type_identifier = ''

    def check_for(self, reference_id: str) -> bool:
        normal_distribution = self._normal_distribution_identifier
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        if any(id_part not in reference_id for id_part in (self._object_type_identifier, self._normal_distribution_identifier, 'Vol')):
            return False
        stripped_obj_type = reference_id.replace(self._object_type_identifier, '')
        stripped_vol = stripped_obj_type.replace('Vol', '')
        if not stripped_vol.endswith(normal_distribution):
            return False
        stripped_distribution = stripped_vol.replace(normal_distribution, '')
        stripped_distribution = stripped_distribution.replace('Log', '')
        return len(stripped_distribution) in (5, 6)

    @classmethod
    def get_params_from_reference(cls, reference_id: str) -> tuple[str, str, str]:
        stripped_obj_type = reference_id.replace(cls._object_type_identifier, '')
        stripped_vol = stripped_obj_type.replace('Vol', '')
        currency, tenor_and_dist = stripped_vol[:3], stripped_vol[3:]
        tenor = tenor_and_dist.replace('Log', '').replace(cls._normal_distribution_identifier, '')
        distribution = tenor_and_dist.replace(tenor, '')
        return currency, tenor, distribution


class SwaptionSurfaceProcessGeneration(SurfaceProcessGeneration):
    signature = signatures.process.swaption_volatility
    reference_id_pattern = '{CCY}{FREQUENCY}{LogNormal__or__Normal}Vol'
    _normal_distribution_identifier = 'Normal'

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = reference_id
        initialized[fields.SwaptionVolatility] = Reference(signatures.swaption_volatility.all.type, reference_id)
        currency, tenor, distribution = self.get_params_from_reference(reference_id)
        initialized[fields.MarketData] = Reference(signatures.ir_index.base.type, f'{currency}{tenor}')
        initialized[fields.Distribution] = distribution
        return initialized


class CapFloorSurfaceProcessGeneration(SurfaceProcessGeneration):
    signature = signatures.process.cap_floor_volatility
    reference_id_pattern = '{CCY}{FREQUENCY}Cap{LogNor__or__Nor}Vol'
    _normal_distribution_identifier = 'Nor'
    _object_type_identifier = 'Cap'

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = reference_id
        initialized[fields.CapFloorVolatility] = Reference(signatures.cap_floor_surface.type, reference_id)
        currency, tenor, distribution = self.get_params_from_reference(reference_id)
        initialized[fields.MarketData] = Reference(signatures.ir_index.base.type, f'{currency}{tenor}')
        initialized[fields.Distribution] = f'{distribution}mal'
        return initialized


class ShortRateProcessCalibrationNoInstrumentGeneration(StorageGeneration):

    def check_for(self, reference_id: str) -> bool:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        id_parts = reference_id.split('#')
        if len(id_parts) != 2:
            return False
        if id_parts[0] != self.reference_id_pattern.split('#', maxsplit=1)[0]:
            return False
        swaption_volatility_id = id_parts[-1]
        id_checker = SwaptionSurfaceProcessGeneration()
        return id_checker.check_for(swaption_volatility_id)

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        _, swaption_volatility_id = reference_id.split('#')
        process_id = self.reference_id_pattern.format(SWAPTION_VOLATILITY_ID=swaption_volatility_id)
        initialized[fields.Id] = process_id
        initialized[fields.SwaptionVolatility] = Reference(signatures.swaption_volatility.all.type,
                                                           swaption_volatility_id)
        initialized[fields.Optimization] = Reference(signatures.optimize.levenberg_marquardt.type, 'OptimizeLevenbergMarquardtStandard')
        currency, tenor, _ = SwaptionSurfaceProcessGeneration.get_params_from_reference(swaption_volatility_id)
        initialized[fields.MarketData] = Reference(signatures.ir_index.base.type, f'{currency}{tenor}')
        return initialized


class HullWhiteCalibrationNoInstrumentGeneration(ShortRateProcessCalibrationNoInstrumentGeneration):  # pylint: disable=abstract-method
    signature = signatures.process.hull_white_calibration_no_instrument
    reference_id_pattern = 'HullWhite#{SWAPTION_VOLATILITY_ID}'


class G2CalibrationNoInstrumentGeneration(ShortRateProcessCalibrationNoInstrumentGeneration):  # pylint: disable=abstract-method
    signature = signatures.process.g2_calibration_no_instrument
    reference_id_pattern = 'G2#{SWAPTION_VOLATILITY_ID}'


class ShortRateProcessCalibrationGeneration(StorageGeneration):

    def check_for(self, reference_id: str) -> bool:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        id_parts = reference_id.split('#')
        if len(id_parts) != 3:
            return False
        if id_parts[0] != self.reference_id_pattern.split('#', maxsplit=1)[0]:
            return False
        swaption_volatility_id = id_parts[-1]
        id_checker = SwaptionSurfaceProcessGeneration()
        return id_checker.check_for(swaption_volatility_id)

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        _, instrument_id, swaption_volatility_id = reference_id.split('#')
        process_id = self.reference_id_pattern.format(INSTRUMENT_ID=instrument_id, SWAPTION_VOLATILITY_ID=swaption_volatility_id)
        initialized[fields.Id] = process_id
        initialized[fields.Instrument] = Reference('Instrument', instrument_id)
        initialized[fields.SwaptionVolatility] = Reference(signatures.swaption_volatility.surface.type, swaption_volatility_id)
        initialized[fields.Optimization] = Reference(signatures.optimize.levenberg_marquardt.type, 'OptimizeLevenbergMarquardtStandard')
        currency, tenor, _ = SwaptionSurfaceProcessGeneration.get_params_from_reference(swaption_volatility_id)
        initialized[fields.MarketData] = Reference(signatures.ir_index.base.type, f'{currency}{tenor}')
        return initialized


class IRSwapIndexGeneration(StorageGeneration):
    signature = signatures.ir_swap_index
    reference_id_pattern = '{INDEX_NAME}vs{SWAP_DURATION}'

    def check_for(self, reference_id: str) -> bool:
        if reference_id != reference_id.strip():
            Log.warning(f'Found trailing or leading spaces in {reference_id}')
        return all((
            'vs' in reference_id,
            '-' not in reference_id,
            len(reference_id) > 3,
            reference_id[reference_id.find('vs') + 2].isnumeric(),
            not reference_id[-1].isnumeric(),
        ))

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = reference_id
        currency, index_name, period = self.get_params_from_reference(reference_id)
        initialized[fields.Currency] = Reference(signatures.currency.all.type, currency)
        initialized[fields.Period] = Period.from_str(period.replace('_', ''))
        initialized[fields.FixedFrequency] = Period.from_str('1Y')
        initialized[fields.IRIndex] = Reference(signatures.ir_index.all.type, index_name)
        initialized[fields.FixingFunction] = Reference(signatures.function.all.type, reference_id)
        return initialized

    @classmethod
    def get_params_from_reference(cls, reference_id: str) -> tuple[str, str, str]:
        return reference_id[:3], reference_id.split('vs')[0], reference_id.split('vs')[1]


class HullWhiteCalibrationGeneration(ShortRateProcessCalibrationGeneration):  # pylint: disable=abstract-method
    signature = signatures.process.hull_white_calibration
    reference_id_pattern = 'HullWhite#{INSTRUMENT_ID}#{SWAPTION_VOLATILITY_ID}'


class G2CalibrationGeneration(ShortRateProcessCalibrationGeneration):  # pylint: disable=abstract-method
    signature = signatures.process.g2_calibration
    reference_id_pattern = 'G2#{INSTRUMENT_ID}#{SWAPTION_VOLATILITY_ID}'


class IRSpreadSwapIndexGeneration(StorageGeneration):
    signature = signatures.ir_spread_index
    reference_id_pattern = '{Optional: GEARING_1*}{INDEX_1_CCY}{INDEX_1_FREQUENCY}vs{SWAP_DURATION_1}-{Optional: GEARING_2*}{INDEX_2_CCY}{INDEX_2_FREQUENCY}vs{SWAP_DURATION_2}'

    def check_for(self, reference_id: str) -> bool:
        if not reference_id.startswith('SpreadIndex#'):
            return False
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        return len(reference_id.split('+')) == 2 and len(reference_id.split('#')) == 2 and len(reference_id.split('*')) == 3

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = reference_id
        index_positive, index_negative = reference_id.split('#', 1)[1].split('+')
        gearing_and_index_positive = index_positive.split('*')
        gearing_and_index_negative = index_negative.split('*')
        if len(gearing_and_index_positive) == 2:
            gearing_positive, index_positive = float(gearing_and_index_positive[0]), gearing_and_index_positive[1]
            initialized[fields.GearingPositive] = gearing_positive
        if len(gearing_and_index_negative) == 2:
            gearing_negative, index_negative = float(gearing_and_index_negative[0]), gearing_and_index_negative[1]
            initialized[fields.GearingNegative] = gearing_negative
        initialized[fields.IRSwapIndexPositive] = Reference.from_str(index_positive)
        initialized[fields.IRSwapIndexNegative] = Reference.from_str(index_negative)
        return initialized


class SpreadInterpolatorGeneration(StorageGeneration):
    signature = signatures.yield_curve.z_spread_interpolated
    reference_id_pattern = 'SpreadInterpolator#{SPREAD_CURVE}#{DISCOUNT_CURVE}#{MATURITY}#{ADDITIVE_FACTOR}'

    def check_for(self, reference_id: str) -> bool:
        return all((
            reference_id.startswith('SpreadInterpolator'),
            len(reference_id.split('#')) == 5
        ))

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        _, spread_curve, base_curve, maturity, additive_factor = reference_id.split('#')
        initialized[fields.Id] = reference_id
        initialized[fields.SpreadCurve] = Reference('ZSpreadCollection', f'{spread_curve}#{base_curve}')
        initialized[fields.Maturity] = date.fromisoformat(maturity)
        initialized[fields.AdditiveFactor] = float(additive_factor)
        initialized[fields.EnableExtrapolation] = False
        return initialized


class IRIndexGeneration(StorageGeneration):
    signature = signatures.ir_index.base
    reference_id_pattern = '{CCY}{Tenor}'

    def check_for(self, reference_id: str) -> bool:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')

        return all((
            '_' not in reference_id,
            len(reference_id) > 3,
            all(not letter.isnumeric() for letter in reference_id[:3]),
            all(letter.isnumeric() for letter in reference_id[3:-1]),
            not reference_id[-1].isnumeric(),
        ))

    def get(self, reference_id: str) -> Storage:
        initialized = self._initialize()
        initialized[fields.Id] = reference_id
        currency, tenor = self.get_params_from_reference(reference_id)
        initialized[fields.Currency] = Reference(signatures.currency.all.type, currency)
        initialized[fields.Tenor] = Period.from_str(tenor.replace('_', ''))
        initialized[fields.DiscountCurve] = Reference(signatures.yield_curve.all.type, currency + tenor)
        initialized[fields.FixingFunction] = Reference(signatures.function.all.type, currency + tenor)
        return initialized

    @classmethod
    def get_params_from_reference(cls, reference_id: str) -> tuple[str, str]:
        return reference_id[:3], reference_id[3:]


def get_generators() -> dict[str, list[StorageGeneration]]:
    _generators: dict[str, list[StorageGeneration]] = defaultdict(list)

    def _get_generators(root: type[StorageGeneration]) -> None:
        if root.signature != signatures.empty:
            _generators[root.signature.type].append(root())
        for child in root.__subclasses__():
            _get_generators(child)

    _get_generators(StorageGeneration)
    return _generators
