from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

from ray import dag as ray_dag
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

from .actor_mixin import Actor


_NodeRet = TypeVar("_NodeRet")

if TYPE_CHECKING:
    from typing import Any
    from typing import Callable

    from typing_extensions import Concatenate
    from typing_extensions import ParamSpec

    import sunray

    from sunray import ObjectRef

    from .core import ObjectRefGenerator

    _P = ParamSpec("_P")
    _T = TypeVar("_T")
    _T0 = TypeVar("_T0")
    _T1 = TypeVar("_T1")
    _T2 = TypeVar("_T2")
    _T3 = TypeVar("_T3")
    _T4 = TypeVar("_T4")
    _T5 = TypeVar("_T5")
    _T6 = TypeVar("_T6")
    _T7 = TypeVar("_T7")
    _T8 = TypeVar("_T8")
    _T9 = TypeVar("_T9")

    _Callable_co = TypeVar("_Callable_co", covariant=True, bound=Callable)
    BindArg = Union[
        _T, sunray.ObjectRef[_T], "DAGNode[_T]", "DAGNode[sunray.ObjectRef[_T]]"
    ]
    ExecArg = Union[_T, sunray.ObjectRef[_T]]

    class DAGNode(ray_dag.DAGNode, Generic[_NodeRet]):
        def execute(  # type: ignore[override]
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> sunray.ObjectRef[_NodeRet]: ...

    class FunctionNode(ray_dag.FunctionNode, DAGNode[_NodeRet]): ...

    class StreamNode(ray_dag.FunctionNode, DAGNode[_NodeRet]):
        def execute(  # type: ignore[override]
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> ObjectRefGenerator[_NodeRet]: ...

    class ClassNode(ray_dag.ClassNode, DAGNode[_NodeRet]):
        @property
        def methods(self) -> type[_NodeRet]: ...

        def execute(  # type: ignore[override]
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> sunray.Actor[_NodeRet]: ...

    class ClassMethodNode(ray_dag.ClassMethodNode, DAGNode[_NodeRet]): ...

    class ClassStreamMethodNode(ray_dag.ClassMethodNode, DAGNode[_NodeRet]):
        def execute(  # type: ignore[override]
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> ObjectRefGenerator[_NodeRet]: ...

    _NodeT = TypeVar("_NodeT", bound=ray_dag.DAGNode)

    class BindCallable(Generic[_Callable_co, _NodeT]):
        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            __arg5: BindArg[_T5],
            __arg6: BindArg[_T6],
            __arg7: BindArg[_T7],
            __arg8: BindArg[_T8],
            __arg9: BindArg[_T9],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            __arg5: BindArg[_T5],
            __arg6: BindArg[_T6],
            __arg7: BindArg[_T7],
            __arg8: BindArg[_T8],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            __arg5: BindArg[_T5],
            __arg6: BindArg[_T6],
            __arg7: BindArg[_T7],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            __arg5: BindArg[_T5],
            __arg6: BindArg[_T6],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            __arg5: BindArg[_T5],
            __arg6: BindArg[_T6],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            __arg5: BindArg[_T5],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            __arg4: BindArg[_T4],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _T3, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            __arg3: BindArg[_T3],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _T2, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            __arg2: BindArg[_T2],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _T1, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            __arg1: BindArg[_T1],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[
                Callable[
                    Concatenate[_T0, _P],
                    Any,
                ],
                _NodeT,
            ],
            __arg0: BindArg[_T0],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        @overload
        def __call__(
            self: BindCallable[Callable[_P, Any], _NodeT],
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _NodeT: ...

        def __call__(self, *args: Any, **kwds: Any) -> _NodeT: ...
else:
    DAGNode = ray_dag.DAGNode
    StreamNode = FunctionNode = ray_dag.FunctionNode
    ClassMethodNode = ClassStreamMethodNode = ray_dag.ClassMethodNode

    class ClassNode(ray_dag.ClassNode):
        def execute(self, *args, _ray_cache_refs=False, **kwargs):
            return Actor(
                super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)
            )

        @property
        def methods(self):
            return self


_AttrT = TypeVar("_AttrT")
_GetItemT = TypeVar("_GetItemT")
_Ts = TypeVarTuple("_Ts")


class InputAttributeNode(ray_dag.InputAttributeNode, DAGNode[_NodeRet]): ...


class InputNode(ray_dag.InputNode, DAGNode, Generic[_NodeRet, Unpack[_Ts]]):
    @overload
    def __class_getitem__(cls, t: type[_NodeRet]) -> type[InputNode[_NodeRet]]: ...

    @overload
    def __class_getitem__(
        cls, t: type[_NodeRet], attr: type[_AttrT]
    ) -> type[InputNode[_NodeRet, _AttrT]]: ...

    @overload
    def __class_getitem__(
        cls, t: type[_NodeRet], attr: type[_AttrT], get_item: type[_GetItemT]
    ) -> type[InputNode[_NodeRet, _AttrT, _GetItemT]]: ...

    def __class_getitem__(cls, t, attr=None, get_item=None):
        return InputNode

    @overload
    def __getattr__(self: InputNode[_NodeRet], key: str) -> InputAttributeNode[Any]: ...

    @overload
    def __getattr__(
        self: InputNode[_NodeRet, _AttrT], key: str
    ) -> InputAttributeNode[_AttrT]: ...

    @overload
    def __getattr__(
        self: InputNode[_NodeRet, _AttrT, Any], key: str
    ) -> InputAttributeNode[_AttrT]: ...

    def __getattr__(self, key):
        return super().__getattr__(key)

    def __getitem__(
        self: InputNode[_NodeRet, _AttrT, _GetItemT], key: int | str
    ) -> InputAttributeNode[_GetItemT]:
        return super().__getitem__(key)


_OutputTs = TypeVarTuple("_OutputTs")

OutputNodeArg = Union[_T, DAGNode[_T]]


class MultiOutputNode(ray_dag.MultiOutputNode, DAGNode, Generic[Unpack[_OutputTs]]):
    if TYPE_CHECKING:

        @overload
        def __new__(
            cls,
            args: tuple[OutputNodeArg[_T0]],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0]: ...

        @overload
        def __new__(
            cls,
            args: tuple[OutputNodeArg[_T0], OutputNodeArg[_T1]],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1]: ...

        @overload
        def __new__(
            cls,
            args: tuple[OutputNodeArg[_T0], OutputNodeArg[_T1], OutputNodeArg[_T2]],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
                OutputNodeArg[_T4],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3, _T4]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
                OutputNodeArg[_T4],
                OutputNodeArg[_T5],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3, _T4, _T5]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
                OutputNodeArg[_T4],
                OutputNodeArg[_T5],
                OutputNodeArg[_T6],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3, _T4, _T5, _T6]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
                OutputNodeArg[_T4],
                OutputNodeArg[_T5],
                OutputNodeArg[_T6],
                OutputNodeArg[_T7],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
                OutputNodeArg[_T4],
                OutputNodeArg[_T5],
                OutputNodeArg[_T6],
                OutputNodeArg[_T7],
                OutputNodeArg[_T8],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]: ...

        @overload
        def __new__(
            cls,
            args: tuple[
                OutputNodeArg[_T0],
                OutputNodeArg[_T1],
                OutputNodeArg[_T2],
                OutputNodeArg[_T3],
                OutputNodeArg[_T4],
                OutputNodeArg[_T5],
                OutputNodeArg[_T6],
                OutputNodeArg[_T7],
                OutputNodeArg[_T8],
                OutputNodeArg[_T9],
            ],
            other_args_to_resolve: dict[str, Any] | None = None,
        ) -> MultiOutputNode[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]: ...

        def __new__(cls, args, other_args_to_resolve=None) -> MultiOutputNode: ...

    @overload  # type: ignore[override]
    def execute(
        self: MultiOutputNode[_T0],
        __arg0: ExecArg[_T0],
        *,
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> ObjectRef[tuple[_T0]]: ...

    @overload
    def execute(
        self: MultiOutputNode[_T0, _T1],
        __arg0: ExecArg[_T0],
        __arg1: ExecArg[_T1],
        *,
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> ObjectRef[tuple[_T0, _T1]]: ...

    @overload
    def execute(
        self: MultiOutputNode[_T0, _T1, _T2],
        __arg0: ExecArg[_T0],
        __arg1: ExecArg[_T1],
        __arg2: ExecArg[_T2],
        *,
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> ObjectRef[tuple[_T0, _T1, _T2]]: ...

    def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> ObjectRef:
        return super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)
