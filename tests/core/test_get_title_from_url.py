from pytest import mark

from gtfu.core import get_title_from_url


@mark.parametrize(
    ("url", "markdown", "expected"),
    [
        ("https://example_url", False, "Example Title"),
        ("https://example_url", True, "[Example Title](https://example_url)"),
        ("http://example_url", False, "Example Title"),
        ("http://example_url", True, "[Example Title](http://example_url)"),
    ],
)
def test(url: str, markdown: bool, expected: str):
    assert get_title_from_url(url, markdown) == expected
