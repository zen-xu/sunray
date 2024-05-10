from __future__ import annotations

import inspect

from typing import TYPE_CHECKING
from typing import Callable
from typing import Generic
from typing import TypeVar
from typing import overload

import ray
import ray.actor

from ray import remote_function as ray_func
from typing_extensions import ParamSpec

from .dag import FunctionNode
from .dag import StreamNode
from .io import Out
from .io import Yield
from .util import get_num_returns


if TYPE_CHECKING:
    from typing import Any
    from typing import Generator
    from typing import Literal

    from ray.actor import ActorClass
    from typing_extensions import Unpack

    from .callable import FunctionBindCallable
    from .callable import RemoteCallable
    from .callable import StreamBindCallable
    from .core import ObjectRef
    from .core import ObjectRefGenerator
    from .typing import FunctionRemoteOptions


_Callable_co = TypeVar("_Callable_co", covariant=True, bound=Callable)
_RemoteRet = TypeVar("_RemoteRet", bound=Out)
_P = ParamSpec("_P")
_R = TypeVar("_R")
_R0 = TypeVar("_R0")
_R1 = TypeVar("_R1")
_R2 = TypeVar("_R2")
_R3 = TypeVar("_R3")
_R4 = TypeVar("_R4")
_R5 = TypeVar("_R5")
_R6 = TypeVar("_R6")
_R7 = TypeVar("_R7")
_R8 = TypeVar("_R8")
_R9 = TypeVar("_R9")


class RemoteFunctionWrapper(Generic[_Callable_co, _RemoteRet]):
    def __init__(
        self, remote_func: ray_func.RemoteFunction, opts: FunctionRemoteOptions
    ) -> None:
        self._remote_func = remote_func
        self._opts = opts

    if TYPE_CHECKING:
        remote: RemoteCallable[_Callable_co, _RemoteRet]
        bind: FunctionBindCallable[_Callable_co, _RemoteRet]
    else:

        def remote(self, *args, **kwargs):
            opts = dict(self._opts)
            return self._remote_func.options(**opts).remote(*args, **kwargs)

        def bind(self, *args, **kwargs):
            return FunctionNode(self._remote_func._function, args, kwargs, self._opts)


class RemoteFunction(RemoteFunctionWrapper, Generic[_Callable_co, _R]):
    remote: RemoteCallable[_Callable_co, Out[ObjectRef[_R]]]

    @overload
    def options(
        self,
        *,
        unpack: Literal[False] = False,
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[_Callable_co, Out[ObjectRef[_R]]]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[_Callable_co, Out[tuple[ObjectRef[_R0]]]]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0, _R1]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co, Out[tuple[ObjectRef[_R0], ObjectRef[_R1]]]
    ]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0, _R1, _R2]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co, Out[tuple[ObjectRef[_R0], ObjectRef[_R1], ObjectRef[_R2]]]
    ]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0, _R1, _R2, _R3]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
            ]
        ],
    ]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0, _R1, _R2, _R3, _R4]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
                ObjectRef[_R4],
            ]
        ],
    ]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0, _R1, _R2, _R3, _R4, _R5]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
                ObjectRef[_R4],
                ObjectRef[_R5],
            ]
        ],
    ]: ...

    @overload
    def options(
        self: RemoteFunction[_Callable_co, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6]],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
                ObjectRef[_R4],
                ObjectRef[_R5],
                ObjectRef[_R6],
            ]
        ],
    ]: ...

    @overload
    def options(
        self: RemoteFunction[
            _Callable_co, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7]
        ],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
                ObjectRef[_R4],
                ObjectRef[_R5],
                ObjectRef[_R6],
                ObjectRef[_R7],
            ]
        ],
    ]: ...

    @overload
    def options(
        self: RemoteFunction[
            _Callable_co, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8]
        ],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
                ObjectRef[_R4],
                ObjectRef[_R5],
                ObjectRef[_R6],
                ObjectRef[_R7],
                ObjectRef[_R8],
            ]
        ],
    ]: ...

    @overload
    def options(
        self: RemoteFunction[
            _Callable_co, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8, _R9]
        ],
        *,
        unpack: Literal[True],
        **opts: Unpack[FunctionRemoteOptions],
    ) -> RemoteFunctionWrapper[
        _Callable_co,
        Out[
            tuple[
                ObjectRef[_R0],
                ObjectRef[_R1],
                ObjectRef[_R2],
                ObjectRef[_R3],
                ObjectRef[_R4],
                ObjectRef[_R5],
                ObjectRef[_R6],
                ObjectRef[_R7],
                ObjectRef[_R8],
                ObjectRef[_R9],
            ]
        ],
    ]: ...

    def options(
        self,
        *,
        unpack: bool = False,
        **opts: Unpack[FunctionRemoteOptions],
    ):
        opts = {**self._opts, **opts}
        num_returns = get_num_returns(self._remote_func._function) if unpack else 1
        opts["num_returns"] = num_returns  # type: ignore[typeddict-unknown-key]
        return RemoteFunctionWrapper(self._remote_func, opts)

    if TYPE_CHECKING:
        bind: FunctionBindCallable[_Callable_co, Out[ObjectRef[_R]]]
    else:

        def bind(self, *args, **kwargs):
            return self._remote_func.bind(*args, **kwargs)


class RemoteStreamWrapper(Generic[_Callable_co, _R]):
    def __init__(
        self, remote_func: ray_func.RemoteFunction, opts: FunctionRemoteOptions
    ) -> None:
        self._remote_func = remote_func
        self._opts = opts

    if TYPE_CHECKING:
        remote: RemoteCallable[_Callable_co, Out[ObjectRefGenerator[_R]]]
        bind: StreamBindCallable[_Callable_co, Yield[_R]]
    else:

        def remote(self, *args, **kwargs):
            opts = dict(self._opts)
            opts["num_returns"] = "streaming"

            return self._remote_func.options(**opts).remote(*args, **kwargs)

        def bind(self, *args, **kwargs):
            opts = dict(self._opts)
            opts["num_returns"] = "streaming"

            return StreamNode(self._remote_func._function, args, kwargs, self._opts)


class RemoteStream(RemoteStreamWrapper[_Callable_co, _R]):
    def options(
        self, **opts: Unpack[FunctionRemoteOptions]
    ) -> RemoteStreamWrapper[_Callable_co, _R]:
        opts = {**self._opts, **opts}
        return RemoteStreamWrapper(self._remote_func, opts)

    if not TYPE_CHECKING:

        def bind(self, *args, **kwargs):  # pragma: no cover
            return self._remote_func.bind(*args, **kwargs)


if TYPE_CHECKING:

    class RemoteDecorator:
        @overload
        def __call__(self, __obj: type) -> ActorClass: ...

        @overload
        def __call__(
            self, __obj: Callable[_P, Generator[_R, Any, Any]]
        ) -> RemoteStream[Callable[_P, Generator[_R, Any, Any]], _R]: ...

        @overload
        def __call__(
            self, __obj: Callable[_P, _R]
        ) -> RemoteFunction[Callable[_P, _R], _R]: ...

        def __call__(self, __obj) -> Any: ...


@overload
def remote(__type: type) -> ActorClass: ...


@overload
def remote(
    __func: Callable[_P, Generator[_R, Any, Any]],
) -> RemoteStream[Callable[_P, Generator[_R, Any, Any]], _R]: ...


@overload
def remote(__func: Callable[_P, _R]) -> RemoteFunction[Callable[_P, _R], _R]: ...


@overload
def remote(**opts: Unpack[FunctionRemoteOptions]) -> RemoteDecorator: ...


def remote(*args, **kwargs) -> ActorClass | RemoteFunction | RemoteStream | Callable:
    """
    This is an enhanced version of ``ray.remote`` that supports improved type hints.

    ```python
    import ray
    from sunray import remote


    @remote
    def f(a: int, b: int, c: int) -> tuple[int, int]:
        return a + b, b + c


    v1, v2 = ray.get(f.options(unpack=True).remote(1, 2, 3))
    assert v1 == 3
    assert v2 == 5
    ```
    """
    ret = ray.remote(*args, **kwargs)
    if isinstance(ret, ray_func.RemoteFunction):
        return (
            RemoteStream(ret, {})
            if inspect.isgeneratorfunction(ret._function)
            else RemoteFunction(ret, {})
        )

    if isinstance(ret, ray.actor.ActorClass):
        return ret

    # ret is decorator
    decorator = ret

    def wrapper(*args, **kwargs):
        ret = decorator(*args, **kwargs)

        if isinstance(ret, ray_func.RemoteFunction):
            return (
                RemoteStream(ret, {})
                if inspect.isgeneratorfunction(ret._function)
                else RemoteFunction(ret, {})
            )

        if isinstance(ret, ray.actor.ActorClass):
            return ret

        raise ValueError(f"Unexpected return value: {ret}")  # pragma: no cover

    return wrapper
