class Encryptor:
    def __init__(self, cipher, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.cipher = cipher
        self.alphabet = alphabet

    #
    # def replace(self, text):
    #     new_text = ""
    #     for i in text:
    #         if i.lower() in self.cipher:
    #             new_text += self.cipher[i] if i.islower() else self.cipher[i.lower()].upper()
    #         else:
    #             new_text += i
    #     return new_text

    @staticmethod
    def replace(text, cipher):
        new_text = ""
        for i in text:
            if i.lower() in cipher:
                new_text += cipher[i] if i.islower() else cipher[
                    i.lower()].upper()
            else:
                new_text += i
        return new_text
