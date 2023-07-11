#!/usr/bin/python3
"""a module defying a function to append to
a file"""


def append_write(filename="", text=""):
    """
    a function to append text to anexisting
    file

    :param filename: the name of file
    :param text: text to append filename
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
