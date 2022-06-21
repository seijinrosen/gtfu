import pyperclip
from pytest import CaptureFixture, mark

from gtfu.core import main

from ..conftest import Example


@mark.parametrize(
    ("user_input_url", "is_markdown", "normalized_url", "clipboard"),
    [
        (Example.URL_HTTPS, False, Example.URL_HTTPS, Example.TITLE),
        (Example.URL_HTTPS, True, Example.URL_HTTPS, Example.MARKDOWN_HTTPS),
        (Example.URL_HTTP, False, Example.URL_HTTP, Example.TITLE),
        (Example.URL_HTTP, True, Example.URL_HTTP, Example.MARKDOWN_HTTP),
        (Example.URL_WITHOUT_SCHEME, False, Example.URL_HTTPS, Example.TITLE),
        (Example.URL_WITHOUT_SCHEME, True, Example.URL_HTTPS, Example.MARKDOWN_HTTPS),
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
    assert clipboard == pyperclip.paste()
