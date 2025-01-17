#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response. If the HTTP status code
is 400 or greater, it prints an error message with status code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
