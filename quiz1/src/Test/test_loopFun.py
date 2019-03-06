from unittest import TestCase
from LoopFun import LoopFun


class TestLoopFun(TestCase):
    def setUp(self):
        self.loop_fun = LoopFun()

    def test_factorial(self):
        expected = 120
        actual = self.loop_fun.factorial(5)
        self.assertEqual(expected, actual)

    def test_factorial2(self):
        expected = 1
        actual = self.loop_fun.factorial(1)
        self.assertEqual(expected, actual)

    def test_factorial3(self):
        expected = 6
        actual = self.loop_fun.factorial(3)
        self.assertEqual(expected, actual)

    def test_factorial4(self):
        expected = 720
        actual = self.loop_fun.factorial(6)
        self.assertEqual(expected, actual)

    def test_acronym(self):
        expected = "PNG"
        actual = self.loop_fun.acronym("Portable Network Graphics")
        self.assertEqual(expected, actual)

    def test_acronym2(self):
        expected = "ROR"
        actual = self.loop_fun.acronym("Ruby on Rails")
        self.assertEqual(expected, actual)

    def test_acronym3(self):
        expected = "FIFO"
        actual = self.loop_fun.acronym("First In, First Out")
        self.assertEqual(expected, actual)

    def test_acronym4(self):
        expected = "TMCA"
        actual = self.loop_fun.acronym("Tuskegee Macon County, Alabama")
        self.assertEqual(expected, actual)

    def test_encrypt_with_the_first_letters(self):
        word: str = "apple"
        expected: str = "dssoh"
        actual: str = self.loop_fun.encrypt(word)
        self.assertEqual(expected, actual)

    def test_encrypt_with_the_last_letters(self):
        word: str = "wxyz"
        expected: str = "zabc"
        actual: str = self.loop_fun.encrypt(word)
        self.assertEqual(expected, actual)
