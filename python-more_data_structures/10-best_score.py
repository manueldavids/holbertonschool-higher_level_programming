#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return the key with the highest integer value in the dictionary.

    Args:
        a_dictionary: The dictionary containing keys and integer values.

    Returns:
        The key with the highest value, or None if the dictionary is empty or None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
