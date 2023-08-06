from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Callable, Generator, Union

from valuation.exceptions import ProgrammingError


class NoValue:
    def __init__(self, description: Any = ''):
        self._description: str = str(description)

    def __str__(self) -> str:
        return self._description

    def __bool__(self) -> bool:
        return True

    def __hash__(self) -> int:
        return 0

    def __copy__(self) -> NoValue:
        return NoValue(self._description)

    def __getattr__(self, item: str) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description}.{item}')
        return self

    def __call__(self, *args: Any, **kwargs: Any) -> NoValue:
        if __debug__:
            arguments = [str(argument) for argument in args] + [f'{key}={value}' for key, value in kwargs.items()]
            result = f'{self._description}(' + ', '.join(arguments) + ')'
            return NoValue(result)
        return self

    def __getitem__(self, item: Any) -> NoValue:
        if __debug__:
            if isinstance(item, slice):
                if item.step:
                    raise NotImplementedError
                item = f'{item.start or ""}:{item.stop or ""}'
            return NoValue(f'{self._description}[{item}]')
        return self

    def map(self, mapping_name: str) -> NoValue:
        if __debug__:
            return NoValue(f'{mapping_name}[{self._description}]')
        return self

    def __add__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} + {other}')
        return self

    def __radd__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{other} + {self._description}')
        return self

    def __sub__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} - {other}')
        return self

    def __rsub__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{other} - {self._description}')
        return self

    def __neg__(self) -> NoValue:
        if __debug__:
            return NoValue(f'- {self._description}')
        return self

    def __mul__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} * {other}')
        return self

    def __rmul__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{other} * {self._description}')
        return self

    def __truediv__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} / {other}')
        return self

    def __rtruediv__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{other} / {self._description}')
        return self

    def __contains__(self, item: Any) -> bool:
        raise ProgrammingError('Use "is_in" or "is_not_in" instead!')

    def __eq__(self, other: Any) -> NoValue:                # type: ignore[override]
        if __debug__:
            return NoValue(f'{self._description} == {other}')
        return self

    def __lt__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} < {other}')
        return self

    def __gt__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} > {other}')
        return self

    def __le__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} <= {other}')
        return self

    def __ge__(self, other: Any) -> NoValue:
        if __debug__:
            return NoValue(f'{self._description} >= {other}')
        return self

    def __ne__(self, other: Any) -> NoValue:                # type: ignore[override]
        if __debug__:
            return NoValue(f'{self._description} != {other}')
        return self

    def __iter__(self) -> Generator[NoValue, None, None]:
        yield self

    @contextmanager
    def safe_access_checks_only(self) -> Generator[None, None, None]:      # pylint: disable=no-self-use
        yield

    @staticmethod
    def replace(item: Any, what: Any, by: Any) -> Any:                          # pylint: disable=invalid-name
        if isinstance(item, NoValue):
            if __debug__:
                return NoValue(str(item).replace(str(what), str(by)))
            return item
        return item

    @staticmethod
    def bracket(item: Any) -> Any:
        if isinstance(item, NoValue):
            if __debug__:
                return f'({item})'
            return item
        return item

    @staticmethod
    def is_in(item: Union[Any, NoValue], container: Union[Any, NoValue]) -> Union[bool, NoValue]:
        if isinstance(item, NoValue) or isinstance(container, NoValue):
            if isinstance(item, str):
                item = f'"{item}"'
            if __debug__:
                return NoValue(f'{item} in {container}')
            return NoValue()
        return item in container

    @staticmethod
    def is_not_in(item: Union[Any, NoValue], container: Union[Any, NoValue]) -> Union[bool, NoValue]:
        if isinstance(item, NoValue) or isinstance(container, NoValue):
            if isinstance(item, str):
                item = f'"{item}"'
            if __debug__:
                return NoValue(f'{item} not in {container}')
            return NoValue()
        return item not in container

    @staticmethod
    def apply(function: Callable[[Any], Any], *args: Any, **kwargs: dict[str, Any]) -> Any:
        if any(isinstance(argument, NoValue) for argument in args):
            if __debug__:
                arguments = [str(argument) for argument in args] + [f'{key}={value}' for key, value in kwargs.items()]
                result = f'{function.__qualname__}(' + ', '.join(arguments) + ')'
                return NoValue(result)
            return NoValue()
        return function(*args)
