from itertools import combinations, permutations
from unittest.mock import MagicMock

from pytest import mark

from gtfu.cli import HELP_FLAGS, MARKDOWN_FLAGS, main

from ..conftest import Example


@mark.parametrize(
    ("prompt_return_value"),
    [
        (Example.URL_HTTPS, True),
        (Example.URL_HTTPS, False),
    ],
)
def test_with_no_arguments(
    prompt_return_value: tuple[str, bool],
    mock_print_help_message: MagicMock,
    mock_prompt: MagicMock,
    mock_core_main: MagicMock,
):
    mock_prompt.return_value = prompt_return_value
    assert main([]) is None
    assert mock_print_help_message.call_count == 0
    mock_prompt.assert_called_once_with(False)
    mock_core_main.assert_called_once_with(*prompt_return_value)


def test_with_help_option(
    mock_print_help_message: MagicMock,
    mock_prompt: MagicMock,
    mock_core_main: MagicMock,
):
    cnt = 0
    other_options = [Example.URL_HTTPS, *MARKDOWN_FLAGS]
    for help_option in HELP_FLAGS:
        for i in range(len(other_options) + 1):
            for comb in combinations(other_options, i):
                for perm in permutations([*comb, help_option]):
                    assert main(list(perm)) is None
                    cnt += 1
    assert mock_print_help_message.call_count == cnt
    assert mock_prompt.call_count == 0
    assert mock_core_main.call_count == 0


def test_with_version_flag(mock_print_version: MagicMock):
    main(["-V"])
    main(["--version"])
    main(["version"])
    assert mock_print_version.call_count == 3


def test_with_markdown_option(
    mock_print_help_message: MagicMock, mock_core_main: MagicMock
):
    args = [Example.URL_WITHOUT_SCHEME, "-m"]
    assert main(args) is None
    mock_core_main.assert_called_once_with(Example.URL_WITHOUT_SCHEME, True)
    assert mock_print_help_message.call_count == 0


def test_with_one_argument(
    mock_print_help_message: MagicMock,
    mock_core_main: MagicMock,
    mock_prompt_url: MagicMock,
):
    assert main([Example.URL_WITHOUT_SCHEME]) is None
    assert not mock_prompt_url.called
    mock_print_help_message.assert_not_called()
    mock_core_main.assert_called_once_with(Example.URL_WITHOUT_SCHEME, False)


def test_with_invalid_but_ok_argument(
    mock_prompt_url: MagicMock,
    mock_print_help_message: MagicMock,
    mock_core_main: MagicMock,
):
    args = [Example.URL_WITHOUT_SCHEME, "-m", "--markdown"]
    assert main(args) is None
    assert mock_print_help_message.call_count == 0
    assert mock_prompt_url.call_count == 0
    mock_core_main.assert_called_once_with(Example.URL_WITHOUT_SCHEME, True)
