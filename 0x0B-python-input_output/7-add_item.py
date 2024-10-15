#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and saves them to a file
"""
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

# Load list from the file if it exists,otherwise start with an empty file
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all command-line arguments (excluding script name) to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
