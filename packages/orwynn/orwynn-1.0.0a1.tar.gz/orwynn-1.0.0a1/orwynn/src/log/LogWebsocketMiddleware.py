from orwynn.src.log.WebsocketLogger import WebsocketLogger
from orwynn.src.middleware.WebsocketMiddleware import WebsocketMiddleware
from orwynn.src.middleware.WebsocketNextCall import WebsocketNextCall
from orwynn.src.web.context.WebsocketRequestContextId import (
    WebsocketRequestContextId,
)
from orwynn.src.web.websocket.Websocket import Websocket


class LogWebsocketMiddleware(WebsocketMiddleware):
    """Logs information about a websocket request.

    It's recommended to be outermost (at custom level) middleware.
    """
    def __init__(self, covered_routes: list[str]) -> None:
        super().__init__(covered_routes)

        self.__logger: WebsocketLogger = WebsocketLogger()

    async def process(
        self, request: Websocket, call_next: WebsocketNextCall
    ) -> None:
        request_id: str = WebsocketRequestContextId().get()
        await self.__logger.log_request(
            request,
            request_id
        )

        await call_next(request)

        # TODO: Maybe somehow listen for websocket messages sent over the
        #   channel?
