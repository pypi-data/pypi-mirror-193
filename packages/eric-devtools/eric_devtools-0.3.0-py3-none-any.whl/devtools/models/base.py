import pydantic
import pydantic.utils

from devtools.models._json import json
from devtools.models._serializers import Serializable
from devtools.utils.string import to_camel
from devtools.utils._helpers import LazyFieldDescriptor


class Model(pydantic.BaseModel, Serializable):
    """Model base usado com conversão json(ujson, orjson), frozen, orm_mode e snake to camel"""

    def serialize(self):
        return self.dict(by_alias=True)

    def raw_dict(self, by_alias: bool = True, exclude: set[str] | None = None):
        return json.loads(
            self.json(by_alias=by_alias, exclude=exclude or set())
        )

    class Config:
        json_loads = json.loads
        json_dumps = json.dumps
        frozen = True
        allow_population_by_field_name = True
        orm_mode = True
        keep_untouched = (LazyFieldDescriptor,)

        @classmethod
        def alias_generator(cls, field: str) -> str:
            return to_camel(field)


class NotEmptyModel(Model):
    """NotEmptyModel garante que pelo menos um
    campo precisa ser diferente de None para ser válido"""

    @pydantic.root_validator
    def model_should_not_be_empty(cls, values: pydantic.utils.GetterDict):
        if all(value is None for value in values.values()):
            raise ValueError(
                f'at least one field must be sent on {cls.__name__}'  # type: ignore
            )
        return values


class UnsafeModel(Model):
    """UnsafeModel remove a imutabilidade default do Model"""

    class Config(Model.Config):
        frozen = False
