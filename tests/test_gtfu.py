from pytest import mark

import gtfu


def test_version():
    assert gtfu.__version__ == "1.3.0"


@mark.parametrize(
    ("url", "markdown", "expected"),
    [
        ("https://example_url", True, "[Example Title](https://example_url)"),
        ("https://example_url", False, "Example Title"),
    ],
)
def test_get(url: str, markdown: bool, expected: str):
    assert gtfu.get(url, markdown) == expected


@mark.parametrize(
    ("url", "expected"),
    [
        ("https://example_url", "Example Title"),
        ("example_url", "Example Title"),
    ],
)
def test_get_only_url(url: str, expected: str):
    assert gtfu.get(url) == expected
