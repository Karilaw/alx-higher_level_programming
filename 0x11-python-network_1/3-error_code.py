#!/usr/bin/env python3
""" Module that sends request and print error code"""
import urllib.request
import urllib.error
import sys


def send_request(url):
    """
    sends a request to url and displays the body of request

    Args:
        url (str): The URL to send the request to

    Prints:
        str: the body of reponse
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


url = sys.argv[1]
send_request(url)
