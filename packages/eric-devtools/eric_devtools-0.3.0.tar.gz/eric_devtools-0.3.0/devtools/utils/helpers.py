import asyncio
import base64
import itertools
from contextlib import contextmanager
from functools import wraps
from typing import (Any, AsyncGenerator, Callable, Coroutine, Literal,
                    MutableMapping, NamedTuple, ParamSpec, Protocol, TypeVar,
                    cast)

from devtools.types.state import State
from devtools.utils.string import to_camel

from ._helpers import AsyncContextHelper, LazyFieldDescriptor, deprecated

DEFAULT_ENCODING = "utf-8"


State = State  # Compatibility
T = TypeVar("T")
SuccessT = TypeVar("SuccessT", contravariant=True)
FailureT = TypeVar("FailureT", contravariant=True)
Self = TypeVar("Self")
P = ParamSpec("P")


@contextmanager
def reset_changes(mapping: MutableMapping):
    before = dict(mapping.items())
    yield mapping
    mapping.update(before)


def is_base_64(value: str | bytes):
    try:
        if isinstance(value, str):
            value = bytes(value, "ascii")
        return base64.b64encode(base64.b64decode(value)) == value
    except (TypeError, ValueError):
        return False


def encode_base_64(content: bytes | str) -> bytes:
    if isinstance(content, str):
        content = bytes(content, "ascii")
    return base64.b64encode(content)


_field_template = "_lazyfield_{name}"


def lazy_field(func: Callable[[Self], T]) -> Callable[[Self], T]:
    name = _field_template.format(name=func.__name__)

    @wraps(func)
    def inner(self: Self) -> T:
        try:
            result = cast(T, object.__getattribute__(self, name))
        except AttributeError:
            result = func(self)
            object.__setattr__(self, name, result)
        return result

    return inner


def lazy_property(func: Callable[[Self], T]) -> LazyFieldDescriptor[Self, T]:
    return LazyFieldDescriptor(func)


def asynccontexthelper(
    func: Callable[P, AsyncGenerator[T, None]]
) -> Callable[P, AsyncContextHelper[P, T]]:
    @wraps(func)
    def helper(*args: P.args, **kwargs: P.kwargs) -> AsyncContextHelper[P, T]:
        return AsyncContextHelper(func, *args, **kwargs)

    return helper


def lazy_async_field(
    func: Callable[[Self], Coroutine[Any, Any, T]]
) -> Callable[[Self], Coroutine[Any, Any, T]]:
    name = _field_template.format(name=func.__name__)

    @wraps(func)
    async def inner(self: Self) -> T:
        try:
            result = cast(T, object.__getattribute__(self, name))
        except AttributeError:
            result = await func(self)
            object.__setattr__(self, name, result)
        return result

    return inner


def update_field(target: object, func: Callable, val: Any):
    object.__setattr__(target, _field_template.format(name=func.__name__), val)


def reset_field(target: object, func: Callable):
    object.__delattr__(target, _field_template.format(name=func.__name__))


async def to_async(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    return await asyncio.to_thread(func, *args, **kwargs)


def to_camel_obj(obj: dict[str, Any]):
    return {
        to_camel(key): (to_camel_obj(value) if isinstance(value, dict) else value)
        for key, value in obj.items()
    }


class FeedableOutput(Protocol[SuccessT, FailureT]):
    def feed_success(self, output: SuccessT):
        ...

    def feed_failure(self, output: FailureT):
        ...


class NullFeedable:
    def feed_success(self, output: Any):
        ...

    def feed_failure(self, output: Any):
        ...


@contextmanager
def with_callbacks(
    exception: type[Exception],
    fail_callback: Callable[[], FailureT],
    success_callback: Callable[[], SuccessT],
    feedable_output: FeedableOutput[SuccessT, FailureT] = NullFeedable(),
):
    try:
        yield
    except exception:
        feedable_output.feed_failure(fail_callback())
        raise
    else:
        feedable_output.feed_success(success_callback())


@asynccontexthelper
async def with_async_callbacks(
    exception: type[Exception],
    fail_callback: Callable[[], Coroutine[Any, Any, FailureT]],
    success_callback: Callable[[], Coroutine[Any, Any, SuccessT]],
    feedable_output: FeedableOutput[SuccessT, FailureT] = NullFeedable(),
):
    try:
        yield
    except exception:
        feedable_output.feed_failure(await fail_callback())
        raise
    else:
        feedable_output.feed_success(await success_callback())


def merge_dicts(
    left: dict[str, Any],
    right: dict[str, Any],
    not_sequence_priority: Literal["left", "right"] = "left",
):
    output_dict = left | right
    for key, left_value in left.items():
        if key not in right:
            continue
        right_value = right[key]
        if type(left_value) is not type(right_value) or not isinstance(
            left_value, (list, set, tuple, dict)
        ):
            output_dict[key] = (
                left_value if not_sequence_priority == "left" else right_value
            )
            continue
        if isinstance(left_value, dict):
            output_dict[key] = merge_dicts(
                left_value, right_value, not_sequence_priority
            )
        else:
            typ = type(left_value)
            output_dict[key] = typ(itertools.chain(left_value, right_value))
    return output_dict


class _ArnTuple(NamedTuple):
    queue_name: str
    account_id: str
    region: str
    rest: str


def arn_parse(arn: str) -> _ArnTuple:
    return _ArnTuple(*arn.rsplit(":", 3)[::-1])


__all__ = ["deprecated"]
