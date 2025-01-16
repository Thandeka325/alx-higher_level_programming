#!/bin/bash
#This script takes in a URL, sends a request to that URL.
# Displays the size of the body of the response.

curl -s "$1" -o /dev/null -w "%{size_download}\n"
