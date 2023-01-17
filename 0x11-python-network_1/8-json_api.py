#!/usr/bin/python3
"""Script that takes in a letter and sends a 'POST' requeset to
'http://0.0.0.0:5000/search_user' with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        data = {'q': ''}
    else:
        data = {'q': argv[1]}
    response = requests.post(url, data=data)
    if response.headers['Content-Type'] == 'application/json':
        content = response.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get('id'), content.get('name')))
    else:
        print("Not a valid JSON")
