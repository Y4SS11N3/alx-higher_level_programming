#!/usr/bin/python3
"""Extends BaseGeometry with integer validation."""


class BaseGeometry:
    """A base geometry class with area and integer validation."""
    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a given integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
