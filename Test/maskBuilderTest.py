import unittest

from masksBuilder import MasksBuilder


class MaskBuilderTest(unittest.TestCase):
    def test_build_mask(self):
        word = "apple"
        expected = "abbcd"
        actual = MasksBuilder.build_mask(word)
        self.assertEqual(expected, actual)
    
    def test_build_masks(self):
        words = ['apple', 'banana', 'cucumber']
        expected = {'apple': 'abbcd',
                    'banana': 'abcbcb',
                    'cucumber': 'ababcdef'}
        actual = MasksBuilder.build_masks(words)
        self.assertEqual(expected, actual)
