from pydantic import root_validator
from pydantic.utils import GetterDict

from devtools.config import MissingKeysError
from devtools.providers.config import ProviderConfig, from_env
from devtools.providers.database import typedef
from devtools.utils.helpers import lazy_property


class DatabaseConfig(ProviderConfig):
    _prefix_ = "db"

    driver: typedef.Driver
    host: str
    name: str = ""
    user: str = ""
    password: str = ""
    port: int = 0
    pool_size: int = 20
    pool_recycle: int = 3600
    max_overflow: int = 0
    connect_timeout: float = -1

    @root_validator
    def validate_fields_received(cls, values: GetterDict):
        driver: typedef.Driver = values.get("driver")
        driver_type = typedef.DRIVER_MAPPING[driver]
        received_fields = {
            item: values.get(item) for item in driver_type.required_fields
        }
        if not received_fields.get("port") and "port" in driver_type.required_fields:
            received_fields["port"] = driver_type.port
        if not all(received_fields.values()):
            raise MissingKeysError(
                [key for key, value in received_fields.items() if not value]
            )
        return values


class DatabaseProperties:
    def __init__(self, config: DatabaseConfig) -> None:
        self._config = config

    def _get_timeout_config(self, is_async: bool):
        return (
            {
                self.driver_type.timeout_arg_name(
                    is_async=is_async
                ): self._config.connect_timeout
            }
            if self._config.connect_timeout != -1
            else {}
        )

    @lazy_property
    def sync_connection_args(self):
        return {"connect_args": self._get_timeout_config(False)}

    @lazy_property
    def async_connection_args(self):
        return {"connect_args": self._get_timeout_config(True)}

    @lazy_property
    def driver_type(self):
        return typedef.DRIVER_MAPPING[self._config.driver]

    @lazy_property
    def get_port(self):
        return self._config.port or self.driver_type.port

    @lazy_property
    def _required_mapping(self):
        return {
            item: getattr(self._config, item)
            for item in self.driver_type.required_fields
        } | {"port": self.get_port}

    @lazy_property
    def async_uri(self):
        template = self.driver_type.get_connection_template(is_async=True)
        return template.format_map(self._required_mapping)

    @lazy_property
    def sync_uri(self):
        template = self.driver_type.get_connection_template(is_async=False)
        return template.format_map(self._required_mapping)

    @lazy_property
    def pool_config(self):
        driver_type = self.driver_type
        if driver_type.has_config:
            return driver_type.config
        return {
            "pool_size": self._config.pool_size,
            "pool_recycle": self._config.pool_recycle,
            "max_overflow": self._config.max_overflow,
        }


def sqlite_config_factory(host: str | None = None):
    if host:
        return DatabaseConfig(driver=typedef.Driver.SQLITE, host=host)
    return from_env(DatabaseConfig, driver=typedef.Driver.SQLITE)


def postgres_config_factory(
    *,
    host: str | None = None,
    port: int = 0,
    user: str | None = None,
    password: str | None = None,
    name: str | None = None
):
    return from_env(
        DatabaseConfig,
        driver=typedef.Driver.POSTGRES,
        host=host,
        port=port,
        user=user,
        password=password,
        name=name,
    )
