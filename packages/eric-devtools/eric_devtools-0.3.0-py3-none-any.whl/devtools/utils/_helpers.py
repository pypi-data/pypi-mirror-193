import warnings
from functools import wraps
from types import TracebackType
from typing import (Any, AsyncGenerator, Callable, Concatenate, Coroutine,
                    Generic, ParamSpec, TypeVar)

T = TypeVar("T")
P = ParamSpec("P")
S = TypeVar("S")
Q = ParamSpec("Q")
Self = TypeVar("Self")
Another = TypeVar("Another")

_field_template = "_lazyfield_{name}"


def deprecated(func: Callable[P, T]) -> Callable[P, T]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        warnings.warn(
            f"{func.__name__} is deprecated and can be removed without notice.",
            DeprecationWarning,
        )
        return func(*args, **kwargs)

    return inner


_obj_getattr = object.__getattribute__
_obj_setattr = object.__setattr__
_obj_delattr = object.__delattr__


class LazyFieldDescriptor(Generic[Self, T]):
    def __init__(self, func: Callable[[Self], T]) -> None:
        self._func = func
        self._name = _field_template.format(name=func.__name__)

    def __get__(
        self,
        instance: Self | None,
        owner: type[Self] | None = None,
    ) -> T:
        if not instance:
            # owner is not None if instance is
            assert owner is not None
            raise AttributeError(
                f"type object{owner.__name__} has no attribute {self._func.__name__!r}"
            )
        try:
            result = self._get_result(instance)
        except AttributeError:
            try:
                result = self._set_result(instance)
            except Exception as err:
                # remove lazyfield exception context
                # to have a clearer response traceback
                raise err from None
        return result

    def _get_result(self, instance: Any) -> T:
        return _obj_getattr(instance, self._name)

    def _set_result(self, instance: Any) -> T:
        val = self._func(instance)
        _obj_setattr(instance, self._name, val)
        return val

    def __set__(self, instance: Any, value: T):
        _obj_setattr(instance, self._name, value)

    def __delete__(self, instance: Any):
        _obj_delattr(instance, self._name)


class AsyncContextHelper(Generic[P, T]):
    """Context manager helper to handle typing correctly
    and with `.param` to use contextmanager result
    as the initial param"""

    def __init__(
        self,
        func: Callable[P, AsyncGenerator[T, None]],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        self._gen = func(*args, **kwargs)
        self._func = func
        self._args = args
        self._kwargs = kwargs

    async def __aenter__(self) -> T:
        del self._args, self._kwargs, self._func
        try:
            return await anext(self._gen)
        except StopAsyncIteration:
            raise RuntimeError("generator didn't yield") from None

    async def __aexit__(
        self,
        typ: type[Exception] | None,
        value: Exception | None,
        traceback: TracebackType | None,
    ):
        if typ is None:
            try:
                await anext(self._gen)
            except StopAsyncIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")
        if value is None:
            value = typ()
        try:
            await self._gen.athrow(typ, value, traceback)
        except StopAsyncIteration as exc:
            return exc is not value
        except RuntimeError as exc:
            if exc is value:
                return False
            if (
                isinstance(value, (StopIteration, StopAsyncIteration))
                and exc.__cause__ is value
            ):
                return False
            raise
        except BaseException as exc:
            if exc is not value:
                raise
            return False
        raise RuntimeError("generator didn't stop after athrow()")

    def __call__(
        self, func: Callable[Q, Coroutine[None, None, S]]
    ) -> Callable[Q, Coroutine[None, None, S]]:
        @wraps(func)
        async def inner(*args: Q.args, **kwargs: Q.kwargs) -> S:
            async with self:
                return await func(*args, **kwargs)

        return inner

    def param(
        self,
        func: Callable[Concatenate[T, Q], Coroutine[None, None, S]],
    ) -> Callable[Q, Coroutine[None, None, S]]:
        @wraps(func)
        async def inner(*args: Q.args, **kwargs: Q.kwargs) -> S:
            async with self as val:
                return await func(val, *args, **kwargs)

        return inner

    def method(
        self,
        func: Callable[Concatenate[Another, T, Q], Coroutine[None, None, S]],
    ) -> Callable[Concatenate[Another, Q], Coroutine[None, None, S]]:
        @wraps(func)
        async def inner(another: Another, *args: Q.args, **kwargs: Q.kwargs) -> S:
            async with self as val:
                return await func(another, val, *args, **kwargs)

        return inner
