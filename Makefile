PACKAGE_NAME = gtfu
VERSION = 0.1.1
PACKAGE_WITH_VERSION = ${PACKAGE_NAME}-${VERSION}

test:
	poetry run pytest --capture=no --cov=${PACKAGE_NAME} --cov-report=term-missing

update:
	make test
	poetry run pip install --upgrade pip setuptools wheel
	poetry update
	make test

build:
	make test
	poetry build
	tar zxvf dist/$(PACKAGE_WITH_VERSION).tar.gz -C ./dist

publish-test:
	make test
	rm -r dist/
	poetry publish --repository testpypi --build
	tar zxvf dist/$(PACKAGE_WITH_VERSION).tar.gz -C ./dist

clean:
	rm -r .pytest_cache/
	rm -r .venv/
	rm -r dist/
	rm .coverage

init:
	/usr/local/bin/python3 -m venv .venv/
	poetry install
	direnv allow
