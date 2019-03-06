
class MathUtilites:

    def add(self, basevalue: int, valueToAdd: int) -> int:
        return basevalue + valueToAdd

    def half(self, basevalue: int) -> float:
        return basevalue/2

    def isOdd(self, value: int) -> bool:
        return value % 2 != 0

    def square(self, value: int) -> int:
        return value * value


