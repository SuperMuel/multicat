#!/usr/bin/env python


from typing import Iterable, Optional
import typer
from pathlib import Path
import pyperclip
import mimetypes


IGNORE = [
    "node_modules",
    "venv",
    "env",
    ".git",
    ".vscode",
    ".idea",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".eggs",
    ".venv",
    ".nox",
    ".cache",
    ".serverless",
    ".serverless_plugins",
]


def should_ignore(path: Path) -> bool:
    """Check if the path should be ignored based on the IGNORE list."""
    for part in path.parts:
        if part in IGNORE:
            return True
    return False


app = typer.Typer()


def list_text_files(base_path: Path, max_depth: Optional[int] = None) -> Iterable[Path]:
    """Recursively list all text files in a directory up to a maximum depth, excluding ignored paths."""
    if not base_path.exists() or not base_path.is_dir():
        typer.echo("Error: Specified path is invalid or not a directory", err=True)
        raise typer.Exit(code=1)

    text_files = []
    for path in base_path.rglob("*"):
        if should_ignore(path) or not is_text_file(path):
            continue
        relative_depth = len(path.relative_to(base_path).parts)
        if max_depth is None or relative_depth <= max_depth:
            text_files.append(path)
    return text_files


def is_text_file(path: Path) -> Optional[bool]:
    """Check if a file is a text file.

    Returns True if the file is a text file, False if it is not, and None if the file type cannot be determined.
    """
    if not path.is_file():
        return False
    _type, encoding = mimetypes.guess_type(path)

    if not _type:
        return None

    return "text" in _type


def read_file_contents(file_path: Path) -> str:
    """Read and return the contents of a text file."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        typer.echo(f"Error reading file {file_path}: {e}", err=True)
        raise typer.Exit(code=1)


def format_file_contents(file_path: Path, contents: str) -> str:
    """Format the contents of a text file."""
    return f"File: {file_path}\n\n{contents}\n\n{'-'*50}\n"


@app.command()
def main(
    directory: str = typer.Argument(
        ".", help="The directory to search for text files."
    ),
    copy: bool = typer.Option(False, "--copy", "-c"),
    max_depth: Optional[int] = typer.Option(
        None, "--max-depth", "-d", help="Maximum depth of subdirectories to search."
    ),
):
    """Concatenate the contents of all text files in a directory."""
    path = Path(directory)

    text_files = [
        file for file in list_text_files(path, max_depth) if is_text_file(file)
    ]

    if not text_files:
        typer.echo(f"No text files found in {path}")
        raise typer.Exit(code=0)

    contents = {}

    for file in text_files:
        try:
            contents[file] = read_file_contents(file)
        except Exception as e:
            typer.echo(f"Error reading file {file}: {e}", err=True)
            contents[file] = None

    formatted_contents = [
        format_file_contents(file, contents[file])
        for file in text_files
        if contents[file]
    ]

    concatenated_contents = "\n".join(formatted_contents)

    if copy:
        pyperclip.copy(concatenated_contents)
        typer.echo("Concatenated contents copied to clipboard")
    else:
        typer.echo(concatenated_contents)


if __name__ == "__main__":
    app()
