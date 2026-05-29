from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from typing_extensions import assert_type

import sunray

from sunray._internal import dag
from sunray._internal import io
from sunray.dag import InputNode
from sunray.dag import MultiOutputNode


if TYPE_CHECKING:
    from collections.abc import AsyncGenerator
    from collections.abc import Generator


def case_actor_bind(init_value: int, v: int) -> None:
    class Actor(sunray.ActorMixin):
        def __init__(self, init_value: int):
            self.i = init_value

        @sunray.remote_method
        def add(self, v: int) -> int:
            return self.i + v

    a1 = Actor.new_actor().bind(init_value)
    val = a1.methods.add.bind(v)
    assert_type(a1, dag.ClassNode[io.NoIn, io.Actor[Actor]])
    assert_type(val, dag.ClassMethodNode[io.NoIn, io.Out[sunray.ObjectRef[int]]])
    assert_type(sunray.get(val.execute()), Any)


def case_actor_bind_async(init_value: int, v: int) -> None:
    class Actor(sunray.ActorMixin):
        def __init__(self, init_value: int):
            self.i = init_value

        @sunray.remote_method
        async def add(self, v: int) -> int:
            return self.i + v

    a1 = Actor.new_actor().bind(init_value)
    val = a1.methods.add.bind(v)
    assert_type(val, dag.ClassMethodNode[io.NoIn, io.Out[sunray.ObjectRef[int]]])
    assert_type(sunray.get(val.execute()), Any)


def case_actor_bind_stream(v: int) -> None:
    class Actor(sunray.ActorMixin):
        @sunray.remote_method
        def gen(self, v: int) -> Generator[int, None, None]:
            yield from range(v)

    a1 = Actor.new_actor().bind()
    val = a1.methods.gen.bind(v)
    assert_type(val, dag.ClassStreamNode[io.NoIn, io.Yield[int]])
    assert_type(next(val.execute()), sunray.ObjectRef[int])


def case_actor_bind_async_stream(v: int) -> None:
    class Actor(sunray.ActorMixin):
        @sunray.remote_method
        async def gen(self, v: int) -> AsyncGenerator[int, None]:
            for i in range(v):
                yield i

    a1 = Actor.new_actor().bind()
    val = a1.methods.gen.bind(v)
    assert_type(val, dag.ClassStreamNode[io.NoIn, io.Yield[int]])
    assert_type(next(val.execute()), sunray.ObjectRef[int])


def case_task_bind(src: int, inc: int) -> None:
    @sunray.remote
    def func(src: int, inc: int = 1) -> int:
        return src + inc

    a_ref = func.bind(src, inc)
    assert_type(a_ref, dag.FunctionNode[io.NoIn, io.Out[sunray.ObjectRef[int]]])
    assert_type(sunray.get(a_ref.execute()), Any)
    b_ref = func.bind(a_ref, inc)  # ty: ignore[no-matching-overload]
    assert_type(b_ref, Any)


def case_stream_bind(count: int) -> None:
    @sunray.remote
    def func(count: int) -> Generator[int, None, None]:
        yield from range(count)

    bind_ref = func.bind(count)
    assert_type(bind_ref, dag.StreamNode[io.NoIn, io.Yield[int]])
    assert_type(bind_ref.execute(), sunray.ObjectRefGenerator[int])


def case_input_node_sequence(data: list[int]) -> None:
    with InputNode[list[int]]() as node:
        v = node[2]
        assert_type(v, dag.InputAttributeNode[io.In[list[int]], int])
        assert_type(node.a, Any)
    ret = v.execute(data)
    assert_type(ret, int)


def case_input_node_mapping(data: dict[str, int]) -> None:
    with InputNode[dict[str, int]]() as node:
        v = node["a"]
        assert_type(v, dag.InputAttributeNode[io.In[dict[str, int]], int])
        assert_type(node.a, Any)
    ret = v.execute(data)
    assert_type(ret, int)


def case_multi_output_node(value: int) -> None:
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
        out = worker.methods.forward.bind(input_data)  # ty: ignore[no-matching-overload]
        dag_node = MultiOutputNode((out,))

    assert_type(dag_node, dag.MultiOutputNode[Any, Any])
    assert_type(dag_node.execute(value), tuple[Any, ...])
    assert_type(worker.methods.num_forwarded.remote(), sunray.ObjectRef[int])
