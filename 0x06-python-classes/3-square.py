#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """This class defines a square with a private instance attribute size."""

    def __init__(self, size=0):
        """Initialize the square with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
