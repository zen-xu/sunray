from __future__ import annotations

import inspect

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import TypeVar
from typing import overload

import ray

from typing_extensions import ParamSpec

from . import io
from .util import get_num_returns


if TYPE_CHECKING:
    from typing import AsyncGenerator
    from typing import Awaitable
    from typing import Callable
    from typing import Generator

    from ray.actor import ActorHandle
    from ray.actor import ActorMethod
    from typing_extensions import Concatenate
    from typing_extensions import Literal
    from typing_extensions import TypedDict
    from typing_extensions import Unpack

    from .callable import ClassBindCallable
    from .callable import ClassMethodBindCallable
    from .callable import ClassStreamBindCallable
    from .callable import RemoteCallable
    from .core import ObjectRef
    from .core import ObjectRefGenerator
    from .typing import ActorRemoteOptions


_Ret = TypeVar("_Ret")
_YieldItem = TypeVar("_YieldItem")
_RemoteRet = TypeVar("_RemoteRet", bound=io.Out)
_ClassT = TypeVar("_ClassT")
_P = ParamSpec("_P")
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
        remote: RemoteCallable[Callable[_P, _ClassT], io.Out[Actor[_ClassT]]]
        bind: ClassBindCallable[Callable[_P, _ClassT], io.Actor[_ClassT]]
    else:

        def remote(self, *args, **kwargs):
            remote_cls = (
                ray.remote(**self._default_opts)(self._klass)
                if self._default_opts
                else ray.remote(self._klass)
            )
            handle = remote_cls.remote(*args, **kwargs)

            return Actor(handle)

        def bind(self, *args, **kwargs):
            from .dag import ClassNode

            return ClassNode(self._klass, args, kwargs, self._default_opts)

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
        remote: RemoteCallable[Callable[_P, _ClassT], io.Out[Actor[_ClassT]]]
        bind: ClassBindCallable[Callable[_P, _ClassT], io.Actor[_ClassT]]
    else:

        def remote(self, *args, **kwargs):
            remote_cls = (
                ray.remote(**self._opts)(self._klass)
                if self._opts
                else ray.remote(self._klass)
            )
            handle = remote_cls.remote(*args, **kwargs)
            return Actor(handle)

        def bind(self, *args, **kwargs):
            from .dag import ClassNode

            return ClassNode(self._klass, args, kwargs, self._opts)


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

    def bind(self, *args, **kwargs):
        return self.actor_method.bind(*args, **kwargs)


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

    class MethodOptions(TypedDict, total=False):
        concurrency_group: str
        max_task_retries: int
        retry_exceptions: bool | list[type[Exception]]
        enable_task_events: bool
        _generator_backpressure_num_objects: Any

    class Method(Generic[_P, _Ret]):
        remote: RemoteCallable[Callable[_P, _Ret], io.Out[ObjectRef[_Ret]]]
        bind: ClassMethodBindCallable[Callable[_P, _Ret], io.Out[ObjectRef[_Ret]]]

        @overload
        def options(
            self,
            *,
            unpack: Literal[False] = False,
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[_P, _Ret, io.Out[ObjectRef[_Ret]]]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[_P, _Ret, io.Out[tuple[ObjectRef[_R0]]]]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[_P, _Ret, io.Out[tuple[ObjectRef[_R0], ObjectRef[_R1]]]]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P, _Ret, io.Out[tuple[ObjectRef[_R0], ObjectRef[_R1], ObjectRef[_R2]]]
        ]: ...

        @overload
        def options(
            self: Method[_P, tuple[_R0, _R1, _R2, _R3]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self: Method[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8, _R9]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            _Ret,
            io.Out[
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
            self, *, unpack: bool = False, **options: Unpack[MethodOptions]
        ) -> MethodWrapper: ...

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _Ret: ...

    class AsyncMethod(Generic[_P, _Ret]):
        remote: RemoteCallable[Callable[_P, Awaitable[_Ret]], io.Out[ObjectRef[_Ret]]]
        bind: ClassMethodBindCallable[
            Callable[_P, Awaitable[_Ret]], io.Out[ObjectRef[_Ret]]
        ]

        @overload
        def options(
            self, *, unpack: Literal[False] = False, **options: Unpack[MethodOptions]
        ) -> MethodWrapper[_P, Awaitable[_Ret], io.Out[ObjectRef[_Ret]]]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[_P, Awaitable[_Ret], io.Out[tuple[ObjectRef[_R0]]]]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P, Awaitable[_Ret], io.Out[tuple[ObjectRef[_R0], ObjectRef[_R1]]]
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[tuple[ObjectRef[_R0], ObjectRef[_R1], ObjectRef[_R2]]],
        ]: ...

        @overload
        def options(
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self: AsyncMethod[_P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8]],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self: AsyncMethod[
                _P, tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8, _R9]
            ],
            *,
            unpack: Literal[True],
            **options: Unpack[MethodOptions],
        ) -> MethodWrapper[
            _P,
            Awaitable[_Ret],
            io.Out[
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
            self, *, unpack: bool = False, **options: Unpack[MethodOptions]
        ) -> MethodWrapper: ...

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> Awaitable[_Ret]: ...

    class StreamMethod(Generic[_P, _Ret, _YieldItem]):
        remote: RemoteCallable[
            Callable[_P, _Ret], io.Out[ObjectRefGenerator[_YieldItem]]
        ]
        bind: ClassStreamBindCallable[Callable[_P, _Ret], io.Yield[_YieldItem]]

        def options(
            self, **options: Unpack[MethodOptions]
        ) -> MethodWrapper[_P, _Ret, io.Out[ObjectRefGenerator[_YieldItem]]]: ...

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _Ret: ...

    class MethodWrapper(Generic[_P, _Ret, _RemoteRet]):
        remote: RemoteCallable[Callable[_P, _Ret], _RemoteRet]

        def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _Ret: ...

    class MethodDecorator:
        @overload
        def __call__(
            self,
            __method: Callable[
                Concatenate[Any, _P], Generator[ObjectRef[_YieldItem], None, None]
            ],
        ) -> StreamMethod[_P, Generator[_YieldItem, None, None], _YieldItem]: ...

        @overload
        def __call__(
            self,
            __method: Callable[Concatenate[Any, _P], Generator[_YieldItem, None, None]],
        ) -> StreamMethod[_P, Generator[_YieldItem, None, None], _YieldItem]: ...

        @overload
        def __call__(
            self,
            __method: Callable[
                Concatenate[Any, _P], AsyncGenerator[ObjectRef[_YieldItem], None]
            ],
        ) -> StreamMethod[_P, AsyncGenerator[_YieldItem, None], _YieldItem]: ...

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
def remote_method(**options: Unpack[MethodOptions]) -> MethodDecorator: ...


@overload
def remote_method(
    __method: Callable[
        Concatenate[Any, _P], Generator[ObjectRef[_YieldItem], None, None]
    ],
) -> StreamMethod[_P, Generator[_YieldItem, None, None], _YieldItem]: ...


@overload
def remote_method(
    __method: Callable[Concatenate[Any, _P], Generator[_YieldItem, None, None]],
) -> StreamMethod[_P, Generator[_YieldItem, None, None], _YieldItem]: ...


@overload
def remote_method(
    __method: Callable[
        Concatenate[Any, _P], AsyncGenerator[ObjectRef[_YieldItem], None]
    ],
) -> StreamMethod[_P, AsyncGenerator[_YieldItem, None], _YieldItem]: ...


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


class ActorMethodWrapper:  # pragma: no cover
    def __init__(self, actor_inst, method) -> None:
        self.actor_inst = actor_inst
        self.method = method

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.method(*args, **kwds)

    @property
    def _sunray_actor(self) -> Actor:
        if not getattr(self.actor_inst, "__sunray_actor__", None):
            import sunray

            ctx = sunray.get_runtime_context()
            current_actor_handle = ctx.current_actor
            self.actor_inst.__sunray_actor__ = Actor(current_actor_handle)
        return self.actor_inst.__sunray_actor__

    def options(self, *args: Any, **kwds: Any) -> Any:
        return getattr(self._sunray_actor.methods, self.method.__name__).options(
            *args, **kwds
        )

    def remote(self, *args: Any, **kwds: Any) -> Any:
        return getattr(self._sunray_actor.methods, self.method.__name__).remote(
            *args, **kwds
        )

    def bind(self, *args: Any, **kwds: Any) -> Any:
        return getattr(self._sunray_actor.methods, self.method.__name__).bind(
            *args, **kwds
        )


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

    def __getattribute__(self, name: str) -> Any:  # pragma: no cover
        attr = super().__getattribute__(name)
        if getattr(attr, "__ray_num_returns__", None):
            attr = ActorMethodWrapper(self, attr)
        return attr

    @classmethod
    def new_actor(cls: Callable[_P, _ClassT]) -> ActorClass[_P, _ClassT]:
        return ActorClass(cls, cls._default_ray_opts)  # type: ignore[attr-defined]
