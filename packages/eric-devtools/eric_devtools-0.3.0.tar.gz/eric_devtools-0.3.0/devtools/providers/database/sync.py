from contextlib import contextmanager
from http import HTTPStatus
from typing import Generator, Literal, overload

import sqlalchemy as sa
import sqlalchemy.engine as sa_engine
import sqlalchemy.orm as sa_orm

from devtools.exceptions.exceptions import UnexpectedDatabaseError
from devtools.providers.config import from_env
from devtools.utils.helpers import lazy_property, merge_dicts

from .config import DatabaseConfig, DatabaseProperties


class SyncDatabaseProvider:
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
        return sa.create_engine(
            self.properties.sync_uri,
            **merge_dicts(
                self.properties.pool_config,
                self.properties.sync_connection_args,
            )
        )

    def health_check(self, should_raise: bool = True):
        try:
            with self.context().acquire('connection') as conn:
                conn.execute(sa.text('SELECT 1'))
        except Exception as e:
            if should_raise:
                raise UnexpectedDatabaseError(
                    'Connection', status=HTTPStatus.SERVICE_UNAVAILABLE
                ) from e
            return False
        else:
            return True

    def connect(self):
        return self.engine.connect()

    def context(self):
        return SyncContext(self)


class SyncContext:
    def __init__(self, provider: SyncDatabaseProvider) -> None:
        self._provider = provider
        self._waiters: list[object] = []

    @lazy_property
    def connect(self):
        return self._provider.connect()

    def session_scope(self):
        return sa_orm.scoped_session(
            sa_orm.sessionmaker(
                self.connect,
                expire_on_commit=False,
                autocommit=False,
                autoflush=False,
            )
        )

    def session(self):
        return self.session_scope()()

    @overload
    @contextmanager
    def acquire(
        self, opt: Literal['session']
    ) -> Generator[sa_orm.Session, None, None]:
        ...

    @overload
    @contextmanager
    def acquire(
        self, opt: Literal['connection']
    ) -> Generator[sa_engine.Connection, None, None]:
        ...

    @contextmanager
    def acquire(self, opt: Literal['session', 'connection']):
        if opt == 'session':
            return self._acquire_session()
        return self._acquire_connection()

    def start(self):
        if not self._waiters:
            self.connect
        self._waiters.append(object())

    def _acquire_session(self):
        with self:
            with self.session() as session:
                yield session

    def _acquire_connection(self):
        with self:
            yield self.connect

    def finish(self):
        self._waiters.pop()
        if not self._waiters:
            self.connect.close()
            del self.connect

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del exc_type, exc_value, traceback
        self.finish()
