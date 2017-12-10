import json
from collections import Counter, defaultdict

from masksBuilder import MasksBuilder


class Stats:
    single_letter_words = set()
    two_letter_words = set()
    with_multiple_occurrences_of_same_letter = set()
    temp_longest = []
    longest = set()
    letters = defaultdict(int)
    bigrams = defaultdict(int)
    trigrams = defaultdict(int)
    most_common = set()
    masks = dict()
    
    def update_masks(self):
        self.longest = set(self.temp_longest)
        interesting_words = self.single_letter_words.union(
            self.two_letter_words).union(self.longest).union(
            self.with_multiple_occurrences_of_same_letter)
        self.masks = MasksBuilder.build_masks(interesting_words)
    
    def save(self, stats_dir):
        try:
            with open(stats_dir + "single_letter_words.txt", 'w+') as f:
                json.dump(list(self.single_letter_words), f)
            with open(stats_dir + "two_letter_words.txt", 'w+') as f:
                json.dump(list(self.two_letter_words), f)
            with open(stats_dir + "with_repeating_letter.txt", 'w+') as f:
                json.dump(list(self.with_multiple_occurrences_of_same_letter),
                          f)
            with open(stats_dir + "longest.txt", 'w+') as f:
                json.dump(list(self.longest), f)
            with open(stats_dir + "letters.txt", 'w+') as f:
                json.dump(dict(Counter(self.letters)), f)
            with open(stats_dir + "bigrams.txt", 'w+') as f:
                json.dump(dict(Counter(self.bigrams)), f)
            with open(stats_dir + "trigrams.txt", 'w+') as f:
                json.dump(dict(Counter(self.trigrams)), f)
            with open(stats_dir + "masks.txt", 'w+') as f:
                json.dump(self.masks, f)
            print("Stats saved to {0}".format(stats_dir))
        except FileNotFoundError as e:
            print(e)
            exit()
    
    @staticmethod
    def load(stats_dir):
        stats = Stats()
        try:
            with open(stats_dir + "single_letter_words.txt",
                      'r') as f:
                print(f.name)
                stats.single_letter_words = set(json.loads(f.read()))
            with open(stats_dir + "two_letter_words.txt", 'r') as f:
                stats.two_letter_words = set(json.loads(f.read()))
            with open(stats_dir + "with_repeating_letter.txt", 'r') as f:
                stats.with_multiple_occurrences_of_same_letter = set(
                    json.loads(f.read()))
            with open(stats_dir + "longest.txt", 'r') as f:
                stats.longest = set(json.loads(f.read()))
            with open(stats_dir + "letters.txt", 'r') as f:
                stats.letters = json.loads(f.read())
            with open(stats_dir + "bigrams.txt", 'r') as f:
                stats.bigrams = json.loads(f.read())
            with open(stats_dir + "trigrams.txt", 'r') as f:
                stats.trigrams = json.loads(f.read())
            with open(stats_dir + "top1000.txt", 'r') as f:
                stats.most_common = {word for word in f}
            with open(stats_dir + "masks.txt") as f:
                stats.masks = json.loads(f.read())
            print("Stats loaded from {0}".format(stats_dir))
            return stats
        except FileNotFoundError as e:
            print(e)
            exit()
