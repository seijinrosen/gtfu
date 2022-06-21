from pytest import CaptureFixture

from gtfu.cli import HELP_MESSAGE, print_help_message


def test(capsys: CaptureFixture[str]):
    print_help_message()
    out, err = capsys.readouterr()
    assert err == ""
    assert out == HELP_MESSAGE + "\n"
