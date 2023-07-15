#!/usr/bin/python3
"""A module with test cases for
RECTANGLE module
"""

import sys
import unittest
from io import StringIO
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_width_property(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        r.width = 30
        self.assertEqual(r.width, 30)
        with self.assertRaises(TypeError):
            r.width = "not an int"
        with self.assertRaises(ValueError):
            r.width = -1

    def test_height_property(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.height, 20)
        r.height = 30
        self.assertEqual(r.height, 30)
        with self.assertRaises(TypeError):
            r.height = "not an int"
        with self.assertRaises(ValueError):
            r.height = -1

    def test_x_property(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.x, 0)
        r.x = 30
        self.assertEqual(r.x, 30)
        with self.assertRaises(TypeError):
            r.x = "not an int"

    def test_y_property(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.y, 0)
        r.y = 30
        self.assertEqual(r.y, 30)
        with self.assertRaises(TypeError):
            r.y = "not an int"

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

        r2 = Rectangle(5, 5)
        self.assertEqual(r2.area(), 25)

        r3 = Rectangle(0, 10)
        self.assertEqual(r3.area(), 0)

        r4 = Rectangle(10, 0)
        self.assertEqual(r4.area(), 0)

        r5 = Rectangle(0, 0)
        self.assertEqual(r5.area(), 0)

    def test_display(self):
        r1 = Rectangle(4, 6)
        output = StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n####\n####\n")

    def test_display_small(self):
        r2 = Rectangle(2, 2)
        output = StringIO()
        sys.stdout = output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_zero_width(self):
        r3 = Rectangle(0, 4)
        output = StringIO()
        sys.stdout = output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n\n\n")

    def test_display_zero_height(self):
        r4 = Rectangle(4, 0)
        output = StringIO()
        sys.stdout = output
        r4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
