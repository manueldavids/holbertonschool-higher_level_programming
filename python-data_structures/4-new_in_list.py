#!/usr/bin/python3
# filepath: python-data_structures/4-new_in_list.py

def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position
    without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        element: The new element to insert.

    Returns:
        list: A new list with the element replaced, or
        a copy of the original list if idx is invalid.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
