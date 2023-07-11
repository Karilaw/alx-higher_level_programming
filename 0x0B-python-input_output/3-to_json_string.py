#!/usr/bin/python3
"""A module that defines a function that
returns JSON data
"""
import json


def to_json_string(my_obj):
    """
    a function that serializes object data

    :para my_obj: the object to serialize
    """
    return json.dumps(my_obj)
