#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (only once for each integer).

    Args:
        my_list: A list of integers.

    Returns:
        The sum of all unique integers in the list.
    """
    return sum(set(my_list))
