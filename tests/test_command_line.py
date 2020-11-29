import io
import unittest

from mapargs.command_line import generate_code


class CommandLineTest(unittest.TestCase):
    def test_generate_python_code(self) -> None:
        infile = io.StringIO(
            """
field1: str
b: int
c: float
"""
        )
        output = list(generate_code(infile))
        assert output == ["field1=source.field1,", "b=source.b,", "c=source.c,"]

    def test_generate_go_code(self) -> None:
        infile = io.StringIO(
            """
ID        int
Field2    string
c         string
"""
        )
        output = list(generate_code(infile))
        assert output == ["ID: source.ID,", "Field2: source.Field2,", "c: source.c,"]
