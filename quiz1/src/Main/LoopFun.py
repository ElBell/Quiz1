import string


class LoopFun(object):

    @staticmethod
    def factorial(number):
        result = number
        while number > 1:
            number -= 1
            result *= number
        return result

    @staticmethod
    def acronym(sentence):
        broken_sentence = sentence.split()
        acronym = ""
        for word in broken_sentence:
            acronym += word[0].upper()
        return acronym

    @staticmethod
    def acronym_alternate(sentence):
        return "".join(letter.upper() for letter, *rest in sentence.split())

    @staticmethod
    def encrypt(word: str) -> str:
        alphabet: str = string.ascii_lowercase
        shifted_alphabet: str = alphabet[3:] + alphabet[:3]
        table = str.maketrans(alphabet, shifted_alphabet)
        return word.translate(table)

