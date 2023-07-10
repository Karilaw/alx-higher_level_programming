#!/usr/bin/python3
"""A module that defines class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size):
        """Initializes a new Square with the given size.

        :param size: The size of the square.
        :type size: int
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
