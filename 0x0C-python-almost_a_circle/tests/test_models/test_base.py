#!/usr/bin/python3
""" A base test Module for the
base class
"""
import os
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test case for the Base class."""

    def test_id(self):
        """Test the behavior of the id attribute."""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        d = [{'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}]
        json_d = Base.to_json_string(d)
        self.assertEqual(json_d, '[{"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}]')
        self.assertIsInstance(json_d, str)

    def test_to_json_string_empty(self):
        json_d = Base.to_json_string(None)
        self.assertEqual(json_d, '[]')
        json_d = Base.to_json_string([])
        self.assertEqual(json_d, '[]')

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')


    def test_save_to_file_empty(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_from_json_string(self):
        json_str = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertEqual(list_dicts, [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}, {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}])
        self.assertIsInstance(list_dicts, list)

    def test_from_json_string_empty(self):
        list_dicts = Base.from_json_string(None)
        self.assertEqual(list_dicts, [])
        list_dicts = Base.from_json_string("")
        self.assertEqual(list_dicts, [])

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file(self):
        # Test for Rectangle
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_input), len(list_rectangles_output))
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_rectangles_input[i].__str__(), list_rectangles_output[i].__str__())

        # Test for Square
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_input), len(list_squares_output))
        for i in range(len(list_squares_input)):
            self.assertEqual(list_squares_input[i].__str__(), list_squares_output[i].__str__())

        # Test for file not found
        os.remove("Rectangle.json")
        os.remove("Square.json")
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
