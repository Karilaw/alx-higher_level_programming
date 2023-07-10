#!/usr/bin/python3
"""A module that check if object is instance"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of class"""
    if isinstance(obj, a_class):
        return True
    return False
