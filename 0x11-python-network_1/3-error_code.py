#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in 'utf-8')
"""
from urllib import request, error
from sys import argv


if __name__ == '__main__':
    if len(argv) == 1:
        exit()

    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            ret = response.read().decode(encoding='utf-8')
            print(ret)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

