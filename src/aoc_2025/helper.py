from collections import abc
import io
import os
import contextlib


@contextlib.contextmanager
def file_opener(filename: str) -> abc.Iterator[io.TextIOWrapper]:
    with open(os.path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        yield file


