#!/usr/bin/python3
# filepath: python-data_structures/3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
        my_list (list): The list of integers to print.
    """
    if my_list is None:
        return
    for i in my_list[::-1]:
        print("{:d}".format(i))
