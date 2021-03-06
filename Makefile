install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall-local:
	poetry run python3 -m pip install --force-reinstall dist/*.whl

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

build_and_reinstall-local:
	poetry build
	poetry run python3 -m pip install --force-reinstall dist/*.whl
