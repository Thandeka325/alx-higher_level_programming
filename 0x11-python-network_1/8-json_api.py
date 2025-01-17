#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter is sent in the variable 'q'. Handles JSON responses & errs
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            print(
                    ("[{}] {}".format(response_json.get("id"),
                     response_json.get("name")))
            )
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
