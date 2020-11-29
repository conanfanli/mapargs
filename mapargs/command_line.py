import argparse
from dataclasses import dataclass
import io
import re
import sys
from typing import Iterator

PYTHON = re.compile(r"(\w+):.*")

GO = re.compile(r"(\w+) +.*")


@dataclass
class CommandLineOptions:
    infile: io.TextIOWrapper


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mapargs")
    parser.add_argument("infile", type=argparse.FileType("r"), default=sys.stdin)
    return parser


def parse_command_line() -> CommandLineOptions:
    parser = get_parser()
    options = parser.parse_args()

    return CommandLineOptions(infile=options.infile)


def generate_code(infile: io.TextIOWrapper) -> Iterator[str]:
    lines = [line.strip() for line in infile.readlines() if line]
    for line in lines:
        if (matched := PYTHON.match(line)) :
            field = matched.group(1)
            yield (f"{field}=source.{field},")
        elif (matched := GO.match(line)) :
            field = matched.group(1)
            yield (f"{field}: source.{field},")


def main() -> None:
    options = parse_command_line()
    for line in generate_code(options.infile):
        print(line)


if __name__ == "__main__":
    main()
