try:
    from starlette.applications import Starlette
    from starlette.datastructures import State
except ImportError as err:
    raise ImportError(
        "Devtools module 'devtools.utils.api' requires starlette>=0.17.1 to work"
    ) from err
import asyncio
import enum
import typing


class EventTypes(str, enum.Enum):
    STARTUP = 'startup'
    SHUTDOWN = 'shutdown'


STARTUP = EventTypes.STARTUP
SHUTDOWN = EventTypes.SHUTDOWN


def on_event(
    app: Starlette,
    event_type: EventTypes,
    *handlers: typing.Callable[[State], typing.Awaitable[typing.Any]]
):
    async def inner():
        await asyncio.gather(*(handler(app.state) for handler in handlers))

    app.add_event_handler(event_type.value, inner)
