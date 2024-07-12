# ruff: noqa: I002
from typing import Tuple  # noqa: UP035

from sunray._internal.util import get_num_returns


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
