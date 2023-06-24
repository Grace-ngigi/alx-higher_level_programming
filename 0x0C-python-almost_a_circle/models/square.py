#!/usr/bin/python3
"""Creating a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherit attrs from rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Print square using __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
