import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 1, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)

    def test_setters(self):
        r = Rectangle(10, 2)

        r.width = 20
        self.assertEqual(r.width, 20)

        r.height = 30
        self.assertEqual(r.height, 30)

        r.x = 40
        self.assertEqual(r.x, 40)

        r.y = 50
        self.assertEqual(r.y, 50)

    def test_setters_validation(self):
        r = Rectangle(10, 2)

        with self.assertRaises(TypeError):
            r.width = "not an int"

        with self.assertRaises(ValueError):
            r.width = -1

        with self.assertRaises(TypeError):
            r.height = "not an int"

        with self.assertRaises(ValueError):
            r.height = -1

        with self.assertRaises(TypeError):
            r.x = "not an int"

        with self.assertRaises(TypeError):
            r.y = "not an int"


if __name__ == '__main__':
    unittest.main()
