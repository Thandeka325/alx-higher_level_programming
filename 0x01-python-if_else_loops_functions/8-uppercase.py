#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Convert to uppercase if character is lowercase
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
