#!/usr/bin/python3
"""a module that defines a function that
creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    a fuction that create python
    object from json file

    :param filename: name of the file
    """
    with open(filename, 'r') as f:
        return json.load(f)
