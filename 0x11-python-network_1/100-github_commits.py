#!/usr/bin/python3
"""A Technical challenge by the Holberton School
    - Please list 10 commits (from the most recent to oldest) of the repository
      “rails” by the user “rails”
    - You must use the GitHub API, here is the documentation
      https://developer.github.com/v3/repos/commits/
    - Print all commits by: `<sha>: <author name>` (one by line)
This Python script takes 2 arguments, 'repository name' and 'owner name'
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/repos/' + argv[2] + '/' + argv[1] + '/commits'
    params = {'owner': 'rails', 'repo': 'rails', 'per_page': 10}
    response = requests.get(url, params=params)
    json_content = response.json()
    for commit in json_content:
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(commit.get('sha'), author_name))
