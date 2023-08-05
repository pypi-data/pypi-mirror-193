"""ASGI-Tools Utils."""

from functools import wraps
from inspect import isasyncgenfunction, iscoroutinefunction
from typing import Awaitable, Callable

from multidict import CIMultiDict

from asgi_tools.types import TASGIHeaders


def is_awaitable(fn: Callable) -> bool:
    """Check than the given function is awaitable."""
    return iscoroutinefunction(fn) or isasyncgenfunction(fn)


def to_awaitable(fn: Callable) -> Callable[..., Awaitable]:
    """Convert the given function to a coroutine function if it isn't"""
    if is_awaitable(fn):
        return fn

    @wraps(fn)
    async def coro(*args, **kwargs):
        return fn(*args, **kwargs)

    return coro


def parse_headers(headers: TASGIHeaders) -> CIMultiDict:
    """Decode the given headers list."""
    return CIMultiDict([(n.decode("latin-1"), v.decode("latin-1")) for n, v in headers])
