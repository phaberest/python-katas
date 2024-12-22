import unittest
from sum_sequence import sum_sequence

class TestSumSequence(unittest.TestCase):
    def test_basic_sequences(self):
        self.assertEqual(sum_sequence(1), 1)
        self.assertEqual(sum_sequence(3), 6)
        self.assertEqual(sum_sequence(5), 15)
        
    def test_larger_number(self):
        self.assertEqual(sum_sequence(10), 55)
        
    def test_invalid_input(self):
        # Test negative number
        with self.assertRaises(ValueError):
            sum_sequence(-1)
            
        # Test zero
        with self.assertRaises(ValueError):
            sum_sequence(0)
            
        # Test float
        with self.assertRaises(ValueError):
            sum_sequence(3.5)
            
        # Test string
        with self.assertRaises(ValueError):
            sum_sequence("3")

if __name__ == '__main__':
    unittest.main()
