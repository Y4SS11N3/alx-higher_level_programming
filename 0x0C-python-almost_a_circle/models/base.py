#!/usr/bin/python3
"""Defines a base model class to manage
id attribute in all your future classes.

This module provides the Base class,
which is intended to be the "base" for other
classes in this project. It handles the initialization of the id attribute for
instances of classes that inherit from it, ensuring that each instance has a
unique id (either manually assigned or automatically generated).
"""

import json
import csv
import turtle
import random


class Base:
    """A base class for managing id attributes in all future classes.

    This class is designed to serve as a foundation for other classes that will
    inherit from it. It provides methods
    for converting dictionary representations
    to JSON strings, saving these representations to files, creating instances
    from dictionaries, and drawing instances using the Turtle graphics library.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of the
                            number of instances created without an explicit id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance, optionally with a specific id.

        Args:
            id (int, optional): An integer to use as the id for the instance.
                                If None, an id is automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list of dict):
            A list of dictionaries to convert.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        This method writes a JSON string representation of list_objs to a file,
        with the filename based on the class name of the objects in list_objs.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from a JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of cls with
        attributes set according to dictionary.

        This method creates a "dummy" instance of cls,
        then updates its attributes
        according to the dictionary passed as a keyword argument.

        Args:
            **dictionary (dict): A dictionary
            of attributes to set on the instance.

        Returns:
            instance: An instance of cls with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.

        This method reads a JSON file named
        after the cls class name, converts it
        from a JSON string to a list of dictionaries,
        and then creates instances
        of cls based on those dictionaries.

        Returns:
            list: A list of instances of cls.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to
        a CSV file named after the cls class.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from
        a CSV file named after the cls class.

        Returns:
            list: A list of instances of cls created from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the Turtle graphics module.

        This method uses the Turtle graphics library
        to draw rectangles and squares
        based on the instances provided in list_rectangles and list_squares.

        Args:
            list_rectangles (list): A list of Rectangle instances to draw.
            list_squares (list): A list of Square instances to draw.
        """
        turtle.speed(1)
        turtle.colormode(255)

        for rect in list_rectangles + list_squares:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.color(
                (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                if hasattr(rect, 'height'):
                    forward_distance = rect.height
                else:
                    forward_distance = rect.size

                turtle.forward(forward_distance)
                turtle.right(90)

        turtle.done()
