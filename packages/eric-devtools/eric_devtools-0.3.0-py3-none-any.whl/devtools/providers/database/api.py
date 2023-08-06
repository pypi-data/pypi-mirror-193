import typing

from fastapi import Request
from starlette.datastructures import State

from devtools.providers.config import from_env
from devtools.providers.database.asyncio import AsyncDatabaseProvider
from devtools.providers.database.config import DatabaseConfig
from devtools.providers.database.sync import SyncDatabaseProvider
from devtools.utils.helpers import to_async

ProviderT = typing.TypeVar(
    'ProviderT', SyncDatabaseProvider, AsyncDatabaseProvider
)


def setup_databases(
    provider_class: type[ProviderT], *configs: tuple[str, DatabaseConfig]
):
    async def _make_provider(config: DatabaseConfig) -> ProviderT:
        provider = provider_class.create(config)
        if isinstance(provider, SyncDatabaseProvider):
            health_check = to_async(provider.health_check)
        else:
            health_check = provider.health_check()
        await health_check
        return provider

    configs = configs or (
        (provider_class.state_name, from_env(DatabaseConfig)),
    )

    async def setup(state: State):
        for name, cfg in configs:
            if hasattr(state, name):
                continue
            setattr(state, name, await _make_provider(cfg))

    return setup


def make_provider_dependency(name: str):
    def _get_provider(request: Request):
        state: State = request.app.state
        return getattr(state, name)

    return _get_provider
