from typing import Any, Callable, Dict, Iterable, Optional, Tuple

from magic_filter import MagicFilter

from .anyio import as_async
from .types import Filter


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
