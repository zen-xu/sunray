from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Callable
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

from typing_extensions import Concatenate
from typing_extensions import ParamSpec

from . import dag
from . import io


if TYPE_CHECKING:
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

RemoteArg = Union[_T, "sunray.ObjectRef[_T]"]


_Callable_co = TypeVar("_Callable_co", covariant=True, bound=Callable)
_RemoteRet = TypeVar("_RemoteRet", covariant=True, bound=io.Out)


class RemoteCallable(Generic[_Callable_co, _RemoteRet]):
    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        __arg5: RemoteArg[_T5],
        __arg6: RemoteArg[_T6],
        __arg7: RemoteArg[_T7],
        __arg8: RemoteArg[_T8],
        __arg9: RemoteArg[_T9],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        __arg5: RemoteArg[_T5],
        __arg6: RemoteArg[_T6],
        __arg7: RemoteArg[_T7],
        __arg8: RemoteArg[_T8],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        __arg5: RemoteArg[_T5],
        __arg6: RemoteArg[_T6],
        __arg7: RemoteArg[_T7],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        __arg5: RemoteArg[_T5],
        __arg6: RemoteArg[_T6],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        __arg5: RemoteArg[_T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            io.Out[_T],
        ],
        __arg0: RemoteArg[_T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[_P, Any],
            io.Out[_T],
        ],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _T: ...

    def __call__(self, *args: Any, **kwds: Any) -> Any: ...


_BindRet = TypeVar("_BindRet", covariant=True)
BindArg = Union[
    _T,
    "sunray.ObjectRef[_T]",
    "dag.DAGNode[dag._InT, io.Out[_T]]",
]


class BindCallable(Generic[_Callable_co, _BindRet]): ...


class FunctionBindCallable(BindCallable[_Callable_co, dag._OutT]):
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        __arg9: BindArg[_T9, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        __arg9: BindArg[_T9, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[Callable[_P, Any], Any],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.FunctionNode[io.NoIn, dag._OutT]: ...

    def __call__(self, *args, **kwargs) -> Any: ...


class ClassMethodBindCallable(BindCallable[_Callable_co, dag._OutT]):
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        __arg9: BindArg[_T9, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        __arg9: BindArg[_T9, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.In[io._In], dag._OutT]: ...

    @overload
    def __call__(
        self: BindCallable[Callable[_P, Any], Any],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassMethodNode[io.NoIn, dag._OutT]: ...

    def __call__(self, *args, **kwargs) -> Any: ...


_YieldT = TypeVar("_YieldT")


class StreamBindCallable(BindCallable[_Callable_co, _YieldT]):
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        __arg9: BindArg[_T9, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        __arg9: BindArg[_T9, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[Callable[_P, Any], Any],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.StreamNode[io.NoIn, _YieldT]: ...

    def __call__(self, *args, **kwargs) -> Any: ...


class ClassStreamBindCallable(BindCallable[_Callable_co, _YieldT]):
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        __arg9: BindArg[_T9, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        __arg9: BindArg[_T9, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.In[io._In], _YieldT]: ...

    @overload
    def __call__(
        self: BindCallable[Callable[_P, Any], Any],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassStreamNode[io.NoIn, _YieldT]: ...

    def __call__(self, *args, **kwargs) -> Any: ...


_ActorT = TypeVar("_ActorT")


class ClassBindCallable(BindCallable[_Callable_co, _ActorT]):
    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        __arg9: BindArg[_T9, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        __arg8: BindArg[_T8, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        __arg7: BindArg[_T7, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        __arg6: BindArg[_T6, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        __arg5: BindArg[_T5, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        __arg4: BindArg[_T4, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        __arg3: BindArg[_T3, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        __arg2: BindArg[_T2, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        __arg1: BindArg[_T1, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        __arg9: BindArg[_T9, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        __arg8: BindArg[_T8, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        __arg7: BindArg[_T7, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        __arg6: BindArg[_T6, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        __arg5: BindArg[_T5, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        __arg4: BindArg[_T4, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        __arg3: BindArg[_T3, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        __arg2: BindArg[_T2, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        __arg1: BindArg[_T1, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: BindArg[_T0, io.In[io._In] | io.NoIn],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.In[io._In], _ActorT]: ...

    @overload
    def __call__(
        self: BindCallable[Callable[_P, Any], Any],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> dag.ClassNode[io.NoIn, _ActorT]: ...

    def __call__(self, *args, **kwargs) -> Any: ...
