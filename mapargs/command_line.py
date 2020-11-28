import argparse
from dataclasses import dataclass
import io
import re
import sys

SEPARATORs = [":", " "]
REGEX = re.compile(rf"({'|'.join(SEPARATORs)}).*")


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


def main() -> None:
    options = parse_command_line()
    lines = [line.strip() for line in options.infile.readlines() if line]
    for line in lines:
        field = REGEX.sub("", line)
        # Map python objects
        print(f"{field}=right.{field},")


if __name__ == "__main__":
    main()
