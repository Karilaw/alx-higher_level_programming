#!/usr/bin/python3
"""a module that define a function that
deserizes json data
"""
import json


def from_json_string(my_str):
    """
    a fuction that returns python object

    :param my_str: json string
    """
    return json.loads(my_str)
