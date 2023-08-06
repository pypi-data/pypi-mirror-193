from datetime import date, time
from typing import Any

from sqlalchemy import Boolean, true
from sqlalchemy.sql import ColumnElement
from sqlalchemy.sql.elements import BooleanClauseList

from devtools.providers.database.filters.base import Comparator

SortableTypeDef = int | float | date | time
SequenceTypeDef = list | tuple


class Equals(Comparator[Any]):
    def __call__(
        self, attr: ColumnElement, expected: Any
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr == expected


class NotEqual(Comparator[Any]):
    def __call__(
        self, attr: ColumnElement, expected: Any
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr != expected


class Greater(Comparator[SortableTypeDef]):
    def __call__(
        self, attr: ColumnElement, expected: SortableTypeDef
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr > expected


class GreaterEquals(Comparator[SortableTypeDef]):
    def __call__(
        self, attr: ColumnElement, expected: SortableTypeDef
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr >= expected


class Lesser(Comparator[SortableTypeDef]):
    def __call__(
        self, attr: ColumnElement, expected: SortableTypeDef
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr < expected


class LesserEquals(Comparator[SortableTypeDef]):
    def __call__(
        self, attr: ColumnElement, expected: SortableTypeDef
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr <= expected


class Between(Comparator[tuple[SortableTypeDef, SortableTypeDef]]):
    def __call__(
        self,
        attr: ColumnElement,
        expected: tuple[SortableTypeDef, SortableTypeDef],
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        left, right = expected
        return attr.between(left, right)


class Like(Comparator[str]):
    def __call__(
        self, attr: ColumnElement, expected: str
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr.like(f'%{expected}%')


class ILike(Comparator[str]):
    def __call__(
        self, attr: ColumnElement, expected: str
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr.ilike(f'%{expected}%')


class Contains(Comparator[SequenceTypeDef]):
    def __call__(
        self, attr: ColumnElement, expected: SequenceTypeDef
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr.in_(expected)


class Excludes(Comparator[SequenceTypeDef]):
    def __call__(
        self, attr: ColumnElement, expected: SequenceTypeDef
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr.not_in(expected)


class IsNull(Comparator[bool]):
    def __call__(
        self, attr: ColumnElement, expected: bool
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        return attr.is_(None) if expected else attr.is_not(None)


class AlwaysTrue(Comparator):
    """Just an empty Comparison, or a comparison placeholder"""

    def __call__(
        self, attr: ColumnElement, expected: Any
    ) -> BooleanClauseList | ColumnElement[Boolean]:
        del attr, expected
        return true()
