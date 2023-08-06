from typing import (Any, Callable, Sequence, TypeVar, Union, get_args,
                    get_origin)

from pydantic.fields import FieldInfo, ModelField, Undefined

from devtools import config as _tk_config
from devtools.models import Model
from devtools.providers.log import LoggerHandler
from devtools.utils.helpers import deprecated, lazy_property

NOT_FOUND = object()

ProviderConfigT = TypeVar("ProviderConfigT", bound="ProviderConfig")


class ProviderConfig(Model):
    _prefix_: str = ""
    _no_prefix_: Sequence[str] = []

    class Config(Model.Config):
        arbitrary_types_allowed = True

        alias_generator = str.upper  # type: ignore

    _logger = LoggerHandler()

    @lazy_property
    @deprecated
    def logger(self):
        return self._logger

    @classmethod
    @deprecated
    def from_env(
        cls: type[ProviderConfigT],
        *,
        config: _tk_config.ConfigLike | None = None,
        ignore_none: bool = True,
        **fields,
    ):
        return from_env(cls, config=config, ignore_none=ignore_none, **fields)


def from_env(
    provider_config: type[ProviderConfigT],
    *,
    config: _tk_config.ConfigLike | None = None,
    ignore_none: bool = True,
    _prefix_: str | None = None,
    _no_prefix_: Sequence[str] | None = None,
    **fields,
):
    """Inicializa a classe através de variáveis de ambiente usando
    o nome dos atributos com UPPER_CASE."""
    cfg: _tk_config.ConfigLike = config if config is not None else _tk_config.Config()
    prefix = _prefix_ if _prefix_ is not None else provider_config._prefix_
    no_prefix = _no_prefix_ if _no_prefix_ is not None else provider_config._no_prefix_
    name_factory = _make_name_factory(prefix, no_prefix)
    if ignore_none:
        fields = {key: value for key, value in fields.items() if value is not None}
    args = {
        field.name: _get_config_value(field, cfg, name_factory)
        for field in provider_config.__fields__.values()
        if field.name not in fields
    }
    return provider_config(**args, **fields)


def _get_config_value(
    field: ModelField,
    config: _tk_config.ConfigLike,
    name_factory: Callable[[str], str],
) -> Any:
    type_, optional = _get_type(field.outer_type_)
    if not optional:
        return _get_config(name_factory, config, field)
    value = _get_config(name_factory, config, field)
    return type_(value) if value else None


def _make_name_factory(prefix: str, exclude: Sequence[str]):
    def _get_env_name(name: str):
        if prefix and name not in exclude:
            name = f'{prefix.removesuffix("_")}_{name}'
        return name.upper()

    return _get_env_name


def _get_config(
    name_factory: Callable[[str], str],
    config: _tk_config.ConfigLike,
    field: ModelField,
    cast: Callable | None = None,
):
    if cast is None:
        cast = field.type_

    default = _get_default(field.field_info)

    def _skip_key_error(name: str):
        try:
            value = config.get(name_factory(name), cast=cast)
        except KeyError:
            return NOT_FOUND
        else:
            return value

    value, name_value = (
        _skip_key_error(field.alias),
        _skip_key_error(field.name),
    )
    if value is not NOT_FOUND:
        return value
    if name_value is not NOT_FOUND:
        return name_value
    if default is not _tk_config.MISSING:
        return default
    raise _tk_config.MissingKeyError(field.name)


def _get_default(field_info: FieldInfo):
    if field_info.default is not Undefined:
        return field_info.default
    if field_info.default_factory is not None:
        return field_info.default_factory()
    return _tk_config.MISSING


def _get_type(field_type: type) -> tuple[type, bool]:
    is_union = get_origin(field_type) is Union
    if not is_union:
        return field_type, False
    args = get_args(field_type)
    if len(args) != 2 or args[1] is not type(None):
        raise NotImplementedError(
            f"from env does not support multiple union types: <{field_type!r}>"
        )
    return args[0], True  # retornando o tipo primário
