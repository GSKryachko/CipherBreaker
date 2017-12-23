from random import shuffle


class CipherGenerator:
    @staticmethod
    def generate_cipher(alphabet):
        shuffled_alphabet = list(alphabet)
        shuffle(shuffled_alphabet)
        return dict(zip(alphabet, shuffled_alphabet))
