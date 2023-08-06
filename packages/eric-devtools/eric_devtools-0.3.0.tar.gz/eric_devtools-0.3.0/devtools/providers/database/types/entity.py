from typing import Any, ClassVar, Generator, Protocol, TypeVar

from sqlalchemy import MetaData, inspect
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy.orm.properties import ColumnProperty

from devtools.utils.string import to_snake

T = TypeVar('T')


class EntityLike(Protocol):
    metadata: ClassVar[MetaData]

    def __init__(self, **kwargs):
        ...

    @classmethod
    @property
    def __tablename__(cls) -> str:
        ...

    def __fields__(self) -> Generator[str, None, None]:
        ...

    def dict(self) -> dict[str, Any]:
        ...

    def set(self, **vals: Any) -> None:
        ...


def _as_declarative(cls: type[T]) -> type[T]:
    return as_declarative()(cls)


def _entity_fields(entity: EntityLike):
    for prop in inspect(type(entity)).iterate_properties:
        if isinstance(prop, ColumnProperty):
            yield prop.key


def _to_dict(entity: EntityLike):
    return {key: getattr(entity, key) for key in _entity_fields(entity)}


def _set_entity(entity: EntityLike, **vals):
    for key, val in vals.items():
        setattr(entity, key, val)


def make_tablename(suffix: str = 'Entity'):
    def __tablename__(entity_cls: type[EntityLike]):
        return to_snake(entity_cls.__name__.removesuffix(suffix))

    return __tablename__


def entity_factory(name: str, suffix: str = 'Entity'):
    tablename = make_tablename(suffix)

    @_as_declarative
    class _Entity:
        metadata: ClassVar[MetaData]

        def __init__(self, **kwargs) -> None:
            del kwargs

        @classmethod
        @declared_attr
        def __tablename__(cls):
            return tablename(cls)

        __fields__ = _entity_fields

        dict = _to_dict

        set = _set_entity

    return type(name, (_Entity,), dict(_Entity.__dict__))


Entity = entity_factory('Entity')
