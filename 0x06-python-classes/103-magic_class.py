#!/usr/bin/python3
"""MagicClass replicating a specific bytecode structure."""

import math


class MagicClass:
    """Circle representation for area and circumference calculations."""

    def __init__(self, radius=0):
        """Initializes the circle."""
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.__radius
