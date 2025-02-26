#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square. """

    def __init__(self, size):
        """Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size  # Private instance attribute
