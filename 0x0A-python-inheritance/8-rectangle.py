#!/usr/bin/python3
"""A module defing class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle."""

    def __init__(self, width, height):
        """Initializes a new Rectangle with the given width and height.

        :param width: The width of the rectangle.
        :type width: int
        :param height: The height of the rectangle.
        :type height: int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
