from __future__ import annotations

import asyncio
import time

from typing import AsyncGenerator

import pytest
import ray

from sunray import Actor
from sunray import ActorMixin
from sunray import remote_method
from sunray.actor_mixin import add_var_keyword_to_klass


@pytest.fixture(scope="module")
def init_ray():
    ray.init(address="local", include_dashboard=False)
    yield
    ray.shutdown()


class Demo(ActorMixin, num_cpus=1, concurrency_groups={"group1": 1}):
    def __init__(self, init: int):
        self.init = init

    @remote_method
    def calculate(self, v1: int, v2: int = 2) -> int:
        return self.init + v1 + v2

    @remote_method
    async def echo(self, message: str) -> str:
        return message

    @remote_method
    async def stream(self, gen_count: int) -> AsyncGenerator[int, None]:
        for i in range(gen_count):
            yield i

    @remote_method
    def get_tuple(self) -> tuple[int, str]:
        return 1, "a"

    @remote_method(concurrency_group="group1")
    async def sleep(self, seconds: float) -> str:
        await asyncio.sleep(seconds)
        return "done"

    @remote_method
    def get_num_cpu(self) -> int:
        return ray.get_runtime_context().get_assigned_resources().get("CPU", 0)

    @remote_method
    def method_with_kwargs(self, **kwargs) -> dict:
        return kwargs


@pytest.fixture(scope="module")
def demo_actor(init_ray) -> Actor[Demo]:
    demo = Demo.new_actor().remote(1)
    return demo


def test_sync_call(demo_actor: Actor[Demo]):
    assert ray.get(demo_actor.methods.calculate.remote(1, 2)) == 4


def test_async_call(demo_actor: Actor[Demo]):
    assert ray.get(demo_actor.methods.echo.remote("hello")) == "hello"


def test_stream(demo_actor: Actor[Demo]):
    stream = demo_actor.methods.stream.remote(4)
    assert [ray.get(next(stream)) for _ in range(4)] == list(range(4))


def test_unpack_result(demo_actor: Actor[Demo]):
    without_unpack_refs = demo_actor.methods.get_tuple.remote()
    assert ray.get(without_unpack_refs) == (1, "a")

    without_unpack_refs = demo_actor.methods.get_tuple.options(unpack=False).remote()
    assert ray.get(without_unpack_refs) == (1, "a")

    obj1_ref, obj2_ref = demo_actor.methods.get_tuple.options(unpack=True).remote()
    assert [ray.get(obj1_ref), ray.get(obj2_ref)] == [1, "a"]


def test_concurrency_group(demo_actor: Actor[Demo]):
    refs = [demo_actor.methods.sleep.remote(1) for _ in range(2)]
    start = time.time()
    ray.wait(refs, num_returns=2)
    assert time.time() - start > 2


def test_default_params(demo_actor: Actor[Demo]):
    assert ray.get(demo_actor.methods.calculate.remote(1)) == 4


def test_keyword_params(demo_actor: Actor[Demo]):
    assert ray.get(demo_actor.methods.calculate.remote(1, v2=2)) == 4
    assert ray.get(demo_actor.methods.calculate.remote(v1=1, v2=2)) == 4


def test_override_default_actor_options(init_ray):
    num_cpus = 2
    demo = Demo.new_actor().options(num_cpus=num_cpus).remote(1)
    assert ray.get(demo.methods.get_num_cpu.remote()) == num_cpus


def test_actor_eq(init_ray):
    demo1 = Demo.new_actor().remote(1)
    demo2 = Demo.new_actor().remote(1)
    assert demo1 != demo2

    @ray.remote
    def cmp_actor(actor1, actor2) -> bool:
        return actor1 == actor2

    assert ray.get(cmp_actor.remote(demo1, demo1))


def test_actor_hash(demo_actor: Actor[Demo]):
    assert hash(demo_actor) == hash(demo_actor._actor_handle._actor_id)


def test_method_with_kwargs(demo_actor: Actor[Demo]):
    assert ray.get(demo_actor.methods.method_with_kwargs.remote(a=1, b=2)) == {
        "a": 1,
        "b": 2,
    }


def test_add_var_keyword_to_klass():
    class C1:
        def __init__(self) -> None: ...

    class C2:
        def __init__(self, **kwargs) -> None: ...

    add_var_keyword_to_klass(C1)(_ray_trace_ctx=123)  # type: ignore[arg-type]

    origin_init = C2.__init__
    assert add_var_keyword_to_klass(C2).__init__ == origin_init