
class MathUtilites:

    @staticmethod
    def add(base_value: int, value_to_add: int) -> int:
        return base_value + value_to_add

    @staticmethod
    def half(base_value: int) -> float:
        return base_value/2

    @staticmethod
    def is_odd(value: int) -> bool:
        return value % 2 != 0

    @staticmethod
    def square(value: int) -> int:
        return value * value


