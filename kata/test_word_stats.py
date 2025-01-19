import unittest
from word_stats import word_stats

class TestWordStats(unittest.TestCase):
    def test_basic_stats(self):
        result = word_stats("Hello hello WORLD")
        self.assertEqual(result['frequencies'], {'hello': 2, 'world': 1})
        self.assertEqual(sorted(result['longest_word']), ['hello', 'world'])
        self.assertEqual(result['avg_length'], 5.0)
    
    def test_empty_input(self):
        result = word_stats("")
        self.assertEqual(result['frequencies'], {})
        self.assertEqual(result['longest_word'], [])
        self.assertEqual(result['avg_length'], 0.0)
        
        result = word_stats("   ")
        self.assertEqual(result['frequencies'], {})
        self.assertEqual(result['longest_word'], [])
        self.assertEqual(result['avg_length'], 0.0)
    
    def test_punctuation(self):
        result = word_stats("Hello, world! How are you?")
        self.assertEqual(
            result['frequencies'],
            {'hello': 1, 'world': 1, 'how': 1, 'are': 1, 'you': 1}
        )
        self.assertEqual(result['longest_word'], ['hello', 'world'])
        self.assertEqual(result['avg_length'], 3.8)
    
    def test_multiple_longest_words(self):
        result = word_stats("The quick brown fox jumps")
        self.assertEqual(
            sorted(result['longest_word']),
            ['brown', 'jumps', 'quick']  # All words with 5 letters
        )
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            word_stats(123)
        with self.assertRaises(ValueError):
            word_stats(['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
