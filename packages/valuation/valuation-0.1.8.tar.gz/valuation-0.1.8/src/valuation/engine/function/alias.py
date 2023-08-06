from valuation.consts import signatures
from valuation.engine import QLAlias


class QLFunctionAlias(QLAlias):
    _signature = signatures.function.alias
