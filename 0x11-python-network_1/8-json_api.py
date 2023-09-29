#!/usr/bin/python3
""" a script that send data to url"""
import requests
import sys


def search_user(q=''):
    """Send post request to a specified URL with a
    letter as parameter
    """
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        json = r.json()
        id = json.get('id')
        name = json.get('name')
        if id and name:
            print("[{}] {}".format(id, name))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
