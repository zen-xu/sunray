from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeVar
from typing import overload

from ray import util as _ray_util

import sunray


if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import Any
    from typing import Callable


_ActorT = TypeVar("_ActorT", bound=sunray.Actor)
_V = TypeVar("_V")
_R = TypeVar("_R")


class ActorPool(Generic[_ActorT], _ray_util.ActorPool):  # pragma: no cover
    """Utility class to operate on a fixed pool of actors.

    Arguments:
        actors: List of Sunray actors to use in this pool.

    Examples:
        ```python
        import sunray
        from sunray.util import ActorPool


        class Actor(sunray.ActorMixin):
            @sunray.remote_method
            def double(self, v):
                return 2 * v


        a1, a2 = Actor.new_actor().remote(), Actor.new_actor().remote()
        pool = ActorPool([a1, a2])
        print(list(pool.map(lambda a, v: a.methods.double.remote(v), [1, 2, 3, 4])))

        [2, 4, 6, 8]
        ```
    """

    def __init__(self, actors: list[_ActorT]) -> None:
        super().__init__(actors)

    if TYPE_CHECKING:

        @overload  # type: ignore[override]
        def map(
            self,
            fn: Callable[[_ActorT, _V], sunray.ObjectRef[_R]],
            values: list[_V],
        ) -> Generator[_R, None, None]: ...

        @overload
        def map(
            self,
            fn: Callable[[_ActorT, _V], _R],
            values: list[_V],
        ) -> Generator[_R, None, None]: ...

        def map(
            self,
            fn: Callable[[_ActorT, _V], _R | sunray.ObjectRef[_R]],
            values: list[_V],
        ) -> Generator[_R, None, None]: ...

        @overload  # type: ignore[override]
        def map_unordered(
            self,
            fn: Callable[[_ActorT, _V], sunray.ObjectRef[_R]],
            values: list[_V],
        ) -> Generator[_R, None, None]: ...

        @overload
        def map_unordered(
            self,
            fn: Callable[[_ActorT, _V], _R],
            values: list[_V],
        ) -> Generator[_R, None, None]: ...

        def map_unordered(
            self,
            fn: Callable[[_ActorT, _V], _R | sunray.ObjectRef[_R]],
            values: list[_V],
        ) -> Generator[_R, None, None]: ...

        @overload
        def submit(
            self, fn: Callable[[_ActorT, _V], sunray.ObjectRef[_R]], value: _V
        ) -> None: ...

        @overload
        def submit(self, fn: Callable[[_ActorT, _V], _R], value: _V) -> None: ...

        def submit(self, fn: Callable[[_ActorT, _V], Any], value: _V) -> None: ...

        def has_next(self) -> bool: ...

        def pop_idle(self) -> _ActorT | None: ...

        def push(self, actor: _ActorT) -> None: ...
