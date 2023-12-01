IMAGE_URI := "advent-of-code-2023:local"

build_image:
	echo "building image" && \
	docker build \
		--no-cache \
		-f ./Dockerfile \
		-t "{{IMAGE_URI}}" \
		.

setup_env_dev:
	pip install --upgrade pip
	pip install --prefer-binary -r ./requirements-dev.txt

setup-env:
	pip install --upgrade pip
	pip install .

run: setup-env
	PYTHONPATH="$${PWD}" python src/run.py

coverage_report: test
	@coverage html
	open ./htmlcov/index.html || echo "Done creating coverage report. Open $${PWD}/htmlcov/index.html in a web browser."

format: setup_env_dev
	ruff format .
	ruff check . --fix

lint: setup_env_dev
	ruff format . --check
	ruff check . --no-fix

test: setup_env_dev
	PYTHONPATH="`pwd`" pytest \
		-m "not integration_test" \
		--cov `pwd`/src \
		-v \
		tests/

test_and_lint_in_docker: build_image
	echo "running tests" && \
	docker run \
		-v $(pwd)/Makefile:/app/Makefile \
		-v $(pwd)/setup.cfg:/app/setup.cfg \
		-v $(pwd)/requirements-dev.txt:/app/requirements-dev.txt \
		-v $(pwd)/tests:/app/tests \
		--workdir /app \
		--entrypoint="" \
		--rm \
		-t "{{IMAGE_URI}}" \
		/bin/bash -c "apt-get update -y && apt-get install --no-install-recommends make && make setup_env_dev lint test"

integration_test: build_image
	echo "running main task" && \
	docker run \
		--rm \
		--env LOGGING_LEVEL=10 \
		-t "{{IMAGE_URI}}" \ \
		main-task && \
	echo "running integration tests" && \
	docker run \
		--rm \
		-v $(pwd)/Makefile:/app/Makefile \
		-v $(pwd)/requirements-dev.txt:/app/requirements-dev.txt \
		-v $(pwd)/tests:/app/tests \
		--entrypoint="" \
		--workdir /app \
		-t "{{IMAGE_URI}}" \
		/bin/bash -c "apt-get update -y && apt-get install --no-install-recommends make && make setup_env_dev && pytest -m 'integration_test' tests/" && \
	echo "Done running integration tests"
