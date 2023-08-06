from __future__ import annotations

import abc
from typing import Any, Awaitable, Callable, Dict


class BaseMiddleware(abc.ABC):
    @abc.abstractmethod
    async def __call__(
        self,
        route: Callable[[Any, Dict[str, Any]], Awaitable[None]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        ...
