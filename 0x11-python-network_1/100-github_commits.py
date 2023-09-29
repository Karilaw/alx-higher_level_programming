#!/usr/bin/python3
""" a module to send data to github"""
import requests


def get_commits(repo_name, owner_name):
    """
    Sends a GET request to the GitHub API
    """
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(owner_name, repo_name))
    json = r.json()
    for i in range(10):
        print("{}: {}".format(json[i].get('sha'), json[i].get('commit').get('author').get('name')))


if __name__ == "__main__":
    import sys
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repo_name, owner_name)
