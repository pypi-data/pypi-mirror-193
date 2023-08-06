from valuations.consts import signatures
from valuations.engine import QLAlias


class QLFunctionAlias(QLAlias):
    _signature = signatures.function.alias
