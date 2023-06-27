#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """This class defines a square with a private instance attribute size."""
    def __init__(self, size=0):
        """Initialize the square with the given size."""
        self.size = size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square to the given value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the current square area."""
        return self.__size ** 2
