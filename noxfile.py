from __future__ import annotations

import nox
import nox.tasks


def _test(session, ray_version):
    packages = ["pytest", "pytest-cov", f"ray=={ray_version}"]
    if session.python < "3.9":
        # https://github.com/ray-project/ray/issues/27299#issuecomment-1239918086
        packages.append("grpcio>1.48")
    session.install(*packages)
    session.run("pytest", "--cov", "-v", "--cov-report=xml")


@nox.session(python="3.7", reuse_venv=True, tags=["py3.7"])
@nox.parametrize("ray_version", ["2.7.2"])
def test_py37(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.8", reuse_venv=True, tags=["py3.8"])
@nox.parametrize("ray_version", ["2.8.1", "2.9.3", "2.10.0"])
def test_py38(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.9", reuse_venv=True, tags=["py3.9"])
@nox.parametrize("ray_version", ["2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py39(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.10", reuse_venv=True, tags=["py3.10"])
@nox.parametrize("ray_version", ["2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py310(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.11", reuse_venv=True, tags=["py3.11"])
@nox.parametrize("ray_version", ["2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py311(session, ray_version):
    _test(session, ray_version)
