import unittest
from find_pairs import find_pairs

class TestFindPairs(unittest.TestCase):
    def test_basic_pairs(self):
        self.assertEqual(find_pairs([1, 2, 3, 4, 5], 7), [(2, 5), (3, 4)])
        self.assertEqual(find_pairs([1, 1, 2, 3], 4), [(1, 3), (1, 3)])
        
    def test_no_pairs(self):
        self.assertEqual(find_pairs([1, 2, 3], 10), [])
        self.assertEqual(find_pairs([], 5), [])
        
    def test_negative_numbers(self):
        self.assertEqual(find_pairs([-1, 1, 2, 3, -2], 0), [(-2, 2), (-1, 1)])
        
    def test_duplicate_numbers(self):
        self.assertEqual(find_pairs([2, 2, 2, 2], 4), [(2, 2), (2, 2)])
        
    def test_invalid_input(self):
        # Test non-list input
        with self.assertRaises(ValueError):
            find_pairs("123", 6)
            
        # Test list with non-integers
        with self.assertRaises(ValueError):
            find_pairs([1, "2", 3], 5)
            
        # Test non-integer target
        with self.assertRaises(ValueError):
            find_pairs([1, 2, 3], "6")

if __name__ == '__main__':
    unittest.main()
