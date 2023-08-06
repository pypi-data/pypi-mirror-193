from asyncio import iscoroutinefunction
from functools import wraps
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from devtools.providers.database.asyncio import AsyncDatabaseProvider
from devtools.providers.database.api import ProviderT
from devtools.providers.database.config import (
    DatabaseConfig,
    sqlite_config_factory,
)
from devtools.providers.database.sync import SyncDatabaseProvider
from devtools.providers.database.types import Entity
from devtools.providers.database.types.entity import EntityLike
from devtools.utils.autodiscovery import ClassFinder
from devtools.utils.helpers import lazy_property

if TYPE_CHECKING:
    from devtools.tests.test_client import NoProxyTestClient


def make_mock_create(provider: ProviderT,):
    def _mock_create(config: DatabaseConfig | None = None) -> ProviderT:
        del config
        return provider

    return _mock_create


class DatabaseTestClient:
    def __init__(
        self,
        root: Path | None = None,
        config: DatabaseConfig | None = None,
        *abstract_entitites: type[EntityLike]
    ) -> None:
        config = config or sqlite_config_factory(':memory:')
        self._internal_provider = SyncDatabaseProvider(config)
        self._sync_create = SyncDatabaseProvider.create
        self._async_create = AsyncDatabaseProvider.create
        self._abstract_entitites = (*abstract_entitites, Entity)
        self._do_find(root)

    def _do_find(self, root: Path | None):
        root = root or Path.cwd() / 'src'
        root = root.resolve()
        for entity in self._abstract_entitites:
            finder = ClassFinder(entity, path=root)
            finder.find()

    @lazy_property
    def sync_context(self):
        return self._internal_provider.context()

    @lazy_property
    def async_context(self):
        return self.async_provider.context()

    def startup(self):
        self.sync_context.start()
        SyncDatabaseProvider.create = make_mock_create(self.provider())
        with self.sync_context.acquire('connection') as conn:
            for entity in self._abstract_entitites:
                entity.metadata.create_all(conn)

    async def async_startup(self):
        self.startup()
        self.async_context.connect_from_sync(self.sync_context.connect)
        AsyncDatabaseProvider.create = make_mock_create(self.async_provider)
        await self.async_context.start()

    def shutdown(self):
        with self.sync_context.acquire('connection') as conn:
            for entity in self._abstract_entitites:
                entity.metadata.drop_all(conn)
        self.sync_context.finish()
        SyncDatabaseProvider.create = self._sync_create

    async def async_shutdown(self):
        self.shutdown()
        await self.async_context.finish()
        AsyncDatabaseProvider.create = self._async_create

    def __enter__(self):
        self.startup()
        return self

    def __exit__(self, *_):
        self.shutdown()

    async def __aenter__(self):
        await self.async_startup()
        return self

    async def __aexit__(self, *_):
        await self.async_shutdown()

    def __call__(self, func) -> Any:
        async def _async_inner(*args, **kwargs):
            async with self:
                return await func(*args, **kwargs)

        def _inner(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wraps(func)(
            _async_inner if iscoroutinefunction(func) else _inner
        )

    def provider(self):
        return self._internal_provider

    @lazy_property
    def async_provider(self):
        return AsyncDatabaseProvider(self._internal_provider.config)

    def setup_api_testclient(
        self,
        test_client: 'NoProxyTestClient',
        database_name: str = 'database',
        async_: bool = True,
    ):
        from starlette.applications import Starlette

        provider = self.async_provider if async_ else self.provider()
        app = cast(Starlette, test_client.app)

        async def startup():
            setattr(app.state, database_name, provider)
            await self.async_startup()

        async def shutdown():
            await self.async_shutdown()

        app.router.on_startup.insert(0, startup)
        app.router.on_shutdown.insert(0, shutdown)
