from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, Type

from magic_filter import MagicFilter

from .anyio import as_async
from .middleware import BaseMiddleware, wrap_middlewares
from .types import Decorated, Filter


def transform_filter(_filter: Filter) -> Filter:
    if not isinstance(_filter, MagicFilter):
        return _filter
    return _filter.resolve


class Route:
    def __init__(
        self,
        endpoint: Callable[..., Any],
        filters: Iterable[Filter],
        *,
        flags: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.endpoint = endpoint
        self.filters = map(transform_filter, filters)
        self.flags = {} if flags is None else flags

    async def matches(self, *args: Any, **kwargs: Any) -> Tuple[bool, Dict[str, Any]]:
        if not self.filters:
            return True, kwargs
        for _filter in self.filters:
            call = await as_async(_filter, *args, **kwargs)
            if not call:
                return False, kwargs
            if isinstance(call, dict):
                kwargs.update(call)
        return True, kwargs

    async def call(self, *args: Any, **kwargs: Any) -> None:
        await as_async(self.endpoint, *args, **kwargs)


class Router:
    def __init__(
        self,
        *,
        on_startup: Optional[Sequence[Callable[..., Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[..., Any]]] = None,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
        outer_middlewares: Optional[Sequence[BaseMiddleware]] = None,
        user_events: Optional[Dict[str, List[Route]]] = None,
        route_class: Type[Route] = Route,
    ) -> None:
        self.on_startup_event = [] if on_startup is None else list(on_startup)
        self.on_shutdown_event = [] if on_shutdown is None else list(on_shutdown)
        self.middlewares = [] if middlewares is None else list(middlewares)
        self.outer_middlewares = [] if outer_middlewares is None else list(outer_middlewares)
        self.route_class = route_class

        self.lifespan_events: Dict[str, List[Callable[..., Any]]] = {
            "startup": self.on_startup_event,
            "shutdown": self.on_shutdown_event,
        }
        self.user_events: Dict[str, List[Route]] = {} if user_events is None else user_events

    async def lifespan(self, method: str, **kwargs: Any) -> None:
        for route in self.lifespan_events[method]:
            await as_async(route, **kwargs)

    async def events(
        self,
        method: str,
        event: Any,
        **kwargs: Any,
    ) -> Any:
        for route in self.user_events[method]:
            matches, data = await route.matches(event, **kwargs)
            if matches:
                kwargs.update(data, route=route)
                wrapped = wrap_middlewares(
                    self.middlewares,
                    route.call,
                )
                return await wrapped(event, kwargs)

    async def __call__(
        self,
        method: str,
        event: Any = None,
        **kwargs: Any,
    ) -> Any:
        if method in self.lifespan_events:
            return await self.lifespan(method=method, **kwargs)

        return await self.events(method=method, event=event, **kwargs)

    def include_router(self, router: Router) -> None:
        for middleware in router.middlewares:
            self.middlewares.append(middleware)
        for outer_middleware in router.outer_middlewares:
            self.outer_middlewares.append(outer_middleware)
        for lifespan_event, endpoints in router.lifespan_events.items():
            self.lifespan_events[lifespan_event].extend(endpoints)
        for telegram_event, routes in router.user_events.items():
            for route in routes:
                self.add_route(
                    method=telegram_event,
                    endpoint=route.endpoint,
                    filters=route.filters,
                    flags=route.flags,
                )

    def add_lifespan(
        self,
        event: str,
        endpoint: Callable[..., Any],
    ) -> None:
        self.lifespan_events[event].append(endpoint)

    def on_lifespan(self, event: str) -> Callable[[Decorated], Decorated]:
        def decorator(endpoint: Decorated) -> Decorated:
            self.add_lifespan(event=event, endpoint=endpoint)
            return endpoint

        return decorator

    def add_route(
        self,
        method: str,
        endpoint: Callable[..., Any],
        filters: Iterable[Filter],
        flags: Optional[Dict[str, Any]] = None,
    ) -> None:
        route = self.route_class(endpoint=endpoint, filters=filters, flags=flags)
        self.user_events[method].append(route)

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
