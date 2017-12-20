import unittest

from Modules.cipherAnalyzer import CipherAnalyzer


class CipherAnalyzerTest(unittest.TestCase):
    
    def test_make_random_transposition(self):
        cipher = {'a': 'b',
                  'c': 'a',
                  'b': 'c'}
        changed_cipher = CipherAnalyzer.make_random_transposition(cipher)
        self.assertSetEqual(set(cipher.keys()), set(changed_cipher.keys()))
        self.assertSetEqual(set(changed_cipher.values()),
                            set(changed_cipher.keys()))
