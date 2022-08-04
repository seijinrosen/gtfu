import pyperclip
import requests
from bs4 import BeautifulSoup

from .util import console


def get_bytes(url: str) -> bytes:
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    return response.content


def get_title(response_content: bytes) -> str:
    soup = BeautifulSoup(response_content, "lxml")
    return "" if soup.title is None else soup.title.text.strip()


def get_title_from_url(url: str, markdown: bool = False) -> str:
    response_bytes = get_bytes(url)
    title = get_title(response_bytes)
    return f"[{title}]({url})" if markdown else title


def normalize_url(user_input_url: str) -> str:
    if user_input_url.startswith(("https://", "http://")):
        return user_input_url
    return "https://" + user_input_url


def main(user_input_url: str, is_markdown: bool) -> None:
    url = normalize_url(user_input_url)
    console.print("[bold]Requesting...:", url)
    to_copied = get_title_from_url(url, is_markdown)
    console.print("Success!:thumbs_up:", style="bold green")
    pyperclip.copy(to_copied)  # type: ignore
    console.print("Copied to the clipboard:", style="bold")
    print(to_copied)
