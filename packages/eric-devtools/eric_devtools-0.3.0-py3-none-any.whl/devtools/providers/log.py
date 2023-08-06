import logging

from devtools.config import Config
from devtools.utils.helpers import lazy_field, update_field


class LoggerHandler:
    def __init__(self, default: str = "gunicorn.error") -> None:
        self._default = default

    def _get_logger(self):
        logger_name = Config()("DEFAULT_LOGGER", str, self._default)
        return logging.getLogger(logger_name)

    @lazy_field
    def _logger(self):
        return self._get_logger()

    @property
    def logger(self):
        return self._logger()

    def __get__(self, instance, owner=None):
        return self.logger

    def __set__(self, _instance, value: logging.Logger):
        update_field(self, self._logger, value)

    def info(self, msg: object, *args, **kwargs):
        return self.__get__(self).info(msg, *args, **kwargs)

    def warning(self, msg: object, *args, **kwargs):
        return self.__get__(self).warning(msg, *args, **kwargs)

    def debug(self, msg: object, *args, **kwargs):
        return self.__get__(self).debug(msg, *args, **kwargs)

    def error(self, msg: object, *args, **kwargs):
        return self.__get__(self).error(msg, *args, **kwargs)

    def exception(self, msg: object, *args, **kwargs):
        return self.__get__(self).exception(msg, *args, **kwargs)
