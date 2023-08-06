import logging
import pickle
from dataclasses import dataclass
from functools import partial
from typing import Any, Optional
from uuid import UUID

import aioredis
from aioredis.exceptions import RedisError
from fastapi import Request
from starlette.datastructures import State
from devtools.exceptions import UnexpectedDatabaseError

from devtools.models.models import GenericModel, ModelT
from devtools.types.config import Env

_CACHE_TIME_ENUM = {
    Env.DEV: 30,
    Env.TEST: 60 ** 2,
    Env.HML: 60 * 10,
    Env.PRD: 60 ** 2,
}


def _get_fakeredis():
    import fakeredis.aioredis

    return fakeredis.aioredis.FakeRedis


@dataclass
class RedisConfig:
    host: str
    port: int
    password: str
    env: Env
    uid: str
    use_ssl: bool
    _time: int | None = None

    @property
    def time(self) -> int:
        return self._time or _CACHE_TIME_ENUM[self.env]

    def _compile_name(self, partner_key: str, user_id: Optional[UUID]):
        return (
            f'{self.uid}-{partner_key}'
            if user_id is None
            else f'{self.uid}-{partner_key}-{user_id}'
        )


def _compile_key(obj_type: str, key: Optional[str]):
    return f'{obj_type}-{key}' if key else obj_type


class RedisProvider:
    state_name = 'redis_provider'

    def __init__(self, config: RedisConfig) -> None:
        self._config = config
        self._redis = self._get_redis()
        self._logger = logging.getLogger('gunicorn.error')

    def _get_redis(self):
        if self._config.env is Env.TEST:
            return _get_fakeredis()()
        pool_factory = partial(
            aioredis.ConnectionPool,
            db=0,
            host=self._config.host,
            port=self._config.port,
            password=self._config.password or None,
        )
        return aioredis.Redis(
            connection_pool=pool_factory(
                connection_class=aioredis.SSLConnection
            )
            if self._config.use_ssl
            else pool_factory(),
        )

    async def set_cache(
        self,
        partner_key: str,
        obj_type: str,
        value: Any,
        user_id: Optional[UUID] = None,
        key: Optional[str] = None,
        expiration: Optional[int] = None,
    ) -> None:
        name = self._config._compile_name(partner_key, user_id)
        key = _compile_key(obj_type, key)
        pipeline = self._redis.pipeline()
        await pipeline.hset(name, key, pickle.dumps(value))
        await pipeline.expire(name, expiration or self._config.time)
        await pipeline.execute()

    async def get_cache(
        self,
        partner_key: str,
        obj_type: str,
        user_id: Optional[UUID] = None,
        key: Optional[str] = None,
    ):
        name = self._config._compile_name(partner_key, user_id)
        key = _compile_key(obj_type, key)
        cached = await self._redis.hget(name, key)
        return pickle.loads(cached) if cached else {}

    async def health_check(self):
        try:
            await self._redis.ping()
        except RedisError:
            self._logger.exception('Failed connecting to redis')
            return False
        else:
            return True


def setup_redis_provider(config: RedisConfig):
    async def _setup_redis(state: State):
        provider = RedisProvider(config)
        setattr(
            state,
            RedisProvider.state_name,
            provider,
        )
        if not await provider.health_check():
            raise UnexpectedDatabaseError('Cache')

    return _setup_redis


class RedisProxy:
    def __init__(self, request: Request) -> None:
        self._redis = getattr(
            request.app.state, RedisProvider.state_name
        )  # type: RedisProvider

    async def healthcheck(self):
        return await self._redis.health_check()

    async def set_cache(
        self,
        partner_key: str,
        obj_type: str,
        value: Any,
        user_id: Optional[UUID] = None,
        key: Optional[str] = None,
        expiration: Optional[int] = None,
    ) -> None:
        await self._redis.set_cache(
            partner_key, obj_type, value, user_id, key, expiration
        )

    async def get_cache(
        self,
        partner_key: str,
        obj_type: str,
        user_id: Optional[UUID] = None,
        key: Optional[str] = None,
    ):
        return await self._redis.get_cache(partner_key, obj_type, user_id, key)


class CacheParser(GenericModel):
    def __init__(
        self, output_class: type[ModelT], obj_type: Any
    ) -> None:
        self._output_class = output_class
        self._obj_type = obj_type

    async def parse(
        self,
        cache_proxy: RedisProxy,
        partner_key: str,
        user_id: Optional[UUID] = None,
        key: Optional[str] = None,
    ) -> Optional[ModelT]:
        response = await cache_proxy.get_cache(
            partner_key, self._obj_type.value, user_id, key
        )
        return self._output_class.parse_obj(response) if response else None

    async def save(
        self,
        cache_proxy: RedisProxy,
        partner_key: str,
        value: ModelT,
        user_id: Optional[UUID] = None,
        key: Optional[str] = None,
        expiration: Optional[int] = None,
    ) -> None:
        await cache_proxy.set_cache(
            partner_key,
            self._obj_type.value,
            value.dict(),
            user_id,
            key,
            expiration,
        )
