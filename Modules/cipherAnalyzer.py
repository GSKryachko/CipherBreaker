import random

from Modules.masksBuilder import MasksBuilder
from Modules.stats import Stats


class CipherAnalyzer:
    def __init__(self, words_with_masks, stats_dir, alphabet):
        self.words_with_masks = words_with_masks
        self.assumed_cipher = dict()
        self.cipher = dict()
        self.ranged_masks = dict()
        self.stats = Stats.load(stats_dir)
        self.one_letter_guesses = dict()
        self.two_letter_guesses = dict()
        self.long_words_guesses = dict()
        self.popular_words_guesses = dict()
        self.strange_words_guesses = dict()
        self.letters_from = {x for x in alphabet.value}
        self.letters_to = {x for x in alphabet.value}
        self.alphabet = alphabet
    
    def analyze_using_lists(self, words):
        for word in words:
            mask = MasksBuilder.build_mask(word, self.alphabet)
            if mask in self.stats.single_letter_words:
                self.register_chars_to_dict(
                    self.stats.single_letter_words[mask], word,
                    self.one_letter_guesses)
            if mask in self.stats.two_letter_words:
                self.register_chars_to_dict(
                    self.stats.two_letter_words[mask], word,
                    self.two_letter_guesses)
            if mask in self.stats.longest:
                self.register_chars_to_dict(
                    self.stats.longest[mask], word,
                    self.long_words_guesses)
            if mask in self.stats.with_frequent_letter:
                self.register_chars_to_dict(
                    self.stats.with_frequent_letter[mask], word,
                    self.strange_words_guesses)
        self.try_get_cipher()
        self.fill_cipher()
        return self.cipher

    def fill_cipher(self):
        for i in self.alphabet.value:
            if i not in self.cipher:
                self.cipher[i] = '_'
    
    def register_chars_to_dict(self, words, encrypted_word, dictionary):
        for word in words:
            for i in range(len(word)):
                if encrypted_word[i] in self.cipher:
                    continue
                if encrypted_word[i] not in dictionary:
                    dictionary[encrypted_word[i]] = set()
                dictionary[encrypted_word[i]].add(word[i])
    
    def try_get_cipher(self):
        self.try_get_cipher_from_dict(self.strange_words_guesses)
        self.try_get_cipher_from_dict(self.long_words_guesses)
        self.try_get_cipher_from_dict(self.two_letter_guesses)
        self.try_get_cipher_from_dict(self.one_letter_guesses)

    def try_get_cipher_from_dict(self, dictionary):
        for i in dictionary:
            if i not in self.letters_from:
                continue
            dictionary[i] = {x for x in dictionary[i] if
                             x in self.letters_to}
            if len(dictionary[i]) == 0:
                continue
            if len(dictionary[i]) == 1:
                if next(iter(dictionary[i])) not in self.letters_to:
                    continue
                self.cipher[i] = next(iter(dictionary[i]))
                self.letters_from.remove(i)
                self.letters_to.remove(next(iter(dictionary[i])))
    
    @staticmethod
    def make_random_transposition(cipher):
        first_letter = random.sample(cipher.keys(), 1)[0]
        second_letter = random.sample(cipher.keys(), 1)[0]
        temp = cipher[first_letter]
        cipher[first_letter] = cipher[second_letter]
        cipher[second_letter] = temp
        return cipher
