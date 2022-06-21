from pytest import mark

from gtfu.core import get_title

from ..conftest import Example


@mark.parametrize(
    ("response_content", "expected"),
    [
        (Example.HTML_BYTES, Example.TITLE),
        ("", ""),
    ],
)
def test(response_content: bytes, expected: str):
    assert get_title(response_content) == expected
