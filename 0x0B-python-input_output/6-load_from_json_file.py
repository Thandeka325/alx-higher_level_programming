#!/usr/bin/python3
"""
This module defines a function that creates an object fron JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The deserialized Python object from JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
