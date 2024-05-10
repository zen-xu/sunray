# mypy: disable-error-code="override"

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import Mapping
from typing import Sequence
from typing import TypeVar
from typing import Union
from typing import overload

from ray import dag as ray_dag
from typing_extensions import Self
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

import sunray

from . import io
from .io import _In
from .io import _Out


_T = TypeVar("_T")
_O0 = TypeVar("_O0")
_O1 = TypeVar("_O1")
_O2 = TypeVar("_O2")
_O3 = TypeVar("_O3")
_O4 = TypeVar("_O4")
_O5 = TypeVar("_O5")
_O6 = TypeVar("_O6")
_O7 = TypeVar("_O7")
_O8 = TypeVar("_O8")
_O9 = TypeVar("_O9")

_InT = TypeVar("_InT", bound=io.BaseIn, covariant=True)
_OutT = TypeVar("_OutT", bound=io.BaseOut, covariant=True)
_Ts = TypeVarTuple("_Ts")

ExecArg = Union[_T, "sunray.ObjectRef[_T]", "DAGNode[Any, io.Out[_T]]"]


class DAGNode(Generic[_InT, _OutT]): ...


class _FunctionLikeNode(DAGNode[_InT, _OutT]):
    if TYPE_CHECKING:
        # ==== without input ====
        @overload
        def execute(
            self: DAGNode[io.NoIn, io.Outs[Unpack[_Ts]]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[Unpack[_Ts]]: ...

        @overload
        def execute(
            self: DAGNode[io.NoIn, io.Out[_Out]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _Out: ...

        # ==== with input ====

        @overload
        def execute(
            self: DAGNode[io.In[_In], io.Outs[Unpack[_Ts]]],
            __in: ExecArg[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[Unpack[_Ts]]: ...

        @overload
        def execute(
            self: DAGNode[io.In[_In], io.Out[_Out]],
            __in: ExecArg[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _Out: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> Any: ...


class FunctionNode(  # type: ignore[misc]
    _FunctionLikeNode[_InT, _OutT], ray_dag.FunctionNode
): ...


_StreamOutT = TypeVar("_StreamOutT", bound=io.Yield)


class _StreamLikeNode(DAGNode[_InT, _StreamOutT]):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: DAGNode[io.NoIn, io.Yield[_Out]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_Out]: ...

        @overload
        def execute(
            self: DAGNode[io.In[_In], io.Yield[_Out]],
            __in: ExecArg[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_Out]: ...

        def execute(
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> sunray.ObjectRefGenerator: ...


class StreamNode(  # type: ignore[misc]
    _StreamLikeNode[_InT, _StreamOutT], ray_dag.FunctionNode
): ...


_ClassOutT = TypeVar("_ClassOutT", bound=io.Actor)


class ClassNode(ray_dag.ClassNode, DAGNode[_InT, _ClassOutT]):
    @property
    def methods(self: DAGNode[_InT, io.Actor[_Out]]) -> type[_Out]:
        return self  # type: ignore[return-value]

    @overload
    def execute(
        self: DAGNode[io.NoIn, io.Actor[_Out]],
        *,
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> sunray.Actor[_Out]: ...

    @overload
    def execute(
        self: DAGNode[io.In[_In], io.Actor[_Out]],
        __in: ExecArg[_In],
        *,
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> sunray.Actor[_Out]: ...

    def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> sunray.Actor:
        handler = super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)
        return sunray.Actor(handler)  # type: ignore[return-value, arg-type]


class ClassMethodNode(  # type: ignore[misc]
    _FunctionLikeNode[_InT, _OutT], ray_dag.ClassMethodNode
): ...


class ClassStreamNode(  # type: ignore[misc]
    _StreamLikeNode[_InT, _StreamOutT], ray_dag.ClassMethodNode
): ...


class InputAttributeNode(  # type: ignore[misc]
    ray_dag.InputAttributeNode, DAGNode[_InT, io.Out[_T]]
):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: DAGNode[io.NoIn, Any],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        @overload
        def execute(
            self: DAGNode[io.In[_In], Any],
            __in: ExecArg[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> _T: ...


_K = TypeVar("_K")
_V = TypeVar("_V")


class InputNode(ray_dag.InputNode, DAGNode[io.In[_In], io.Out[_In]]):
    if TYPE_CHECKING:

        def __getattr__(self, key) -> Any: ...

        @overload
        def __getitem__(
            self: InputNode[Mapping[_K, _V]], key: _K
        ) -> InputAttributeNode[io.In[_In], _V]: ...

        @overload
        def __getitem__(
            self: InputNode[Sequence[_V]], key: int
        ) -> InputAttributeNode[io.In[_In], _V]: ...

        @overload
        def __getitem__(self, key) -> InputAttributeNode[io.In[_In], Any]: ...

        def __getitem__(self, key) -> Any: ...

        def __enter__(self) -> Self: ...

        @overload
        def execute(
            self: DAGNode[io.NoIn, Any],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _In: ...

        @overload
        def execute(
            self: DAGNode[io.In[_In], Any],
            __in: ExecArg[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _In: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> _In: ...


MoArg = DAGNode[_InT, io.Out[_Out]]


class MultiOutputNode(DAGNode[_InT, _OutT]):
    @overload
    def __new__(
        cls,
        args: tuple[MoArg[_InT, _O0]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[MoArg[_InT, _O0], MoArg[_InT, _O1]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[MoArg[_InT, _O0], MoArg[_InT, _O1], MoArg[_InT, _O2]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1, _O2]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0], MoArg[_InT, _O1], MoArg[_InT, _O2], MoArg[_InT, _O3]
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1, _O2, _O3]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0],
            MoArg[_InT, _O1],
            MoArg[_InT, _O2],
            MoArg[_InT, _O3],
            MoArg[_InT, _O4],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1, _O2, _O3, _O4]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0],
            MoArg[_InT, _O1],
            MoArg[_InT, _O2],
            MoArg[_InT, _O3],
            MoArg[_InT, _O4],
            MoArg[_InT, _O5],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1, _O2, _O3, _O4, _O5]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0],
            MoArg[_InT, _O1],
            MoArg[_InT, _O2],
            MoArg[_InT, _O3],
            MoArg[_InT, _O4],
            MoArg[_InT, _O5],
            MoArg[_InT, _O6],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0],
            MoArg[_InT, _O1],
            MoArg[_InT, _O2],
            MoArg[_InT, _O3],
            MoArg[_InT, _O4],
            MoArg[_InT, _O5],
            MoArg[_InT, _O6],
            MoArg[_InT, _O7],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[_InT, io.Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0],
            MoArg[_InT, _O1],
            MoArg[_InT, _O2],
            MoArg[_InT, _O3],
            MoArg[_InT, _O4],
            MoArg[_InT, _O5],
            MoArg[_InT, _O6],
            MoArg[_InT, _O7],
            MoArg[_InT, _O8],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _InT, io.Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7, _O8]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            MoArg[_InT, _O0],
            MoArg[_InT, _O1],
            MoArg[_InT, _O2],
            MoArg[_InT, _O3],
            MoArg[_InT, _O4],
            MoArg[_InT, _O5],
            MoArg[_InT, _O6],
            MoArg[_InT, _O7],
            MoArg[_InT, _O8],
            MoArg[_InT, _O9],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        _InT, io.Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7, _O8, _O9]
    ]: ...

    def __new__(cls, args, other_args_to_resolve=None) -> MultiOutputNode:
        return ray_dag.MultiOutputNode(args, other_args_to_resolve)  # type: ignore[return-value]

    if TYPE_CHECKING:

        @overload
        def execute(
            self: DAGNode[io.In[_In] | io.NoIn, io.Outs[Unpack[_Ts]]],
            __in: ExecArg[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[Unpack[_Ts]]: ...

        @overload
        def execute(
            self: DAGNode[Any, io.Outs[Unpack[_Ts]]],
            *args,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[Unpack[_Ts]]: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> Any: ...
