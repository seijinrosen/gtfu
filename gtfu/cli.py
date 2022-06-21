import sys
from itertools import filterfalse

from readchar import key, readchar

from . import __version__, core
from .util import console, includes

HELP_MESSAGE = """\
Get Title From URL

See https://github.com/seijinrosen/gtfu for usage.\
"""
EXIT_MESSAGE = "\nBye."
PROMPT_MESSAGE = "Ctrl+C か Ctrl+D で中断します"
PROMPT_URL_MESSAGE = "Enter URL: "
PROMPT_IS_MARKDOWN_MESSAGE = "マークダウン形式でコピーしますか？ (y/N): "

HELP_FLAGS = {"-h", "--help", "help"}
VERSION_FLAGS = {"-V", "--version", "version"}
MARKDOWN_FLAGS = {"-m", "--markdown"}


def print_help_message() -> None:
    console.print(HELP_MESSAGE)


def print_version() -> None:
    console.print(__version__)


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
