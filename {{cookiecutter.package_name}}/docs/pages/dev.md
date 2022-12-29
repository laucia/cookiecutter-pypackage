# Development
_This section contains informations about the development of the package, as well as decision records for technical choices. It is not meant for users, though they sat their curiosity in the reading_

## Library Used for development
_Knowing these libraries is helpful to navigate the codebase_

* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
* Linter Management: [pre-commit](https://pre-commit.com/)
* Build / Dependency Management: [poetry](https://python-poetry.org/)
* Documentation: [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
* Test: [pytest](https://docs.pytest.org/en/7.2.x/)


## Decision Record

_If you make decisions about your library: codestyle, architecture, organisation ..., document them here_

### #1 Use [laucia/cookiecutter-pypackage](https://github.com/laucia/cookiecutter-pypackage)

This repository was generated from [laucia/cookiecutter-pypackage](https://github.com/laucia/cookiecutter-pypackage) and inherits from its technology and workflow choices.

Many of the decision about the setup, the choice of libraries and dev tools stems can be found justified in https://github.com/laucia/cookiecutter-pypackage#decision-records
