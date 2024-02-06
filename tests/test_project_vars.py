from __future__ import annotations


try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata  # type: ignore[no-redef]

from sunray import __version__


def test_version():
    assert __version__ == metadata.metadata("sunray").get("version")
