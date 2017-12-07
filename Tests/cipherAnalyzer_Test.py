import unittest

from cipherAnalyzer import CipherAnalyzer


class CipherAnalyzerTest(unittest.TestCase):
    def test_try_get_cipher_when_determined(self):
        analyzer = CipherAnalyzer(None)
        assumed_cipher = {'a': ['e'],
                          'p': ['a'],
                          'l': ['l'],
                          'e': ['p']
                          }
        analyzer.assumed_cipher = assumed_cipher
        expected = {'a': 'e',
                    'p': 'a',
                    'l': 'l',
                    'e': 'p'
                    }
        analyzer.try_get_cipher()
        actual = analyzer.cipher
        self.assertEqual(expected, actual)
    
    def test_try_get_cipher_when_undetermined(self):
        analyzer = CipherAnalyzer(None)
        assumed_cipher = {'a': ['e', 'p'],
                          'p': ['a'],
                          'l': ['l'],
                          'e': ['p']
                          }
        analyzer.assumed_cipher = assumed_cipher
        expected = None
        actual = analyzer.try_get_cipher()
        self.assertEqual(expected, actual)
    
    def test_register_chars(self):
        analyzer = CipherAnalyzer(None)
        mask = 'abcde'
        words = ['plant', 'world', 'close']
        analyzer.register_chars(words, mask)
        actual = analyzer.assumed_cipher
        expected = {'a': {'p', 'w', 'c'},
                    'b': {'l', 'o', 'l'},
                    'c': {'a', 'r', 'o'},
                    'd': {'n', 'l', 's'},
                    'e': {'t', 'd', 'e'}
                    }
        self.assertEqual(actual, expected)
    
    def test_analyze_cipher_with_sufficient_data(self):
        words_with_masks = {'abcd': ['time'],
                            'abcde': ['cloud']}
        analyzer = CipherAnalyzer(words_with_masks)
        text = ['zero', 'dalxw']
        expected = {'z': 't',
                    'e': 'i',
                    'r': 'm',
                    'o': 'e',
                    'd': 'c',
                    'a': 'l',
                    'l': 'o',
                    'x': 'u',
                    'w': 'd'}
        actual = analyzer.analyze_cipher_using_range(text)
        self.assertDictEqual(actual, expected)
    
    def test_prepare_words(self):
        text = "I have a pen. I have an apple."
        expected = ['i', 'have', 'a', 'an', 'pen', 'apple']
        actual = CipherAnalyzer.prepare_words(text)
        self.assertSetEqual(set(actual), set(expected))
    
    def test_range_mask(self):
        self.assertEqual(14, CipherAnalyzer.range_mask('bonobo'))
