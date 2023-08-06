from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Optional

from ..anyio import as_async

if TYPE_CHECKING:
    from ..routing import Router


class ExceptionMiddleware(abc.ABC):
    def __init__(self, router: Router) -> None:
        self.router = router

    def _lookup_exception_handler(self, exception: Exception) -> Optional[Callable[..., Any]]:
        for cls in type(exception).__mro__:
            if cls in self.router.exception_handlers:
                return self.router.exception_handlers[cls]
        return None

    async def __call__(
        self,
        route: Callable[[Any, Dict[str, Any]], Awaitable[None]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        try:
            return await route(event, data)
        except Exception as e:
            handler = self._lookup_exception_handler(e)
            if handler is None:
                raise e

            await as_async(handler, event, e, **data)
