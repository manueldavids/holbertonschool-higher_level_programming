#!/usr/bin/python3
"""Module that defines Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize size after validation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
