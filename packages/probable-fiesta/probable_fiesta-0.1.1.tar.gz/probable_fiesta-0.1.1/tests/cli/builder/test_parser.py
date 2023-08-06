"""Test file for parser.py."""
from src.probable_fiesta.cli.builder.parser import Parser
from src.probable_fiesta.cli.builder.my_args_parser import MyArgsParser
from src.probable_fiesta.logger.builder.logger_factory import LoggerFactory as LF

from unittest import TestCase

LOG = LF.new_logger_get_logger("test_parser", "DEBUG")


class TestCliParser(TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_init(self):
        self.parser = Parser()
        self.assertEqual(str(self.parser.parser.__class__), "<class 'src.probable_fiesta.cli.builder.my_args_parser.MyArgsParser'>")

    def test_add_argument_long_flag(self):
        self.parser = Parser()
        args = "--version"
        self.parser.add_argument(args)
        parsed = self.parser.parse_args('--version 1'.split()) 
        self.assertEqual(str(parsed), "Namespace(version='1')")

    def test_add_argument_short_flag(self):
        self.parser = Parser()
        args = "-v"
        self.parser.add_argument(args)
        parsed = self.parser.parse_args('-v 1'.split())
        self.assertEqual(str(parsed), "Namespace(v='1')")
        
    def test_parse_args_valid(self):
        self.parser = Parser()
        args = "--version"
        self.parser.parser.add_argument(args)
        parsed = self.parser.parser.parse_args('--version 1'.split()) 
        self.assertEqual(str(parsed), "Namespace(version='1')")

    def test_parse_args_no_args(self):
        self.parser = Parser()
        args = "-v"
        self.parser.add_argument(args)
        parsed = self.parser.parse_args(None)
        self.assertEqual(parsed, None)

    def test_get_parsed_args(self):
        self.parser = Parser()
        args = "-v"
        self.parser.add_argument(args)
        parsed = self.parser.parse_args(['-v', '1'])
        self.assertEqual(parsed, self.parser.get_parsed_args())

    def test_get_parsed_arg(self):
        self.parser = Parser()
        args = "-v"
        self.parser.add_argument(args)
        self.parser.parse_args(['-v', '1'])
        self.assertEqual(self.parser.get_parsed_arg('v'), '1')

    def test_validate_true(self):
        self.parser = Parser()
        args = "-v"
        self.parser.add_argument(args)
        self.parser.validate(['-v', '1'])
        self.assertEqual(self.parser.valid, True)

    # Warning error message differs
    def test_validate_false(self):
        self.parser = Parser()
        args = "-x"
        self.parser.add_argument(args)
        self.parser.validate(['-x'])  # Missing argument
        self.assertEqual(self.parser.valid, False)
        # Don't know why it shows unrecognized instead of missing argument
        self.assertEqual(self.parser.error, "unrecognized arguments: -x")

    def test_new(self):
        self.parser = Parser.new()
        args = "-v"
        self.parser.add_argument(args)
        self.parser.validate(['-v', '1'])
        self.assertEqual(self.parser.valid, True)

    def test_factory_new(self):
        self.parser = Parser.new()
        args = "-v"
        self.parser.add_argument(args)
        self.parser.validate(['-v', '1'])
        self.assertEqual(self.parser.valid, True)
