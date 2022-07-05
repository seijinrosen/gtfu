from pytest import CaptureFixture

from gtfu.cli import print_help_message


def test(capsys: CaptureFixture[str]):
    print_help_message()
    out, err = capsys.readouterr()
    assert err == ""
    assert "See https://github.com/seijinrosen/gtfu for more information." in out
