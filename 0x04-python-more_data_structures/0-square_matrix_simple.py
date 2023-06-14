#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        new_row = list(map(lambda x: x ** 2, row))
        new_list.append(new_row)
    return new_list
