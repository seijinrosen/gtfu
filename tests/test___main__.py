from unittest.mock import MagicMock

from gtfu.__main__ import main


def test_main(mock_cli_main: MagicMock):
    assert main() is None
    assert mock_cli_main.call_count == 1
