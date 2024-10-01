#!/usr/bin/python3
"""
This module defines a Square with size and position attribute validation,\
        property methods, and methods to compute the area of the square\
        and print the square using '#'.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with an optional size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square,\
                    defined as a tuple of 2 positive integers.\
                    Default is (0, 0).
        Raises:
            TypeError: If size is not an integer or if position\
                    is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if any value\
                    position is less than 0.
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
            value (int): The size value to set.

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
            value (tuple): The position value to set, which should\
                    be a tuple of 2 positive integers.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character '#'\
                based on the size & position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print the new lines for vertical position (position[1])
        print("\n" * self.__position[1], end="")

        # Print the square with spaces for horizontal position (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
