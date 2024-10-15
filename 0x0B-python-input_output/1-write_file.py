#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns the number of
    characters written.

    Args:
        filename (str): The path to the file to be written to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
