#!/usr/bin/python3
"""Defines a Square class with size validation and printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square's sides (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Uses setter to validate size

    @property
    def size(self):
        """Getter method to retrieve the size.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):  # Type check
            raise TypeError("size must be an integer")
        if value < 0:  # Value check
            raise ValueError("size must be >= 0")
        self.__size = value  # Stores the validated value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the character #.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):  # Loop through size
                print("#" * self.__size)  # Print size times #
