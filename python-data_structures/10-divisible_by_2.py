#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of booleans where True means the corresponding integer
              in the original list is divisible by 2, and False otherwise.
    """
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
