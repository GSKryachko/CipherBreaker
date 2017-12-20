from random import shuffle


class CipherGenerator:
    @staticmethod
    def generate_cipher(alphabet):
        shuffled_alphabet = list(alphabet)
        shuffle(shuffled_alphabet)
        cipher = dict()
        for i in range(len(alphabet)):
            cipher[alphabet[i]] = shuffled_alphabet[i]
        return cipher
