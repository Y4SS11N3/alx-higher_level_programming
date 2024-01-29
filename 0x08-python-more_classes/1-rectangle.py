#!/usr/bin/python3
"""
Module 1-rectangle
Defines a class Rectangle with private attribute width and height
"""


class Rectangle:
    """
    Defines a rectangle by its width and height

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
