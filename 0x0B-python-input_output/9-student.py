#!/usr/bin/python3
"""a module that defines a class student"""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        :param first_name: the student's first name
        :param last_name: the student's last name
        :param age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the student.

        :return: the dictionary representation of the student
        """
        return self.__dict__
