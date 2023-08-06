import importlib
import subprocess
import sys
from pathlib import Path

import nox

nox.options.sessions = ["lint"]
nox.options.reuse_existing_virtualenvs = True

PACKAGE_NAME = "pawapi"
VERSION_MODULE = "version"

PYPI_PROJECT_NAME = "pypawapi"
RELEASE_BRANCH = "master"

PYTHON_VERSION = "3.10"
PYTHON_ALL_VERSIONS = ["3.7", "3.8", "3.9", "3.10"]
SOURCE_FILES = [f"src/{PACKAGE_NAME}", "noxfile.py", "tests"]


@nox.session(python=PYTHON_VERSION)
def lint(session: nox.Session) -> None:
    upgrade_pip(session)
    session.install("-e", ".[lint]")
    session.install("types-requests")
    session.run("flake8", *SOURCE_FILES)
    session.run("isort", "--check-only", *SOURCE_FILES)
    session.run("yapf", "--parallel", "--quiet", "--recursive", *SOURCE_FILES)
    session.run(
        "mypy",
        "--strict-equality",
        "--implicit-optional",
        "--warn-unreachable",
        SOURCE_FILES[0],
    )


@nox.session
def dev(session: nox.Session) -> None:
    path = Path("./.nox/dev").resolve()
    session.install("virtualenv")
    session.run("virtualenv", str(path), silent=True)
    python = str(path / "bin/python")
    session.run(
        python, "-m", "pip", "install", "--upgrade", "pip", external=True
    )
    session.run(python, "-m", "pip", "install", "-e", ".[dev]", external=True)


@nox.session(python=PYTHON_ALL_VERSIONS)
def tests(session: nox.Session) -> None:
    upgrade_pip(session)
    session.install("-e", ".[test]")
    session.run(
        "pytest",
        "--strict-config",
        f"--cov={PACKAGE_NAME}",
        "--cov-report=",
    )
    session.notify("coverage")


@nox.session(python=PYTHON_VERSION)
def coverage(session: nox.Session) -> None:
    upgrade_pip(session)
    session.install("coverage")
    session.run(
        "coverage",
        "report",
        "--show-missing",
        "--fail-under=80",
    )
    session.run("coverage", "erase")


@nox.session(python=PYTHON_VERSION)
def build(session: nox.Session) -> None:
    check_branch(session, RELEASE_BRANCH)

    dist = Path("dist")
    if dist.exists():
        session.error("/dist already exists! Delete and try again")

    version = get_version()
    ver = version.split(".")
    if len(ver) != 3 or any([not x.isdigit() for x in ver]):
        session.error("Invalid version format")

    session.install("twine", "build")
    session.run("pyproject-build")

    files = sorted(map(str, dist.glob("*")))
    expected_files = sorted([
        f"dist/{PYPI_PROJECT_NAME}-{version}-py3-none-any.whl",
        f"dist/{PYPI_PROJECT_NAME}-{version}.tar.gz",
    ])
    if files != expected_files:
        session.error("Got wrong files")
    session.run("twine", "check", *files)


def upgrade_pip(session: nox.Session) -> None:
    session.run("python", "-m", "pip", "install", "--upgrade", "pip")


def get_version() -> str:
    sys.path.append(f"src/{PACKAGE_NAME}")
    version = importlib.import_module(VERSION_MODULE, package=PACKAGE_NAME)
    return version.__version__


def get_current_branch() -> str:
    return subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout.decode().strip()


def check_branch(session: nox.Session, branch="master") -> str:
    current_branch = get_current_branch()
    if current_branch != branch:
        session.error(
            f"Release branch is {branch!r}, "
            f"your current branch is {current_branch!r}."
        )
