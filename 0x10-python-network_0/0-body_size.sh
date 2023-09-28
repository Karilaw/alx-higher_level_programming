#!/bin/bash
# this script takes a URL as an argument, sends a request to that URL
URL=$1
curl -sI $URL | grep 'Content-Length' | cut -d' ' -f2
