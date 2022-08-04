from gtfu.core import get_bytes

from ..conftest import EXAMPLE_HTML_BYTES


def test():
    assert get_bytes("https://example_url") == EXAMPLE_HTML_BYTES
