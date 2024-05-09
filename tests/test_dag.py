from __future__ import annotations

from typing import AsyncGenerator
from typing import Generator

import sunray

from sunray.dag import InputNode
from sunray.dag import MultiOutputNode


def test_func_bind(init_ray):
    @sunray.remote
    def func(src: int, inc: int = 1) -> int:
        return src + inc

    a_ref = func.bind(1, inc=2)
    a_ref.execute()
    assert sunray.get(a_ref.execute()) == 3
    b_ref = func.bind(a_ref, 3)
    assert sunray.get(b_ref.execute()) == 6
    c_ref = func.bind(b_ref, a_ref)
    assert sunray.get(c_ref.execute()) == 9


def test_stream_bind(init_ray):
    @sunray.remote
    def func(count: int) -> Generator[int, None, None]:
        yield from range(count)

    gen_ref = func.bind(3)
    assert [sunray.get(ref) for ref in gen_ref.execute()] == list(range(3))


def test_actor_bind(init_ray):
    class Actor(sunray.ActorMixin):
        def __init__(self, init_value: int):
            self.i = init_value

        @sunray.remote_method
        def inc(self, x: int):
            self.i += x

        @sunray.remote_method
        def get(self) -> int:
            return self.i

    a0 = Actor.new_actor().bind(10).execute()
    assert isinstance(a0, sunray.Actor)

    a1 = Actor.new_actor().bind(10)
    val = a1.methods.get.bind()
    assert sunray.get(val.execute()) == 10

    @sunray.remote
    def combine(x: int, y: int) -> int:
        return x + y

    a2 = Actor.new_actor().bind(10)
    a1.methods.inc.bind(2)
    a1.methods.inc.bind(4)
    a2.methods.inc.bind(6)

    dag = combine.bind(a1.methods.get.bind(), a2.methods.get.bind())
    assert sunray.get(dag.execute()) == 32


def test_actor_async_method_bind(init_ray):
    class Actor(sunray.ActorMixin):
        @sunray.remote_method
        async def cal(self, x: int) -> int:
            return x + 2

    a1 = Actor.new_actor().bind()
    node = a1.methods.cal.bind(1)
    assert sunray.get(node.execute()) == 3


def test_actor_stream_bind(init_ray):
    class Actor(sunray.ActorMixin):
        @sunray.remote_method
        def gen(self, x: int) -> Generator[int, None, None]:
            yield from range(x)

    a1 = Actor.new_actor().bind()
    node = a1.methods.gen.bind(3)
    assert [sunray.get(ref) for ref in node.execute()] == list(range(3))


def test_actor_async_stream_bind(init_ray):
    class Actor(sunray.ActorMixin):
        @sunray.remote_method
        async def gen(self, x: int) -> AsyncGenerator[int, None]:
            for i in range(x):
                yield i

    a1 = Actor.new_actor().bind()
    node = a1.methods.gen.bind(3)
    assert [sunray.get(ref) for ref in node.execute()] == list(range(3))


def test_reuse_ray_actor_in_dag(init_ray):
    class Worker(sunray.ActorMixin):
        def __init__(self):
            self.forwarded = 0

        @sunray.remote_method
        def forward(self, input_data: int) -> float:
            self.forwarded += 1
            return input_data + 1.0

        @sunray.remote_method
        def num_forwarded(self) -> int:
            return self.forwarded

    worker = Worker.new_actor().remote()

    with InputNode[int]() as input_data:
        dag = MultiOutputNode((worker.methods.forward.bind(input_data),))

    assert sunray.get(dag.execute(1)) == (2,)
    assert sunray.get(dag.execute(2)) == (3,)
    assert sunray.get(dag.execute(3)) == (4,)
    assert sunray.get(worker.methods.num_forwarded.remote()) == 3


def test_func_with_input_data(init_ray):
    @sunray.remote
    def func(v: int) -> int:
        return v + 1

    with InputNode[int]() as input_data:
        dag = func.bind(input_data)

    assert sunray.get(dag.execute(1)) == 2
    ref = sunray.put(1)
    assert sunray.get(dag.execute(ref)) == 2


def test_stream_with_input_data(init_ray):
    @sunray.remote
    def func(v: int) -> Generator[int, None, None]:
        yield from range(v)

    with InputNode[int]() as input_data:
        dag = func.bind(input_data)

    assert sunray.get(list(dag.execute(3))) == tuple(range(3))
    ref = sunray.put(3)
    assert sunray.get(list(dag.execute(ref))) == tuple(range(3))


def test_actor_method_with_input_data(init_ray):
    class Worker(sunray.ActorMixin):
        def __init__(self, v: int) -> None:
            self.v = v

        @sunray.remote_method
        def add(self, v: int) -> int:
            return self.v + v

    a1 = Worker.new_actor().bind(1)
    with InputNode[int]() as input_data:
        dag = a1.methods.add.bind(input_data)

    assert sunray.get(dag.execute(1)) == 2
    ref = sunray.put(2)
    assert sunray.get(dag.execute(ref)) == 3


def test_actor_async_method_with_input_data(init_ray):
    class Worker(sunray.ActorMixin):
        def __init__(self, v: int) -> None:
            self.v = v

        @sunray.remote_method
        async def add(self, v: int) -> int:
            return self.v + v

    a1 = Worker.new_actor().bind(1)
    with InputNode[int]() as input_data:
        dag = a1.methods.add.bind(input_data)

    assert sunray.get(dag.execute(1)) == 2
    ref = sunray.put(2)
    assert sunray.get(dag.execute(ref)) == 3


def test_actor_stream_with_input_data(init_ray):
    class Worker(sunray.ActorMixin):
        def __init__(self, v: int) -> None:
            self.v = v

        @sunray.remote_method
        def gen(self, v: int) -> Generator[int, None, None]:
            yield from range(v)

    a1 = Worker.new_actor().bind(1)
    with InputNode[int]() as input_data:
        dag = a1.methods.gen.bind(input_data)

    assert sunray.get(list(dag.execute(2))) == tuple(range(2))
    ref = sunray.put(2)
    assert sunray.get(list(dag.execute(ref))) == tuple(range(2))


def test_actor_async_stream_with_input_data(init_ray):
    class Worker(sunray.ActorMixin):
        def __init__(self, v: int) -> None:
            self.v = v

        @sunray.remote_method
        async def gen(self, v: int) -> AsyncGenerator[int, None]:
            for i in range(v):
                yield i

    a1 = Worker.new_actor().bind(1)
    with InputNode[int]() as input_data:
        dag = a1.methods.gen.bind(input_data)

    assert sunray.get(list(dag.execute(2))) == tuple(range(2))
    ref = sunray.put(2)
    assert sunray.get(list(dag.execute(ref))) == tuple(range(2))
