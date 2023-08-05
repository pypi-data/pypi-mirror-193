from __future__ import annotations

from typing import Any, Protocol


class EventProtocol(Protocol):
    @property
    def type(self) -> str:
        ...

    @property
    def update(self) -> Any:
        ...
