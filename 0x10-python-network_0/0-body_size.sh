#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response
URL=$1; curl -sI $URL | awk '/Content-Length/ {print $2}'
