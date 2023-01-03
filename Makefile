VERSION = 1.4.0
PACKAGE_WITH_VERSION = ${PACKAGE_NAME}-${VERSION}

test:
	poetry run pytest --capture=no --cov=${PACKAGE_NAME} --cov-report=term-missing --cov-report=html

lint:
	pre-commit run --all-files

switch:
	git switch --create develop

after-develop-merged:
	git switch main
	git pull --prune
	git branch --delete develop
	make switch

update:
	poetry run pip install --upgrade pip setuptools wheel
	poetry update
	tox

build:
	poetry build
	tar zxvf dist/${PACKAGE_WITH_VERSION}.tar.gz -C ./dist
	unzip dist/${PACKAGE_WITH_VERSION}-py3-none-any.whl -d ./dist

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
	rm -r htmlcov/
	rm .coverage

init:
	python3.7 -m venv .venv/
	poetry install
	direnv allow
	pre-commit install
