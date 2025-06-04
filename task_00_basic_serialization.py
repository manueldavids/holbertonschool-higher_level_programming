#!/usr/bin/env python3
"""
Basic serialization module: serialize a Python dictionary to JSON file
and deserialize JSON file back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename to save the JSON data.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The filename from which to read the JSON data.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
