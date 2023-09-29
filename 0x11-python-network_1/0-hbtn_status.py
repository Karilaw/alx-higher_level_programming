#!/usr/bin/python3
"""
A module to fetch request
"""
import urllib.request


def fetch_url():
    """
    Fetches a given URL using the urllib package in Python.

    The URL of the resource to fetch is hardcoded as
    "https://alx-intranet.hbtn.io/status".

    Prints:
        str: The body of the response, showing its type, content,
        and utf8 content.
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_url()
