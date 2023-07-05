#!/usr/bin/python3
"""This module provides a solution to the N queens problem
using a recursive backtracking algorithm.
"""


import sys


def can_place(board, row, col):
    """
    Check if a queen can be placed in a given position.

    Args:
        board (list): A list representing
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if a queen can be placed, False otherwise.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row):
    """
    Find all solutions to the N queens problem using backtracking.

    Args:
        board (list): A list representing the current state of the chessboard.
        row (int): The current row to place a queen in.

    Returns:
        None
    """
    n = len(board)
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if can_place(board, row, col):
            board[row] = col
            solve(board, row + 1)
            board[row] = -1

def main():
    """
    Parse command line arguments and solve the N queens problem.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0)

if __name__ == "__main__":
    main()
