from __future__ import annotations

from collections.abc import Awaitable
from collections.abc import Callable
from collections.abc import Generator

from typing_extensions import assert_type

import sunray

from sunray import ActorMixin
from sunray import remote_method
from sunray._internal import actor_mixin
from sunray._internal import io
from sunray._internal.callable import RemoteCallable


def case_without_args__new_actor() -> None:
    class Actor(ActorMixin): ...

    assert_type(Actor.new_actor(), actor_mixin.ActorClass[[], Actor])


def case_without_args__remote() -> None:
    class Actor(ActorMixin): ...

    assert_type(
        Actor.new_actor().remote,
        RemoteCallable[Callable[[], Actor], io.Out[actor_mixin.Actor[Actor]]],
    )


def case_without_args__remote_call() -> None:
    class Actor(ActorMixin): ...

    assert_type(Actor.new_actor().remote(), actor_mixin.Actor[Actor])


def case_without_args__options_call() -> None:
    class Actor(ActorMixin): ...

    assert_type(
        Actor.new_actor().options(num_cpus=1),
        actor_mixin.ActorClassWrapper[[], Actor],
    )


def case_with_args__new_actor() -> None:
    class Actor(ActorMixin):
        def __init__(self, a: int, b: str, /): ...

    assert_type(Actor.new_actor(), actor_mixin.ActorClass[[int, str], Actor])


def case_with_args__remote() -> None:
    class Actor(ActorMixin):
        def __init__(self, a: int, b: str, /): ...

    assert_type(
        Actor.new_actor().remote,
        RemoteCallable[Callable[[int, str], Actor], io.Out[actor_mixin.Actor[Actor]]],
    )


def case_with_args__remote_call() -> None:
    class Actor(ActorMixin):
        def __init__(self, a: int, b: str, /): ...

    assert_type(Actor.new_actor().remote(1, "a"), actor_mixin.Actor[Actor])


def case_with_args__remote_call_missing_args() -> None:
    class Actor(ActorMixin):
        def __init__(self, a: int, b: str, /): ...

    Actor.new_actor().remote()  # ty: ignore[no-matching-overload]


def case_with_args__options_call() -> None:
    class Actor(ActorMixin):
        def __init__(self, a: int, b: str, /): ...

    assert_type(
        Actor.new_actor().options(num_cpus=1),
        actor_mixin.ActorClassWrapper[[int, str], Actor],
    )


def case_actor__methods() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self) -> str:
            return "hello"

    assert_type(Actor.new_actor().remote().methods, type[Actor])


def case_remote_method_without_args() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self) -> str:
            return "hello"

    assert_type(
        Actor.new_actor().remote().methods.echo,
        actor_mixin.Method[[], str],
    )


def case_remote_method_without_args__options_call() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self) -> str:
            return "hello"

    assert_type(
        Actor.new_actor().remote().methods.echo.options(concurrency_group="test"),
        actor_mixin.MethodWrapper[[], str, io.Out[sunray.ObjectRef[str]]],
    )


def case_remote_method_without_args__remote() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self) -> str:
            return "hello"

    assert_type(
        Actor.new_actor().remote().methods.echo.remote,
        RemoteCallable[Callable[[], str], io.Out[sunray.ObjectRef[str]]],
    )


def case_remote_method_without_args__remote_call() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self) -> str:
            return "hello"

    assert_type(
        Actor.new_actor().remote().methods.echo.remote(),
        sunray.ObjectRef[str],
    )


def case_remote_method_with_args() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self, msg: str, /) -> str:
            return msg

    assert_type(
        Actor.new_actor().remote().methods.echo,
        actor_mixin.Method[[str], str],
    )


def case_remote_method_with_args__options_call() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self, msg: str, /) -> str:
            return "hello"

    assert_type(
        Actor.new_actor().remote().methods.echo.options(concurrency_group="test"),
        actor_mixin.MethodWrapper[[str], str, io.Out[sunray.ObjectRef[str]]],
    )


def case_remote_method_with_args__remote() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self, msg: str, /) -> str:
            return msg

    assert_type(
        Actor.new_actor().remote().methods.echo.remote,
        RemoteCallable[Callable[[str], str], io.Out[sunray.ObjectRef[str]]],
    )


def case_remote_method_with_args__remote_call() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self, msg: str, /) -> str:
            return msg

    assert_type(
        Actor.new_actor().remote().methods.echo.remote("hello"),
        sunray.ObjectRef[str],
    )


def case_remote_method_with_args__remote_call_missing_args() -> None:
    class Actor(ActorMixin):
        @remote_method
        def echo(self, msg: str, /) -> str:
            return msg

    Actor.new_actor().remote().methods.echo.remote()  # ty: ignore[no-matching-overload]


def case_async_method__remote() -> None:
    class Actor(ActorMixin):
        @remote_method
        async def echo(self, msg: str, /) -> str:
            return msg

    assert_type(
        Actor.new_actor().remote().methods.echo.remote,
        RemoteCallable[Callable[[str], Awaitable[str]], io.Out[sunray.ObjectRef[str]]],
    )


def case_async_method__remote_call() -> None:
    class Actor(ActorMixin):
        @remote_method
        async def echo(self, msg: str, /) -> str:
            return msg

    assert_type(
        Actor.new_actor().remote().methods.echo.remote("abc"),
        sunray.ObjectRef[str],
    )


def case_stream() -> None:
    class Actor(ActorMixin):
        @remote_method
        def g(self) -> Generator[int, None, None]:
            yield from range(10)

    obj_ref_generator = Actor.new_actor().remote().methods.g.remote()
    assert_type(obj_ref_generator, sunray.ObjectRefGenerator[int])
    assert_type(next(obj_ref_generator), sunray.ObjectRef[int])


def case_async_stream() -> None:
    from collections.abc import AsyncGenerator

    class Actor(ActorMixin):
        @remote_method
        async def g(self) -> AsyncGenerator[int, None]:
            for i in range(10):
                yield i

    obj_ref_generator = Actor.new_actor().remote().methods.g.remote()
    assert_type(obj_ref_generator, sunray.ObjectRefGenerator[int])
    assert_type(next(obj_ref_generator), sunray.ObjectRef[int])


def case_default_tuple_returns() -> None:
    class Actor(ActorMixin):
        @remote_method
        def f(self) -> tuple[int, str]:
            return 1, "A"

    assert_type(
        Actor.new_actor().remote().methods.f.remote(),
        sunray.ObjectRef[tuple[int, str]],
    )


def case_unpack_tuple_returns() -> None:
    class Actor(ActorMixin):
        @remote_method
        def f(self) -> tuple[int, str]:
            return 1, "A"

    assert_type(
        Actor.new_actor().remote().methods.f.options(unpack=True).remote(),
        tuple[sunray.ObjectRef[int], sunray.ObjectRef[str]],
    )


def case_do_not_unpack_tuple_returns() -> None:
    class Actor(ActorMixin):
        @remote_method
        def f(self) -> tuple[int, str]:
            return 1, "A"

    assert_type(
        Actor.new_actor().remote().methods.f.options(unpack=False).remote(),
        sunray.ObjectRef[tuple[int, str]],
    )


def case_actor_mixin_class_args() -> None:
    class Dummy: ...

    obj = Dummy()

    class A1(ActorMixin, num_cpus=obj): ...  # ty: ignore[invalid-argument-type]

    class A2(ActorMixin, num_gpus=obj): ...  # ty: ignore[invalid-argument-type]

    class A3(ActorMixin, resources=obj): ...  # ty: ignore[invalid-argument-type]

    class A4(ActorMixin, accelerator_type=obj): ...  # ty: ignore[invalid-argument-type]

    class A5(ActorMixin, memory=obj): ...  # ty: ignore[invalid-argument-type]

    class A6(
        ActorMixin, object_store_memory=obj
    ): ...  # ty: ignore[invalid-argument-type]

    class A7(ActorMixin, max_restarts=obj): ...  # ty: ignore[invalid-argument-type]

    class A8(ActorMixin, max_task_retries=obj): ...  # ty: ignore[invalid-argument-type]

    class A9(
        ActorMixin, max_pending_calls=obj
    ): ...  # ty: ignore[invalid-argument-type]

    class A10(ActorMixin, max_concurrency=obj): ...  # ty: ignore[invalid-argument-type]

    class A11(ActorMixin, name=obj): ...  # ty: ignore[invalid-argument-type]

    class A12(ActorMixin, namespace=obj): ...  # ty: ignore[invalid-argument-type]

    class A13(ActorMixin, lifetime=obj): ...  # ty: ignore[invalid-argument-type]

    class A14(ActorMixin, runtime_env=obj): ...  # ty: ignore[invalid-argument-type]

    class A15(
        ActorMixin, concurrency_groups=obj
    ): ...  # ty: ignore[invalid-argument-type]

    class A16(
        ActorMixin, scheduling_strategy=obj
    ): ...  # ty: ignore[invalid-argument-type]


def case_actor_mixin_class_with_invalid_args() -> None:
    class Actor(ActorMixin, num_cpu=1): ...


def case_remote_method_with_options() -> None:
    from collections.abc import AsyncGenerator

    class Actor(ActorMixin):
        @remote_method(concurrency_group="g1")
        def method(self) -> int:
            return 1

        @remote_method(concurrency_group="g2")
        async def async_method(self) -> int:
            return 1

        @remote_method(concurrency_group="g3")
        def stream(self) -> Generator[int, None, None]:
            yield from range(10)

        @remote_method(concurrency_group="g4")
        async def async_stream(self) -> AsyncGenerator[int, None]:
            for i in range(10):
                yield i


def case_covariant_actor() -> None:
    class Base(sunray.ActorMixin): ...

    class Child(Base): ...

    def f1(actor: sunray.Actor[Base]): ...

    @sunray.remote
    def f2(actor: sunray.Actor[Base]): ...

    def main(actor: sunray.Actor[Child]) -> None:
        f1(actor)
        f2.remote(actor)
