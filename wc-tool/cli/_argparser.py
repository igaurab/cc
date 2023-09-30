from collections import namedtuple
import sys
from io import TextIOWrapper
import argparse
from dataclasses import dataclass
from typing import Iterator

@dataclass
class HelpText:
    COUNT: str = "Number of bytes"
    WORDS: str = "Number of words"
    LINE: str = "Number of lines"
    CHARACTER: str = "Number of characters"

@dataclass
class Args:
    file_content: Iterator[str]
    count: bool = False
    words: bool = False
    line: bool = False
    characters: bool = False
    filename: str = "<stdin>"

    @property
    def flags(self):
        return (
            self.count,
            self.words,
            self.line,
            self.characters
        )

def read_textio_wrapper(file: TextIOWrapper):
    if not file.readable():
        raise ValueError("File exhausted!")
    for line in file:
        yield line
    file.close()

parser = argparse.ArgumentParser(
    prog='ccwc',
    description='wc written in python',
    epilog=''
)

# https://stackoverflow.com/questions/7576525/optional-stdin-in-python-with-argparse
parser.add_argument("filename", nargs="?", type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
parser.add_argument('-c', '--count', action="store_true", help=HelpText.COUNT)
parser.add_argument('-w', '--words', action="store_true", help=HelpText.WORDS)
parser.add_argument('-l', '--line', action="store_true", help=HelpText.LINE)
parser.add_argument('-m', '--character', action="store_true", help=HelpText.CHARACTER)


_args = parser.parse_args()

filename = _args.filename.name

from functools import partial
file_content = partial(read_textio_wrapper,file=_args.filename)

args = Args(
    file_content=file_content,
    filename=filename,
    count=_args.count,
    words=_args.words,
    line=_args.line,
    characters=_args.character
)