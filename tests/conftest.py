from pathlib import Path
from typing import Any, Callable
from unittest.mock import create_autospec

from pytest import fixture
from pytest_mock import MockerFixture
from requests.models import Response

from gtfu.__main__ import cli

EXAMPLE_HTML_PATH = Path("tests/example.html")
EXAMPLE_HTML_BYTES = EXAMPLE_HTML_PATH.read_bytes()


def get_namespace(func: Callable[..., Any]) -> str:
    return func.__module__ + "." + func.__name__


@fixture(autouse=True)
def mock_requests_get(mocker: MockerFixture):
    mock_response = create_autospec(Response)
    mock_response.content = EXAMPLE_HTML_BYTES
    mock_requests_get = mocker.patch("requests.get", autospec=True)
    mock_requests_get.return_value = mock_response


@fixture
def mock_cli_main(mocker: MockerFixture):
    yield mocker.patch.object(cli, cli.main.__name__, autospec=True)
