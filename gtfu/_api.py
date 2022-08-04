from .core import get_title_from_url, normalize_url


def get(url: str, markdown: bool = False) -> str:
    """
    Get title from URL.
    """
    normalized_url = normalize_url(url)
    return get_title_from_url(normalized_url, markdown)
