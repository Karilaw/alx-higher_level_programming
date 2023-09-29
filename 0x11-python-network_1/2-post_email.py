#!/usr/bin/env python3
""" a module that sens email data to url"""
import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Sends a POST request to a given URL with the email as a parameter
    and displays the body of response

    Args:
        url (str): The URL to send the Post request to.
        email (str): The email to send as a parameter.

    Prints:
        str: The body of the response, decoded in utf-8.
    """
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Failed to make a request to {}: {}".format(url, e.reason))


url = sys.argv[1]
email = sys.argv[2]

send_post_request(url, email)
