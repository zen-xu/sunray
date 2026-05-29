from __future__ import annotations

from typing import Any

import ray.actor

from typing_extensions import assert_type

import sunray

from sunray import ActorMixin
from sunray import get
from sunray import get_actor
from sunray import put
from sunray import wait


def case_put(value: int) -> None:
    assert_type(put(value), sunray.ObjectRef[int])


def case_get(int_ref: sunray.ObjectRef[int], str_ref: sunray.ObjectRef[str]) -> None:
    assert_type(get(int_ref), int)
    assert_type(get([int_ref, int_ref]), tuple[int, ...])
    assert_type(get([int_ref, str_ref]), tuple[Any, ...])
    assert_type(get((int_ref, str_ref)), tuple[int, str])


def case_wait(int_ref: sunray.ObjectRef[int], str_ref: sunray.ObjectRef[str]) -> None:
    assert_type(
        wait([int_ref, int_ref]),
        tuple[list[sunray.ObjectRef[int]], list[sunray.ObjectRef[int]]],
    )
    assert_type(
        wait([int_ref, str_ref]),
        tuple[list[sunray.ObjectRef[Any]], list[sunray.ObjectRef[Any]]],
    )


def case_get_actor() -> None:
    class MyActor(ActorMixin, name="my-actor"): ...

    assert_type(get_actor("my-actor"), ray.actor.ActorHandle)
    assert_type(get_actor[MyActor]("my-actor"), sunray.Actor[MyActor])


def case_init_runtime_env_with_extra_options() -> None:
    sunray.init(
        runtime_env={
            "working_dir": ".",
            "custom": {"key": "value"},
        }
    )


def case_put_owner() -> None:
    class MyActor(ActorMixin, name="my-actor"): ...

    actor = MyActor.new_actor().remote()
    put(1, _owner=actor)


def case_object_ref_covariant() -> None:
    class Base: ...

    class Child(Base): ...

    def func(ref: sunray.ObjectRef[Base]): ...

    def main(ref: sunray.ObjectRef[Child]):
        func(ref)
