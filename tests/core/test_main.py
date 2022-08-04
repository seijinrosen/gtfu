import pyperclip
from pytest import CaptureFixture, mark

from gtfu.core import main


@mark.parametrize(
    (
        "user_input_url",
        "is_markdown",
        "normalized_url",
        "clipboard",
    ),
    [
        (
            "https://example_url",
            False,
            "https://example_url",
            "Example Title",
        ),
        (
            "https://example_url",
            True,
            "https://example_url",
            "[Example Title](https://example_url)",
        ),
        (
            "http://example_url",
            False,
            "http://example_url",
            "Example Title",
        ),
        (
            "http://example_url",
            True,
            "http://example_url",
            "[Example Title](http://example_url)",
        ),
        (
            "example_url",
            False,
            "https://example_url",
            "Example Title",
        ),
        (
            "example_url",
            True,
            "https://example_url",
            "[Example Title](https://example_url)",
        ),
    ],
)
def test(
    user_input_url: str,
    is_markdown: bool,
    normalized_url: str,
    clipboard: str,
    capsys: CaptureFixture[str],
):
    assert main(user_input_url, is_markdown) is None
    out, err = capsys.readouterr()
    assert err == ""
    assert normalized_url in out
    assert "Success" in out
    assert clipboard in out
    assert clipboard == pyperclip.paste()
