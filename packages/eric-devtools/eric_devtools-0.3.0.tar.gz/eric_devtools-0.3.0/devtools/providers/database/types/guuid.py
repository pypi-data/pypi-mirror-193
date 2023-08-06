import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.engine import Dialect
from sqlalchemy.types import TypeDecorator


class GUUID(TypeDecorator):

    impl = String

    cache_ok = True

    def __init__(self) -> None:
        super().__init__(length=32)

    def load_dialect_impl(self, dialect: Dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID)
        else:
            return dialect.type_descriptor(String)

    def process_bind_param(
        self, value: str | uuid.UUID | None, dialect: Dialect
    ):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            return (
                '%.32x' % value.int
                if isinstance(value, uuid.UUID)
                else '%.32x' % uuid.UUID(value).int
            )

    def process_result_value(
        self, value: str | uuid.UUID | None, dialect: Dialect
    ):
        if value is not None and not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
