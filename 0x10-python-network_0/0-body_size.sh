#!/bin/bash
# Takes in a URL and displays the size of the body of the response using curl
curl -s -i $1 | grep 'Content-Length' | cut -d " " -f2
