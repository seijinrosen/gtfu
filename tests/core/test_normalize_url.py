from pytest import mark

from gtfu.core import normalize_url

URL_BODY = "example_url"
HTTP = "http://"
HTTPS = "https://"


@mark.parametrize(
    ("user_input_url", "expected"),
    [
        (URL_BODY, HTTPS + URL_BODY),
        (HTTP + URL_BODY, HTTP + URL_BODY),
        (HTTPS + URL_BODY, HTTPS + URL_BODY),
    ],
)
def test(user_input_url: str, expected: str):
    assert normalize_url(user_input_url) == expected
