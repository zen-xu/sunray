from __future__ import annotations

import nox
import nox.tasks


MIN_RAY_VERSION = "==2.7.2"


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"], reuse_venv=True)
@nox.parametrize(
    "ray_version", [MIN_RAY_VERSION, ""], ids=["min-version", "latest-version"]
)
def test(session, ray_version):
    packages = [
        "pytest",
        "pytest-cov",
        "typing-extensions",
        "async-timeout",
        f"ray[default]{ray_version}",
    ]
    if session.python < "3.9":
        # https://github.com/ray-project/ray/issues/27299#issuecomment-1239918086
        packages.append("grpcio>1.48")

    coverage_file = session.posargs[0] if session.posargs else "coverage.xml"
    session.install(*packages)
    session.run("pytest", "--cov", "-v", f"--cov-report=xml:{coverage_file}")


@nox.session(python="3.11", reuse_venv=True)
@nox.parametrize(
    "ray_version", [MIN_RAY_VERSION, ""], ids=["min-version", "latest-version"]
)
def test_mypy(session, ray_version):
    session.install(
        "pytest",
        "typing-extensions",
        "mypy==1.9",
        "pytest-mypy-plugins",
        f"ray[default]{ray_version}",
    )

    session.run(
        "pytest",
        "tests/mypy",
        "-v",
        "--mypy-only-local-stub",
        "--mypy-pyproject-toml-file=pyproject.toml",
    )
