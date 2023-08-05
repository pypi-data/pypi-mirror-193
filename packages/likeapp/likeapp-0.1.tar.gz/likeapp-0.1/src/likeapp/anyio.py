from __future__ import annotations

import functools
import inspect
from asyncio import iscoroutinefunction
from typing import Any, Callable, Dict, ParamSpec, TypeVar

import anyio


def isasynccallable(__object: Any) -> bool:  # noqa
    while isinstance(__object, functools.partial):
        __object = __object.func

    return iscoroutinefunction(__object) or (
        callable(__object) and iscoroutinefunction(__object.__call__)
    )


_RT = TypeVar("_RT")
_P = ParamSpec("_P")


def _prepare_kwargs(spec: Any, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    if spec.varkw:
        return kwargs
    return {k: v for k, v in kwargs.items() if k in spec.args or k in spec.kwonlyargs}


async def as_async(
    function: Callable[_P, _RT],
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> _RT:
    _s = inspect.getfullargspec(inspect.unwrap(function))
    function = functools.partial(function, *args, **_prepare_kwargs(_s, kwargs))
    if isasynccallable(function):
        return await function()
    return await anyio.to_thread.run_sync(function)
