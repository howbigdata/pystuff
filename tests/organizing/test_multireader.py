import unittest

from organizing.core.demo_reader.multireader import MultiReader


class TestMultireader(unittest.TestCase):
    def test_initialization(self):
        MultiReader("tests/organizing/test_file.txt")
