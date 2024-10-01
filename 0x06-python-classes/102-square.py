#!/usr/bin/python3
"""
Tis module defines a Square with comparison based on area.
"""


class Square:
    """A class that defines a square based on its size."""

    def __init__(self, size=0):
        """Initializes the square with the given size.

        Args:
            size (float or int): The size of the square. Default is 0.
            Raises:
                TypeError: If size is not a number(float or integer)
                ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the current square is < other square based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if current square is <= to another square based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """check if current square is greater other square based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if current square is >= to another square based on area."""
        return self.area() >= other.area()
