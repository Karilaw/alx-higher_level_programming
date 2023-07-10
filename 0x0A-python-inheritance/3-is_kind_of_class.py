#!/usr/bin/python3
"""Defining a module that check if obj
is instance of class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is
    an instance of class
    """
    return isinstance(obj, a_class)
