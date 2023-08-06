from valuation.consts import signatures
from valuation.engine import QLAlias


class QLYieldCurveAlias(QLAlias):
    _signature = signatures.yield_curve.alias
