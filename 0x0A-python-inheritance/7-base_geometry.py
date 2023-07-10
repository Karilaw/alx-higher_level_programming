#!/usr/bin/python3
"""A module defining BaseGeometry"""


class BaseGeometry:
    """a class that implement area methods"""

    def area(self):
        """A function defining area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that that validates value"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
