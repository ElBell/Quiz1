import string


class LoopFun(object):

    def factorial(self, number):
        result = number
        while number > 1:
            number -= 1
            result *= number
        return result

    def acronym(self, sentence):
        broken_sentence = sentence.split()
        acronym = ""
        for word in broken_sentence :
            acronym += word[0].upper()
        return acronym

    def encrypt(self, word: str) -> str:
        alphabet: str = string.ascii_lowercase
        shifted_alphabet: str = alphabet[3:] + alphabet[:3]
        table = str.maketrans(alphabet, shifted_alphabet)
        return word.translate(table)
