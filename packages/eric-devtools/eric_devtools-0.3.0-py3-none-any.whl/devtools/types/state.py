from typing import Any, MutableMapping


class State:
    _mapping: MutableMapping[str, Any]

    def __init__(self, mapping: MutableMapping[str, Any] | None = None) -> None:
        if not mapping:
            mapping = {}
        super().__setattr__("_mapping", mapping)

    def __setattr__(self, key: str, value: Any) -> None:
        self._mapping[key] = value

    def __getattr__(self, key: str) -> Any:
        try:
            return self._mapping[key]
        except KeyError as err:
            message = "'{}' object has no attribute '{}'"
            raise AttributeError(message.format(self.__class__.__name__, key)) from err

    def __delattr__(self, key: str) -> None:
        del self._mapping[key]

    def __str__(self) -> str:
        return f"State({str(self._mapping)})"

    def get(self, key: str) -> Any | None:
        return self._mapping.get(key, None)
