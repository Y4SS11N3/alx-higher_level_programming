#!/usr/bin/python3
"""
Module 5-rectangle
Defines a class Rectangle with private attribute width and height,
methods for area, perimeter, string representation, repr, and del
"""


class Rectangle:
    """
    Defines a rectangle by its width and height with methods
    for area, perimeter, string representation, recreation, and deletion
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance"""
        self.width = width
        self.height = height

    # [Property methods for width and height as in previous snippets]

    def area(self):
        """Returns the area of the rectangle"""
        # [As in previous snippet]

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        # [As in previous snippet]

    def __str__(self):
        """Returns the printable string representation of the Rectangle"""
        # [As in previous snippet]

    def __repr__(self):
        """Returns the string representation for recreation of the Rectangle"""
        # [As in previous snippet]

    def __del__(self):
        """Prints a message upon deletion of a Rectangle instance"""
        print("Bye rectangle...")
