#!/usr/bin/python3
"""a module defining Rectangle
class
"""
from models.base import Base
import json


class Rectangle(Base):
    """Represents a rectangle shape.

    Inherits from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The id of the rectangle
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be a positive integer")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be a positive integer")
        self._height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle
        """
        return self._x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle.

        Args:
            value (int): The new x-coordinate of the rectangle.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self._x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self._y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle.

        Args:
            value (int): The new y-coordinate of the rectangle.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self._y = value

    def area(self):
        """ Gets the area of Rectangle"""
        return self._width * self._height

    def display(self):
        """ A fuction that print # when it finds instance
        of Rectangle"""
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """Returns string representation of instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwags):
        """assign each arg to attribute"""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwags.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation
        of a Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height':
                self.height, 'x': self.x, 'y': self.y}
