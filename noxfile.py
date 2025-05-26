from __future__ import annotations

import nox
import nox.tasks


MIN_RAY_VERSION = "==2.20.0"


@nox.session(python=["3.9", "3.10", "3.11", "3.12"], reuse_venv=True)
@nox.parametrize(
    "ray_version", [MIN_RAY_VERSION, ""], ids=["min-version", "latest-version"]
)
def test(session: nox.Session, ray_version):
    packages = [
        "pytest",
        "pytest-cov",
        "typing-extensions",
        "async-timeout",
        f"ray[default]{ray_version}",
    ]
    if session.python == "3.12" and ray_version == MIN_RAY_VERSION:
        session.skip()

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
