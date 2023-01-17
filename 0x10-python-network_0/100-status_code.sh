#!/bin/bash
# Sends a request to a URL passed and displays only the status code
curl -i -s -o /dev/null -w "%{http_code}" $1
