from __future__ import annotations

import nox
import nox.tasks


def _test(session, ray_version):
    packages = [
        "pytest",
        "pytest-cov",
        "typing-extensions",
        f"ray[default]=={ray_version}",
    ]
    if session.python < "3.9":
        # https://github.com/ray-project/ray/issues/27299#issuecomment-1239918086
        packages.append("grpcio>1.48")
    if ray_version < "2.9":
        packages.append("async-timeout")

    coverage_file = session.posargs[0] if session.posargs else "coverage.xml"
    session.install(*packages)
    session.run("pytest", "-s", "--cov", "-v", f"--cov-report=xml:{coverage_file}")


def _test_mypy(session, ray_version):
    session.install(
        "pytest",
        "typing-extensions",
        f"ray[default]=={ray_version}",
        "mypy==1.9",
        "pytest-mypy-plugins",
    )
    session.run(
        "pytest",
        "tests/mypy",
        "-v",
        "--mypy-only-local-stub",
        "--mypy-pyproject-toml-file=pyproject.toml",
    )


@nox.session(python="3.7", reuse_venv=True, tags=["py3.7"])
@nox.parametrize("ray_version", ["2.7.2"])
def test_py37(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.8", reuse_venv=True, tags=["py3.8"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0"])
def test_py38(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.9", reuse_venv=True, tags=["py3.9"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py39(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.10", reuse_venv=True, tags=["py3.10"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py310(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.11", reuse_venv=True, tags=["py3.11"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py311(session, ray_version):
    _test(session, ray_version)


@nox.session(python="3.8", reuse_venv=True, tags=["py3.8_mypy"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0"])
def test_py38_mypy(session, ray_version):
    _test_mypy(session, ray_version)


@nox.session(python="3.9", reuse_venv=True, tags=["py3.9_mypy"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py39_mypy(session, ray_version):
    _test_mypy(session, ray_version)


@nox.session(python="3.10", reuse_venv=True, tags=["py3.10_mypy"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py310_mypy(session, ray_version):
    _test_mypy(session, ray_version)


@nox.session(python="3.11", reuse_venv=True, tags=["py3.11_mypy"])
@nox.parametrize("ray_version", ["2.7.2", "2.8.1", "2.9.3", "2.10.0", "2.11.0"])
def test_py311_mypy(session, ray_version):
    _test_mypy(session, ray_version)
