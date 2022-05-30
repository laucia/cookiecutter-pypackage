# cookiecutter-pypackage
Cookiecutter template for Python packages on Github

This tries to leverage Github Actions and Github features (like pages, template) as much as possible, while limiting the amount of setup. So devs can focus on writing the library code and not figure out the boilerplate.

**Workflow**

> While you are working a change is a branch, and its PR (that gets reviewed)  
> Once you are done, a change is boiled down to a single commit with all relevant informations about the change for posterity.  

From there everything else from release management, changelogs to linting can be automated!

## Features

* **package management**: Poetry
* **tests**: Pytest
* **tests env**: Tox `TODO`
  * Cross-Platform / Cross Python Versions
* **docs**: Mkdocs (Mkdocstrings) `TODO`
  * Publishing docs as Github Page
* **linting**: pre-commit
  * black
  * mypy
  * pyflake
  * isort
  * detect-secrets
  * trailing whitespace / linebreak cleanup
* **Versioning & Publishing**: SemVer 
  * Conventional Commit styled PR
  * Automatic Versioning
  * Publishing to Pypi `TODO`

## Quickstart

1. Click `Use This Template`
1. Fill out the desired repository name, and description.
1. Create the repository.
1. Wait 30 seconds for the github action to apply the cookiecutter and settings

**Troubleshooting**  
Worflow will fail if required secrets (Github Personal Access Token & PyPI API token) are not provided:
1. Create required secrets (`PERSONAL_ACCESS_TOKEN` & `PYPI_API_TOKEN`)
1. Retry the failed github action to apply the cookiecutter and settings

## Decision Records

### Lock files & Version bumping
One goal of packages is to not be too restrictive in the version of the underlying packages they support to make it easy on end users.
When running the tests, version resolution is performed by poetry to the latest available package for the python version.

This means that the tests will start failing for non-code related changes (i.e. a new incompatible version of a dependency is released), BUT this means that the test will reproduce errors that users see in their deployment, and discover them early. And enforce a more rigorous dependency management.

This means `poetry.lock` is in the `.gitignore`