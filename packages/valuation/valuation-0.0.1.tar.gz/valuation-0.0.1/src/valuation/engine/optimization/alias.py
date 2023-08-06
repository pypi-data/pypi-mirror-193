from valuations.consts import signatures
from valuations.engine import QLAlias


class QLOptimizationAlias(QLAlias):
    _signature = signatures.optimize.alias
