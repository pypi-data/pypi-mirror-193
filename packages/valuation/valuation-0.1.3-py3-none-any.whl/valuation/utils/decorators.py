from functools import wraps
from typing import Any, Callable, TypeVar, Union


# Todo: (2020/12) Possibly replace by functools.lru_cache. However, if in our cases the underlying memory does not grow too large, it might be better to keep this one.
def memoize(function: Callable[..., Any]) -> Callable[..., Any]:
    function_results: dict[Any, Any] = {}

    @wraps(function)
    def helper(*args: Any) -> Any:
        if args not in function_results:
            function_results[args] = function(*args)
        return function_results[args]

    return helper


SerializeIn = TypeVar('SerializeIn')
SerializeOut = TypeVar('SerializeOut')


def serialize_function(function: Callable[[SerializeIn], SerializeOut]) -> Callable[[Union[SerializeIn, list[SerializeIn], set[SerializeIn], tuple[SerializeIn]]], Union[SerializeOut, list[SerializeOut], set[SerializeOut], tuple[SerializeOut, ...]]]:
    @wraps(function)
    def helper(*args: Union[SerializeIn, list[SerializeIn], set[SerializeIn], tuple[SerializeIn, ...]]) -> Union[SerializeOut, list[SerializeOut], set[SerializeOut], tuple[SerializeOut, ...]]:
        assert len(args) == 1
        if isinstance(args[0], list):
            return [function(arg) for arg in args[0]]
        if isinstance(args[0], set):
            return {function(arg) for arg in args[0]}
        if isinstance(args[0], tuple):
            return tuple(function(arg) for arg in args[0])
        return function(args[0])
    return helper
