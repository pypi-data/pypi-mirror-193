

from orwynn.src.app.App import App
from orwynn.src.boot.api_version.ApiVersion import ApiVersion
from orwynn.src.controller.Controller import Controller
from orwynn.src.controller.ControllerRegister import ControllerRegister
from orwynn.src.error.ExceptionHandler import ExceptionHandler
from orwynn.src.middleware.Middleware import Middleware
from orwynn.src.middleware.MiddlewareRegister import MiddlewareRegister
from orwynn.src.module.Module import Module
from orwynn.src.router.WebsocketStack import WebsocketStack
from orwynn.src.web.http.Cors import Cors
from orwynn.src.worker.Worker import Worker


class Router(Worker):
    """
    Manages how the requests and responses flow through the app.
    """
    def __init__(
        self,
        app: App,
        *,
        modules: list[Module],
        controllers: list[Controller],
        middleware_arr: list[Middleware],
        exception_handlers: list[ExceptionHandler],
        cors: Cors | None,
        global_http_route: str,
        global_websocket_route: str,
        api_version: ApiVersion
    ) -> None:
        super().__init__()
        self.__app: App = app

        self.__modules: list[Module] = modules
        self.__controllers: list[Controller] = controllers
        self.__middleware_arr: list[Middleware] = middleware_arr
        self.__exception_handlers: list[ExceptionHandler] = exception_handlers

        self.__cors: Cors | None = cors

        self.__websocket_stack: WebsocketStack = WebsocketStack(
            self.__app.websocket_handler
        )

        self.__middleware_register: MiddlewareRegister = MiddlewareRegister(
            app=self.__app,
            middleware_arr=self.__middleware_arr,
            exception_handlers=self.__exception_handlers,
            cors=self.__cors,
            websocket_stack=self.__websocket_stack
        )
        self.__controller_register: ControllerRegister = ControllerRegister(
            app=self.__app,
            modules=self.__modules,
            controllers=self.__controllers,
            websocket_stack=self.__websocket_stack,
            global_http_route=global_http_route,
            global_websocket_route=global_websocket_route,
            api_version=api_version
        )

        self.__start_registering()

    def __start_registering(self) -> None:
        # Register middleware, it should be done before the controller's
        # adding due to the special websocket middleware registering
        self.__middleware_register.register_all()

        # And finally controllers
        self.__controller_register.register_all()

        # After all actions the websocket stack needs to call register action.
        # It is populated during middleware and controller registering.
        self.__websocket_stack.register_all()
