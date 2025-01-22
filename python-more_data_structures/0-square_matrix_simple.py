#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square of all integers in a 2D matrix.

    Args:
        matrix: A 2D list of integers.

    Returns:
        A new matrix with the square of each integer in the input matrix.
    """
    return [[element ** 2 for element in row] for row in matrix]
