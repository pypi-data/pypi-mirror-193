from typing import TypeVar, Generic

from pydantic.generics import GenericModel

from devtools.models.base import Model

DataT = TypeVar('DataT')
ModelT = TypeVar('ModelT')


class BaseResponse(GenericModel, Generic[DataT]):
    data: DataT


class Page(Model):
    offset: int | None
    total: int


class PagedResponse(BaseResponse, Generic[DataT]):
    page: Page


class BaseListResponse(GenericModel, Generic[DataT]):
    data: list[DataT]


class FieldError(Model):
    type_: str | None
    object_name: str | None = None
    field: str
    message: str


class Cause(Model):
    status: int
    message: str


class BaseResponseError(Model):
    path: str
    status: int
    title: str
    detail: str
    error_key: str | None = None
    field_errors: list[FieldError] | None = None


class DirectResponseError(Model):
    title: str | None = None
    detail: str
    error_key: str | None = None
    field_errors: list[FieldError] | None = None
