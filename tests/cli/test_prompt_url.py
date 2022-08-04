from unittest.mock import MagicMock

from pytest import CaptureFixture, mark

from gtfu.cli import PROMPT_URL_MESSAGE, prompt_url


@mark.parametrize(
    ("console_input_return_value", "expected"),
    [
        ("https://example_url", "https://example_url"),
        (f" 　\n\f\t\v\r{'https://example_url'} 　\n\f\t\v\r", "https://example_url"),
    ],
)
def test(
    console_input_return_value: str,
    mock_console_input: MagicMock,
    expected: str,
    capsys: CaptureFixture[str],
):
    mock_console_input.return_value = console_input_return_value
    assert prompt_url() == expected
    out, err = capsys.readouterr()
    assert err == ""
    assert PROMPT_URL_MESSAGE in out
