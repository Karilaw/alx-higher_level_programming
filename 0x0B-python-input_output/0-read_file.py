#!/usr/bin/python3
"""A module defining a functin that
reads files"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    :param filename: the name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

