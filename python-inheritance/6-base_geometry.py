#!/usr/bin/python3
"""Module that defines BaseGeometry class with area method."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
