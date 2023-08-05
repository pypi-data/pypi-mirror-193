from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict, Iterable, List, Optional, Sequence

from .middleware import BaseMiddleware, wrap_middlewares
from .routing import Route, Router
from .types import Decorated, EventProtocol, Filter


class _CallExecutor:
    def __init__(
        self,
        router: Router,
        wrapped: Optional[Callable[[EventProtocol, Any], Awaitable[Any]]] = None,
    ) -> None:
        self.router = router
        self.wrapped = wrapped

    async def __call__(self, update: Any, **kwargs: Any) -> None:
        async def wrapped_default(event: EventProtocol, **data: Any) -> None:
            return await self.router(method=event.type, event=event.update, **data)

        wrapped = wrap_middlewares(
            self.router.outer_middlewares,
            wrapped_default if self.wrapped is None else self.wrapped,
        )
        await wrapped(update, kwargs)


class LikeApp:
    def __init__(
        self,
        executor: Optional[Callable[..., Awaitable[Any]]] = None,
        *,
        on_startup: Optional[Sequence[Callable[..., Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[..., Any]]] = None,
        user_events: Optional[Dict[str, List[Route]]] = None,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
        outer_middlewares: Optional[Sequence[BaseMiddleware]] = None,
    ) -> None:
        self.router: Router = Router(
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            user_events=user_events,
            middlewares=middlewares,
            outer_middlewares=outer_middlewares,
        )
        self.executor = _CallExecutor(router=self.router, wrapped=executor)

    async def __call__(self, update: EventProtocol, **kwargs: Any) -> None:
        await self.executor(update, **kwargs)

    def include_router(self, router: Router) -> None:
        self.router.include_router(router=router)

    def add_lifespan(
        self,
        event: str,
        endpoint: Callable[..., Any],
    ) -> None:
        self.router.add_lifespan(event=event, endpoint=endpoint)

    def on_lifespan(self, event: str) -> Callable[[Decorated], Decorated]:
        return self.router.on_lifespan(event=event)

    def add_route(
        self,
        method: str,
        endpoint: Callable[..., Any],
        filters: Iterable[Filter],
        flags: Optional[Dict[str, Any]] = None,
    ) -> None:
        return self.router.add_route(
            method=method, endpoint=endpoint, filters=filters, flags=flags
        )

    def route(
        self,
        *filters: Filter,
        method: str,
        flags: Optional[Dict[str, Any]] = None,
    ) -> Callable[[Decorated], Decorated]:
        return self.router.route(*filters, method=method, flags=flags)
