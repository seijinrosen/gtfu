from unittest.mock import MagicMock

from pytest import CaptureFixture, mark, raises

from gtfu.cli import PROMPT_MESSAGE, prompt

from ..conftest import Example


@mark.parametrize(
    (
        "is_markdown",
        "prompt_url_return_value",
        "prompt_is_markdown_return_value",
        "expected",
    ),
    [
        (True, Example.URL_HTTPS, None, (Example.URL_HTTPS, True)),
        (True, Example.URL_HTTPS, None, (Example.URL_HTTPS, True)),
        (False, Example.URL_HTTPS, True, (Example.URL_HTTPS, True)),
        (False, Example.URL_HTTPS, False, (Example.URL_HTTPS, False)),
    ],
)
def test(
    is_markdown: bool,
    prompt_url_return_value: str,
    prompt_is_markdown_return_value: bool,
    expected: tuple[str, bool],
    mock_prompt_url: MagicMock,
    mock_prompt_is_markdown: MagicMock,
    capsys: CaptureFixture[str],
):
    mock_prompt_url.return_value = prompt_url_return_value
    mock_prompt_is_markdown.return_value = prompt_is_markdown_return_value
    assert prompt(is_markdown) == expected
    assert mock_prompt_url.call_count == 1
    assert mock_prompt_is_markdown.call_count == (0 if is_markdown else 1)
    out, err = capsys.readouterr()
    assert err == ""
    assert PROMPT_MESSAGE in out


@mark.parametrize(
    ("is_markdown", "prompt_url_exception", "prompt_is_markdown_exception"),
    [
        (True, KeyboardInterrupt, None),
        (True, EOFError, None),
        (False, KeyboardInterrupt, None),
        (False, EOFError, None),
        (False, None, KeyboardInterrupt),
        (False, None, EOFError),
    ],
)
def test_interrupt(
    is_markdown: bool,
    prompt_url_exception: type,
    prompt_is_markdown_exception: type,
    mock_prompt_url: MagicMock,
    mock_prompt_is_markdown: MagicMock,
    capsys: CaptureFixture[str],
):
    mock_prompt_url.side_effect = prompt_url_exception
    mock_prompt_is_markdown.side_effect = prompt_is_markdown_exception
    with raises(SystemExit):
        assert prompt(is_markdown) is None
    out, err = capsys.readouterr()
    assert err == ""
    assert PROMPT_MESSAGE in out
