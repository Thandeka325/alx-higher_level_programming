#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after\
        each of the following characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """

    Prints text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text to be processed and printed.

    Raises:
        TypeError: If `text` is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a variable to hold the modified text
    result = ""

    # loop through each character in the text
    i = 0
    while i < len(text):
        result += text[i]
        # If the character is one of the specified, add two new lines
        if text[i] in ['.', '?', ':']:
            result += "\n\n"
            # skip consecutive spaces after these characters
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print the final result with no extra spaces
    print(result, end="")
