# ppt (package pptm)

[![PyPI](https://img.shields.io/pypi/v/pptm?style=flat-square)](https://pypi.python.org/pypi/pptm/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pptm?style=flat-square)](https://pypi.python.org/pypi/pptm/)
[![PyPI - License](https://img.shields.io/pypi/l/pptm?style=flat-square)](https://pypi.python.org/pypi/pptm/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://Michael-Cohen.github.io/ppt](https://Michael-Cohen.github.io/ppt)

**Source Code**: [https://github.com/Michael-Cohen/ppt](https://github.com/Michael-Cohen/ppt)

**PyPI**: [https://pypi.org/project/pptm/](https://pypi.org/project/pptm/)

---

A short description of the project

## Installation

```sh
pip install pptm
```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/Michael-Cohen/ppt/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/Michael-Cohen/ppt/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/Michael-Cohen/ppt/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

Install `pre-commit` with:
```sh
poetry add pre-commit
```


You can then install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

Because the pre-commit includes a hook for commit messages (`commitizen`), you should also run:
```sh
pre-commit install --hook-type commit-msg 
```

---

This project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
