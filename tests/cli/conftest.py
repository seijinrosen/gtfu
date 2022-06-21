from pytest import fixture
from pytest_mock import MockerFixture
from rich.console import Console

from gtfu import cli
from gtfu.cli import (
    core,
    print_help_message,
    print_version,
    prompt,
    prompt_is_markdown,
    prompt_url,
)

from ..conftest import get_namespace


@fixture(autouse=True)
def mock_console(mocker: MockerFixture):
    yield mocker.patch.object(cli, "console", new=Console(color_system=None))


@fixture
def mock_console_input(mock_console: Console, mocker: MockerFixture):
    yield mocker.patch.object(mock_console, "input", autospec=True)


@fixture
def mock_readchar(mocker: MockerFixture):
    yield mocker.patch.object(cli, "readchar", autospec=True)


@fixture
def mock_core_main(mocker: MockerFixture):
    yield mocker.patch.object(core, core.main.__name__, autospec=True)


@fixture
def mock_print_help_message(mocker: MockerFixture):
    yield mocker.patch(get_namespace(print_help_message), autospec=True)


@fixture
def mock_print_version(mocker: MockerFixture):
    yield mocker.patch(get_namespace(print_version), autospec=True)


@fixture
def mock_prompt_is_markdown(mocker: MockerFixture):
    yield mocker.patch(get_namespace(prompt_is_markdown), autospec=True)


@fixture
def mock_prompt_url(mocker: MockerFixture):
    yield mocker.patch(get_namespace(prompt_url), autospec=True)


@fixture
def mock_prompt(mocker: MockerFixture):
    yield mocker.patch(get_namespace(prompt), autospec=True)
