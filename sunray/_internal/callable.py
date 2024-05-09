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
from typing_extensions import TypeVarTuple


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
_Ts = TypeVarTuple("_Ts")

RemoteArg = Union[_T, "sunray.ObjectRef[_T]"]


_Callable_co = TypeVar("_Callable_co", covariant=True, bound=Callable)
_RemoteRet = TypeVar("_RemoteRet", covariant=True)


class RemoteCallable(Generic[_Callable_co, _RemoteRet]):
    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _P],
                Any,
            ],
            Any,
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
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _P],
                Any,
            ],
            Any,
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
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _P],
                Any,
            ],
            Any,
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
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _P],
                Any,
            ],
            Any,
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
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _T5, _P],
                Any,
            ],
            Any,
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        __arg5: RemoteArg[_T5],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _T4, _P],
                Any,
            ],
            Any,
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        __arg4: RemoteArg[_T4],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _T3, _P],
                Any,
            ],
            Any,
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        __arg3: RemoteArg[_T3],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _T2, _P],
                Any,
            ],
            Any,
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        __arg2: RemoteArg[_T2],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _T1, _P],
                Any,
            ],
            Any,
        ],
        __arg0: RemoteArg[_T0],
        __arg1: RemoteArg[_T1],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[
            Callable[
                Concatenate[_T0, _P],
                Any,
            ],
            Any,
        ],
        __arg0: RemoteArg[_T0],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    @overload
    def __call__(
        self: RemoteCallable[Callable[_P, Any], Any],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _RemoteRet: ...

    def __call__(self, *args: Any, **kwds: Any) -> Any: ...
