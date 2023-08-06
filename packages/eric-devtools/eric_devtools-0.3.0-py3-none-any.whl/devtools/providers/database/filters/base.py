from typing import Any, Protocol, TypeVar

from sqlalchemy import Boolean
from sqlalchemy.sql import ColumnElement
from sqlalchemy.sql.elements import BooleanClauseList

from devtools.providers.database.types.entity import Entity


class Filter(Protocol):
    def apply(
        self, entity_cls: type[Entity]
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        ...

    def __bool__(self) -> bool:
        ...


T = TypeVar('T', contravariant=True)


class Comparator(Protocol[T]):
    def __call__(
        self, attr: ColumnElement, expected: T
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        ...


class Wrapper(Protocol[T]):
    def __call__(self, val: T) -> Any:
        ...
