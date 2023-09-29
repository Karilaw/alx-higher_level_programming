#!/usr/bin/env python3
"""
A module to get Request id
"""
import urllib.request
import sys


def fetch_url(url):
    """
    Fetches a given URL and displays the value of
    X-Request-ID

    Args:
        url (str): The URL of the resource to fetch

    Prints:
        str: The value of the X-Request-Id
    """

    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])


url = sys.argv[1]
fetch_url(url)
