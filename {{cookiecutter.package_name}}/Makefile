.PHONY: test lint docs

help:
	@echo "test - Run tests with pytest"
	@echo "lint - Run all the linters on all the files"
	@echo "help - this command"

test:
	poetry run pytest test/unit
    # We use coverage to make sure all tests in the `test/unit` folder are run.
    # This helps finding missnamed filed and tests
	poetry run coverage report --include="test/unit/*" --fail-under=100 --show-missing --skip-covered --skip-empty

lint:
	poetry run pre-commit run --all-files

docs:
	poetry run mkdocs build -f docs/mkdocs.yml
