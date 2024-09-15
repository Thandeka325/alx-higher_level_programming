#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]

    # Check if idx is within the valid range
    if 0 <= idx < len(my_list):
        # Relace the element at the given index
        new_list[idx] = element

    # Return the new list (either modified or an exact copy)
    return new_list
