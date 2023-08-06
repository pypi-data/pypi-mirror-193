from typing import Any, Protocol

from devtools.models._serializers import serializer


class Json(Protocol):
    def loads(self, obj) -> Any:
        ...

    def dumps(self, v, *, default: Any = None) -> str:
        ...

    @property
    def DecodeError(self) -> type[Exception]:
        ...

    @property
    def EncodeError(self) -> type[Exception]:
        ...


class Orjson:
    def __init__(self) -> None:
        try:
            import orjson
        except ImportError as exc:
            raise ImportError(
                'Unable to import orjson,'
                'try installing "eric-devtools[orjson]"'
            ) from exc
        else:
            self._orjson = orjson

    def loads(self, obj):
        return self._orjson.loads(obj)

    def dumps(self, v, *, default=None):
        return self._orjson.dumps(v, default=serializer or default).decode()

    @property
    def DecodeError(self):
        return self._orjson.JSONDecodeError

    @property
    def EncodeError(self):
        return self._orjson.JSONEncodeError


json: Json = Orjson()
