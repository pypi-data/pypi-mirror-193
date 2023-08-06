from typing import Any, Generic, TypeVar

import sqlalchemy as sa

from devtools import exceptions, models
from devtools.providers.database.filters import And, Filter, OrderBy
from devtools.providers.database.filters.operators import Paginate
from devtools.providers.database.sync import SyncContext
from devtools.providers.database.typedef import DictConvertable
from devtools.providers.database.types import Entity
from devtools.utils.helpers import lazy_field
from devtools.utils.string import to_spaced

EntityT = TypeVar('EntityT', bound=Entity)
ModelT = TypeVar('ModelT', bound=models.Model)


def get(
    context: SyncContext, entity_cls: type[EntityT], clause: Filter,
) -> EntityT:
    with context.acquire('session') as session:
        query = sa.select(entity_cls).where(clause.apply(entity_cls))
        result = session.execute(query)
        if first := result.scalars().first():
            return first
        raise exceptions.NotFoundError(to_spaced(entity_cls.__name__))


def search(
    context: SyncContext,
    entity_cls: type[EntityT],
    *clauses: Filter,
    order_by: OrderBy = OrderBy.none(),
    paginate: Paginate = Paginate.none(),
) -> list[EntityT]:
    with context.acquire('session') as session:
        query = sa.select(entity_cls).where(
            And.build(clauses).apply(entity_cls)
        )
        if order_by.should_apply():
            query = query.order_by(order_by.apply(entity_cls))
        query = paginate.apply(query)
        result = session.execute(query)
        return result.scalars().all()


def create(
    context: SyncContext, entity_cls: type[EntityT], payload: dict[str, Any],
) -> EntityT:
    with context.acquire('session') as session:
        with session.begin():
            entity = entity_cls(**payload)
            session.add(entity)
            session.flush([entity])
            return entity


def update(
    context: SyncContext,
    entity_cls: type[EntityT],
    clause: Filter,
    payload: dict[str, Any],
) -> EntityT:
    with context.acquire('session') as session:
        with session.begin():
            entity = get(context, entity_cls, clause)
            entity.set(**payload)
            session.add(entity)
            session.flush([entity])
            return entity


def delete(
    context: SyncContext, entity_cls: type[Entity], clause: Filter,
):
    with context.acquire('session') as session:
        with session.begin():
            entity = get(context, entity_cls, clause)
            session.delete(entity)
            session.flush()


class _Response(Generic[EntityT, ModelT]):
    def __init__(self, entity: EntityT, model_cls: type[ModelT]) -> None:
        self._entity = entity
        self._model_cls = model_cls

    @lazy_field
    def get(self) -> ModelT:
        return self._model_cls.parse_obj(self._entity.dict())

    def unsafe_get(self) -> EntityT:
        return self._entity


class _ListResponse(Generic[EntityT, ModelT]):
    def __init__(
        self, entities: list[EntityT], model_cls: type[ModelT]
    ) -> None:
        self._entities = entities
        self._model_cls = model_cls

    @lazy_field
    def get(self) -> list[ModelT]:
        return [
            self._model_cls.parse_obj(entity.dict())
            for entity in self._entities
        ]

    def unsafe_get(self) -> list[EntityT]:
        return self._entities

    def __iter__(self):
        yield from self.get()

    def size(self):
        return len(self.get())

    def __len__(self):
        return self.size()


class SyncRepository(Generic[EntityT, ModelT]):
    def __init__(
        self, entity_cls: type[EntityT], model_cls: type[ModelT]
    ) -> None:
        self._entity_cls = entity_cls
        self._model_cls = model_cls

    def _as_response(self, entity: EntityT) -> _Response[EntityT, ModelT]:
        return _Response(entity, self._model_cls)

    def _as_list_response(
        self, entities: list[EntityT]
    ) -> _ListResponse[EntityT, ModelT]:
        return _ListResponse(entities, self._model_cls)

    def get(
        self, context: SyncContext, clause: Filter
    ) -> _Response[EntityT, ModelT]:
        entity = get(context, self._entity_cls, clause)
        return self._as_response(entity=entity)

    def create(
        self,
        context: SyncContext,
        payload: DictConvertable,
        by_alias: bool = False,
    ):
        parsed_payload = self._parse_payload(payload, by_alias)
        result = create(context, self._entity_cls, parsed_payload)
        return self._as_response(result)

    def _parse_payload(self, payload: DictConvertable, by_alias: bool):
        return (
            payload.dict(by_alias=by_alias)
            if isinstance(payload, models.Model)
            else dict(payload)
        )

    def search(
        self,
        context: SyncContext,
        *clauses: Filter,
        order_by: OrderBy = OrderBy.none(),
        paginate: Paginate = Paginate.none(),
    ) -> _ListResponse[EntityT, ModelT]:
        result = search(
            context,
            self._entity_cls,
            *clauses,
            order_by=order_by,
            paginate=paginate,
        )
        return self._as_list_response(result)

    def update(
        self,
        context: SyncContext,
        clause: Filter,
        payload: DictConvertable,
        by_alias: bool = False,
    ):
        parsed_payload = self._parse_payload(payload, by_alias)
        result = update(context, self._entity_cls, clause, parsed_payload)
        return self._as_response(result)

    def delete(self, context: SyncContext, clause: Filter) -> None:
        delete(context, self._entity_cls, clause)
