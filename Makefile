
.PHONY: test

help:
	@echo "test - Run cookiecutter locally and check that the generated package is sensible"
	@echo "help - this command"

test:
	cookiecutter --no-input --overwrite-if-exists .
	cd custom-package && git init --initial-branch=main
	cd custom-package && git add .
	cd custom-package && poetry install
	cd custom-package && $(MAKE) lint
	cd custom-package && $(MAKE) test
	cd custom-package && $(MAKE) docs
