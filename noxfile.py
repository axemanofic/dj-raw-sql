import nox


@nox.session(python=["3.11", "3.10"])
@nox.parametrize("django", ["3.2"])
def tests_django3(session, django):
    session.install(f"django=={django}")
    session.install("pytest", "pytest-django", ".")
    session.run("pytest")


@nox.session(python=["3.12", "3.11", "3.10"])
@nox.parametrize("django", ["4.2", "5.0"])
def tests_django(session, django):
    session.install(f"django=={django}")
    session.install("pytest", "pytest-django", ".")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("ruff", "pyright", ".")
    session.run("ruff", "./src/")
    session.run("pyright", "./src/")
