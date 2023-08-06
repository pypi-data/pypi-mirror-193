from __future__ import annotations

import functools
from typing import Any, Callable, Dict, List, Optional, Sequence

from .base import BaseMiddleware


class MiddlewareManager:
    def __init__(
        self,
        middlewares: Optional[Sequence[BaseMiddleware]] = None,
    ) -> None:
        self.middlewares = [] if middlewares is None else list(middlewares)

    def add_middleware(self, middleware: BaseMiddleware) -> None:
        self.middlewares.append(middleware)

    def copy(self) -> List[BaseMiddleware]:
        return self.middlewares.copy()

    def wrap(self, route: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(route)
        def wrapped(event: Any, kwargs: Dict[str, Any]) -> Any:
            return route(event, **kwargs)

        app = wrapped
        for middleware in reversed(self.middlewares):
            app = functools.partial(middleware, app)
        return app
