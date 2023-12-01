# Advent Of Code 2023

Code for my submissions to Advent of Code 2023 using Python 3.12

Heavily relies on the excellent AOCD package created by @wimglenn: https://github.com/wimglenn/advent-of-code-data

#### Local development

Format code using:

```shell
make format
```

Lint code using:

```shell
make lint
```

Run unit tests using:

```shell
make test
```

Run linting and testing in Docker (also useful for CI integrations):
```shell
make test_and_lint_in_docker
```

Run integration tests:

```shell
make integration-test
```

### Running code

```shell
AOC_DAY=1 make run
```


### Submitting solutions

```shell
AOC_DAY=1 \
make submit_part_a \
make submit_part_b
```