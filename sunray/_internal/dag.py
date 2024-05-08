from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Callable
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

from ray import dag as ray_dag
from typing_extensions import Concatenate
from typing_extensions import ParamSpec
from typing_extensions import Self
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

import sunray


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
_In = TypeVar("_In")
_Outs = TypeVarTuple("_Outs")
_Out = TypeVar("_Out")
_Out0 = TypeVar("_Out0")
_Out1 = TypeVar("_Out1")
_Out2 = TypeVar("_Out2")
_Out3 = TypeVar("_Out3")
_Out4 = TypeVar("_Out4")
_Out5 = TypeVar("_Out5")
_Out6 = TypeVar("_Out6")
_Out7 = TypeVar("_Out7")
_Out8 = TypeVar("_Out8")
_Out9 = TypeVar("_Out9")


class DAGNode(Generic[_In, Unpack[_Outs]]): ...


class FunctionNode(ray_dag.FunctionNode, DAGNode[_In, _Out]):
    def execute(  # type: ignore[override]
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.ObjectRef[_Out]:
        return super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)  # type: ignore[return-value]


class StreamNode(ray_dag.FunctionNode, DAGNode[_In, _Out]):
    def execute(  # type: ignore[override]
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.ObjectRefGenerator[_Out]:
        return super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)  # type: ignore[return-value]


class ClassNode(ray_dag.ClassNode, DAGNode[_In, _Out]):
    @property
    def methods(self) -> type[_Out]:
        return self  # type: ignore[return-value]

    def execute(  # type: ignore[override]
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.Actor[_Out]:
        handler = super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)
        return sunray.Actor(handler)  # type: ignore[return-value, arg-type]


class ClassMethodNode(ray_dag.ClassMethodNode, DAGNode[_In, _Out]):
    def execute(  # type: ignore[override]
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.ObjectRef[_Out]:
        return super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)  # type: ignore[return-value]


class ClassStreamMethodNode(ray_dag.ClassMethodNode, DAGNode[_In, _Out]):
    def execute(  # type: ignore[override]
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.ObjectRefGenerator[_Out]:
        return super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)  # type: ignore[return-value]


class InputAttributeNode(ray_dag.InputAttributeNode, DAGNode[_In, _Out]):
    def execute(  # type: ignore[override]
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.ObjectRef[_Out]:
        return super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)  # type: ignore[return-value]


_AttrT = TypeVar("_AttrT")
_GetItemT = TypeVar("_GetItemT")


_Ts = TypeVarTuple("_Ts")


class InputNode(
    ray_dag.InputNode,
    DAGNode[_In, _In],
    Generic[_In, Unpack[_Ts]],
):
    @overload
    def __class_getitem__(cls, t: type[_In]) -> type[InputNode[_In]]: ...

    @overload
    def __class_getitem__(
        cls, t: type[_In], attr: type[_AttrT]
    ) -> type[InputNode[_In, _AttrT]]: ...

    @overload
    def __class_getitem__(
        cls, t: type[_In], attr: type[_AttrT], get_item: type[_GetItemT]
    ) -> type[InputNode[_In, _AttrT, _GetItemT]]: ...

    def __class_getitem__(cls, t, attr=None, get_item=None):
        return InputNode

    @overload
    def __getattr__(self: InputNode[_In], key: str) -> InputAttributeNode[_In, Any]: ...

    @overload
    def __getattr__(
        self: InputNode[_In, _AttrT], key: str
    ) -> InputAttributeNode[_In, _AttrT]: ...

    @overload
    def __getattr__(
        self: InputNode[_In, _AttrT, Any], key: str
    ) -> InputAttributeNode[_In, _AttrT]: ...

    def __getattr__(self, key):
        return super().__getattr__(key)

    def __getitem__(
        self: InputNode[_In, _AttrT, _GetItemT], key: int | str
    ) -> InputAttributeNode[_In, _GetItemT]:
        return super().__getitem__(key)

    def __enter__(self) -> Self:
        return super().__enter__()


OutputArg = Union[DAGNode[_In, _Out], _In]


class MultiOutputNode(DAGNode[_In, Unpack[_Outs]]):
    @overload
    def __new__(
        cls,
        args: tuple[DAGNode[_In, _Out0]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_In, _Out0]: ...

    @overload
    def __new__(
        cls,
        args: tuple[OutputArg[_In, _Out0], OutputArg[_In, _Out1]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_In, _Out0, _Out1]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0], OutputArg[_In, _Out1], OutputArg[_In, _Out2]
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_In, _Out0, _Out1, _Out2]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_In, _Out0, _Out1, _Out2, _Out3]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
            OutputArg[_In, _Out4],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _In,
        _Out0,
        _Out1,
        _Out2,
        _Out3,
        _Out4,
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
            OutputArg[_In, _Out4],
            OutputArg[_In, _Out5],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _In,
        _Out0,
        _Out1,
        _Out2,
        _Out3,
        _Out4,
        _Out5,
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
            OutputArg[_In, _Out4],
            OutputArg[_In, _Out5],
            OutputArg[_In, _Out6],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
            OutputArg[_In, _Out4],
            OutputArg[_In, _Out5],
            OutputArg[_In, _Out6],
            OutputArg[_In, _Out7],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
            OutputArg[_In, _Out4],
            OutputArg[_In, _Out5],
            OutputArg[_In, _Out6],
            OutputArg[_In, _Out7],
            OutputArg[_In, _Out8],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            OutputArg[_In, _Out0],
            OutputArg[_In, _Out1],
            OutputArg[_In, _Out2],
            OutputArg[_In, _Out3],
            OutputArg[_In, _Out4],
            OutputArg[_In, _Out5],
            OutputArg[_In, _Out6],
            OutputArg[_In, _Out7],
            OutputArg[_In, _Out8],
            OutputArg[_In, _Out9],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9
    ]: ...

    def __new__(cls, args, other_args_to_resolve=None) -> MultiOutputNode:
        return ray_dag.MultiOutputNode(args, other_args_to_resolve)  # type: ignore[return-value]

    if TYPE_CHECKING:

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0]]: ...

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0, _Out1],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1]]: ...

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0, _Out1, _Out2],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2]]: ...

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0, _Out1, _Out2, _Out3],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3]]: ...

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0, _Out1, _Out2, _Out3, _Out4],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3, _Out4]]: ...

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]]: ...

        @overload
        def execute(
            self: MultiOutputNode[_In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                _In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7
            ],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                _In, _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8
            ],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                _In,
                _Out0,
                _Out1,
                _Out2,
                _Out3,
                _Out4,
                _Out5,
                _Out6,
                _Out7,
                _Out8,
                _Out9,
            ],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9]
        ]: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs):
            raise NotImplementedError()


_NodeT = TypeVar("_NodeT", bound=DAGNode)
_Callable_co = TypeVar("_Callable_co", covariant=True, bound=Callable)
BindArg = Union[
    "DAGNode[_In, _T]",
    "sunray.ObjectRef[_T]",
    _T,
]


class BindCallable(Generic[_Callable_co, _NodeT, _Out]):
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        __arg9: BindArg[_In, _T9],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            StreamNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[_P, Any],
            StreamNode,
            _Out,
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Any, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        __arg9: BindArg[_In, _T9],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            FunctionNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[_P, Any],
            FunctionNode,
            _Out,
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Any, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        __arg9: BindArg[_In, _T9],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            ClassNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[_P, Any],
            ClassNode,
            _Out,
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Any, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        __arg9: BindArg[_In, _T9],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            ClassMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[_P, Any],
            ClassMethodNode,
            _Out,
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Any, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        __arg9: BindArg[_In, _T9],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        __arg8: BindArg[_In, _T8],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        __arg7: BindArg[_In, _T7],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        __arg6: BindArg[_In, _T6],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        __arg5: BindArg[_In, _T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        __arg4: BindArg[_In, _T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        __arg3: BindArg[_In, _T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        __arg2: BindArg[_In, _T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        __arg1: BindArg[_In, _T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            ClassStreamMethodNode,
            _Out,
        ],
        __arg0: BindArg[_In, _T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[_In, _Out]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[_P, Any],
            ClassStreamMethodNode,
            _Out,
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Any, _Out]: ...

    def __call__(self, *args: Any, **kwds: Any):
        raise NotImplementedError
