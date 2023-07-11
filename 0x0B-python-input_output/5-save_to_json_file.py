#!/usr/bin/python3
"""a module that define a fuction that
serializes python object and saves it
into a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a fuction that saves json data into
    given filename

    :param my_obj: the object to serialize
    :filename: name of the file
    """
    data = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(data)
