#!/bin/bash
#This script takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i "^ALLOW:" | cut -d " " -f2-
