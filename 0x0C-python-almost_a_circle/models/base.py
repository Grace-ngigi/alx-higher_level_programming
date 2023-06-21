#!/usr/bin/python3
"""a new class"""


class Base:
    """base class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
