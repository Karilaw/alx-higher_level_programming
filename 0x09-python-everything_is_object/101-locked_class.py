#!/usr/bin/python3
"""Defining a module LockedClass"""


class LockedClass:
    """A class that prevents dynamic creation of instance attributes.

    This class uses the `__slots__` attribute to define a list of allowed
    instance attributes. The only allowed instance attribute is `first_name`.

    Attempting to create an instance attribute with a different name will
    result in an `AttributeError`.
    """

    __slots__ = ['first_name']
