import unittest

from encryptor import Encryptor


class MaskBuilderTest(unittest.TestCase):
    def test_encrypt_word(self):
        word = "apple"
        alphabet = "aple"
        cipher = {'a': 'e',
                  'p': 'a',
                  'l': 'l',
                  'e': 'p'
                  }
        encryptor = Encryptor(cipher, alphabet)
        expected = "eaalp"
        actual = encryptor.replace(word)
        self.assertEqual(expected, actual)
    
    def test_ignore_unknown_chars(self):
        word = "apples"
        alphabet = "aple"
        cipher = {'a': 'e',
                  'p': 'a',
                  'l': 'l',
                  'e': 'p'
                  }
        encryptor = Encryptor(cipher, alphabet)
        expected = "eaalps"
        actual = encryptor.replace(word)
        self.assertEqual(expected, actual)

    def test_save_cases(self):
        word = "Apple"
        alphabet = "aple"
        cipher = {'a': 'e',
                  'p': 'a',
                  'l': 'l',
                  'e': 'p'
                  }
        encryptor = Encryptor(cipher, alphabet)
        expected = "Eaalp"
        actual = encryptor.replace(word)
        self.assertEqual(expected, actual)