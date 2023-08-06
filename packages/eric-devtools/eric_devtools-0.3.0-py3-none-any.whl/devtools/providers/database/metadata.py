from pathlib import Path

from devtools.providers.database.types.entity import Entity
from devtools.utils.autodiscovery import ClassFinder


def get_metadata(path: Path):
    ClassFinder(Entity, path=path).find()
    return Entity.metadata
