import os
import pathlib
import typing

StrOrPath = str | pathlib.Path


class EnvironError(Exception):
    pass


MISSING = object()
T = typing.TypeVar("T")
CastType = typing.Callable[[typing.Any], typing.Any]


class MissingKeyError(KeyError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Config '{name}' is missing, and has no default.")


class MissingKeysError(KeyError):
    def __init__(self, names: list[str]) -> None:
        super().__init__(
            f"Config keys {', '.join(names)!r} are missing, and has no default."
        )


class Environ(typing.MutableMapping):
    def __init__(self, environ: typing.MutableMapping[str, str] = os.environ):
        self._environ = environ
        self._has_been_read: set[typing.Any] = set()

    def __getitem__(self, key: typing.Any) -> typing.Any:
        self._has_been_read.add(key)
        return self._environ.__getitem__(key)

    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        if key in self._has_been_read:
            raise EnvironError(
                f"Attempting to set environ['{key}'], but the value has already been "
                "read."
            )
        self._environ.__setitem__(key, value)

    def __delitem__(self, key: typing.Any) -> None:
        if key in self._has_been_read:
            raise EnvironError(
                f"Attempting to delete environ['{key}'], but the value has already "
                "been read."
            )
        self._environ.__delitem__(key)

    def __iter__(self) -> typing.Iterator:
        return iter(self._environ)

    def __len__(self) -> int:
        return len(self._environ)


environ = Environ()


class Config:
    """Config busca variáveis de ambiente com default e cast
    para reduzir dependencias com starlette"""

    def __init__(
        self,
        env_file: StrOrPath | None = None,
        environ: typing.Mapping[str, str] = environ,
    ) -> None:
        self._environ = environ
        self._file_vals: dict[str, str] = {}
        if env_file is not None and os.path.isfile(env_file):
            self._file_vals = self._read_file(env_file)

    def _read_file(self, env_file: StrOrPath) -> dict[str, str]:
        output = {}
        with open(env_file) as stream:
            for line in stream:
                if line.startswith("#") or "=" not in line:
                    continue
                name, value = line.split("=", 1)
                output[name.strip()] = value.strip()
        return output

    def _get_value(self, name: str, default: typing.Any) -> str:
        value = self._environ.get(name, self._file_vals.get(name, default))
        if value is MISSING:
            raise MissingKeyError(name)
        return value

    def _cast(self, key: str, value: typing.Any, cast: type | CastType) -> typing.Any:
        try:
            return cast(value)
        except (TypeError, ValueError) as e:
            raise ValueError(
                f"Config '{key}' has value '{value}'. Not a valid {cast.__name__}."
            ) from e

    def get(
        self,
        key: str,
        cast: CastType | None = None,
        default: typing.Any = MISSING,
    ) -> typing.Any:
        value = self._get_value(key, default)
        if cast is None:
            return value
        if cast is bool:
            cast = boolean
        return self._cast(key, value, cast)

    @typing.overload
    def __call__(
        self,
        key: str,
        cast: typing.Callable[[str], T],
        default: typing.Any = MISSING,
    ) -> T:
        ...

    @typing.overload
    def __call__(
        self,
        key: str,
        cast: None = None,
        default: typing.Any = MISSING,
    ) -> str:
        ...

    def __call__(
        self,
        key: str,
        cast: CastType | None = None,
        default: typing.Any = MISSING,
    ) -> typing.Any:
        return self.get(key, cast, default)


ConfigLike = typing.Callable[[str, typing.Callable, typing.Any], typing.Any]

_boolean_vals = {
    "true": True,
    "false": False,
    "0": False,
    "1": True,
}


def boolean(val: str | None | bool) -> bool:
    if not val:
        return False
    if isinstance(val, bool):
        return val
    try:
        return _boolean_vals[val.lower()]
    except KeyError as err:
        raise ValueError(
            f'Received invalid bool: {val}, try: {",".join(_boolean_vals)}'
        ) from err
