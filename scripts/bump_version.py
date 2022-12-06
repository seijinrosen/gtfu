import subprocess
from pathlib import Path

import pyperclip

target_files = [
    ".github/workflows/python-publish.yml",
    "gtfu/__init__.py",
    "tests/test_gtfu.py",
    "Makefile",
    "pyproject.toml",
]

current_version = subprocess.run(
    ["poetry", "version"], capture_output=True, check=True, text=True
).stdout.split()[1]

print("current_version:", current_version)

new_version = input("? new_version: ")

for file in target_files:
    p = Path(file)
    p.write_text(p.read_text().replace(current_version, new_version))

commit_message = f"Bump version from {current_version} to {new_version}"
pyperclip.copy(commit_message)  # type: ignore
print("Copied:", commit_message)
