#!/usr/bin/python3


def add_integer(a, b=98):
    """
    adds two integer
    Args:
        a(int, float) The first integer or float to add
        b(int, float) The second integer or float to add Default to 98
    Returns:
        int: The sum of a and b as a integer
    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
