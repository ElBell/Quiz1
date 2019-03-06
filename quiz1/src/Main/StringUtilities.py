
class StringUtilities:
    def return_string(self, string: str) -> str:
        return string

    def concatinate_string(self, string1: str, string2: str) -> str:
        return string1 + string2

    def reverse_string(self, string: str) -> str:
        return string[::-1]

    def get_middle_character(self, string: str) -> str:

        return string[int(len(string)/2)]

    def remove_final_character(self, string: str) -> str:
        return string[:len(string)-1]

    def get_last_word(self, string: str) -> str:
        return string.split()[-1]
