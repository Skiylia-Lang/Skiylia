import nox

directories = ["src"]

format_dirs = ["noxfile.py"] + directories


@nox.session
def black(session: nox.session) -> None:
    """Reformat python files."""
    session.install("black")
    session.run("black", *format_dirs)


@nox.session
def isort(session: nox.session) -> None:
    session.install("isort")
    session.run(
        "isort",
        "--profile",
        "black",
        *format_dirs,
    )


@nox.session
def lint(session: nox.session) -> None:
    """Lint all python files."""
    session.install("flake8")
    session.run("flake8", *format_dirs, "--max-line-length", "88", "--ignore", "E203")


@nox.session
def mypy(session: nox.session) -> None:
    """Check python files for type violations."""
    dirs = []
    for dire in directories:
        dirs.extend(["-p", dire])

    session.install("mypy")
    session.run("mypy", *dirs, "--ignore-missing-imports")


@nox.session
def tests(session: nox.session) -> None:
    """Run the python test suite."""
    session.install("pytest")
    session.install("coverage")
    session.run(
        "coverage",
        "run",
        "-m",
        "pytest",
        "python-tests",
        "--import-mode=importlib",
        "-v",
    )
    session.run("coverage", "report", "-m")


@nox.session
def skiytests(session: nox.session) -> None:
    """Run the skiylia test suite (Non-functional for now)"""
    # session.run("python3 src/skiylia.py")