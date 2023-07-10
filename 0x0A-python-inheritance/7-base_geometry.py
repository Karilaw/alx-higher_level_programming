#!/usr/bin/python3
"""A module defining BaseGeomety"""


class BaseGeometry:
    """A class that represents a geometric shape."""

    def area(self):
        """Calculates the area of the shape. Not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        :param name: The name of the value being validated.
        :type name: str
        :param value: The value to validate.
        :type value: int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
