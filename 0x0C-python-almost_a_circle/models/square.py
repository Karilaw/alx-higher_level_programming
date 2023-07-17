#!/usr/bin/python3
"""A module that defines class
Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
            y (int, optional): The y-coordinate of the square.
            id (int, optional): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance.

        Returns:
            str: A string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwags):
        """Set attributes to arguments
        provided"""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwags.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation
        of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
