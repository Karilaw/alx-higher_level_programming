#!/usr/bin/python3
"""a module to send data to url"""
import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to a given URL with
    the email as a parameter
    and displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to send as a parameter.

    Prints:
        str: The body of the response, decoded in utf-8.
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
