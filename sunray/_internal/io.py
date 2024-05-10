from __future__ import annotations

from typing import Generic
from typing import TypeVar

from typing_extensions import TypeVarTuple
from typing_extensions import Unpack


_In = TypeVar("_In", covariant=True)
_Out = TypeVar("_Out", covariant=True)
_YieldT = TypeVar("_YieldT", covariant=True)
_ActorT = TypeVar("_ActorT", covariant=True)
_Outs = TypeVarTuple("_Outs")


class BaseIn: ...


class In(BaseIn, Generic[_In]): ...


class NoIn(BaseIn): ...


class BaseOut: ...


class Out(BaseOut, Generic[_Out]): ...


class Outs(BaseOut, Generic[Unpack[_Outs]]): ...


class Yield(BaseOut, Generic[_YieldT]): ...


class Actor(BaseOut, Generic[_ActorT]): ...
