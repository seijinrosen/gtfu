from rich.console import Console

console = Console()


def includes(args: list[str], flags: set[str]) -> bool:
    return any(s in args for s in flags)
