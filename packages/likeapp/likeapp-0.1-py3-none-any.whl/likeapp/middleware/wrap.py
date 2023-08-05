from functools import partial, wraps
from typing import Any, Callable, Dict, Sequence

from .base import BaseMiddleware


def wrap_middlewares(
    middlewares: Sequence[BaseMiddleware], route: Callable[..., Any]
) -> Callable[..., Any]:
    @wraps(route)
    def wrapped(event: Any, kwargs: Dict[str, Any]) -> Any:
        return route(event, **kwargs)

    app = wrapped
    for middleware in reversed(middlewares):
        app = partial(middleware, app)
    return app
