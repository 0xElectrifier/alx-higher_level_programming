#!/usr/bin/python3
"""Script that fetches 'https://alx-intranet.hbtn.io/status'
"""
from urllib import request, parse


req = request.Request('https://alx-intranet.hbtn.io/status')
with request.urlopen(req) as res:
    res_read = res.read()
    response = [type(res_read),
                     res_read,
                     res.msg]
    print("Body response:\n\
    - type: {}\n\
    - content: {}\n\
    - utf8 content: {}".format(response[0],
                               response[1],
                               response[2]))


#        for item in response.values()
