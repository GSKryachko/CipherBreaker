import re

from masksBuilder import MasksBuilder


class CipherAnalyzer:
    def __init__(self, words_with_masks):
        self.words_with_masks = words_with_masks
        self.assumed_cipher = dict()
    
    def analyze_cipher(self, words):
        for word in words:
            mask = MasksBuilder.build_mask(word)
            if mask in self.words_with_masks:
                self.register_chars(self.words_with_masks[mask], word)
        return self.try_get_cipher()
    
    def register_chars(self, words, encrypted_word):
        for word in words:
            for i in range(len(word)):
                if encrypted_word[i] not in self.assumed_cipher:
                    self.assumed_cipher[encrypted_word[i]] = [word[i]]
                else:
                    self.assumed_cipher[encrypted_word[i]].append(word[i])
    
    def try_get_cipher(self):
        cipher = dict()
        for i in self.assumed_cipher:
            if len(self.assumed_cipher[i]) == 1:
                cipher[i] = self.assumed_cipher[i][0]
            else:
                return None
        return cipher
    
    @staticmethod
    def prepare_words(text):
        words = set()
        for word in re.sub('[!@#$.,\'?:;]', '', text).split(' '):
            words.add(word.lower())
        return list(words)
