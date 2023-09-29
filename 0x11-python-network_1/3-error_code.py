#!/usr/bin/python3
"""
A module that sends a request to a URL and prints the error code if any
"""
import urllib.request
import urllib.error
import sys


def send_request(url):
    """
    Sends a request to a given URL and displays the body of the response.
    If an HTTP error occurs, it prints the error code.

    Args:
        url (str): The URL to send the request to.

    Prints:
        str: The body of the response, decoded in utf-8,
        or the HTTP error code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
