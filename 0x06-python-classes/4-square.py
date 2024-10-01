#!/usr/bin/python3
"""
This module defines a Square class with size attribute validation,\
        property methods,and a method to compute the area of the square.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with an optional size.


        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.


        Returs:
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
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Computes and returns the are of the square.


        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
