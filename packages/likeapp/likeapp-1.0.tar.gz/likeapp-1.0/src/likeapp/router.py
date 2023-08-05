from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Type

from .anyio import as_async
from .middleware import BaseMiddleware, MiddlewareManager
from .route import Route
from .types import Decorated, Filter


class _Middlewares:
    def __init__(
        self,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
        outer_middlewares: Optional[Sequence[BaseMiddleware]] = None,
    ) -> None:
        self.middleware = MiddlewareManager(middlewares)
        self.outer_middleware = MiddlewareManager(outer_middlewares)

    def include_middlewares(self, another: _Middlewares) -> None:
        self.middleware.add_middlewares(*another.middleware.copy())
        self.outer_middleware.add_middleware(*another.outer_middleware.copy())


class _Events(_Middlewares):
    def __init__(
        self,
        on_startup: Optional[Sequence[Callable[..., Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[..., Any]]] = None,
        methods: Optional[Dict[str, List[Route]]] = None,
        route_class: Type[Route] = Route,
        *,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
        outer_middlewares: Optional[Sequence[BaseMiddleware]] = None,
    ) -> None:
        super(_Events, self).__init__(middlewares=middlewares, outer_middlewares=outer_middlewares)

        self.on_startup = [] if on_startup is None else list(on_startup)
        self.on_shutdown = [] if on_shutdown is None else list(on_shutdown)
        self.lifespan = {"startup": self.on_startup, "shutdown": self.on_shutdown}
        self.methods = {} if methods is None else methods

        self.route_class = route_class

    async def _lifespan(
        self,
        method: str,
        event: Any,
        **kwargs: Any,
    ) -> None:
        for endpoint in self.lifespan[method]:
            await as_async(endpoint, event, **kwargs)

    def add_middleware(self, middleware: BaseMiddleware) -> None:
        self.middleware.add_middleware(middleware=middleware)

    def add_outer_middleware(self, outer_middleware: BaseMiddleware) -> None:
        self.outer_middleware.add_middleware(outer_middleware)

    def add_lifespan(
        self,
        method: str,
        endpoint: Callable[..., Any],
    ) -> None:
        self.lifespan[method].append(endpoint)

    def add_route(
        self,
        method: str,
        endpoint: Callable[..., Any],
        filters: Iterable[Filter],
        flags: Optional[Dict[str, Any]] = None,
    ) -> None:
        route = self.route_class(endpoint=endpoint, filters=filters, flags=flags)
        self.methods[method] = route

    def include_events(self, another: _Events) -> None:
        for lifespan, endpoints in another.lifespan.items():
            for endpoint in endpoints:
                self.add_lifespan(method=lifespan, endpoint=endpoint)
        for method, routes in another.methods.items():
            for route in routes:
                self.add_route(
                    method=method,
                    endpoint=route.endpoint,
                    filters=route.filters,
                    flags=route.flags,
                )

    def include_router(self, router: Router) -> None:
        self.include_middlewares(router)
        self.include_events(router)


class Router(_Events):
    def __init__(
        self,
        *,
        on_startup: Optional[Sequence[Callable[..., Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[..., Any]]] = None,
        methods: Optional[Dict[str, List[Route]]] = None,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
        outer_middlewares: Optional[Sequence[BaseMiddleware]] = None,
        route_class: Type[Route] = Route,
    ) -> None:
        super(Router, self).__init__(
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            methods=methods,
            route_class=route_class,
            middlewares=middlewares,
            outer_middlewares=outer_middlewares,
        )

    async def __call__(
        self,
        method: str,
        event: Any,
        **kwargs: Any,
    ) -> None:
        if method in self.lifespan:
            await self._lifespan(method=method, event=event, **kwargs)
            return

        for route in self.methods[method]:
            matches, data = await route.matches(method)
            if matches:
                kwargs.update(data, route=route)
                wrapped = self.middleware.wrap(
                    route=route.call,
                )
                await wrapped(event, kwargs)
                return

    def on_lifespan(self, method: str) -> Callable[[Decorated], Decorated]:
        def decorator(endpoint: Decorated) -> Decorated:
            self.add_lifespan(method=method, endpoint=endpoint)
            return endpoint

        return decorator

    def route(
        self,
        method: str,
        filters: Iterable[Filter],
        flags: Optional[Dict[str, Any]] = None,
    ) -> Callable[[Decorated], Decorated]:
        def decorator(endpoint: Decorated) -> Decorated:
            self.add_route(method=method, endpoint=endpoint, filters=filters, flags=flags)
            return endpoint

        return decorator
