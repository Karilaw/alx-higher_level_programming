#!/usr/bin/python3
"""A module defining BaseGeomety"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculates the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer
        Args:
            name (str): the name of the value being checked
            value (int): the value to check
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
