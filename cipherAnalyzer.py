import re
from collections import Counter

from masksBuilder import MasksBuilder
from stats import Stats


class CipherAnalyzer:
    def __init__(self, words_with_masks, stats_dir):
        self.words_with_masks = words_with_masks
        self.assumed_cipher = dict()
        self.cipher = dict()
        self.ranged_masks = dict()
        self.stats = Stats.load(stats_dir)
    
    def analyze_using_lists(self, words):
        for word in words:
            mask = MasksBuilder.build_mask(word)
            if mask in self.stats.masks:
                self.register_chars(self.stats.masks[mask], word)
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
    
    def try_get_cipher(self):
        for i in self.assumed_cipher:
            if i in self.cipher:
                continue
            if len(self.assumed_cipher[i]) == 1:
                self.cipher[i] = next(iter(self.assumed_cipher[i]))
        self.assumed_cipher.clear()
    
    @staticmethod
    def prepare_words(text):
        words = set()
        for word in re.sub('[!@#$.,\'?:;`\"()[\]{}\-%*1-9]', '', text).replace(
                '\n', ' ').split(' '):
            if word != '':
                words.add(word.lower())
        return list(words)
