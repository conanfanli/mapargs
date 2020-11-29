import io
import unittest

from mapargs.command_line import generate_code


class CommandLineTest(unittest.TestCase):
    def test_generate_python_code(self) -> None:
        infile = io.StringIO(
            """
a: str
b: int
c: float
"""
        )
        output = list(generate_code(infile))
        assert output == ["a=right.a,", "b=right.b,", "c=right.c,"]
