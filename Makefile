VERSION = 0.1.1
PACKAGE_WITH_VERSION = ${PACKAGE_NAME}-${VERSION}

test:
	poetry run pytest --capture=no --cov=${PACKAGE_NAME} --cov-report=term-missing --cov-report=html

update:
	tox
	poetry run pip install --upgrade pip setuptools wheel
	poetry update
	tox

build:
	tox
	poetry build
	tar zxvf dist/$(PACKAGE_WITH_VERSION).tar.gz -C ./dist

publish-test:
	rm -r dist/
	make build
	poetry publish --repository testpypi

publish-production:
	rm -r dist/
	make build
	poetry publish

clean:
	rm -r .pytest_cache/
	rm -r .tox/
	rm -r .venv/
	rm -r dist/
	rm .coverage

init:
	/usr/local/bin/python3 -m venv .venv/
	poetry install
	direnv allow
