#!/usr/bin/python3
"""
This module provides the matrix_divided function for dividing all elements
of a matrix by a number with specific validation checks.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide the elements of the matrix.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
                   If each row of the matrix is not the same size.
                   If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate the matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row sizes
    row_sizes = {len(row) for row in matrix}
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide elements of the matrix
    return [[round(element / div, 2) for element in row] for row in matrix]
