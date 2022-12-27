# cookiecutter-pypackage
_Cookiecutter template for Python packages on Github_


 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Build Passing](https://github.com/laucia/cookiecutter-pypackage/actions/workflows/test_generation.yaml/badge.svg?branch=main)

This provides a boilerplate to leverage Github provided features and patterns: Pull Requests, Actions, Pages, Template.

Devs can then focus on writing the library code and not figure out the boilerplate, and are assisted in keeping their code documented and consistent by the tooling.

**Workflow**  

> New changes are
> 1. proposed via Github Pull Request
> 1. Reviewed (and iterated) 
> 1. Squash merged to `main`.
>
> Everything else: release management, changelogs, docs, linting can (and should) be automated!  


**Forking & Contribution**  
This is meant to be usable to publish public packages, and demonstrate some automation possibilities by example: feel free to fork to adjust it to your personal projects / work situation (pypi is a likely culprit to be changed)

## Features

* **package management**: [`poetry`](https://python-poetry.org/)
* **tests**: [`pytest`](https://docs.pytest.org/en/7.2.x/)
* **linting**: [`pre-commit`](https://pre-commit.com/)
  * [`black`](https://github.com/psf/black): style formatter
  * [`mypy`](http://mypy-lang.org/): static typing for python
  * [`pyflake`](https://github.com/PyCQA/pyflakes): basic synthax checking
  * [`isort`](https://github.com/PyCQA/isort): consistent imports order
  * [`detect-secrets`](https://github.com/Yelp/detect-secrets): avoid checking in your password / secrets
  * trailing whitespace / linebreak cleanup: the pre-commit classics
* **Versioning & Publishing**: [`SemVer`](https://semver.org/) 
  * [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) styled PR
  * Automatic Versioning
  

## Quickstart

**Prerequisites**  
1. Create a [PAT](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with write access: the semantic versioning requires it to create the versions and changelog.
1. [pypi API Token](https://pypi.org/help/#apitoken): to publish your package to pypi

**Instructions**  

1. Click `Use This Template`
1. Fill out the desired repository name, and description.
1. Create the repository.
1. Wait 30 seconds for the github action to apply the cookiecutter and settings
1. Create required secrets (`PERSONAL_ACCESS_TOKEN` & `PYPI_API_TOKEN`)
1. Retry the failed github action to apply the cookiecutter and settings

**Troubleshooting**  
Worflow will fail if required secrets (Github Personal Access Token & PyPI API token) are not provided:
1. Create required secrets (`PERSONAL_ACCESS_TOKEN` & `PYPI_API_TOKEN`)
1. Retry the failed github action to apply the cookiecutter and settings

**Note**  
* `PERSONAL_ACCESS_TOKEN` won't be used past the initial setup, as of today, but this might change as features gets added.

## Decision Records

### Run locally
Most commands should work locally and not just in CI.
This helps with debugging and reproducing the errors seen in CI.

This is especially true for tests.


### Follow Conventional Commits
https://www.conventionalcommits.org/en/v1.0.0/
A standard is needed to allow to automate the documentation and version bumping by having the engineers providing information about the changes in a structured manner.

Conventional commit is chosen as it is easy and has enough adoption and a large enough tool ecosystem.

### Lock files & Version bumping
One goal of packages is to not be too restrictive in the version of the underlying packages they support to make it easy on end users.
When running the tests, version resolution is performed by poetry to the latest available package for the python version.

This means that the tests will start failing for non-code related changes (i.e. a new incompatible version of a dependency is released), BUT this means that the test will reproduce errors that users see in their deployment, and discover them early. And enforce a more rigorous dependency management.

This means `poetry.lock` is in the `.gitignore`