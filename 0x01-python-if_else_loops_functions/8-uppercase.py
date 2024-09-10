#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        # Convert to uppercase if character is lowercase
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
