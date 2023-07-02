#!/usr/bin/python3
""" A module that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number

    Args:
            matrix(list): A list of lists of intergers or false
            div(int/float): The number to divide the matrix elements by
    Returns:
        list : A new matrix with the divided elements rounded off to 2 decimal places
    Raises:
        TypeError: If the matrix is not list of list of lists of intergers or floats
                if the rows of the matrix are not all the same size, or if div is not
                an interger or float
        ZeroDivision: If div is equal to 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
