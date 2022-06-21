# gtfu

[English ver.](https://github.com/seijinrosen/gtfu/blob/main/README.md)
URLからページタイトルを取得するスクリプトです。
`gtfu` は Get Title From Url の略です。

## インストール

Python 3.9 以上で利用可能です。
ターミナルアプリに以下のコマンドを入力してください。

```sh
pip install gtfu
```

## 使い方

インストールに成功したら、以下のコマンドをターミナルアプリに入力してください。

- ```sh
  gtfu https://example.com/
  ```

  ページタイトルがクリップボードにコピーされます。
  - `Example Domain`

- ```sh
  gtfu -m https://example.com/
  ```

  ページタイトルとURLが、Markdown形式でクリップボードにコピーされます。
  - `[Example Domain](https://example.com/)`

- ```sh
  gtfu
  ```

  対話形式のプロンプトを開始します。
  取得対象のURLと、Markdown形式にするかどうかを聞かれます。
