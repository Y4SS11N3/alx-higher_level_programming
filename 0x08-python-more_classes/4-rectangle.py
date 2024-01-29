#!/usr/bin/python3
"""
Module 4-rectangle
Defines a class Rectangle with private attribute width and height,
methods area, perimeter, string representation, and repr for recreation
"""


class Rectangle:
    """
    Defines a rectangle by its width and height with methods
    to calculate the area, perimeter, and string representations
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance"""
        self.width = width
        self.height = height

    # [Property methods for width and height as in previous snippet]

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable string representation of the Rectangle"""
        # [As in previous snippet]

    def __repr__(self):
        """Returns the string representation for recreation of the Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
