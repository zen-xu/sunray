# mypy: disable-error-code="override"

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
_Ins = TypeVarTuple("_Ins")
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


ExecArg = Union[_T, "sunray.ObjectRef[_T]"]


class Ins(Generic[Unpack[_Ins]]): ...


class Outs(Generic[Unpack[_Outs]]): ...


_InsT = TypeVar("_InsT", bound=Ins)
_OutsT = TypeVar("_OutsT", bound=Outs)


class DAGNode(Generic[_InsT, _OutsT]): ...


class FunctionNode(ray_dag.FunctionNode, DAGNode[_InsT, Outs[_T]]):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: FunctionNode[Ins[()], Any],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        @overload
        def execute(
            self: FunctionNode[Ins[_In], Any],
            __arg0: ExecArg[_In],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> _T: ...


class StreamNode(
    ray_dag.FunctionNode, DAGNode[_InsT, Outs["sunray.ObjectRefGenerator[_T]"]]
):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: StreamNode[Ins[()], Any],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_T]: ...

        @overload
        def execute(
            self: StreamNode[Ins[_In], Any],
            __arg0: ExecArg[_In],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_T]: ...

        def execute(
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> sunray.ObjectRefGenerator[_T]: ...


_ActorT = TypeVar("_ActorT")


class ClassNode(ray_dag.ClassNode, DAGNode[_InsT, Outs[sunray.Actor[_ActorT]]]):
    @property
    def methods(self) -> type[_ActorT]:
        return self  # type: ignore[return-value]

    @overload
    def execute(
        self: ClassNode[Ins[()], Any],
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> sunray.Actor[_ActorT]: ...

    @overload
    def execute(
        self: ClassNode[Ins[_In], Any],
        __arg0: ExecArg[_In],
        _ray_cache_refs: bool = False,
        **kwargs,
    ) -> sunray.Actor[_ActorT]: ...

    def execute(
        self, *args, _ray_cache_refs: bool = False, **kwargs
    ) -> sunray.Actor[_ActorT]:
        handler = super().execute(*args, _ray_cache_refs=_ray_cache_refs, **kwargs)
        return sunray.Actor(handler)  # type: ignore[return-value, arg-type]


class ClassMethodNode(ray_dag.ClassMethodNode, DAGNode[_InsT, Outs[_T]]):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: ClassMethodNode[Ins[()], Any],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        @overload
        def execute(
            self: ClassMethodNode[Ins[_In], Any],
            __arg0: ExecArg[_In],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> _T: ...


class ClassStreamMethodNode(
    ray_dag.ClassMethodNode, DAGNode[_InsT, Outs["sunray.ObjectRefGenerator[_T]"]]
):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: ClassStreamMethodNode[Ins[()], Any],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_T]: ...

        @overload
        def execute(
            self: ClassStreamMethodNode[Ins[_In], Any],
            __arg0: ExecArg[_In],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRefGenerator[_T]: ...

        def execute(
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> sunray.ObjectRefGenerator[_T]: ...


class InputAttributeNode(  # type: ignore[misc]
    ray_dag.InputAttributeNode, DAGNode[_InsT, Outs[_T]]
):
    if TYPE_CHECKING:

        @overload
        def execute(
            self: InputAttributeNode[Ins[()], Any],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        @overload
        def execute(
            self: InputAttributeNode[Ins[_In], Any],
            __arg0: ExecArg[_In],
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> _T: ...

        def execute(self, *args, _ray_cache_refs: bool = False, **kwargs) -> _T: ...


_AttrT = TypeVar("_AttrT")
_GetItemT = TypeVar("_GetItemT")


_Ts = TypeVarTuple("_Ts")


class InputNode(
    ray_dag.InputNode,
    DAGNode[Ins[_In], Outs[_In]],
    Generic[_In, Unpack[_Ts]],
):
    if TYPE_CHECKING:

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
        def __getattr__(
            self: InputNode[_In], key: str
        ) -> InputAttributeNode[Ins[_In], Outs[Any]]: ...

        @overload
        def __getattr__(
            self: InputNode[_In, _AttrT], key: str
        ) -> InputAttributeNode[Ins[_In], Outs[_AttrT]]: ...

        @overload
        def __getattr__(
            self: InputNode[_In, _AttrT, Any], key: str
        ) -> InputAttributeNode[Ins[_In], Outs[_AttrT]]: ...

        def __getattr__(self, key): ...  # type: ignore[overload]

        def __getitem__(
            self: InputNode[_In, _AttrT, _GetItemT], key: int | str
        ) -> InputAttributeNode[Ins[_In], Outs[_GetItemT]]: ...

        def __enter__(self) -> Self: ...


OutputArg = Union[DAGNode[Ins[_In], Outs[_Out]], _In]


class MultiOutputNode(DAGNode[_InsT, _OutsT]):
    @overload
    def __new__(
        cls,
        args: tuple[DAGNode[Ins[()], Outs[_Out0]]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[()], Outs[_Out0]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[()], Outs[_Out0, _Out1]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2, _Out3]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
            DAGNode[Ins[()], Outs[_Out4]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
            DAGNode[Ins[()], Outs[_Out4]],
            DAGNode[Ins[()], Outs[_Out5]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
            DAGNode[Ins[()], Outs[_Out4]],
            DAGNode[Ins[()], Outs[_Out5]],
            DAGNode[Ins[()], Outs[_Out6]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
            DAGNode[Ins[()], Outs[_Out4]],
            DAGNode[Ins[()], Outs[_Out5]],
            DAGNode[Ins[()], Outs[_Out6]],
            DAGNode[Ins[()], Outs[_Out7]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
            DAGNode[Ins[()], Outs[_Out4]],
            DAGNode[Ins[()], Outs[_Out5]],
            DAGNode[Ins[()], Outs[_Out6]],
            DAGNode[Ins[()], Outs[_Out7]],
            DAGNode[Ins[()], Outs[_Out8]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[()], Outs[_Out0]],
            DAGNode[Ins[()], Outs[_Out1]],
            DAGNode[Ins[()], Outs[_Out2]],
            DAGNode[Ins[()], Outs[_Out3]],
            DAGNode[Ins[()], Outs[_Out4]],
            DAGNode[Ins[()], Outs[_Out5]],
            DAGNode[Ins[()], Outs[_Out6]],
            DAGNode[Ins[()], Outs[_Out7]],
            DAGNode[Ins[()], Outs[_Out8]],
            DAGNode[Ins[()], Outs[_Out9]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[()],
        Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9],
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[DAGNode[Ins[_In], Outs[_Out0]]],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[_In], Outs[_Out0]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[_In], Outs[_Out0, _Out1]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
            DAGNode[Ins[_In], Outs[_Out4]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
            DAGNode[Ins[_In], Outs[_Out4]],
            DAGNode[Ins[_In], Outs[_Out5]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
            DAGNode[Ins[_In], Outs[_Out4]],
            DAGNode[Ins[_In], Outs[_Out5]],
            DAGNode[Ins[_In], Outs[_Out6]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
            DAGNode[Ins[_In], Outs[_Out4]],
            DAGNode[Ins[_In], Outs[_Out5]],
            DAGNode[Ins[_In], Outs[_Out6]],
            DAGNode[Ins[_In], Outs[_Out7]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
            DAGNode[Ins[_In], Outs[_Out4]],
            DAGNode[Ins[_In], Outs[_Out5]],
            DAGNode[Ins[_In], Outs[_Out6]],
            DAGNode[Ins[_In], Outs[_Out7]],
            DAGNode[Ins[_In], Outs[_Out8]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8]
    ]: ...

    @overload
    def __new__(
        cls,
        args: tuple[
            DAGNode[Ins[_In], Outs[_Out0]],
            DAGNode[Ins[_In], Outs[_Out1]],
            DAGNode[Ins[_In], Outs[_Out2]],
            DAGNode[Ins[_In], Outs[_Out3]],
            DAGNode[Ins[_In], Outs[_Out4]],
            DAGNode[Ins[_In], Outs[_Out5]],
            DAGNode[Ins[_In], Outs[_Out6]],
            DAGNode[Ins[_In], Outs[_Out7]],
            DAGNode[Ins[_In], Outs[_Out8]],
            DAGNode[Ins[_In], Outs[_Out9]],
        ],
        other_args_to_resolve: dict[str, Any] | None = None,
    ) -> MultiOutputNode[
        Ins[_In],
        Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9],
    ]: ...

    def __new__(cls, args, other_args_to_resolve=None) -> MultiOutputNode:
        return ray_dag.MultiOutputNode(args, other_args_to_resolve)  # type: ignore[return-value]

    if TYPE_CHECKING:

        @overload
        def execute(
            self: MultiOutputNode[Ins[()], Outs[_Out0]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[()], Outs[_Out0, _Out1]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2, _Out3]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4]],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3, _Out4]]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]
            ],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]
            ],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[()], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7]
            ],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[()],
                Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8],
            ],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[()],
                Outs[
                    _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9
                ],
            ],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[
            tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9]
        ]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[_In], Outs[_Out0]],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[_In], Outs[_Out0, _Out1]],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2]],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3]],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3]]: ...

        @overload
        def execute(
            self: MultiOutputNode[Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4]],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3, _Out4]]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]
            ],
            __arg0: _In | sunray.ObjectRef[_In],
            *,
            _ray_cache_refs: bool = False,
            **kwargs,
        ) -> sunray.ObjectRef[tuple[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5]]: ...

        @overload
        def execute(
            self: MultiOutputNode[
                Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6]
            ],
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
                Ins[_In], Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7]
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
                Ins[_In],
                Outs[_Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8],
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
                Ins[_In],
                Outs[
                    _Out0, _Out1, _Out2, _Out3, _Out4, _Out5, _Out6, _Out7, _Out8, _Out9
                ],
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
    _T,
    "sunray.ObjectRef[_T]",
    "DAGNode[_InsT, Outs[_T]]",
    "DAGNode[_InsT, Outs[sunray.ObjectRef[_T]]]",
]


class BindCallable(Generic[_Callable_co, _NodeT, _Out]):
    # ============ Stream Node ============
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        __arg9: BindArg[_T9, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        __arg9: BindArg[_T9, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> StreamNode[Ins[_In], _Out]: ...

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

    # # ============ Function Node ============
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        __arg9: BindArg[_T9, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        __arg9: BindArg[_T9, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> FunctionNode[Ins[_In], _Out]: ...

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

    # # ============ Class Node ============
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        __arg9: BindArg[_T9, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[()], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        __arg9: BindArg[_T9, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            ClassNode,
            _ActorT,
        ],
        __arg0: BindArg[_T0, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Ins[_In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[_P, Any],
            ClassNode,
            _ActorT,
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassNode[Any, _ActorT]: ...

    # # ============ Class Method Node ============
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        __arg9: BindArg[_T9, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        __arg9: BindArg[_T9, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassMethodNode[Ins[_In], _Out]: ...

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

    # # ============ Class Stream Method Node ============
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        __arg9: BindArg[_T9, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...
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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        __arg8: BindArg[_T8, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        __arg7: BindArg[_T7, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        __arg6: BindArg[_T6, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        __arg5: BindArg[_T5, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        __arg4: BindArg[_T4, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        __arg3: BindArg[_T3, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        __arg2: BindArg[_T2, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        __arg1: BindArg[_T1, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[()]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[()], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        __arg9: BindArg[_T9, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        __arg8: BindArg[_T8, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        __arg7: BindArg[_T7, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        __arg6: BindArg[_T6, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        __arg5: BindArg[_T5, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        __arg4: BindArg[_T4, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        __arg3: BindArg[_T3, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        __arg2: BindArg[_T2, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        __arg1: BindArg[_T1, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
        __arg0: BindArg[_T0, Ins[_In]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> ClassStreamMethodNode[Ins[_In], _Out]: ...

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
