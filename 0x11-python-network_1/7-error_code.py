#!/usr/bin/python3
""" a module that sends request to url"""
import requests
import sys


def send_request(url):
    """
    send a request to a given URL and display the body of
    response
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
