from __future__ import annotations

import os
import sys

from typing import TYPE_CHECKING

import pytest
import ray

from sunray import remote


if TYPE_CHECKING:
    from collections.abc import Generator


def test_remote_func(init_ray):
    @remote
    def func(v1: int, v2: int = 2) -> int:
        return v1 + v2

    assert ray.get(func.remote(1, 2)) == 3


def test_remote_func_options(init_ray):
    @remote(num_cpus=0, runtime_env={"env_vars": {"ARG": "Hello"}})
    def func() -> str:
        return f'{os.environ["ARG"]} sunray'

    assert ray.get(func.remote()) == "Hello sunray"
    assert (
        ray.get(func.options(runtime_env={"env_vars": {"ARG": "Hi"}}).remote())
        == "Hi sunray"
    )


def test_stream_func(init_ray):
    @remote
    def stream(n: int) -> Generator[int, None, None]:
        yield from range(n)

    n = 3
    stream_gen = stream.remote(n)
    assert [ray.get(next(stream_gen)) for _ in range(n)] == list(range(n))


@pytest.mark.skipif(
    sys.version_info >= (3, 11) and os.getenv("GITHUB_ACTIONS") == "true",
    reason="Python 3.11 will OOM in github actions",
)
def test_stream_func_with_options(init_ray):
    @remote(num_cpus=0, runtime_env={"env_vars": {"BASE": "1"}})
    def stream(n: int) -> Generator[int, None, None]:
        base = int(os.environ["BASE"])
        for i in range(n):
            yield base + i

    n = 3
    stream_gen = stream.remote(n)
    assert [ray.get(next(stream_gen)) for _ in range(n)] == [1 + i for i in range(n)]

    stream_gen2 = stream.options(runtime_env={"env_vars": {"BASE": "2"}}).remote(n)
    assert [ray.get(next(stream_gen2)) for _ in range(n)] == [2 + i for i in range(n)]


def test_call_remote_func_in_another_remote_func(init_ray):
    @remote(num_cpus=0)
    def sum(v1: int, v2: int) -> int:
        return v1 + v2

    @remote(num_cpus=0)
    def main(v1: int, v2: int) -> int:
        return ray.get(sum.remote(v1, v2))

    assert ray.get(main.remote(1, 2)) == 3


def test_unpack_remote_func_result(init_ray):
    @remote(num_cpus=0)
    def get() -> tuple[int, str]:
        return 1, "a"

    without_unpack_refs = get.remote()
    assert ray.get(without_unpack_refs) == (1, "a")

    without_unpack_refs = get.options(unpack=False).remote()
    assert ray.get(without_unpack_refs) == (1, "a")

    obj1_ref, obj2_ref = get.options(unpack=True).remote()
    assert [ray.get(obj1_ref), ray.get(obj2_ref)] == [1, "a"]


def test_remote_class(init_ray):
    @remote
    class C1:
        def echo(self, message: str) -> str:
            return "C1 " + message

    @remote(num_cpus=0)
    class C2:
        def echo(self, message: str) -> str:
            return "C2 " + message

    assert ray.get(C1.remote().echo.remote("hello")) == "C1 hello"
    assert ray.get(C2.remote().echo.remote("hello")) == "C2 hello"
