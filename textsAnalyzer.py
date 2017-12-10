import os
import re
from collections import Counter

from stats import Stats


class TextsAnalyzer:
    shortest_longest_word_length = 0
    
    def __init__(self, texts_dir, stats_dir):
        self.texts_dir = texts_dir
        self.stats_dir = stats_dir
        self.stats = Stats()
    
    def analyze(self):
        for text in os.listdir(self.texts_dir):
            for word in self.get_words_from_file(self.texts_dir + text):
                self.register_word(word)
        self.stats.update_masks()
        self.stats.save(self.stats_dir)
    
    # 
    # def save_masks(self):
    #     interesting_words = self.single_letter_words.union(
    #         self.two_letter_words).union(self.stats.longest).union(
    #         self.with_multiple_occurrences_of_same_letter)
    #     masks = MasksBuilder.build_masks(interesting_words)
    #     with open(self.stats_dir + "masks.txt",'w+') as f:
    #         json.dump(masks, f)
    # 
    
    @staticmethod
    def get_words_from_file(filename):
        with open(filename, 'r') as f:
            for line in f:
                for word in TextsAnalyzer.clean_words(line):
                    yield word
    
    @staticmethod
    def clean_words(text):
        text = re.sub('[^a-z^A-Z]', ' ', text)
        for word in text.split(' '):
            if word != '':
                yield word.lower()
    
    @staticmethod
    def contains_letter_four_times(word):
        return max(Counter(word).values()) > 3
    
    def register_100_longest(self, word):
        if len(self.stats.temp_longest) < 100:
            self.stats.temp_longest.append(word)
            return
        if word in self.stats.temp_longest:
            return
        if len(word) > self.shortest_longest_word_length:
            self.stats.temp_longest.append(word)
            self.stats.temp_longest.sort(key=len, reverse=True)
            self.stats.temp_longest = self.stats.temp_longest[0:100]
            self.shortest_longest_word_length = len(
                self.stats.temp_longest[-1])
    
    def register_word(self, word):
        if len(word) == 1:
            self.stats.single_letter_words.add(word)
        elif len(word) == 2:
            self.stats.two_letter_words.add(word)
        if TextsAnalyzer.contains_letter_four_times(word):
            self.stats.with_multiple_occurrences_of_same_letter.add(word)
        self.register_ngrams(word)
        self.register_100_longest(word)
    
    def register_ngrams(self, word):
        for i in range(0, len(word)):
            self.stats.letters[word[i]] += 1
            if i < len(word) - 1:
                self.stats.bigrams[word[i:i + 2]] += 1
            if i < len(word) - 2:
                self.stats.trigrams[word[i:i + 3]] += 1
