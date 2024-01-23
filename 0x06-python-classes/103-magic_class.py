#!/usr/bin/python3
import math


class MagicClass:
    """Represents a circle with methods for
    calculating its area and circumference."""

    def __init__(self, radius=0):
        """Initializes the circle with a given radius."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle."""
        return 2 * math.pi * self.__radius
