#!/usr/bin/python3
"""Module that defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherits
    from a_class, otherwise False."""
    return isinstance(obj, a_class)
