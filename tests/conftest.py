from __future__ import annotations

import pytest
import ray


@pytest.fixture(scope="module")
def init_ray():
    ray.init(address="local", include_dashboard=False)
    yield
    ray.shutdown()
