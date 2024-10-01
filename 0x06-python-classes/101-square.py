#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
It includes methods to calculate the area and print the square.
"""


class Square:
    """A class that defines a square by its size & position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size & position.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or if position\
                    is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.size == 0:
            print("")
            return

        # Print new lines for vertical position
        for _ in range(self.position[1]):
            print()
        # Print the square with spaces for horizontal position
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns the string representation of the square."""
        if self.size == 0:
            return ""

        result = []
        # Add new lines for vertical posistion
        result.append("\n" * self.position[1])
        # Add the square representation
        for _ in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)
            # Only add new line between rows, not at the end
            if _ < self.size - 1:
                result.append("\n")
        return "".join(result)
