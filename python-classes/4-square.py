#!/usr/bin/python3
"""Defines a Square class with size property and validation."""


class Square:
    """Class that defines a square by its size."""
    def __init__(self, size=0):
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
