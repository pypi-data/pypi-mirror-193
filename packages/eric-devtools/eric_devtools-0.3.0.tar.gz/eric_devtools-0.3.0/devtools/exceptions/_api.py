try:
    from fastapi.responses import ORJSONResponse

    ResponseClass = ORJSONResponse
except ImportError:
    from fastapi.responses import UJSONResponse

    ResponseClass = UJSONResponse


from fastapi import FastAPI as FastAPI  # noqa
from fastapi import Request as Request  # noqa

ResponseClass: type['ORJSONResponse'] | type['UJSONResponse']
