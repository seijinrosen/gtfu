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

URL からページタイトルを取得するスクリプトです。`gtfu` は Get Title From Url の略です。

## インストール

Python 3.7 以上で利用可能です。
ターミナルアプリに以下のコマンドを入力してください。

```sh
pip install gtfu
```

## 使い方

インストールに成功したら、以下のコマンドをターミナルアプリに入力してください。

### 通常モード

```sh
gtfu https://example.com/
```

ページタイトルがクリップボードにコピーされます。

- `Example Domain`

### Markdown モード

```sh
gtfu -m https://example.com/
```

ページタイトルと URL が、Markdown 形式でクリップボードにコピーされます。

- `[Example Domain](https://example.com/)`

### 対話モード

```sh
gtfu
```

対話形式のプロンプトを開始します。取得対象の URL と、Markdown 形式にするかどうかを聞かれます。
