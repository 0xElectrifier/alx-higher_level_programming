#!/bin/bash
# Sends a JSON 'POST' request to a URL and displays the body of the response
curl -sX 'POST' -d @$2 -H 'Content-Type: application/json' $1;
