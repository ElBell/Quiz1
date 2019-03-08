
class StringUtilities:
    @staticmethod
    def return_string(string: str) -> str:
        return string

    @staticmethod
    def concatenate_string(string1: str, string2: str) -> str:
        return string1 + string2

    @staticmethod
    def reverse_string(string: str) -> str:
        return string[::-1]

    @staticmethod
    def get_middle_character(string: str) -> str:
        return string[int(len(string)/2)]

    @staticmethod
    def remove_final_character(string: str) -> str:
        return string[:-1]

    @staticmethod
    def get_last_word(string: str) -> str:
        return string.split()[-1]

