from Modules.alphabets import Alphabet


class Encryptor:
    def __init__(self, cipher, alphabet=Alphabet.EN.value):
        self.cipher = cipher
        self.alphabet = alphabet

    @staticmethod
    def replace(text, cipher):
        new_text = []
        for i in text:
            if i.lower() in cipher:
                new_text.append(cipher[i] if i.islower() else cipher[
                    i.lower()].upper())
            else:
                new_text.append(i)
        return ''.join(new_text)
