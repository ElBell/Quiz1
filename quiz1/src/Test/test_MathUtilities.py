from unittest import TestCase
from MathUtilities import MathUtilites


class TestMathUtilities(TestCase):
    def setUp(self):
        self.test_math_utilities: MathUtilites = MathUtilites()

    def test_add(self):
        var1: int = 3
        var2: int = 56
        expected: int = var1 + var2
        actual: int = self.test_math_utilities.add(var1, var2)
        self.assertEqual(expected, actual)

    def test_add2(self):
        var1: int = 45
        var2: int = 450
        expected: int = var1 + var2
        actual: int = self.test_math_utilities.add(var1, var2)
        self.assertEqual(expected, actual)

    def test_add3(self):
        var1: int = 45.5
        var2: int = 45.5
        expected: int = 91
        actual: int = self.test_math_utilities.add(var1, var2)
        self.assertEqual(expected, actual)

    def test_half(self):
        expected: int = 10.5
        actual: int = self.test_math_utilities.half(21)
        self.assertEqual(expected, actual)

    def test_half2(self):
        expected: int = 2.0
        actual: int = self.test_math_utilities.half(4)
        self.assertEqual(expected, actual)

    def test_is_odd(self):
        actual: bool = self.test_math_utilities.isOdd(3)
        self.assertTrue(actual)

    def test_isOddFalse(self):
        actual: bool = self.test_math_utilities.isOdd(4)
        self.assertFalse(actual)

    def test_square(self):
        expected: int = 16
        actual: bool = self.test_math_utilities.square(4)
        self.assertEqual(expected, actual)

    def test_square2(self):
        expected: int = 25
        actual: bool = self.test_math_utilities.square(5)
        self.assertEqual(expected, actual)
