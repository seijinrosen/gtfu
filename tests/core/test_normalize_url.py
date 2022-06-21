from pytest import mark

from gtfu.core import normalize_url

from ..conftest import Example


@mark.parametrize(
    ("user_input_url", "expected"),
    [
        ("example_url", Example.URL_HTTPS),
        (Example.URL_WITHOUT_SCHEME, Example.URL_HTTPS),
        ("http://example_url", Example.URL_HTTP),
        (Example.URL_HTTP, Example.URL_HTTP),
        ("https://example_url", Example.URL_HTTPS),
        (Example.URL_HTTPS, Example.URL_HTTPS),
    ],
)
def test(user_input_url: str, expected: str):
    assert normalize_url(user_input_url) == expected
