#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4) # Get all names from hidden_4
    for name in sorted(names): # Sorts names alphabetically
        if not name.startswith("__"): # Filter out
                print(name)
