class Encryptor:
    def __init__(self, cipher, alphabet):
        self.cipher = cipher
        self.alphabet = alphabet
    
    def encrypt(self, text):
        return self.replace(text)
    
    def replace(self, text):
        new_text = ""
        for i in text:
            if i in self.cipher:
                new_text += self.cipher[i]
            else:
                new_text += i
        return new_text
