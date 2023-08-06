from valuations.consts import signatures
from valuations.engine import QLAlias


class QLYieldCurveAlias(QLAlias):
    _signature = signatures.yield_curve.alias
