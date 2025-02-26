#!/usr/bin/python3
"""Defines a Square class with size and position validation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a private size and position attribute.

        Args:
            size (int): The size of the square's sides (default is 0).
            position (tuple): The (x, y) position offset (default is (0, 0)).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Uses setter to validate size
        self.position = position  # Uses setter to validate position

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

    @property
    def position(self):
        """Getter method to retrieve the position.

        Returns:
            tuple: The (x, y) position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position.

        Args:
            value (tuple): The (x, y) position offset.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Stores the validated value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the character #, considering position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print the top margin (newlines based on position[1])
        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):  # Loop through size
            print(" " * self.__position[0] + "#" * self.__size)  # Offset spaces + square
