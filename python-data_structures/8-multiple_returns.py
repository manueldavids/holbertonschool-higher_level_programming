#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Return a tuple with the length of a string
    and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the string and
        its first character.
               If the string is empty, the first character is None.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
