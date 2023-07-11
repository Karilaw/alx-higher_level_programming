#!/usr/bin/python3
"""
A module that defines function to
write contents to the file
"""


def write_file(filename="", text=""):
    """
    a fuction that write contents too the file

    :param filename: the name of file being written
    :param text: text to append to file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
