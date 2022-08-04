from pytest import mark

from gtfu.core import get_title

from ..conftest import EXAMPLE_HTML_BYTES


@mark.parametrize(
    ("response_content", "expected"),
    [
        (EXAMPLE_HTML_BYTES, "Example Title"),
        (b"", ""),
    ],
)
def test(response_content: bytes, expected: str):
    assert get_title(response_content) == expected
