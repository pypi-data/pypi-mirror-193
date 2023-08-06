from typing import Any
from warnings import warn
from daa_utils import Log


class DAAException(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)               # type: ignore[call-arg]
        self._additional_info: str = ''

    def set_additional_information(self, info: str) -> None:
        if self._additional_info:
            if info not in self._additional_info:
                self._additional_info = f'{self._additional_info} # {info}'
        else:
            self._additional_info = info

    def __str__(self) -> str:
        if self._additional_info:
            prefix: str = f'{self.__class__.__name__}! {self._additional_info} # '
        else:
            prefix = f'{self.__class__.__name__}! '
        if isinstance(self.args, tuple) and len(self.args) == 1:            # pylint: disable=unsubscriptable-object
            return f'{prefix}{self.args[0]}'   # pylint: disable=unsubscriptable-object
        return f'{prefix}{self.args}'


class ProgrammingError(DAAException):
    pass


SILENT_WARNING = False


def daa_warn(message: str) -> None:
    if not SILENT_WARNING:
        warn(message)
    Log.warning(message)
