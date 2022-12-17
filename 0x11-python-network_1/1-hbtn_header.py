#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays the
value of the 'X-Request-Id' variable found in the header of the response
"""
from urllib import request
from sys import argv


if __name__ == '__main__':
    if len(argv) == 1:
        exit()
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
