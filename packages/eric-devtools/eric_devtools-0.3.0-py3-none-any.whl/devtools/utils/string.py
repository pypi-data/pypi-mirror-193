import re
import sys

from devtools.utils._helpers import deprecated

IS_PY_38 = sys.version_info < (3, 9)

_to_snake_pattern = re.compile(r"(?!^)([A-Z]+)")
_snake_case_regexp = re.compile("_([a-z])")


def to_snake(camel_string: str):
    return re.sub(_to_snake_pattern, r"_\1", camel_string).lower()


def to_spaced(camel_string: str):
    """to_spaced receives a 'CamelString' and returns 'camel string'"""
    return to_snake(camel_string).replace("_", " ")


def to_camel(string: str):
    string = "_".join(string.split())
    return re.sub(
        _snake_case_regexp,
        lambda match: match[1].upper(),
        string.removesuffix("_"),
    )


@deprecated
def removesuffix(string: str, suffix: str):
    if not string.endswith(suffix):
        return string
    return string[: -len(suffix)] if IS_PY_38 else string.removesuffix(suffix)
