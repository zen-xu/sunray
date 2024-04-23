# ruff: noqa: I002
from typing import Tuple

from sunray.util import get_num_returns


def func1() -> Tuple[int, float]:
    return 1, 1.1


def func2() -> int:
    return 1


def func3():
    return None


def test_get_num_returns():
    assert get_num_returns(func1) == 2
    assert get_num_returns(func2) == 1
    assert get_num_returns(func3) == 1
