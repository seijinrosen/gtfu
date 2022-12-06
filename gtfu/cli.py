from __future__ import annotations

import platform
import sys
from itertools import filterfalse
from pathlib import Path

from readchar import key, readchar

from . import __version__, core
from .util import console, includes

HELP_MESSAGE = """\
Command line tool to Get pageTitle From Url.

[bold]Usage:[/bold]
  gtfu https://example.com/
  gtfu https://example.com/ -m
  gtfu
  gtfu -h
  gtfu -V

[bold]Options:[/bold]
  [blue]-m, --markdown[/blue]  The page title will be copied to the clipboard in markdown format.

[bold]Global options:[/bold]
  [blue]-h, --help[/blue]      Show this help message and exit.
  [blue]-V, --version[/blue]   Show program's version number and exit.

See https://github.com/seijinrosen/gtfu for more information.\
"""
EXIT_MESSAGE = "\nBye."
PROMPT_MESSAGE = "Ctrl+C or Ctrl+D to abort."
PROMPT_URL_MESSAGE = "Enter URL: "
PROMPT_IS_MARKDOWN_MESSAGE = "In markdown? (y/N): "

HELP_FLAGS = {"-h", "--help", "help"}
VERSION_FLAGS = {"-V", "--version", "version"}
MARKDOWN_FLAGS = {"-m", "--markdown"}


def print_help_message() -> None:
    console.print(HELP_MESSAGE)


def print_version() -> None:
    console.print("gtfu:  ", __version__)
    console.print("Python:", platform.python_version())
    console.print("from:  ", Path(__file__).parent)


def prompt(is_markdown: bool) -> tuple[str, bool]:
    console.print(PROMPT_MESSAGE)
    try:
        user_input_url = prompt_url()
        is_markdown = prompt_is_markdown() if not is_markdown else True
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)
        sys.exit()
    return user_input_url, is_markdown


def prompt_url() -> str:
    url = ""
    while url == "":
        console.print(PROMPT_URL_MESSAGE, end="", style="bold blue")
        url = console.input().strip()
    return url


def prompt_is_markdown() -> bool:
    console.print(PROMPT_IS_MARKDOWN_MESSAGE, end="", style="bold blue")
    # Match statements require Python 3.10 or newer
    ch = readchar()
    if ch == key.CTRL_C:
        raise KeyboardInterrupt
    if ch == key.CTRL_D:
        raise EOFError
    is_y = ch == "y"
    # match readchar():
    #     case key.CTRL_C:
    #         raise KeyboardInterrupt
    #     case key.CTRL_D:
    #         raise EOFError
    #     case ch:
    #         is_y = ch == "y"
    console.print("Yes" if is_y else "No")
    return is_y


def main(args: list[str]) -> None:
    if includes(args, HELP_FLAGS):
        print_help_message()
        return
    if includes(args, VERSION_FLAGS):
        print_version()
        return

    user_input_url = next(filterfalse(lambda x: x.startswith("-"), args), "")
    is_markdown = includes(args, MARKDOWN_FLAGS)
    if user_input_url == "":
        user_input_url, is_markdown = prompt(is_markdown)

    core.main(user_input_url, is_markdown)
