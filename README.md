# gtfu

[日本語](https://github.com/seijinrosen/gtfu/blob/main/README.ja.md) |
[English](https://github.com/seijinrosen/gtfu/blob/main/README.md)

[![PyPI](https://img.shields.io/pypi/v/gtfu)](https://pypi.python.org/pypi/gtfu)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gtfu)](https://pypi.python.org/pypi/gtfu)
[![Tests](https://github.com/seijinrosen/gtfu/actions/workflows/tests.yml/badge.svg)](https://github.com/seijinrosen/gtfu/actions/workflows/tests.yml)
[![CodeQL](https://github.com/seijinrosen/gtfu/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/seijinrosen/gtfu/actions/workflows/codeql-analysis.yml)
[![codecov](https://codecov.io/gh/seijinrosen/gtfu/branch/main/graph/badge.svg)](https://codecov.io/gh/seijinrosen/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu)](https://pepy.tech/project/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu/month)](https://pepy.tech/project/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu/week)](https://pepy.tech/project/gtfu)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Command line tool to Get pageTitle From Url.

## Installation

It supports Python 3.7+.

```sh
pip install gtfu
```

## Usage

After installation, type the following command into your terminal application.

### Standard mode

```sh
gtfu https://example.com/
```

The page title will be copied to the clipboard.

- `Example Domain`

### Markdown mode

```sh
gtfu -m https://example.com/
```

The page title will be copied to the clipboard in markdown format.

- `[Example Domain](https://example.com/)`

### Prompt mode

```sh
gtfu
```

An interactive prompt will begin. You will be asked for the URL to be retrieved and whether you want it in Markdown format.
