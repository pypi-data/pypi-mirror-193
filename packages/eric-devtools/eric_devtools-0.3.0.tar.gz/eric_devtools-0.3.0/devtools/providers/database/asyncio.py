import asyncio
from http import HTTPStatus
from typing import AsyncGenerator, Literal, overload

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
from sqlalchemy.ext import asyncio as sa_asyncio
from sqlalchemy.future.engine import Connection

from devtools.exceptions.exceptions import UnexpectedDatabaseError
from devtools.providers.config import from_env
from devtools.providers.database.config import (
    DatabaseConfig,
    DatabaseProperties,
)
from devtools.utils.helpers import (
    asynccontexthelper,
    lazy_property,
    merge_dicts,
)


class AsyncDatabaseProvider:
    state_name = 'database_provider'

    def __init__(self, config: DatabaseConfig | None = None) -> None:
        self._config = config or from_env(DatabaseConfig)
        self._properties = DatabaseProperties(self._config)

    @classmethod
    def create(cls, config: DatabaseConfig | None = None):
        return cls(config)

    @property
    def config(self):
        return self._config

    @property
    def properties(self):
        return self._properties

    @lazy_property
    def engine(self):
        return sa_asyncio.create_async_engine(
            self.properties.async_uri,
            **merge_dicts(
                self.properties.pool_config,
                self.properties.async_connection_args,
            )
        )

    async def health_check(self, should_raise: bool = True):
        try:
            async with self.context().acquire('connection') as conn:
                await conn.execute(sa.text('SELECT 1'))
        except Exception as e:
            if should_raise:
                raise UnexpectedDatabaseError(
                    'Connection', status=HTTPStatus.SERVICE_UNAVAILABLE
                ) from e
            return False
        else:
            return True

    def connect(self) -> sa_asyncio.AsyncConnection:
        return self.engine.connect()

    def context(self):
        return AsyncContext(self)


class AsyncContext:
    def __init__(self, provider: AsyncDatabaseProvider) -> None:
        self._provider = provider
        self._waiters = []

    @lazy_property
    def connect(self):
        return self._provider.connect()

    def session_scope(self):
        return sa_asyncio.async_scoped_session(
            sa_orm.sessionmaker(
                self.connect,
                expire_on_commit=False,
                autocommit=False,
                autoflush=False,
                class_=sa_asyncio.AsyncSession,  # type: ignore
            ),
            asyncio.current_task,
        )

    def session(self):
        return self.session_scope()()

    def connect_from_sync(self, conn: Connection):
        async_conn = sa_asyncio.AsyncConnection(self._provider.engine, conn)
        self.connect = async_conn
        self._waiters.append(object())

    @overload
    @asynccontexthelper
    async def acquire(
        self, opt: Literal['session']
    ) -> AsyncGenerator[sa_asyncio.AsyncSession, None]:
        ...

    @overload
    @asynccontexthelper
    def acquire(
        self, opt: Literal['connection']
    ) -> AsyncGenerator[sa_asyncio.AsyncConnection, None]:
        ...

    @asynccontexthelper
    def acquire(self, opt: Literal['session', 'connection']):
        if opt == 'session':
            return self._acquire_session()
        return self._acquire_connection()

    @asynccontexthelper
    async def begin(
        self,
    ) -> AsyncGenerator[
        tuple[sa_asyncio.AsyncSession, sa_asyncio.AsyncSessionTransaction],
        None,
    ]:
        async with self.acquire('session') as session:
            async with session.begin() as trx:
                yield session, trx

    async def _acquire_session(self):
        async with self:
            async with self.session() as session:
                yield session

    async def _acquire_connection(self):
        async with self:
            yield self.connect

    async def start(self):
        if not self._waiters:
            await self.connect
        self._waiters.append(object())

    def __await__(self):
        return self.start().__await__()

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        del exc_type, exc_value, traceback
        await self.finish()

    async def finish(self):
        self._waiters.pop()
        if not self._waiters:
            await self.connect.close()
            del self.connect
