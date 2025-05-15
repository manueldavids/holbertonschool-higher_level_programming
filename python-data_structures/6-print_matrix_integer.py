#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
        matrix (list of lists): The matrix to print.
    """
    if not matrix or matrix == [[]]:
        print("")
        return
    for row in matrix:
        for i, num in enumerate(row):
            if i != len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print("")
        