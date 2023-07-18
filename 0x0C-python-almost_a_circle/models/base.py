#!/usr/bin/python3
"""A module that define a class Base
"""
import json
import csv
from os import path


class Base:
    """Base class for managing id attribute in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The id of the new Base instance. If not provided,
                the id is assigned the value of __nb_objects + 1.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + '.json'
        if not path.exists(filename):
            return []
        with open(filename, 'r') as f:
            data = f.read()
            dict_l = cls.from_json_string(data)
            return [cls.create(**d) for d in dict_l]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes data to csv data
        in a csv file"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                fieldnames = list(list_objs[0].to_dictionary().keys())
                writer_file = csv.DictWriter(f, fieldnames=fieldnames)
                writer_file.writeheader()
                for obj in list_objs:
                    writer_file.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserilizes csv data to python
        objects"""
        filename = cls.__name__+'.csv'
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                dict_list = [row for row in reader]
                result = []
                for d in dict_list:
                    int_dict = {k: int(v) for k, v in d.items()}
                    obj = cls.create(**int_dict)
                    result.append(obj)
                return result

        except FileNotFoundError:
            return []
