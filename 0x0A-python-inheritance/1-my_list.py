#!/usr/bin/python3
"""A module 1-my_list.py"""


class MyList(list):
    """Defining a class MyList"""

    def print_sorted(self):
        """prints the list in sorted order"""
        print(sorted(self))
