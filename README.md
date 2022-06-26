# gtfu

[日本語(Japanese)はこちら](https://github.com/seijinrosen/gtfu/blob/main/README.ja.md)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gtfu)](https://pypi.python.org/pypi/gtfu)
[![PyPI](https://img.shields.io/pypi/v/gtfu)](https://pypi.python.org/pypi/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu)](https://pepy.tech/project/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu/month)](https://pepy.tech/project/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu/week)](https://pepy.tech/project/gtfu)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Command line tool to Get pageTitle From Url.

## Installation

It supports Python 3.9+.

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
