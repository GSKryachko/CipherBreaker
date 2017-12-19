import unittest

from cipherAnalyzer import CipherAnalyzer


class CipherAnalyzerTest(unittest.TestCase):
    # def test_try_get_cipher_when_determined(self):
    #     analyzer = CipherAnalyzer(None, None, 'aple')
    #     assumed_cipher = {'a': ['e'],
    #                       'p': ['a'],
    #                       'l': ['l'],
    #                       'e': ['p']
    #                       }
    #     analyzer.assumed_cipher = assumed_cipher
    #     expected = {'a': 'e',
    #                 'p': 'a',
    #                 'l': 'l',
    #                 'e': 'p'
    #                 }
    #     analyzer.try_get_cipher()
    #     actual = analyzer.cipher
    #     self.assertEqual(expected, actual)
    #
    # def test_try_get_cipher_when_undetermined(self):
    #     analyzer = CipherAnalyzer(None,None,'aple')
    #     assumed_cipher = {'a': ['e', 'p'],
    #                       'p': ['a'],
    #                       'l': ['l'],
    #                       'e': ['p']
    #                       }
    #     analyzer.assumed_cipher = assumed_cipher
    #     expected = None
    #     actual = analyzer.try_get_cipher()
    #     self.assertEqual(expected, actual)
    #
    # def test_register_chars(self):
    #     analyzer = CipherAnalyzer(None,None,'abcdefghijklmnopqrstuvwxyz')
    #     mask = 'abcde'
    #     words = ['plant', 'world', 'close']
    #     analyzer.register_chars(words, mask)
    #     actual = analyzer.assumed_cipher
    #     expected = {'a': {'p', 'w', 'c'},
    #                 'b': {'l', 'o', 'l'},
    #                 'c': {'a', 'r', 'o'},
    #                 'd': {'n', 'l', 's'},
    #                 'e': {'t', 'd', 'e'}
    #                 }
    #     self.assertEqual(actual, expected)
    #
    # def test_analyze_cipher_with_sufficient_data(self):
    #     words_with_masks = {'abcd': ['time'],
    #                         'abcde': ['cloud']}
    #     analyzer = CipherAnalyzer(words_with_masks)
    #     text = ['zero', 'dalxw']
    #     expected = {'z': 't',
    #                 'e': 'i',
    #                 'r': 'm',
    #                 'o': 'e',
    #                 'd': 'c',
    #                 'a': 'l',
    #                 'l': 'o',
    #                 'x': 'u',
    #                 'w': 'd'}
    #     actual = analyzer.analyze_cipher_using_range(text)
    #     self.assertDictEqual(actual, expected)
    #
    
    def test_range_mask(self):
        self.assertEqual(14, CipherAnalyzer.range_mask('bonobo'))
    
    def test_make_random_transposition(self):
        cipher = {'a': 'b',
                  'c': 'a',
                  'b': 'c'}
        changed_cipher = CipherAnalyzer.make_random_transposition(cipher)
        self.assertSetEqual(set(cipher.keys()), set(changed_cipher.keys()))
        self.assertSetEqual(set(changed_cipher.values()),
                            set(changed_cipher.keys()))