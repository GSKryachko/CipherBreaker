import unittest

from encryptor import Encryptor


class MaskBuilderTest(unittest.TestCase):
    def test_encrypt_word(self):
        word = "apple"
        encryptor = Encryptor("aple")
        encryptor.cipher = {'a': 'e',
                            'p': 'a',
                            'l': 'l',
                            'e': 'p'
                            }
        expected = "eaalp"
        actual = encryptor.encrypt(word)
        self.assertEqual(expected, actual)
    
    def test_ignore_unknown_chars(self):
        word = "apples"
        encryptor = Encryptor("aple")
        encryptor.cipher = {'a': 'e',
                            'p': 'a',
                            'l': 'l',
                            'e': 'p'
                            }
        expected = "eaalps"
        actual = encryptor.encrypt(word)
        self.assertEqual(expected, actual)
