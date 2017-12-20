from collections import Counter, defaultdict

from Modules.masksBuilder import MasksBuilder
from Modules.stats import Stats
from Modules.textCleaner import TextCleaner


class TextsAnalyzer:
    shortest_longest_word_length = 0

    def __init__(self, alphabet):
        self.letters = defaultdict(int)
        self.bigrams = defaultdict(int)
        self.trigrams = defaultdict(int)
        self.stats = Stats()
        self.temp_longest = []
        self.two_letter_words = set()
        self.single_letter_words = set()
        self.with_frequent_letter = set()
        self.alphabet = alphabet

    def analyze(self, words):
        for word in words:
            if not TextCleaner.is_meaningful_word(word, self.alphabet):
                continue
            self.register_word(word)
        self.add_ngrams_to_stats()
        self.add_words_with_masks_to_stats()
    
    @staticmethod
    def has_frequent_letter(word):
        return max(Counter(word).values()) > 3

    @staticmethod
    def get_normalized_dictionary(dictionary):
        values_sum = sum(dictionary.values())
        normalized = dict()
        for key in dictionary:
            normalized[key] = dictionary[key] / values_sum
        return normalized
    
    def register_100_longest(self, word):
        if len(self.temp_longest) < 100:
            self.temp_longest.append(word)
            return
        if word in self.temp_longest:
            return
        if len(word) > self.shortest_longest_word_length:
            self.temp_longest.append(word)
            self.temp_longest.sort(key=len, reverse=True)
            self.temp_longest = self.temp_longest[0:100]
            self.shortest_longest_word_length = len(
                self.temp_longest[-1])
    
    def register_word(self, word):
        if len(word) == 1:
            self.single_letter_words.add(word)
        elif len(word) == 2:
            self.two_letter_words.add(word)
        if TextsAnalyzer.has_frequent_letter(word):
            self.with_frequent_letter.add(word)
        self.register_ngrams(word)
        self.register_100_longest(word)
    
    def register_ngrams(self, word):
        for i in range(0, len(word)):
            self.letters[word[i]] += 1
            if i < len(word) - 1:
                self.bigrams[word[i:i + 2]] += 1
            if i < len(word) - 2:
                self.trigrams[word[i:i + 3]] += 1

    def add_words_with_masks_to_stats(self):
        self.stats.single_letter_words = MasksBuilder.build_masks(
            self.single_letter_words, self.alphabet)
        self.stats.two_letter_words = MasksBuilder.build_masks(
            self.two_letter_words, self.alphabet)
        self.stats.longest = MasksBuilder.build_masks(self.temp_longest,
                                                      self.alphabet)
        self.stats.with_frequent_letter = \
            MasksBuilder.build_masks(
                self.with_frequent_letter, self.alphabet)
    
    def add_ngrams_to_stats(self):
        self.stats.letters = TextsAnalyzer.get_normalized_dictionary(
            self.letters)
        self.stats.bigrams = TextsAnalyzer.get_normalized_dictionary(
            self.bigrams)
        self.stats.trigrams = TextsAnalyzer.get_normalized_dictionary(
            self.trigrams)
