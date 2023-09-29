#!/usr/bin/python3
"""a module that prints Request id"""
import requests
import sys


def fetch_url(url):
    """
    Fetches a given URL using the requests package in Python

    Args:
        url (str): The URL of the resource to fetch.

    Prints:
        str: The value of the X-Request-Id variable
    """
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
