import abc
from dataclasses import dataclass
from typing import Literal, final

from sqlalchemy.sql import ColumnElement, Select

from devtools.providers.database.filters.comp import Greater
from devtools.providers.database.filters.where import Field, retrieve_attr
from devtools.providers.database.types import Entity


@dataclass
class OrderBy:
    field: str
    order: Literal['asc', 'desc'] | None = None

    def apply(self, entity_cls: type[Entity]) -> ColumnElement:
        attr = retrieve_attr(entity_cls, self.field)
        if self.order is None:
            return attr
        elif self.order == 'asc':
            return attr.asc()
        else:
            return attr.desc()

    @staticmethod
    def none():
        return _none

    def should_apply(self):
        return self is not _none

    def __bool__(self):
        return self.should_apply()


_none = OrderBy('')


class Paginate(abc.ABC):
    @final
    def __init__(self, *, limit: int, offset: int) -> None:
        self._limit = limit
        self._offset = offset

    @abc.abstractmethod
    def apply(self, query: Select) -> Select:
        ...

    @classmethod
    def none(cls):
        return _NullPaginate(limit=0, offset=0)

    def __bool__(self):
        return isinstance(self, _NullPaginate)


class LimitOffsetPaginate(Paginate):
    def apply(self, query: Select) -> Select:
        return query.limit(self._limit).offset(self._offset)


class IdPaginate(Paginate):
    def apply(self, query: Select) -> Select:
        return query.where(
            Field('id', self._offset, comparator=Greater()).apply(
                query.selected_columns
            )
        ).limit(self._limit)


class _NullPaginate(Paginate):
    def apply(self, query: Select) -> Select:
        return query
