#!/bin/bash
# sends a request to a URL passed as argument and displays only the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
