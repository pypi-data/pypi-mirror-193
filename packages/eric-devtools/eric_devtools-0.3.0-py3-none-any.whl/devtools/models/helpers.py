import typing

import pydantic

from devtools.models import base

ModelT = typing.TypeVar('ModelT', bound=base.Model)

_model_cache: dict[
    tuple[type[base.Model], tuple[str, ...]], type[base.Model],
] = {}


def optional_model(
    model: type[ModelT], exclude: tuple[str, ...] = ()
) -> type[ModelT]:
    """optional_model converte o :param:`model`
    em um model com todos os campos opcionais
    e remove os campos passados em exclude, se passados.
    O model resultante também herda de NotEmptyModel.
    """
    if (new_t := _model_cache.get((model, exclude))) is not None:
        return new_t  # type:ignore
    new_t = pydantic.create_model(
        f'Optional{model.__name__}',
        __base__=type(f'Optional{model.__name__}', (model, base.NotEmptyModel), dict(model.__dict__)),  # type: ignore
        __module__=model.__module__,
    )
    new_t.__fields__.pop('external_id', None)
    for item in exclude:
        new_t.__fields__.pop(item, None)
    for field in new_t.__fields__.values():
        field.required = False
        field.allow_none = True
        field.default = None
    _model_cache[(model, exclude)] = new_t
    return new_t  # type: ignore


def clone(model: ModelT, **fields) -> ModelT:
    return model.parse_obj(dict(model) | fields)


def model_if_valid(
    model_type: type[ModelT], mapping: typing.Mapping[str, typing.Any],
) -> ModelT | None:
    try:
        return model_type.parse_obj(mapping)
    except pydantic.ValidationError:
        return None
