# mypy: disable-error-code="override"

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

from ray import dag as ray_dag
from typing_extensions import ParamSpec
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

_I = TypeVar("_I")
_O = TypeVar("_O")
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
_Os = TypeVarTuple("_Os")


class In(Generic[_I]): ...


class NoInput(In): ...


class _BaseOut: ...


class Out(_BaseOut, Generic[_O]): ...


class Outs(_BaseOut, Generic[Unpack[_Os]]): ...


class Yield(_BaseOut, Generic[_O]): ...


class Actor(_BaseOut, Generic[_T]): ...


_InT = TypeVar("_InT", bound=In, covariant=True)
_OutT = TypeVar("_OutT", bound=_BaseOut, covariant=True)
_OutsT = TypeVar("_OutsT", bound=Outs, covariant=True)

ExecArg = Union[_T, "sunray.ObjectRef[_T]", "DAGNode[Any, Out[_T]]"]


class DAGNode(Generic[_InT, _OutT]): ...


class _FunctionLikeNode(DAGNode[_InT, _OutT]):
    if TYPE_CHECKING:
        # ==== without input ====
        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[sunray.ObjectRef[_O0]]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[sunray.ObjectRef[_O0], sunray.ObjectRef[_O1]]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0], sunray.ObjectRef[_O1], sunray.ObjectRef[_O2]
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2, _O3]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2, _O3, _O4]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2, _O3, _O4, _O5]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
            sunray.ObjectRef[_O7],
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7, _O8]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
            sunray.ObjectRef[_O7],
            sunray.ObjectRef[_O8],
        ]: ...

        @overload
        def execute(
            self: DAGNode[
                NoInput, Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7, _O8, _O9]
            ],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
            sunray.ObjectRef[_O7],
            sunray.ObjectRef[_O8],
            sunray.ObjectRef[_O9],
        ]: ...

        @overload
        def execute(
            self: DAGNode[NoInput, Out[_O]],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[_O]: ...

        # ==== with input ====

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[sunray.ObjectRef[_O0]]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[sunray.ObjectRef[_O0], sunray.ObjectRef[_O1]]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0], sunray.ObjectRef[_O1], sunray.ObjectRef[_O2]
        ]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2, _O3]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
        ]: ...
        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2, _O3, _O4]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
        ]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2, _O3, _O4, _O5]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
        ]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
        ]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
            sunray.ObjectRef[_O7],
        ]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7, _O8]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
            sunray.ObjectRef[_O7],
            sunray.ObjectRef[_O8],
        ]: ...

        @overload
        def execute(
            self: DAGNode[
                In[_I], Outs[_O0, _O1, _O2, _O3, _O4, _O5, _O6, _O7, _O8, _O9]
            ],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> tuple[
            sunray.ObjectRef[_O0],
            sunray.ObjectRef[_O1],
            sunray.ObjectRef[_O2],
            sunray.ObjectRef[_O3],
            sunray.ObjectRef[_O4],
            sunray.ObjectRef[_O5],
            sunray.ObjectRef[_O6],
            sunray.ObjectRef[_O7],
            sunray.ObjectRef[_O8],
            sunray.ObjectRef[_O9],
        ]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Out[_O]],
            __arg: ExecArg[_I],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[_O]: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> Any: ...


class FunctionNode(  # type: ignore[misc]
    _FunctionLikeNode[_InT, _OutT],
    ray_dag.FunctionNode,
): ...


class StreamNode(ray_dag.FunctionNode, DAGNode[_InT, Yield[_O]]):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: DAGNode[NoInput, Any],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_O]: ...

        @overload
        def execute(
            self: DAGNode[In[_I], Any],
            __arg0: ExecArg[_I],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_O]: ...

        def execute(
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> sunray.ObjectRefGenerator[_O]: ...


_ActorT = TypeVar("_ActorT", bound=sunray.ActorMixin)


class ClassNode(ray_dag.ClassNode, DAGNode[_InT, Actor[_ActorT]]):
    @property
    def methods(self) -> type[_ActorT]:
        return self  # type: ignore[return-value]

    @overload
    def execute(
        self: DAGNode[NoInput, Any],
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> sunray.Actor[_ActorT]: ...

    @overload
    def execute(
        self: DAGNode[In[_I], Any],
        __arg0: ExecArg[_I],
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> sunray.Actor[_ActorT]: ...

    def execute(
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.Actor[_ActorT]:
        handler = super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)
        return sunray.Actor(handler)  # type: ignore[return-value, arg-type]


class ClassMethodNode(  # type: ignore[misc]
    _FunctionLikeNode[_InT, _OutT],
    ray_dag.ClassMethodNode,
): ...
