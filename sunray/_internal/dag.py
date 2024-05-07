from __future__ import annotations

from typing import TYPE_CHECKING

from ray import dag as ray_dag


if TYPE_CHECKING:
    from typing import Any
    from typing import Callable
    from typing import Generic
    from typing import TypeVar
    from typing import Union
    from typing import overload

    from typing_extensions import Concatenate
    from typing_extensions import ParamSpec

    import sunray

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
    _NodeRet = TypeVar("_NodeRet")

    _Callable_co = TypeVar("_Callable_co", covariant=True, bound=Callable)
    BindArg = Union[
        _T, sunray.ObjectRef[_T], "DAGNode[_T]", "DAGNode[sunray.ObjectRef[_T]]"
    ]

    class DAGNode(ray_dag.DAGNode, Generic[_NodeRet]):
        def execute(  # type: ignore[override]
            self, *args, _ray_cache_refs: bool = False, **kwargs
        ) -> _NodeRet: ...

    class FunctionNode(ray_dag.FunctionNode, DAGNode[sunray.ObjectRef[_NodeRet]]): ...

    class StreamNode(ray_dag.FunctionNode, DAGNode[ObjectRefGenerator[_NodeRet]]): ...

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
