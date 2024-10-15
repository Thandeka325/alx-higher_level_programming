#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file(UTF8) and returns the
    number of characters added.

    Args:
        filename (str): The path to the file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
