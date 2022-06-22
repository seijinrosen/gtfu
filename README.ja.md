# gtfu

[English ver.](https://github.com/seijinrosen/gtfu/blob/main/README.md)

[![Downloads](https://pepy.tech/badge/gtfu)](https://pepy.tech/project/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu/month)](https://pepy.tech/project/gtfu)
[![Downloads](https://pepy.tech/badge/gtfu/week)](https://pepy.tech/project/gtfu)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

URLからページタイトルを取得するスクリプトです。`gtfu` は Get Title From Url の略です。

## インストール

Python 3.9 以上で利用可能です。
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

### Markdownモード

```sh
gtfu -m https://example.com/
```

ページタイトルとURLが、Markdown形式でクリップボードにコピーされます。

- `[Example Domain](https://example.com/)`

### 対話モード

```sh
gtfu
```

対話形式のプロンプトを開始します。取得対象のURLと、Markdown形式にするかどうかを聞かれます。
