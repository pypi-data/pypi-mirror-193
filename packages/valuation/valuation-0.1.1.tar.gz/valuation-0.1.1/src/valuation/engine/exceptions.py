from __future__ import annotations

from typing import Any, Optional, Union

from valuation.consts import signatures
from valuation.exceptions import DAAException
from valuation.global_settings import __type_checking__

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Signature


class QLException(DAAException):
    pass


class QLInputError(QLException):
    pass


class QLInputWarning(QLInputError):
    pass


class DAARuntimeException(DAAException):
    pass


class UnsupportedValuationError(DAARuntimeException):

    def __init__(self, valuation: Signature, instrument: Signature, *args: Any, message: Optional[str] = None, **kwargs: Any) -> None:
        error_message = f'{valuation} is not supported for {instrument}'
        if message:
            error_message += f' - {message}'
        super().__init__(error_message, *args, **kwargs)


class UnsupportedProcessError(DAARuntimeException):

    def __init__(self, process: Signature, valuations: Union[Signature, tuple[Signature, ...]], *args: Any, instrument: Optional[Signature] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        error_message = f'{process} is not compatible with '
        if isinstance(valuations, tuple):
            valuations = ', '.join(str(valuation) for valuation in valuations)      # type: ignore[assignment]
        error_message += f'{valuations} for {instrument}' if instrument else f'{valuations}'
        if process == signatures.process.base:
            error_message += ', possibly because no specific process was given'
        if message:
            error_message += f' - {message}'
        super().__init__(error_message, *args, **kwargs)


def ql_require(check: bool, message: str = '', object_id: str = '') -> None:
    if not check:
        if object_id:
            message = ' | '.join([message, f'Raised in {object_id}'])
        raise DAARuntimeException(message)
