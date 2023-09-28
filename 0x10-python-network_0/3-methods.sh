#!/bin/bash
# this scipt sends OPTIONS request to a URL and display all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f2-
