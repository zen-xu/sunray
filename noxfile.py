from __future__ import annotations

import nox
import nox.tasks


MIN_RAY_VERSION = "==2.55.1"


@nox.session(python=["3.10", "3.11", "3.12", "3.13", "3.14"], reuse_venv=True)
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
    coverage_file = session.posargs[0] if session.posargs else "coverage.xml"
    session.install(*packages)
    session.run("pytest", "--cov", "-v", f"--cov-report=xml:{coverage_file}")


@nox.session(python="3.11", reuse_venv=True)
@nox.parametrize(
    "ray_version", [MIN_RAY_VERSION, ""], ids=["min-version", "latest-version"]
)
def test_ty(session, ray_version):
    session.install(
        "pytest",
        "pytest-ty",
        "typing-extensions",
        f"ray[default]{ray_version}",
    )

    session.run("ty", "check", "sunray")
    session.run("pytest", "tests/ty", "-v", "--ty")
