from pytest import CaptureFixture

from gtfu import __version__
from gtfu.cli import print_version


def test(capsys: CaptureFixture[str]):
    print_version()
    out, err = capsys.readouterr()
    assert err == ""
    assert "gtfu:" in out
    assert "Python:" in out
    assert "from:" in out
