import os
import sys

import nox


nox.options.sessions = ["linting", "tests"]


@nox.session
def linting(session: nox.Session) -> None:
    """runs linting"""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session
def tests(session: nox.Session) -> None:
    """runs unit and regular tests"""
    session.install(".[testing]")
    session.run("pytest", *session.posargs)


@nox.session(venv_backend="none")
def contrib(session: nox.Session) -> None:
    """prepares a .venv folder for contributors"""
    session.run(sys.executable, "-m", "venv", ".venv")

    if sys.platform == "win32":
        executable = os.path.join(".venv", "Scripts", "pip")
    else:
        executable = os.path.join(".venv", "bin", "pip")

    session.run(
        executable,
        "install",
        "-e.",
        "-Ccmake.define.CMAKE_EXPORT_COMPILE_COMMANDS=1",
        "-Cbuild-dir=build",
    )
