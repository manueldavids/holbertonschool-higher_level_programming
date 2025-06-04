#!/usr/bin/python3
"""
Function that returns the dictionary description
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return the dictionary description of obj for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary of obj’s attributes.
    """
    return obj.__dict__
