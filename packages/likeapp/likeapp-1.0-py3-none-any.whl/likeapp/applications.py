from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence

from .filters import Filter
from .middleware import BaseMiddleware
from .route import Route
from .router import Router
from .types import Decorated, EventProtocol


class LikeApp:
    def __init__(
        self,
        *,
        on_startup: Optional[Sequence[Callable[..., Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[..., Any]]] = None,
        methods: Optional[Dict[str, List[Route]]] = None,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
        outer_middlewares: Optional[Sequence[BaseMiddleware]] = None,
    ) -> None:
        self.router: Router = Router(
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            methods=methods,
            middlewares=middlewares,
            outer_middlewares=outer_middlewares,
        )

    async def __call__(self, update: EventProtocol, **kwargs: Any) -> None:
        async def _wrapped(event: EventProtocol, **data: Any) -> None:
            await self.router(method=event.type, event=event.update, **data)

        wrapped = self.router.outer_middleware.wrap(_wrapped)
        await wrapped(update, kwargs)

    def add_middleware(self, middleware: BaseMiddleware) -> None:
        self.router.add_middleware(middleware=middleware)

    def add_outer_middleware(self, outer_middleware: BaseMiddleware) -> None:
        self.router.add_outer_middleware(outer_middleware=outer_middleware)

    def add_lifespan(
        self,
        method: str,
        endpoint: Callable[..., Any],
    ) -> None:
        self.router.add_lifespan(method=method, endpoint=endpoint)

    def add_route(
        self,
        method: str,
        endpoint: Callable[..., Any],
        filters: Iterable[Filter],
        flags: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.router.add_route(method=method, endpoint=endpoint, filters=filters, flags=flags)

    def on_lifespan(self, method: str) -> Callable[[Decorated], Decorated]:
        return self.router.on_lifespan(method=method)

    def route(
        self,
        *filters: Iterable[Filter],
        method: str,
        flags: Optional[Dict[str, Any]] = None,
    ) -> Callable[[Decorated], Decorated]:
        return self.router.route(method=method, filters=filters, flags=flags)

    def include_router(self, router: Router) -> None:
        self.router.include_router(router)
