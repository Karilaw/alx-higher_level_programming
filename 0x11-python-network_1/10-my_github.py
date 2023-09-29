#!/usr/bin/python3
""" A module that sends data into Github
"""
import requests


def get_github_id(username, token):
    """
    a function that returns github id
    """
    r = requests.get('https://api.github.com/user', auth=(username, token))
    json = r.json()
    print(json.get('id'))


if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
