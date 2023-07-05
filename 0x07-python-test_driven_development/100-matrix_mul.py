#!/usr/bin/python3
"""A function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    # Check if m_a and m_b are not empty
    if not any(m_a) or not any(m_b):
        raise ValueError("m_a can't be empty" if not any(m_a) else "m_b can't be empty")
    # Check if all elements of m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")
    # Check if all rows of m_a and m_b are of the same size
    row_len = len(m_a[0])
    for row in m_a:
        if len(row) != row_len:
            raise TypeError("each row of m_a must be of the same size")
    row_len = len(m_b[0])
    for row in m_b:
        if len(row) != row_len:
            raise TypeError("each row of m_b must be of the same size")
    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
