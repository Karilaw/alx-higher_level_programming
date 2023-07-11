#!/usr/bin/python3
"""A module that defines a function
that describes json data
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure for
    JSON serialization of an object

    :param obj: an instance of a Class
    :return: the dictionary description of the object
    """
    return obj.__dict__
