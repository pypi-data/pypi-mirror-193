from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Column

from devtools.providers.database.types import GUUID

from . import base, comp, where, wrap


def external_id_filter(
    expected: str | UUID | Column[GUUID],
) -> where.Field[str | UUID | Column[GUUID]]:
    return where.Field('external_id', expected, wrapper=wrap.UUIDWrapper())


def partner_key_filter(expected: str) -> where.Field[str]:
    return where.Field('partner_key', expected)


def is_active(expected: bool) -> where.Field[bool]:
    return where.Field('active', expected, wrapper=wrap.BoolWrapper())


def created_at_between(
    start: date | datetime, end: date | datetime
) -> where.Field[tuple[date, date]]:
    return where.Field('created_at', (start, end), comparator=comp.Between())


def int_parsed_filter(
    field: str,
    expected: wrap.IntImpl,
    comparator: base.Comparator[int] = comp.Equals(),
) -> where.Field[int]:
    return where.Field(
        field, wrap.IntWrapper()(expected), comparator=comparator
    )
