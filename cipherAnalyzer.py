import random
import re
from collections import Counter

from encryptor import Encryptor
from masksBuilder import MasksBuilder
from stats import Stats
from textsAnalyzer import TextsAnalyzer


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
        self.letters_from = {x for x in alphabet}
        self.letters_to = {x for x in alphabet}
        self.alphabet = alphabet
    
    def analyze_using_lists(self, words):
        for word in words:
            mask = MasksBuilder.build_mask(word)
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
        return self.cipher
    
    def analyze_cipher_using_range(self, words):
        ranged_words = self.range_words(words)
        for count in sorted(ranged_words, reverse=True):
            for word in ranged_words[count]:
                mask = MasksBuilder.build_mask(word)
                if mask in self.words_with_masks:
                    self.register_chars(self.words_with_masks[mask], word)
                    self.try_get_cipher()
        return self.cipher
    
    def range_masks(self):
        for mask in self.words_with_masks:
            mask_frequency_index = CipherAnalyzer.range_mask(mask)
            if mask_frequency_index not in self.ranged_masks:
                self.ranged_masks[mask_frequency_index] = set()
            self.ranged_masks[mask_frequency_index].add(mask)
    
    @staticmethod
    def range_mask(mask):
        counter = Counter(mask)
        return sum([x ** 2 for x in counter.values()])
    
    def range_words(self, words):
        words_with_mask = dict()
        for word in words:
            mask_frequency_index = CipherAnalyzer.range_mask(word)
            if mask_frequency_index not in words_with_mask:
                words_with_mask[mask_frequency_index] = set()
            words_with_mask[mask_frequency_index].add(word)
        return words_with_mask
    
    def register_chars(self, words, encrypted_word):
        for word in words:
            for i in range(len(word)):
                if encrypted_word[i] in self.cipher:
                    continue
                if encrypted_word[i] not in self.assumed_cipher:
                    self.assumed_cipher[encrypted_word[i]] = set()
                self.assumed_cipher[encrypted_word[i]].add(word[i])
    
    def register_chars_to_dict(self, words, encrypted_word, dictionary):
        for word in words:
            for i in range(len(word)):
                if encrypted_word[i] in self.cipher:
                    continue
                if encrypted_word[i] not in dictionary:
                    dictionary[encrypted_word[i]] = set()
                dictionary[encrypted_word[i]].add(word[i])

    # def try_get_cipher(self):
    #     for i in self.assumed_cipher:
    #         if i in self.cipher:
    #             continue
    #         if len(self.assumed_cipher[i]) == 1:
    #             self.cipher[i] = next(iter(self.assumed_cipher[i]))
    #     self.assumed_cipher.clear()
    
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
    def prepare_words(text):
        words = set()
        for word in re.sub('[!@#$.,\'?:;`\"()[\]{}\-%*0-9]', '', text).replace(
                '\n', ' ').split(' '):
            if word != '':
                words.add(word.lower())
        return list(words)
    
    @staticmethod
    def make_random_transposition(cipher):
        first_letter = random.sample(cipher.keys(), 1)[0]
        second_letter = random.sample(cipher.keys(), 1)[0]
        temp = cipher[first_letter]
        cipher[first_letter] = cipher[second_letter]
        cipher[second_letter] = temp
        return cipher
    
    def decrypt_using_gradient(self, text_sample):
        best_cipher = self.cipher
        max_fitness = 0
        for i in range(100):
            cipher = self.make_random_transposition(best_cipher)
            new_fitness = self.calculate_fitness_function(text_sample, cipher)
            if new_fitness > max_fitness:
                max_fitness = new_fitness
                best_cipher = cipher
        return best_cipher
    
    def calculate_fitness_function(self, text_sample, cipher):
        decoded = Encryptor.replace(text_sample, cipher)
        current_frequencies = TextsAnalyzer.get_trigram_frequencies(decoded)
        natural_frequencies = self.stats.trigrams
        fitness = 0
        for i in natural_frequencies.keys() | current_frequencies.keys():
            if i not in natural_frequencies:
                natural_frequencies[i] = 0
            if i not in current_frequencies:
                current_frequencies[i] = 0
            fitness += abs(
                natural_frequencies[i] - current_frequencies[i])
        return fitness
