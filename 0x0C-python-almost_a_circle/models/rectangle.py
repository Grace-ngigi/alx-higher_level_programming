#!/usr/bin/python3
"""a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
