from dataclasses import dataclass
from inspect import isclass
from typing import Any, Generic, Sequence, TypeVar

import sqlalchemy as sa
from sqlalchemy.sql import ColumnCollection, ColumnElement
from sqlalchemy.sql.elements import BooleanClauseList

from devtools.providers.database.filters import base, comp, wrap
from devtools.providers.database.types.entity import Entity
from devtools.utils.helpers import lazy_property

T = TypeVar('T')


@dataclass(frozen=True)
class Field(Generic[T]):
    field: str
    expected: T | None
    comparator: base.Comparator[T] = comp.Equals()
    wrapper: base.Wrapper[T] = wrap.DefaultWrapper()

    @lazy_property
    def processed_expected(self) -> Any:
        return None if self.expected is None else self.wrapper(self.expected)

    def apply(
        self, entity_cls: type[Entity] | ColumnCollection
    ) -> BooleanClauseList | ColumnElement[sa.Boolean]:
        attr = retrieve_attr(entity_cls, self.field)
        return (
            self.comparator(attr, self.processed_expected)
            if self.expected_is_valid
            else sa.true()
        )

    def __bool__(self):
        return self.expected_is_valid

    @property
    def expected_is_valid(self):
        return self.expected is not None


class Operator:
    def __init__(self, *filters: base.Filter) -> None:
        self._filters = filters

    @classmethod
    def build(cls, filters: Sequence[base.Filter]):
        return cls(*filters)

    def __bool__(self):
        return True


class And(Operator):
    def apply(
        self, entity_cls: type[Entity]
    ) -> BooleanClauseList | ColumnElement[sa.Boolean]:
        return sa.and_(
            sa.true(), *(f.apply(entity_cls) for f in self._filters)
        )


class Or(Operator):
    def apply(
        self, entity_cls: type[Entity]
    ) -> BooleanClauseList | ColumnElement[sa.Boolean]:
        return sa.or_(*(f.apply(entity_cls) for f in self._filters))


def retrieve_attr(
    entity: type[Entity] | ColumnCollection, field: str
) -> ColumnElement:
    if isclass(entity) and issubclass(entity, Entity):
        field = 'id_' if field == 'id' else field
    return getattr(entity, field)
