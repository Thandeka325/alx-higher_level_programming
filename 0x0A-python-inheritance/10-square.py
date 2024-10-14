#!/usr/bin/python3
"""
This module contans the Square class that inherits from Ractangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class named Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to zero.
        """
        self.integer_validator("size", size)
        self.__size = size

        # Initialize the Rectangle with width & height equal to size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
