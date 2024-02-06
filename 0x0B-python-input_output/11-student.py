#!/usr/bin/python3
"""Defines a student."""


class Student:
    """A student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the student filtered by attrs."""
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from json."""
        for key, value in json.items():
            setattr(self, key, value)
