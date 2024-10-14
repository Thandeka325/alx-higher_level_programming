#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and includes a method to print the
    list sorted in asscending order.
    """

    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """

        Prints the list in ascending sorted order.

        Assumes all elements of type int.
        """
        print(sorted(self))
