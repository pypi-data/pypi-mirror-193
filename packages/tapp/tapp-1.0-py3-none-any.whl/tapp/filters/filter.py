from __future__ import annotations

import abc
import typing


class Filter(abc.ABC):
    @abc.abstractmethod
    async def __call__(
        self, *args: typing.Any, **kwargs: typing.Any
    ) -> typing.Union[bool, typing.Dict[str, typing.Any]]:
        ...

    def __await__(
        self,
    ) -> typing.Callable[
        ..., typing.Awaitable[typing.Union[bool, typing.Dict[str, typing.Any]]]
    ]:  # pragma: no cover
        return self.__call__
