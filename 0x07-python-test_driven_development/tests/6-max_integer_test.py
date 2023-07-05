#!/usr/bin/python3
"""This is unit test module"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_integer(self):
        """Test normal input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test empty list input"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
