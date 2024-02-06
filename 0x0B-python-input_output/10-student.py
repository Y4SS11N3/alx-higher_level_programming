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
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is not None and all(isinstance(n, str) for n in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
