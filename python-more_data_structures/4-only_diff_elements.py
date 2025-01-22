#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Find all elements present in only one of two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A set containing elements present in only one of the two sets.
    """
    return set_1 ^ set_2
