#!/bin/bash
# this script takes a URL as an argument, sends a request to that URL,
# and displays the size of the body of the response

URL=$1

curl -sI "URL" | grep 'Content-Length' | cut -d' ' -f2
