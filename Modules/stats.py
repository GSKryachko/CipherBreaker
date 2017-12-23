import json


class Stats:
    single_letter_words = {}
    two_letter_words = {}
    with_frequent_letter = {}
    longest = {}
    letters = {}
    bigrams = {}
    trigrams = {}
    masks = {}
    
    def save(self, stats_file):
        with open(stats_file, 'w+', encoding='UTF-8') as f:
            json.dump(self.single_letter_words, f)
            f.write('\n')
            json.dump(self.two_letter_words, f)
            f.write('\n')
            json.dump(self.with_frequent_letter, f)
            f.write('\n')
            json.dump(self.longest, f)
            f.write('\n')
            json.dump(self.letters, f)
            f.write('\n')
            json.dump(self.bigrams, f)
            f.write('\n')
            json.dump(self.trigrams, f)
            f.write('\n')
            json.dump(self.masks, f)
            f.write('\n')
    
    @staticmethod
    def load(stats_file):
        stats = Stats()
        with open(stats_file, 'r', encoding='UTF-8') as f:
            stats.single_letter_words = json.loads(f.readline())
            stats.two_letter_words = json.loads(f.readline())
            stats.with_frequent_letter = json.loads(f.readline())
            stats.longest = json.loads(f.readline())
            stats.letters = sorted(json.loads(f.readline()))
            stats.bigrams = sorted(json.loads(f.readline()))
            stats.trigrams = sorted(json.loads(f.readline()))
            stats.masks = json.loads(f.readline())
        return stats
