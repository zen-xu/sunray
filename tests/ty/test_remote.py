from __future__ import annotations

from collections.abc import Callable
from collections.abc import Generator
from typing import Any
from typing import Protocol

from typing_extensions import assert_type

import sunray

from sunray import ObjectRef
from sunray import remote
from sunray._internal import io
from sunray._internal.remote import RemoteFunction
from sunray._internal.remote import RemoteFunctionWrapper
from sunray._internal.remote import RemoteStream


class _IntFunc(Protocol):
    def __call__(self, v: int) -> int: ...


def case_func_without_args() -> None:
    @remote
    def f() -> int:
        return 1

    assert_type(f, RemoteFunction[Callable[[], int], int])


def case_func_with_args() -> None:
    @remote
    def f(v: int) -> int:
        return v

    assert_type(f, RemoteFunction[_IntFunc, int])


def case_remote_decorator_with_args() -> None:
    @remote(num_cpus=1)
    def f(v: int) -> int:
        return v

    assert_type(f, RemoteFunction[_IntFunc, int])


def case_remote_call() -> None:
    @remote
    def f() -> int:
        return 1

    assert_type(f.remote(), ObjectRef[int])


def case_remote_call_mismatch_args() -> None:
    @remote
    def f(v1: int, v2: int, v3: int, v4: int, v5: int) -> int:
        return 1

    f.remote(1, 2)  # ty: ignore[no-matching-overload]


def case_remote_with_default_args() -> None:
    @remote
    def f(v1: int, v2: int = 2) -> int:
        return 1

    f.remote(1)


def case_remote_with_object_ref(v: ObjectRef[int]) -> None:
    @remote
    def f(v1: int) -> int:
        return v1

    # ty cannot resolve `ObjectRef[int]` against the `int | ObjectRef[int]`
    # overload union, so a valid object-ref argument is reported as an error.
    f.remote(v)  # ty: ignore[no-matching-overload]


def case_remote_with_invalid_object_ref(v: ObjectRef[str]) -> None:
    @remote
    def f(v1: int) -> int:
        return v1

    f.remote(v)  # ty: ignore[no-matching-overload]


def case_invoke_options() -> None:
    @remote
    def f() -> int:
        return 1

    assert_type(
        f.options(num_cpus=1),
        RemoteFunctionWrapper[Callable[[], int], io.Out[ObjectRef[int]]],
    )


def case_default_return_tuple() -> None:
    @remote
    def f() -> tuple[int, int]:
        return 1, 2

    assert_type(f.remote(), ObjectRef[tuple[int, int]])


def case_unpack_return_tuple() -> None:
    @remote
    def f() -> tuple[int, int]:
        return 1, 2

    assert_type(
        f.options(unpack=True).remote(),
        tuple[ObjectRef[int], ObjectRef[int]],
    )


def case_disable_unpack_return_tuple() -> None:
    @remote
    def f() -> tuple[int, int]:
        return 1, 2

    assert_type(f.options(unpack=False).remote(), ObjectRef[tuple[int, int]])


def case_stream() -> None:
    @remote
    def stream() -> Generator[int, None, None]:
        yield from range(10)

    assert_type(
        stream,
        RemoteStream[Callable[[], Generator[int, Any, Any]], int],
    )
    stream_gen = stream.remote()
    assert_type(stream_gen, sunray.ObjectRefGenerator[int])
    assert_type(next(stream_gen), ObjectRef[int])


def case_stream_tuple_unsupported_unpack() -> None:
    @remote
    def stream() -> Generator[tuple[int, int], None, None]:
        for i in range(10):
            yield i, i + 1

    # ty (unlike mypy) does not reject the unexpected `unpack` keyword against
    # `Unpack[FunctionRemoteOptions]`, so this type-checks cleanly.
    stream.options(unpack=True).remote()
