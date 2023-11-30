# Canary Python Project

A generic template project for writing Python tasks 

## Getting Started

### Recommended: Use `just`

`just` is a command runner. 
It is similar to `make`, but without some of the fun idiosyncrasies like `PHONY` or double escaping `$` 

#### Installing `just`

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


### Alternative: Use `make`

If you would rather use `make`, this is supported as well:


Format code using:

```shell
make test
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
