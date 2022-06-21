from gtfu.core import get_bytes

from ..conftest import Example


def test():
    assert get_bytes(Example.URL_HTTPS) == Example.HTML_BYTES
