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

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_no_id(self):
        r2 = Rectangle(5, 5, 1)
        self.assertRegex(str(r2), r"\[Rectangle\] \(\d+\) 1/0 - 5/5")

    def test_str_zero_values(self):
        r3 = Rectangle(0, 0, 0, 0, 0)
        self.assertEqual(str(r3), "[Rectangle] (0) 0/0 - 0/0")

    def test_str_negative_values(self):
        r4 = Rectangle(-4, -6, -2, -1, -12)
        self.assertEqual(str(r4), "[Rectangle] (-12) -2/-1 - -4/-6")


    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        output = StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_no_offset(self):
        r2 = Rectangle(3, 2)
        output = StringIO()
        sys.stdout = output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "###\n###\n")

    def test_display_zero_width(self):
        r3 = Rectangle(0, 4, 2, 2)
        output = StringIO()
        sys.stdout = output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  \n  \n  \n  \n")

    def test_display_zero_height(self):
        r4 = Rectangle(4, 0, 2, 2)
        output = StringIO()
        sys.stdout = output
        r4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_multiple_args(self):
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89, 2, 3)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_all_args(self):
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r3), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args(self):
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(89, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r4), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_args_multiple(self):
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89, 2, 3)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_kwargs(self):
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(height=1)
        self.assertRegex(str(r3), r"\[Rectangle\] \(\d+\) 10/10 - 10/1")

    def test_update_kwargs_multiple(self):
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(width=1, x=2)
        self.assertRegex(str(r4), r"\[Rectangle\] \(\d+\) 2/10 - 1/10")

    def test_update_args_kwargs(self):
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, height=1)
        self.assertEqual(str(r5), "[Rectangle] (89) 10/10 - 10/10")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        self.assertIsInstance(d, dict)

    def test_to_dictionary_update(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)


if __name__ == '__main__':
    unittest.main()
