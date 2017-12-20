import unittest

from Modules.alphabets import Alphabet
from Modules.textCleaner import TextCleaner


class TextsCleanerTest(unittest.TestCase):
    def test_is_meaningful_english_word(self):
        self.assertFalse(
            TextCleaner.is_meaningful_word('boooom', Alphabet.EN.value))
        self.assertTrue(
            TextCleaner.is_meaningful_word('test', Alphabet.EN.value))
    
    def test_clean_words(self):
        text = "Probably, it wasn't a good idea?"
        expected = ['probably', 'it', 'wasn', 't', 'a', 'good', 'idea']
        actual = [x for x in TextCleaner.clean_text(text, Alphabet.EN.value)]
        self.assertEqual(expected, actual)
        
        # def test_get_words_from_file(self):
        #     expected = ['probably', 'it', 'wasn', 't', 'a', 'good', 'idea']
        #     actual = [x for x in
        #               TextsAnalyzer.get_words_from_file(
        #                   'tests/textAnalyzerTest.txt')]
        #     self.assertEqual(expected, actual)
