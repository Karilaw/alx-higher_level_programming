#!/usr/bin/python3
"""a module that defines a class that
operators inverted"""


class MyInt(int):
    """A rebel subclass of int with
    inverted == and != operators"""

    def __eq__(self, other):
        """Override the == operator to return the
        opposite of the superclass result"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to return the
        opposite of the superclass result"""
        return super().__eq__(other)
