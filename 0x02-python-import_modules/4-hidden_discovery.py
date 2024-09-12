#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4) # Get all names from hidden_4
    for name in names: # Sorts names alphabetically
        if name[:2] != "__": # Filter out
                print(name)
