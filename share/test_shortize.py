#!/usr/bin/python
import unittest
from shortize import shortize

class TestShortize(unittest.TestCase):

    def test_short_name(self):
        self.assertEqual(shortize("short"), "SHORT")

    def test_short_name_uppercase(self):
        self.assertEqual(shortize("SHORT"), "SHORT")

    def test_short_name_and_extension(self):
        self.assertEqual(shortize("short.nam"), "SHORT.NAM")

    def test_long_name(self):
        self.assertEqual(shortize("verylongname"), "VERYLO~1")

    def test_long_extension(self):
        self.assertEqual(shortize("verylong.extension"), "VERYLO~1.EXT")

    def test_name_with_space(self):
        self.assertEqual(shortize("no name"), "NONAME~1")

    def test_extension_with_space(self):
        self.assertEqual(shortize("short.n m"), "SHORT~1.NM")

    def test_name_with_space_before(self):
        self.assertEqual(shortize(" before"), "BEFORE~1")

    def test_name_with_space_after(self):
        self.assertEqual(shortize("after "), "AFTER~1")

    def test_long_name_with_space(self):
        self.assertEqual(shortize("Program Files"), "PROGRA~1")

    def test_gog_games(self):
        self.assertEqual(shortize("gog games"), "GOGGAM~1")

    def test_more_than_two_components(self):
        self.assertEqual(shortize("one.two.3"), "ONE~1.3")

    def test_components_all_short(self):
        self.assertEqual(shortize("one\\two\\three"), "ONE\\TWO\\THREE")

    def test_components_one_long(self):
        self.assertEqual(shortize("one\\no name\\three"), "ONE\\NONAME~1\\THREE")


if __name__ == '__main__':
    unittest.main()
