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
        expected = {'abbcd': ['apple'],
                    'abcbcb': ['banana'],
                    'ababcdef': ['cucumber']}
        actual = MasksBuilder.build_masks(words)
        self.assertEqual(expected, actual)
    
    def test_build_masks_when_several_words_have_same_mask(self):
        words = ['apple', 'banana', 'cucumber', 'peach', 'table']
        expected = {'abbcd': ['apple'],
                    'abcbcb': ['banana'],
                    'ababcdef': ['cucumber'],
                    'abcde': ['peach', 'table']}
        actual = MasksBuilder.build_masks(words)
        self.assertEqual(expected, actual)
