import unittest

from Modules.cipherGenerator import CipherGenerator


class CipherGeneratorTest(unittest.TestCase):
    def test_cipher_should_be_substitution(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        cipher = CipherGenerator.generate_cipher(alphabet)
        self.assertEqual(len(alphabet), len(cipher))
        
        for i in alphabet:
            self.assertTrue(i in cipher.keys())
            self.assertTrue(i in cipher.values())
            self.assertTrue(cipher[i] in alphabet)
