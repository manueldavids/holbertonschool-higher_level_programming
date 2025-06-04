#!/usr/bin/python3
"""
This module provides a function to convert a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
