from pathlib import Path
from inspect import signature
from typing import Callable


def file_ext(filename: str) -> str:
    return filename.split(".")[-1]


def enpath(path: str | Path) -> Path:
    return Path(path) if isinstance(path, str) else path


def get_doc(value: any) -> str:
    return value.__doc__ if value.__doc__ else ""


def inspect_function(f: Callable):
    doc = get_doc(f)
    return "\n".join([doc, f"{f.__name__}{str(signature(f))}"]).strip()
