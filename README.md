# gtfu

Command line tool to Get pageTitle From Url.

## Installation

It supports Python 3.9+.

```sh
pip install gtfu
```

## Usage

After installation, type the following command into your terminal application.

- ```sh
  gtfu https://example.com/
  ```

  The page title will be copied to the clipboard.
  - `Example Domain`

- ```sh
  gtfu -m https://example.com/
  ```

  The page title will be copied to the clipboard in markdown format.
  - `[Example Domain](https://example.com/)`

- ```sh
  gtfu
  ```

  An interactive prompt will begin.
