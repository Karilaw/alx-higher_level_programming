#!/usr/bin/python3
"""A module that defines a MyList class"""


class MyList(list):
    """A class that represents a custom list."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
