from typing import Any, Protocol


class EventProtocol(Protocol):
    @property
    def type(self) -> str:
        ...

    @property
    def update(self) -> Any:
        ...
