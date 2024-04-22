from __future__ import annotations

import inspect

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import TypeVar
from typing import overload

import ray

from .util import get_num_returns


if TYPE_CHECKING:
    from typing import AsyncGenerator
    from typing import Awaitable
    from typing import Callable
    from typing import Concatenate
    from typing import Generator
    from typing import Literal
    from typing import ParamSpec
    from typing import Unpack

    from ray.actor import ActorHandle
    from ray.actor import ActorMethod

    from .typing import ActorRemoteOptions
    from .typing import RemoteCallable
    from .typing import StreamingObjectRefGenerator

    _P = ParamSpec("_P")

else:
    _P = TypeVar("_P")

_Ret = TypeVar("_Ret")
_YieldItem = TypeVar("_YieldItem")
_RemoteRet = TypeVar("_RemoteRet")
_ClassT = TypeVar("_ClassT")
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


def add_var_keyword_to_klass(klass):
    # change klass.__init__ signature to fix ray injecting `_ray_trace_ctx`
    orig_init = klass.__init__
    sig = inspect.signature(orig_init)
    if list(sig.parameters.values())[-1].kind == inspect.Parameter.VAR_KEYWORD:
        return klass

    new_params = [
        *sig.parameters.values(),
        inspect.Parameter("_kwargs", inspect.Parameter.VAR_KEYWORD),
    ]

    def __init__(*args, **kwargs):  # noqa: N807 # pragma: no cover
        kwargs.pop("_ray_trace_ctx", None)
        orig_init(*args, **kwargs)

    __init__.__signature__ = sig.replace(parameters=new_params)
    klass.__init__ = __init__
    return klass


class ActorClass(Generic[_P, _ClassT]):
    def __init__(self, klass: Callable[_P, _ClassT], default_opts: ActorRemoteOptions):
        self._klass = add_var_keyword_to_klass(klass)
        self._default_opts = default_opts

    if TYPE_CHECKING:
        remote: RemoteCallable[Callable[_P, _ClassT], Actor[_ClassT]]
    else:

        def remote(self, *args, **kwargs):
            if self._default_opts:
                handle = ray.remote(**self._default_opts)(self._klass).remote(
                    *args, **kwargs
                )
            else:
                handle = ray.remote(self._klass).remote(*args, **kwargs)
            return Actor(handle)

    def options(
        self, **opts: Unpack[ActorRemoteOptions]
    ) -> ActorClassWrapper[_P, _ClassT]:
        opts = {**self._default_opts, **opts}
        return ActorClassWrapper(self._klass, opts)


class ActorClassWrapper(Generic[_P, _ClassT]):
    def __init__(self, klass: Callable[_P, _ClassT], opts: ActorRemoteOptions):
        self._klass = add_var_keyword_to_klass(klass)
        self._opts = opts

    if TYPE_CHECKING:
        remote: RemoteCallable[Callable[_P, _ClassT], Actor[_ClassT]]
    else:

        def remote(self, *args, **kwargs):
            if self._opts:
                handle = ray.remote(**self._opts)(self._klass).remote(*args, **kwargs)
            else:
                handle = ray.remote(self._klass).remote(*args, **kwargs)
            return Actor(handle)


class ActorHandleProxy:
    def __init__(self, actor_handle: ActorHandle) -> None:
        self.actor_handle = actor_handle

    def __getattr__(self, k):
        method = getattr(self.actor_handle, k)
        return ActorMethodProxy(method)


class ActorMethodProxy:
    def __init__(self, actor_method: ActorMethod) -> None:
        self.actor_method = actor_method

    def remote(self, *args, **kwargs):
        if self.actor_method._num_returns == "streaming":
            return self.actor_method.remote(*args, **kwargs)

        return self.actor_method.options(num_returns=1).remote(*args, **kwargs)

    def options(self, *, unpack: bool = False, **options):
        if self.actor_method._num_returns != "streaming" and not unpack:
            options["num_returns"] = 1

        return self.actor_method.options(**options)


class Actor(Generic[_ClassT]):
    def __init__(self, actor_handle: ActorHandle):
        self._actor_handle = actor_handle

    @property
    def methods(self) -> type[_ClassT]:  # pragma: no cover
        return ActorHandleProxy(self._actor_handle)  # type: ignore[return-value]

    def __repr__(self) -> str:
        return repr(self._actor_handle)

    def __str__(self) -> str:
        return str(self._actor_handle)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Actor)
            and self._actor_handle._actor_id == other._actor_handle._actor_id
        )

    def __hash__(self) -> int:
        return hash(self._actor_handle._actor_id)


if TYPE_CHECKING:

    class Method(Generic[_P, _Ret]):
        remote: RemoteCallable[Callable[_P, _Ret], ray.ObjectRef[_Ret]]

        @overload
        def options(
            self, *, name: str = ..., concurrency_group: str = ...
        ) -> MethodWrapper[_P, _Ret, ray.ObjectRef[_Ret]]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[_P, _Ret, tuple[ray.ObjectRef[_R0]]]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[_P, _Ret, tuple[ray.ObjectRef[_R0], ray.ObjectRef[_R1]]]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P, _Ret, tuple[ray.ObjectRef[_R0], ray.ObjectRef[_R1], ray.ObjectRef[_R2]]
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
            ],
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
            ],
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
            ],
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
            ],
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
                ray.ObjectRef[_R7],
            ],
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
                ray.ObjectRef[_R7],
                ray.ObjectRef[_R8],
            ],
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8, _R9]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            _Ret,
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
                ray.ObjectRef[_R7],
                ray.ObjectRef[_R8],
                ray.ObjectRef[_R9],
            ],
        ]: ...

        def options(
            self, *, unpack: bool = False, name: str = ..., concurrency_group: str = ...
        ) -> MethodWrapper: ...

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _Ret: ...

    class AsyncMethod(Generic[_P, _Ret]):
        remote: RemoteCallable[Callable[_P, Awaitable[_Ret]], ray.ObjectRef[_Ret]]

        @overload
        def options(
            self, *, name: str = ..., concurrency_group: str = ...
        ) -> MethodWrapper[_P, Awaitable[_Ret], ray.ObjectRef[_Ret]]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[_P, Awaitable[_Ret], tuple[ray.ObjectRef[_R0]]]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P, Awaitable[_Ret], tuple[ray.ObjectRef[_R0], ray.ObjectRef[_R1]]
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[ray.ObjectRef[_R0], ray.ObjectRef[_R1], ray.ObjectRef[_R2]],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
            ],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
            ],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
            ],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
            ],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
                ray.ObjectRef[_R7],
            ],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8]],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
                ray.ObjectRef[_R7],
                ray.ObjectRef[_R8],
            ],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[
                _P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8, _R9]
            ],
            *,
            unpack: Literal[True],
            name: str = ...,
            concurrency_group: str = ...,
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            tuple[
                ray.ObjectRef[_R0],
                ray.ObjectRef[_R1],
                ray.ObjectRef[_R2],
                ray.ObjectRef[_R3],
                ray.ObjectRef[_R4],
                ray.ObjectRef[_R5],
                ray.ObjectRef[_R6],
                ray.ObjectRef[_R7],
                ray.ObjectRef[_R8],
                ray.ObjectRef[_R9],
            ],
        ]: ...

        def options(
            self, *, unpack: bool = False, name: str = ..., concurrency_group: str = ...
        ) -> MethodWrapper: ...

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> Awaitable[_Ret]: ...

    class StreamMethod(Generic[_P, _Ret, _YieldItem]):
        remote: RemoteCallable[
            Callable[_P, _Ret], StreamingObjectRefGenerator[_YieldItem]
        ]

        def options(
            self, *, name: str = ..., concurrency_group: str = ...
        ) -> MethodWrapper[_P, _Ret, StreamingObjectRefGenerator[_YieldItem]]: ...

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _Ret: ...

    class MethodWrapper(Generic[_P, _Ret, _RemoteRet]):
        remote: RemoteCallable[Callable[_P, _Ret], _RemoteRet]

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _Ret: ...

    class MethodDecorator:
        @overload
        def __call__(
            self,
            __method: Callable[Concatenate[Any, _P], Generator[_YieldItem, None, None]],
        ) -> StreamMethod[_P, Generator[_YieldItem, None, None], _YieldItem]: ...

        @overload
        def __call__(
            self,
            __method: Callable[Concatenate[Any, _P], AsyncGenerator[_YieldItem, None]],
        ) -> StreamMethod[_P, AsyncGenerator[_YieldItem, None], _YieldItem]: ...

        @overload
        def __call__(
            self, __method: Callable[Concatenate[Any, _P], Awaitable[_Ret]]
        ) -> AsyncMethod[_P, _Ret]: ...

        @overload
        def __call__(
            self, __method: Callable[Concatenate[Any, _P], _Ret]
        ) -> Method[_P, _Ret]: ...

        def __call__(self, __method) -> Any: ...


@overload
def remote_method(*, concurrency_group: str = ..., **kwargs) -> MethodDecorator: ...


@overload
def remote_method(
    __method: Callable[Concatenate[Any, _P], Generator[_YieldItem, None, None]],
) -> StreamMethod[_P, Generator[_YieldItem, None, None], _YieldItem]: ...


@overload
def remote_method(
    __method: Callable[Concatenate[Any, _P], AsyncGenerator[_YieldItem, None]],
) -> StreamMethod[_P, AsyncGenerator[_YieldItem, None], _YieldItem]: ...


@overload
def remote_method(
    __method: Callable[Concatenate[Any, _P], Awaitable[_Ret]],
) -> AsyncMethod[_P, _Ret]: ...


@overload
def remote_method(
    __method: Callable[Concatenate[Any, _P], _Ret],
) -> Method[_P, _Ret]: ...


def remote_method(__method=None, **kwargs):
    """
    Mark the method is a remote method
    """

    def build_method(method, options):
        if inspect.isgeneratorfunction(method) or inspect.isasyncgenfunction(method):
            options["num_returns"] = "streaming"
        else:
            options["num_returns"] = get_num_returns(method)

        sig = inspect.signature(method)
        if list(sig.parameters.values())[-1].kind == inspect.Parameter.VAR_KEYWORD:
            return ray.method(**options)(method)

        if inspect.iscoroutinefunction(method):

            async def async_wrapper(*args, **kwargs):  # pragma: no cover
                kwargs.pop("_ray_trace_ctx", None)
                return await method(*args, **kwargs)

            wrapper_method = async_wrapper

        elif inspect.isasyncgenfunction(method):

            async def async_gen_wrapper(*args, **kwargs):  # pragma: no cover
                kwargs.pop("_ray_trace_ctx", None)
                async for obj in method(*args, **kwargs):
                    yield obj

            wrapper_method = async_gen_wrapper

        else:

            def wrapper(*args, **kwargs):  # pragma: no cover
                kwargs.pop("_ray_trace_ctx", None)
                return method(*args, **kwargs)

            wrapper_method = wrapper

        new_params = [
            *sig.parameters.values(),
            inspect.Parameter("_kwargs", inspect.Parameter.VAR_KEYWORD),
        ]
        wrapper_method.__signature__ = sig.replace(parameters=new_params)
        for assigned in ["__name__", "__module__", "__qualname__"]:
            setattr(wrapper_method, assigned, getattr(method, assigned))
        return ray.method(**options)(wrapper_method)

    if kwargs:
        return lambda method: build_method(method, kwargs)

    return build_method(__method, kwargs)


class ActorMixin:
    """
    Make a class into an actor class.

    Example:
        ```python
        from __future__ import annotations

        from typing import AsyncGenerator

        import ray

        from sunray import ActorMixin
        from sunray import remote_method


        class Demo(ActorMixin, num_cpus=1, concurrency_groups={"group1": 1}):
            def __init__(self, init: int):
                self.init = init

            @remote_method
            def calculate(self, v1: int, v2: int) -> int:
                return self.init + v1 + v2

            @remote_method(concurrency_group="group1")
            async def echo(self, message: str) -> str:
                return message

            @remote_method
            async def stream(self, gen_count: int) -> AsyncGenerator[int, None]:
                for i in range(gen_count):
                    yield i

            @remote_method
            def get_tuple(self) -> tuple[int, str]:
                return 1, "a"


        demo = Demo.new_actor().remote(1)

        # sync method
        calculate_ref = demo.methods.calculate.remote(1, 2)
        assert ray.get(calculate_ref) == 4

        # async method
        echo_ref = demo.methods.echo.remote("hello")
        assert ray.get(echo_ref) == "hello"

        # stream method
        stream = demo.methods.stream.remote(4)
        assert [ray.get(next(stream)) for _ in range(4)] == list(range(4))

        # unpack returns
        # default unpack is False
        without_unpack_refs = demo.methods.get_tuple.options().remote()
        assert ray.get(without_unpack_refs) == (1, "a")

        # enable unpack
        obj1_ref, obj2_ref = demo.methods.get_tuple.options(unpack=True).remote()
        assert [ray.get(obj1_ref), ray.get(obj2_ref)] == [1, "a"]
        ```
    """

    _default_ray_opts: ActorRemoteOptions

    def __init__(self) -> None:  # pragma: no cover
        ...

    def __init_subclass__(cls, **default_ray_opts: Unpack[ActorRemoteOptions]) -> None:
        super().__init_subclass__()
        cls._default_ray_opts = default_ray_opts

    @classmethod
    def new_actor(cls: Callable[_P, _ClassT]) -> ActorClass[_P, _ClassT]:
        return ActorClass(cls, cls._default_ray_opts)  # type: ignore[attr-defined]
