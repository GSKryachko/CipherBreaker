import json


class Stats:
    single_letter_words = dict()
    two_letter_words = dict()
    with_frequent_letter = dict()
    longest = dict()
    letters = dict()
    bigrams = dict()
    trigrams = dict()
    most_common = dict()
    masks = dict()
    
    def save(self, stats_dir):
        try:
            with open(stats_dir + "single_letter_words.txt", 'w+') as f:
                json.dump(self.single_letter_words, f)
            with open(stats_dir + "two_letter_words.txt", 'w+') as f:
                json.dump(self.two_letter_words, f)
            with open(stats_dir + "with_repeating_letter.txt", 'w+') as f:
                json.dump(self.with_frequent_letter, f)
            with open(stats_dir + "longest.txt", 'w+') as f:
                json.dump(self.longest, f)
            with open(stats_dir + "letters.txt", 'w+') as f:
                json.dump(self.letters, f)
            with open(stats_dir + "bigrams.txt", 'w+') as f:
                json.dump(self.bigrams, f)
            with open(stats_dir + "trigrams.txt", 'w+') as f:
                json.dump(self.trigrams, f)
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
                stats.single_letter_words = json.loads(f.read())
            with open(stats_dir + "two_letter_words.txt", 'r') as f:
                stats.two_letter_words = json.loads(f.read())
            with open(stats_dir + "with_repeating_letter.txt", 'r') as f:
                stats.with_frequent_letter = json.loads(f.read())
            with open(stats_dir + "longest.txt", 'r') as f:
                stats.longest = json.loads(f.read())
            with open(stats_dir + "letters.txt", 'r') as f:
                stats.letters = sorted(json.loads(f.read()))
            with open(stats_dir + "bigrams.txt", 'r') as f:
                stats.bigrams = sorted(json.loads(f.read()))
            with open(stats_dir + "trigrams.txt", 'r') as f:
                stats.trigrams = sorted(json.loads(f.read()))
            with open(stats_dir + "top1000.txt", 'r') as f:
                stats.most_common = {word for word in f}
            with open(stats_dir + "masks.txt") as f:
                stats.masks = json.loads(f.read())
            print("Stats loaded from {0}".format(stats_dir))
            return stats
        except FileNotFoundError as e:
            print(e)
            exit()
