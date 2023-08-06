from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import declared_attr

from .guuid import GUUID


class SerialIdMixin:
    @declared_attr
    def id_(self):
        return sa.Column('id', sa.Integer, primary_key=True)


class UUIDIdMixin:
    @declared_attr
    def id_(self):
        return sa.Column('id', GUUID(), default=uuid4)  # type: ignore
