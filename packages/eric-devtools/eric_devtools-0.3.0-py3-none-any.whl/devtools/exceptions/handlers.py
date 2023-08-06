import http
from typing import Union

from devtools import models
from devtools.exceptions import _api, exceptions
from devtools.models.models import FieldError
from devtools.utils.string import to_spaced

_Exception = Union[
    exceptions.Error, exceptions.ValidationError, exceptions.DirectError
]


def _error_handler(request: _api.Request, exc: exceptions.Error):
    exc_response = exc.response()
    return _api.ResponseClass(
        models.BaseResponseError(
            title=to_spaced(type(exc).__name__),
            path=request.url.path,
            status=exc_response.status_code,
            detail=exc_response.message,
        ).dict(by_alias=True),
        status_code=exc_response.status_code,
    )


def _validation_error_handler(
    request: _api.Request, exc: exceptions.ValidationError
):
    exc_response = exc.response()
    return _api.ResponseClass(
        models.BaseResponseError(
            title=to_spaced(type(exc).__name__),
            path=request.url.path,
            error_key='error.validation',
            status=exc_response['status'],
            detail=exc_response['message'],
            field_errors=[FieldError.parse_obj(exc_response)],
        ).dict(by_alias=True),
        status_code=exc_response['status'],
    )


def _direct_error_handler(request: _api.Request, exc: exceptions.DirectError):
    exc_response = exc.payload.dict(exclude_none=True, exclude_unset=True)
    exc_response.setdefault('title', to_spaced(type(exc).__name__))
    return _api.ResponseClass(
        models.BaseResponseError(
            path=request.url.path, **exc_response, status=exc.status
        ).dict(by_alias=True),
        status_code=exc.status,
    )


def _base_exception_handler(request: _api.Request, exc: Exception):
    status = http.HTTPStatus.INTERNAL_SERVER_ERROR
    return _api.ResponseClass(
        models.BaseResponseError(
            title='exception',
            path=request.url.path,
            status=status,
            detail='Internal Server Error',
        ).dict(by_alias=True),
        status_code=status,
    )


def add_exception_handlers(
    app: _api.FastAPI,
    *exclude: type[_Exception],
    exclude_base_exception_handler: bool = False
):
    for exception, handler in (
        (exceptions.Error, _error_handler),
        (exceptions.ValidationError, _validation_error_handler),
        (exceptions.DirectError, _direct_error_handler),
    ):
        if exception in exclude:
            continue
        app.add_exception_handler(exception, handler)
    if not exclude_base_exception_handler:
        app.add_exception_handler(Exception, _base_exception_handler)
