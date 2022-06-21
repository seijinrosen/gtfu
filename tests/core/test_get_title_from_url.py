from pytest import mark

from gtfu.core import get_title_from_url

from ..conftest import Example


@mark.parametrize(
    ("url", "markdown", "expected"),
    [
        (Example.URL_HTTPS, False, Example.TITLE),
        (Example.URL_HTTPS, True, Example.MARKDOWN_HTTPS),
        (Example.URL_HTTP, False, Example.TITLE),
        (Example.URL_HTTP, True, Example.MARKDOWN_HTTP),
    ],
)
def test(url: str, markdown: bool, expected: str):
    assert get_title_from_url(url, markdown) == expected
