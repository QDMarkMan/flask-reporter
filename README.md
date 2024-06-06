# Hey, Look at me! 👇

**Please delete this part after you read it.**

If you are first create this repository, please read [DELETE_ME.md](./DELETE_ME.md) to get started.

# rgp

<div align="center">

[![Build status](https://github.com/rgp/rgp/workflows/build/badge.svg?branch=main&event=push)](https://github.com/rgp/rgp/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/rgp.svg)](https://pypi.org/project/rgp/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/rgp/rgp/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/rgp/rgp/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/rgp/rgp/releases)
[![License](https://img.shields.io/github/license/rgp/rgp)](https://github.com/rgp/rgp/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Report generate  platform

</div>

## 🎯 Tech Stack

- [`Typer`](https://github.com/tiangolo/typer) is great for creating CLI applications.
- [`Rich`](https://github.com/willmcgugan/rich) makes it easy to add beautiful formatting in the terminal.
- [`Pydantic`](https://github.com/samuelcolvin/pydantic/) – data validation and settings management using Python type hinting.
- [`Loguru`](https://github.com/Delgan/loguru) makes logging (stupidly) simple.
- [`tqdm`](https://github.com/tqdm/tqdm) – fast, extensible progress bar for Python and CLI.
- [`IceCream`](https://github.com/gruns/icecream) is a little library for sweet and creamy debugging.
- [`orjson`](https://github.com/ijl/orjson) – ultra fast JSON parsing library.
- [`Returns`](https://github.com/dry-python/returns) makes you function's output meaningful, typed, and safe!
- [`Hydra`](https://github.com/facebookresearch/hydra) is a framework for elegantly configuring complex applications.
- [`FastAPI`](https://github.com/tiangolo/fastapi) is a type-driven asynchronous web framework.

## 1. Prepare environment

### 1.1. Initialize your code

1. Initialize `git` inside your repo:

```bash
cd rgp && git init
```

2. If you don't have `Poetry`. 

Conda environment is is recommended.

```bash
conda create -n rgp python==3.10
```

Please activate python of current project and install run:

```bash
conda activate rgp
pip install poetry
```

3. Initialize poetry and `pre-commit` hooks:

```bash
make install
```

If you obtain a timeout error when installing, you can try to append an image source config in `poetry.toml`. The following example is tsinghua image source.

```toml
[[tool.poetry.source]]
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
priority = "default"
```

4. Run the codestyle to polish your code:

```bash
make polish-codestyle
```

## Quick start

Conda package manager is recommended. Create a conda environment.

```bash
conda create -n rgp python==3.10
```

Activate conda environment and install poetry

```bash
conda activate rgp
pip install poetry
```

Then you can run the client using the following command:

```bash
rgp --help
```

or with `Poetry`:

```bash
poetry run rgp --help
```

### Makefile usage

[`Makefile`](https://github.com/rgp/rgp/blob/main/Makefile) contains a lot of functions for faster development.


<details>
<summary>Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>Codestyle and type checks</summary>
<p>

Automatic formatting uses `ruff`.

```bash
make polish-codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `ruff` and `darglint` library

</p>
</details>

<details>
<summary>Code security</summary>
<p>

> If this command is not selected during installation, it cannnot be used.

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>All linters</summary>
<p>

Of course there is a command to run all linters in one:

```bash
make lint
```

the same as:

```bash
make check-codestyle && make test && make check-safety
```

</p>
</details>

<details>
<summary>Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/Undertone0809/python-package-template/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

</p>
</details>

<details>
<summary>Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 🛡 License

[![License](https://img.shields.io/github/license/rgp/rgp)](https://github.com/rgp/rgp/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/rgp/rgp/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{rgp,
  author = {rgp},
  title = {Report generate  platform},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/rgp/rgp}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/P3G-%F0%9F%9A%80-brightgreen)](https://github.com/Undertone0809/python-package-template)

This project was generated with [P3G](https://github.com/Undertone0809/P3G)
