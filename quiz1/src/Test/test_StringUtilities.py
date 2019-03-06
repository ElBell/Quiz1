from unittest import TestCase
from StringUtilities import StringUtilities


class TestMathUtilites(TestCase):
    def setUp(self):
        self.test_string_utilities: StringUtilities = StringUtilities()

    def test_return_string(self):
        expected: str = "Something"
        actual: str = self.test_string_utilities.return_string(expected)
        self.assertEqual(expected, actual)

    def test_return_string2(self):
        expected: str = "something_else"
        actual: str = self.test_string_utilities.return_string(expected)
        self.assertEqual(expected, actual)

    def test_concatinate(self):
        expected: str = "something_else"
        actual: str = self.test_string_utilities.concatinate_string("something_", "else")
        self.assertEqual(expected, actual)

    def test_reverse_string(self):
        expected: str = "dlrow olleH"
        actual: str = self.test_string_utilities.reverse_string("Hello world")
        self.assertEqual(expected, actual)

    def test_get_middle_character(self):
        expected: str = "a"
        actual: str = self.test_string_utilities.get_middle_character("Aggadah")
        self.assertEqual(expected, actual)

    def test_remove_character(self):
        expected: str = "Somethin"
        actual: str = self.test_string_utilities.remove_final_character("Something")
        self.assertEqual(expected, actual)

    def test_get_last_word(self):
        expected: str = "Somethin"
        actual: str = self.test_string_utilities.get_last_word("Say anything or Somethin")
        self.assertEqual(expected, actual)
