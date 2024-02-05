#!/usr/bin/python3
"""Extends BaseGeometry with integer validation."""


class BaseGeometry:
    """A base geometry class with area and integer validation."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The identifier of the parameter being validated.
            value (int): Validate the name parameter’s value.

        Raises:
            TypeError: If `value` is not an integer or is actually a boolean.
            ValueError: If `value` is less than or equal to 0.
        """
        if type(value) != int or type(value) == bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
