#!/bin/bash
#This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL -X GET "$1"
