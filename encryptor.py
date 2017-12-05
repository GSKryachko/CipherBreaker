
class Encryptor:
    def __init__(self, alphabet):
        self.cipher = None
        self.alphabet = alphabet
      
    def encrypt(self, text):
        if self.cipher is None:
            print("Cipher not registered")
            return
        return self.replace(text)
    
    def replace(self, text):
        new_text = ""
        for i in text:
            if i in self.cipher:
                new_text += self.cipher[i]
            else:
                new_text += i
        return new_text
