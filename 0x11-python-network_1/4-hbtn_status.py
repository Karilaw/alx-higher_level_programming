#!/usr/bin/python3
"""
A module that sends a request to a
URL and prints the body of the response.
"""
import requests


def fetch_url():
    """
    Fetches a given URL using the requests package in Python.

    The URL of the resource to fetch is hardcoded as
    "https://alx-intranet.hbtn.io/status".

    Prints:
        str: The body of the response, showing its type,
        content, and utf8 content.
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_url()
