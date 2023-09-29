#!/usr/bin/env python3
""" A module to fetch request """
import urllib.request


def fetch_url(url):
    """
    fetches a given URL using the urllib package in Python

    Args:
        url (str): the url of resource to fetch

    Prints:
        str: the body of response, showing its type, content
        and utf8 content.
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body response")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_url(url)
