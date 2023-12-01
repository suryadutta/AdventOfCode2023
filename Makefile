VERSION ?= local
IMAGE_REPOSITORY=canary-python
IMAGE_URI=$(IMAGE_REPOSITORY):$(VERSION)

.PHONY: build_image
build_image:
	echo "building image" && \
	docker build \
		--no-cache \
		-f ./Dockerfile \
		-t "${IMAGE_URI}" \
		.

.PHONY: run
run: setup-env
	PYTHONPATH="$${PWD}" python src/run.py

.PHONY: coverage_report
coverage_report: test
	@coverage html
	open ./htmlcov/index.html || echo "Done creating coverage report. Open $${PWD}/htmlcov/index.html in a web browser."

.PHONY: format
format: setup_env_dev
	ruff format .
	ruff check . --fix

.PHONY: lint
lint: setup_env_dev
	ruff format . --check
	ruff check . --no-fix

.PHONY: setup_env_dev
setup_env_dev:
	pip install --upgrade pip
	pip install --prefer-binary -r ./requirements-dev.txt

.PHONY: test
test: setup_env_dev
	PYTHONPATH="$${PWD}" pytest \
		-m "not integration_test" \
		--cov $${PWD}/src \
		-v \
		tests/

.PHONY: test_and_lint_in_docker
test_and_lint_in_docker: build_image
	echo "running tests" && \
	docker run \
		-v $$(pwd)/Makefile:/app/Makefile \
		-v $$(pwd)/setup.cfg:/app/setup.cfg \
		-v $$(pwd)/requirements-dev.txt:/app/requirements-dev.txt \
		-v $$(pwd)/tests:/app/tests \
		--workdir /app \
		--entrypoint="" \
		--rm \
		-t "${IMAGE_URI}" \
		/bin/bash -c "apt-get update -y && apt-get install --no-install-recommends make && make setup_env_dev lint test"
