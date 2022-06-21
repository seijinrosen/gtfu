from unittest.mock import MagicMock

from pytest import CaptureFixture, mark, raises
from readchar import key

from gtfu.cli import PROMPT_IS_MARKDOWN_MESSAGE, prompt_is_markdown


@mark.parametrize(
    ("readchar_input", "printed_answer", "expected"),
    [
        ("y", "Yes", True),
        ("", "No", False),
        ("3", "No", False),
        ("Y", "No", False),
        ("nnn", "No", False),
        (None, "No", False),
    ],
)
def test(
    readchar_input: str,
    printed_answer: str,
    expected: bool,
    mock_readchar: MagicMock,
    capsys: CaptureFixture[str],
):
    mock_readchar.return_value = readchar_input
    assert prompt_is_markdown() == expected
    out, err = capsys.readouterr()
    assert err == ""
    assert PROMPT_IS_MARKDOWN_MESSAGE in out
    assert printed_answer in out


@mark.parametrize(
    ("interrupt_key", "exception"),
    [
        (key.CTRL_C, KeyboardInterrupt),
        (key.CTRL_D, EOFError),
    ],
)
def test_raise_exception(
    interrupt_key: str,
    exception: type,
    mock_readchar: MagicMock,
    capsys: CaptureFixture[str],
):
    mock_readchar.return_value = interrupt_key
    with raises(exception):
        assert prompt_is_markdown() is None
    out, err = capsys.readouterr()
    assert err == ""
    assert PROMPT_IS_MARKDOWN_MESSAGE in out
    assert all(x not in out for x in {"Yes", "No"})
