import sys
import unittest
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_str(self):
        s1 = Square(5)
        self.assertRegex(str(s1), r"\[Square\] \(\d+\) 0/0 - 5")

    def test_str_with_offset(self):
        s2 = Square(2, 2, 2)
        self.assertRegex(str(s2), r"\[Square\] \(\d+\) 2/2 - 2")

    def test_area(self):
        s3 = Square(3)
        self.assertEqual(s3.area(), 9)

    def test_display(self):
        s4 = Square(3, 1, 1)
        output = StringIO()
        sys.stdout = output
        s4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n ###\n ###\n ###\n")

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_validation(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"
        with self.assertRaises(ValueError):
            s.size = -1

    def test_update_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=1, size=2, x=3, y=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_args_kwargs(self):
        s = Square(5)
        s.update(1, 2, x=3, y=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 3)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 3, 'size': 5, 'x': 1, 'y': 2})
        self.assertIsInstance(d, dict)

    def test_to_dictionary_update(self):
        s1 = Square(5, 1, 2, 3)
        s2 = Square(1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == '__main__':
    unittest.main()
