Info: str = 'info'
Delta: str = 'delta'            # pylint: disable=invalid-name
PV: str = 'pv'
Rho: str = 'rho'                # pylint: disable=invalid-name
Vega: str = 'vega'
DV01: str = 'dv01'              # given together with rho automatically whenever possible
Gamma: str = 'gamma'
DRho: str = 'drho'
DDV01: str = 'ddv01'
Volga: str = 'volga'
CashFlows: str = 'cfs'
CashFlowsAdditionalInfo: str = "cfInfo"
CleanDirty: str = 'cleanDirty'
SensitivityRange: str = 'sensitivityRange'
MarketDataRange: str = 'marketDataRange'
AdditionalInfo: str = 'additionalInfo'

AllGreeksWithoutShift: list[str] = [Info, PV, CashFlows, CleanDirty, AdditionalInfo, CashFlowsAdditionalInfo]
AllGreeksWithShift: list[str] = [Delta, Rho, Vega]
AllRanges: list[str] = [SensitivityRange, MarketDataRange]
AllGreeks: list[str] = AllGreeksWithoutShift + AllGreeksWithShift + AllRanges

Amount: str = 'amount'

Units: dict[int, str] = {
    1: '',
    100: 'pct',
    10000: 'bps'
}


# volga not added yet
SndDerivatives: dict[str, str] = {
    Delta: Gamma,
    Rho: DRho,
    DV01: DDV01
}
