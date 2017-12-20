import unittest

from Modules.alphabets import Alphabet
from Modules.textCleaner import TextCleaner


class TextsCleanerTest(unittest.TestCase):
    def test_is_meaningful_english_word(self):
        self.assertFalse(
            TextCleaner.is_meaningful_word('boooom', Alphabet.EN))
        self.assertTrue(
            TextCleaner.is_meaningful_word('test', Alphabet.EN))
    
    def test_clean_words(self):
        text = ["Probably, it wasn't a good idea?"]
        expected = ['probably', 'it', 'wasn', 't', 'a', 'good', 'idea']
        actual = [x for x in TextCleaner.clean_text(text, Alphabet.EN)]
        self.assertEqual(expected, actual)

    def test_is_meaningful_word(self):
        self.assertFalse(TextCleaner.is_meaningful_word('boooom', Alphabet.EN))
        self.assertTrue(TextCleaner.is_meaningful_word('test', Alphabet.EN))
