import re


class Encryptor:
    def __init__(self, cipher, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.cipher = cipher
        self.alphabet = alphabet
    
    def encrypt(self, text):
        new_text = []
        for word in text:
            new_text.append(self.replace(word))
        return new_text
    
    def replace(self, text):
        new_text = ""
        for i in text:
            if i in self.cipher:
                new_text += self.cipher[i]
            else:
                new_text += i
        return new_text
    
    @staticmethod
    def prepare_words(text):
        return [word.lower() for word in
                re.sub('[!@#$.,\'?:;]', '', text).split(' ')]
