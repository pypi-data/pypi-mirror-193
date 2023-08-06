import abc
from datetime import date
from decimal import Decimal
from typing import Any, Callable, NoReturn, final
from uuid import UUID

ConverterTypeDef = Callable[[Any], Any]


def decimal_serializer(obj: Decimal):
    return float(obj)


def uuid_serializer(uuid: UUID):
    return str(uuid)


def date_serializer(dt: date):
    return dt.isoformat()


class Serializable(abc.ABC):
    @abc.abstractmethod
    def serialize(self) -> Any:
        ...  # pragma: no cover

    @final
    @staticmethod
    def parse(val: 'Serializable'):
        return val.serialize()


_SERIALIZER_MAPPING: dict[type, ConverterTypeDef] = {
    Decimal: decimal_serializer,
    UUID: uuid_serializer,
    date: date_serializer,
    Serializable: Serializable.parse,
}


class NotSerializable(Exception):
    def __init__(self, type_: type, val: Any) -> None:
        super().__init__(type_, val)
        self._type = type_
        self._val = val

    def __str__(self) -> str:
        return f'Object {self._val} of type {self._type} is not serializable'


def _default_serializer(obj) -> NoReturn:
    raise NotSerializable(type(obj), obj)


def _get_serializer(typ: type) -> ConverterTypeDef:
    serializer = _SERIALIZER_MAPPING.get(typ) or _find_by_intersection(typ)
    return serializer or _default_serializer


def _find_by_intersection(typ: type) -> ConverterTypeDef | None:
    keys_set = set(_SERIALIZER_MAPPING)
    bases_set = set(typ.__bases__)
    intersection = keys_set.intersection(bases_set)
    if not intersection:
        intersection = {val for val in keys_set if issubclass(typ, val)}
    return _get_serializer(intersection.pop()) if intersection else None


def serializer(obj: Any) -> Any:
    _serializer = _get_serializer(type(obj))
    return _serializer(obj)
