# cookiecutter-pypackage
Cookiecutter template for Python packages on Github

## Features
* **package management**: Poetry
* **tests**: Pytest
* **tests env**: Tox `TODO`
* **docs**: Mkdocs (Mkdocstrings) `TODO`
* **linting**: pre-commit
  * black
  * mypy
  * pyflake
  * isort
  * detect-secrets
  * trailing whitespace / linebreak cleanup
* **CI/CD**: Github Actions `TODO`
  * Publishing to Pypi
  * Publishing docs as Github Page

## Quickstart


## Decision Records

### local pre-commit linting
Most of the linting pre-commits python hooks are installed by poetry directly rather than via the `pre-commit` environment, to make it easy for people to run the linting tools, in the correct version, without pre-commit getting involved (e.g. from vs-code, or just manually on one file)

### Lock files & Version bumping
One goal of packages is to not be too restrictive in the version of the underlying packages they support to make it easy on end users.
When running the tests, version resolution is performed by poetry to the latest available package for the python version.

This means that the tests will start failing for non-code related changes (i.e. a new incompatible version of a dependency is released), BUT this means that the test will reproduce errors that users see in their deployment, and discover them early. And enforce a more rigorous dependency management.

This means `poetry.lock` is in the `.gitignore`