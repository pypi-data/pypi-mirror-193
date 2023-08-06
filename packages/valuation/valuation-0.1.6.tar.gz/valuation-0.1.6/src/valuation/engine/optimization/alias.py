from valuation.consts import signatures
from valuation.engine import QLAlias


class QLOptimizationAlias(QLAlias):
    _signature = signatures.optimize.alias
