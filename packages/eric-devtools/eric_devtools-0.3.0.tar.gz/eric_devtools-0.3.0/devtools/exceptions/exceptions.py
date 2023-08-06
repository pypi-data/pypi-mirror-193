import http
from typing import NamedTuple, TypedDict, final

from devtools.models.models import DirectResponseError

OptionalStatus = http.HTTPStatus | None


class _Response(NamedTuple):
    message: str
    status_code: int


def _append_exclamation_mark(message: str):
    return message if message.endswith('!') else f'{message}!'


class Error(Exception):
    _default_status = http.HTTPStatus.BAD_REQUEST

    def __init__(self, message: str, status: OptionalStatus = None) -> None:
        self._message = message
        self._status = status or self._default_status

    def __str__(self) -> str:
        return self._get_message()

    def get_message(self):
        return self._message

    @final
    def _get_message(self):
        return _append_exclamation_mark(self.get_message())

    @final
    def response(self) -> _Response:
        return _Response(self._get_message(), self._status)


class APIError(Error):
    ...


class DatabaseError(Error):
    _default_status = http.HTTPStatus.BAD_REQUEST

    def __init__(self, target: str, status: OptionalStatus = None) -> None:
        self._target = target
        self._status = status or self._default_status

    def get_message(self):
        return f'An error occured with {self._target}'

    def __str__(self) -> str:
        return self._get_message()


class ValidationResponse(TypedDict):
    type_: str
    field: str
    message: str
    status: int


class ValidationError(Exception):
    _default_status = http.HTTPStatus.UNPROCESSABLE_ENTITY

    def __init__(
        self,
        type_: str,
        field: str,
        message: str,
        status: OptionalStatus = None,
    ) -> None:
        self._error = Error(message, status or self._default_status)
        self._type = type_
        self._field = field

    def response(self) -> ValidationResponse:
        error_response = self._error.response()
        return {
            'type_': self._type,
            'field': self._field,
            'message': error_response.message,
            'status': error_response.status_code,
        }

    def __str__(self) -> str:
        return self._error.__str__()


class DirectError(Exception):
    _default_status = http.HTTPStatus.BAD_REQUEST

    def __init__(
        self, payload: DirectResponseError, status: OptionalStatus = None,
    ) -> None:
        self._payload = payload
        self._status = status

    @property
    def status(self):
        return (
            self._status if self._status is not None else self._default_status
        )

    @property
    def payload(self):
        return self._payload


class NotFoundError(DatabaseError):
    _default_status = http.HTTPStatus.NOT_FOUND

    def get_message(self):
        return f'{self._target} not found'


class ConflictError(DatabaseError):
    _default_status = http.HTTPStatus.CONFLICT

    def get_message(self):
        return f'{self._target} already exists'


class ForbiddenError(APIError):
    _default_status = http.HTTPStatus.FORBIDDEN

    def __init__(self) -> None:
        super().__init__('You do not have permission to use this route')


class UnexpectedDatabaseError(DatabaseError):
    _default_status = http.HTTPStatus.INTERNAL_SERVER_ERROR

    def get_message(self):
        return f'An unhandled error happened while using {self._target}'


class UnexpectedError(APIError):
    _default_status = http.HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, target: str) -> None:
        super().__init__(f'An unhandled error happened while using {target}')
