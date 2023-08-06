from valuation.exceptions import ProgrammingError
from valuation.universal_transfer import Signature


class Groups:
    base: str = 'base'
    instrument: str = 'instrument'
    market_data: str = 'market_data'
    utility: str = 'utility'


class SignatureCollection:
    def __init__(self, object_type: str) -> None:
        self.all: Signature = Signature(object_type, Signature.ALL)
        self._registered: set[str] = {Signature.ALL}

    def __call__(self, sub_type: str) -> Signature:
        if sub_type in self._registered:
            raise ProgrammingError()
        self._registered.add(sub_type)
        return self.all.specify_sub_type(sub_type)


class CurrencySignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Currency')

        self.alias: Signature = self('Alias')
        self.standard: Signature = self('Standard')
        self.variable: Signature = self('')


class FunctionSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Function')

        self.alias: Signature = self('Alias')
        self.api_call_fixing: Signature = self('APICallFixing')
        self.api_call_fixing_v2: Signature = self('APICallFixingV2')
        self.api_call_cms_fixing_v2: Signature = self('APICallCMSFixingV2')
        self.api_call_fx_rate_v2: Signature = self('APICallFXRateV2')
        self.constant: Signature = self('Constant')
        self.fixing: Signature = self('Fixing')
        self.swap_rate_fixing: Signature = self('SwapRateFixing')
        self.json: Signature = self('JSON')


class FxRateSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('FXRate')

        self.direct: Signature = self('Direct')
        self.direct_parity: Signature = self('DirectParity')
        self.direct_spot: Signature = self('DirectSpot')
        self.no_forward: Signature = self('NoForward')
        self.standard: Signature = self('')
        self.triangle: Signature = self('Triangle')


class InstrumentSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Instrument')

        self.callable_fixed_bond: Signature = self('CallableFixedBond')
        self.callable_flexible_bond: Signature = self('CallableBond')
        self.flexible_montecarlo: Signature = self('Flexible')
        self.cap_floor: Signature = self('CapFloor')
        self.fixed_bond: Signature = self('FixedBond')
        self.flexible_bond: Signature = self('Bond')
        self.flexible_swap: Signature = self('Swap')
        self.currency_swap: Signature = self('CrossCurrencySwap')
        self.float_bond: Signature = self('FloatBond')
        self.fx_continuous_barrier_option: Signature = self('FxContinuousBarrierOption')
        self.stock_continuous_barrier_option: Signature = self('StockContinuousBarrierOption')
        self.fx_european_option: Signature = self('FxEuropeanOption')
        self.stock_european_option: Signature = self('StockEuropeanOption')
        self.quanto_european_option: Signature = self('StockEuropeanQuantoOption')
        self.fx_forward: Signature = self('FxForward')
        self.stock_forward: Signature = self('StockForward')
        self.swaption: Signature = self('Swaption')
        self.vanilla_swap: Signature = self('VanillaSwap')
        self.zero_bond: Signature = self('ZeroBond')


class OptimizationSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Optimize')

        self.alias: Signature = self('Alias')
        self.levenberg_marquardt: Signature = self('LevenbergMarquardt')
        self.levenberg_marquardt_fast: Signature = self('LevenbergMarquardtFast')


class ProcessSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Process')
        self.base: Signature = self('')

        self.basket: Signature = self('Basket')
        self.black_fx: Signature = self('BlackFX')
        self.black_stock: Signature = self('BlackStock')
        self.black_scholes_merton_fx: Signature = self('BlackScholesMertonFX')
        self.black_scholes_merton_stock: Signature = self('BlackScholesMertonStock')
        self.black_scholes_merton_quanto: Signature = self('BlackScholesMertonQuanto')
        self.cap_floor_volatility: Signature = self('CapFloorVolatility')
        self.cms: Signature = self('CMS')
        self.cms_spread: Signature = self('CMSSpread')
        self.g2: Signature = self('G2')  # pylint: disable=invalid-name
        self.g2_calibration: Signature = self('G2Calibration')
        self.g2_calibration_no_instrument: Signature = self('G2CalibrationNoInstrument')
        self.heston_fx: Signature = self('HestonFX')
        self.heston_stock: Signature = self('HestonStock')
        self.hull_white: Signature = self('HullWhite')
        self.hull_white_calibration: Signature = self('HullWhiteCalibration')
        self.hull_white_calibration_no_instrument: Signature = self('HullWhiteCalibrationNoInstrument')
        self.simple_black: Signature = self('SimpleBlack')
        self.swaption_volatility: Signature = self('SwaptionVolatility')
        self.uncorrelated_basket: Signature = self('UncorrelatedBasket')


class ValuationSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Valuation')

        self.analytic: Signature = self('Analytic')
        self.analytic_quantlib: Signature = self('AnalyticQuantlib')
        self.financial_program: Signature = self('FinancialProgram')
        self.implied_zspread: Signature = self('ImpliedZSpread')
        self.simple: Signature = self('Simple')
        self.tree_quantlib: Signature = self('TreeQuantlib')
        self.market_data: Signature = self('MarketData')


class YieldCurveSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('YieldCurve')

        self.alias: Signature = self('Alias')
        self.calibration: Signature = self('Calibration')
        self.constant_spread: Signature = self('ConstantSpread')
        self.cross_currency_spread: Signature = self('CrossCurrencySpread')
        self.discount: Signature = self('Discount')
        self.outright: Signature = self('Outright')
        self.spread: Signature = self('Spread')
        self.z_spread_interpolated: Signature = self('ZSpreadInterpolated')  # pylint: disable=invalid-name
        self.zero: Signature = self('Zero')


class IRIndexSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('IRIndex')

        self.base: Signature = self('')
        self.alias: Signature = self('Alias')


class UtilityObjectSignatureCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('Utility')

        self.schedule: Signature = self('Schedule')
        self.date_roller: Signature = self('DateRoller')


class SwaptionVolatilityCollection(SignatureCollection):
    def __init__(self) -> None:
        super().__init__('SwaptionVolatility')

        self.surface: Signature = self('Surface')
        self.points: Signature = self('Points')


class Coupon:
    fixed = Signature('Fixed')
    fixed_full = Signature('FixedFull')
    floating = Signature('Floating')
    capped_floored = Signature('CappedFloored')
    cms = Signature('CMS')
    cms_spread = Signature('CMSSpread')
    overnight = Signature('Overnight')


empty = Signature('', '')

currency = CurrencySignatureCollection()
function = FunctionSignatureCollection()
fx_rate = FxRateSignatureCollection()
index_and_cms = Signature('MarketData', 'IndexAndCMS_VIRTUAL')
index_and_cms_spread = Signature('MarketData', 'IndexAndCMSSpread_VIRTUAL')
instrument = InstrumentSignatureCollection()
coupon = Coupon()
leg_operator = Signature('LegOperator')
ir_index = IRIndexSignatureCollection()
ir_swap_index = Signature('IRSwapIndex')
ir_swap_index_alias = Signature('IRSwapIndex', 'Alias')
ir_spread_index = Signature('IRSpreadIndex')
market_data_basket = Signature('MarketData', 'Basket')
optimize = OptimizationSignatureCollection()
process = ProcessSignatureCollection()
stock: Signature = Signature('Stock')
valuation = ValuationSignatureCollection()
cap_floor_surface: Signature = Signature('CapFloorVolatility', 'Surface')
swaption_volatility = SwaptionVolatilityCollection()
swaption_point: Signature = Signature('SwaptionPoint')
yield_curve = YieldCurveSignatureCollection()
z_spread_collection: Signature = Signature('ZSpreadCollection')
utilities = UtilityObjectSignatureCollection()
