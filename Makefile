PACKAGE_NAME = gtfu
VERSION = 0.1.0
PACKAGE_WITH_VERSION = ${PACKAGE_NAME}-${VERSION}

.PHONY: test
test:
	poetry run pytest --capture=no --cov=${PACKAGE_NAME} --cov-report=term-missing

.PHONY: update
update:
	poetry run pip install --upgrade pip setuptools wheel
	poetry update
	make test

.PHONY: build
build:
	poetry build
	tar zxvf dist/$(PACKAGE_WITH_VERSION).tar.gz -C ./dist

.PHONY: publish-test
publish-test:
	rm -r dist/
	poetry publish -r testpypi --build
	tar zxvf dist/$(PACKAGE_WITH_VERSION).tar.gz -C ./dist

.PHONY: clean
clean:
	rm -r .pytest_cache/
	rm -r .venv/
	rm .coverage

.PHONY: init
init:
	/usr/local/bin/python3 -m venv .venv/
	poetry install
	direnv allow
