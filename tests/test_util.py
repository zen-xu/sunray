# ruff: noqa: I002
from typing import Tuple  # noqa: UP035

import sunray

from sunray._internal.util import get_num_returns
from sunray.util import ActorPool


def func1() -> Tuple[int, float]:  # noqa: UP006
    return 1, 1.1


def func2() -> tuple[int, float]:
    return 1, 1.1


def func3() -> int:
    return 1


def func4():
    return None


def test_get_num_returns():
    assert get_num_returns(func1) == 2
    assert get_num_returns(func2) == 2
    assert get_num_returns(func3) == 1
    assert get_num_returns(func4) == 1


def test_actor_pool(init_ray):
    class Actor(sunray.ActorMixin):
        @sunray.remote_method
        def double(self, v: int) -> int:
            return 2 * v

    a1, a2 = Actor.new_actor().remote(), Actor.new_actor().remote()
    pool = ActorPool([a1, a2])
    assert list(pool.map(lambda a, v: a.methods.double.remote(v), [1, 2, 3, 4])) == [
        2,
        4,
        6,
        8,
    ]

    assert set(
        pool.map_unordered(lambda a, v: a.methods.double.remote(v), [1, 2, 3, 4])
    ) == {2, 4, 6, 8}
