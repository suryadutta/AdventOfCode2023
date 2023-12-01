# Advent Of Code 2023

Code for my submissions to Advent of Code 2023 using Python 3.12

Heavily relies on the excellent AOCD package created by @wimglenn: https://github.com/wimglenn/advent-of-code-data

### Prerequisites

#### Installing `just`

`just` is a command runner. 
It is similar to `make`, but without some of the fun idiosyncrasies like `PHONY` or double escaping `$` 

Installation instructions can be found at https://github.com/casey/just#installation

For macOS + Homebrew, run

```shell
brew install just
```

#### Local development using `just`

Format code using:

```shell
just format
```

Lint code using:

```shell
just lint
```

Run unit tests using:

```shell
just test
```

Run linting and testing in Docker (also useful for CI integrations):
```shell
just test_and_lint_in_docker
```

Run integration tests:

```shell
just integration-test
```

### Running code

```shell
AOC_DAY=1 just run
```


### Submitting solutions

```shell
AOC_DAY=1 \
just submit_part_a \
just submit_part_b
```