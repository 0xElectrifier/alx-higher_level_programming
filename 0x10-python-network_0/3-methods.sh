#!/bin/bash
# Displays all HTTP methods the first argument(server) will accept
curl -isX "OPTIONS" $1 | grep "Allow: " | cut -d " " -f2
