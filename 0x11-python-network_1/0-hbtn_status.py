#!/usr/bin/python3
"""Script that fetches 'https://alx-intranet.hbtn.io/status'
"""
from urllib import request, parse


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as res:
        res_read = res.read()
        response = [type(res_read),
                    res_read,
                    res_read.decode()]
        print("Body response:")
        print("    - type: {}".format(response[0]))
        print("    - content: {}".format(response[1]))
        print("    - utf8 content: {}".format(response[2]))
