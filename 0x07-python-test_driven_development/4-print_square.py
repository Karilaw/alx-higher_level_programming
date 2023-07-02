#!/usr/bin/python3
"""Defining a fuction Square"""


def print_square(size):
    """
    Prints a square wth the given size using # character

    Args:
        size(int): The length of square

    Raises:
        TypeError: if size is not an interger
        ValueError: if size is less than 0

    """
    if isinstance(size, float) and size < 0:
         raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

