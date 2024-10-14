#!/usr/bin/python3
"""
This module defines a MyInt class that inherits from int.
MyInt inverts the behavior of equality and inequality operators.
"""


class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators
    """

    def __eq__(self, other):
        """
        Invert the equality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the inequality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
