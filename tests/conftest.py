from __future__ import annotations

import pytest
import ray


@pytest.fixture
def init_ray():
    ray.init(address="local", include_dashboard=True)
    yield
    ray.shutdown()


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers",
        "min_ray_version(min_version): run only when ray version is greater than min version",
    )


def get_ray_version() -> tuple[int, int, int]:
    major, minor, patch = ray.__version__.split(".")
    return int(major), int(minor), int(patch)


RAY_VERSION = get_ray_version()


def pytest_runtest_setup(item):
    markers = list(item.iter_markers(name="min_ray_version"))
    if markers:
        [marker] = markers
        if marker.args > RAY_VERSION:
            pytest.skip(f"at least ray-{'.'.join(map(str, marker.args))} required")
