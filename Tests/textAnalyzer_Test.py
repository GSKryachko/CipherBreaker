import unittest
from random import shuffle

from textsAnalyzer import TextsAnalyzer


class TextsAnalyzerTest(unittest.TestCase):
    def test_register_top_100(self):
        analyzer = TextsAnalyzer("stub", "stub")
        for word in self.generate_words(1, 201):
            analyzer.register_100_longest(word)
        actual = analyzer.longest
        expected = self.generate_words(101, 201)
        self.assertEqual(len(actual), 100)
        self.assertSetEqual(set(actual), set(expected))
    
    def test_contains_letter_for_four_times(self):
        self.assertTrue(TextsAnalyzer.contains_letter_four_times("degenerate"))
        self.assertFalse(TextsAnalyzer.contains_letter_four_times("revenge"))
    
    def test_register_ngrams(self):
        analyzer = TextsAnalyzer("stub", "stub")
        analyzer.register_ngrams("python")
        self.assertEqual(analyzer.letters, ['p', 'y', 't', 'h', 'o', 'n'])
        self.assertEqual(analyzer.bigrams, ['py', 'yt', 'th', 'ho', 'on'])
        self.assertEqual(analyzer.trigrams, ['pyt', 'yth', 'tho', 'hon'])
    
    def test_register_one_letter_word(self):
        analyzer = TextsAnalyzer("stub", "stub")
        analyzer.register_word('i')
        self.assertTrue('i' in analyzer.letters)
    
    def test_register_two_letter_word(self):
        analyzer = TextsAnalyzer("stub", "stub")
        analyzer.register_word('if')
        self.assertTrue('if' in analyzer.two_letter_words)
    
    def test_register_word_with_four_occurrences_of_same_letter(self):
        analyzer = TextsAnalyzer("stub", "stub")
        analyzer.register_word('degenerate')
        self.assertTrue(
            'degenerate' in analyzer.with_multiple_occurrences_of_same_letter)
    
    def test_clean_words(self):
        text = "Probably, it wasn't a good idea?"
        expected = ['probably', 'it', 'wasn', 't', 'a', 'good', 'idea']
        actual = [x for x in TextsAnalyzer.clean_words(text)]
        self.assertEqual(expected, actual)
    
    def test_get_words_from_file(self):
        expected = ['probably', 'it', 'wasn', 't', 'a', 'good', 'idea']
        actual = [x for x in
                  TextsAnalyzer.get_words_from_file('textAnalyzerTest.txt')]
        self.assertEqual(expected, actual)
    
    @staticmethod
    def generate_words(shortest, longest):
        words = []
        for i in range(longest, shortest, -1):
            words.append('a' * i)
        shuffle(words)
        return words
