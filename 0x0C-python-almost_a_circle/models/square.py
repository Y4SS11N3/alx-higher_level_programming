#!/usr/bin/python3
"""Defines the Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square object that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The id of the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square, along with
        width and height from Rectangle."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Update the Square's attributes with
        non-keyword or keyword arguments."""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                if attr == 'size':
                    self.size = value
                else:
                    setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'x', 'y']:
                    setattr(self, key, value)
                elif key == 'size':
                    self.size = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
