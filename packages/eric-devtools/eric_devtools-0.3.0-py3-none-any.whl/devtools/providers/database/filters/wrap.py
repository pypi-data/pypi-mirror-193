from datetime import date
from enum import Enum
from typing import Any, Protocol
from uuid import UUID

from sqlalchemy import Column, false, func, true

from devtools.providers.database.filters import base
from devtools.providers.database.types.guuid import GUUID


class DateWrapper(base.Wrapper[str | date]):
    def __call__(self, val: str | date):
        return func.date(val)


class NullWrapper(base.Wrapper[Any]):
    def __call__(self, val: Any) -> Any:
        return val


class EnumWrapper(base.Wrapper[Enum]):
    def __call__(self, val: Enum) -> Any:
        return val.value


class EnumNameWrapper(base.Wrapper[Enum]):
    def __call__(self, val: Enum) -> Any:
        return val.name


class UUIDWrapper(base.Wrapper[UUID | str | Column[GUUID]]):
    def __call__(self, val: UUID | str) -> Any:
        if isinstance(val, str):
            val = UUID(val)
        return val


class IntImpl(Protocol):
    def __int__(self) -> int:
        ...


class IntWrapper(base.Wrapper[IntImpl]):
    def __call__(self, val: IntImpl) -> Any:
        return int(val)


class BoolWrapper(base.Wrapper[bool]):
    def __call__(self, val: bool) -> Any:
        return true() if val else false()


class DefaultWrapper(base.Wrapper[Any]):
    def __call__(self, val: Any) -> Any:
        return EnumWrapper()(val) if isinstance(val, Enum) else val
