#!/usr/bim/python3
"""A module for list of available attributes and methods of an object"""


def lookup(obj):
    """A function that returns the list of available attributes and methods of an object"""
    return(dir(obj))
