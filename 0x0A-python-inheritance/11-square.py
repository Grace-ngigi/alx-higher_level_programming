#!/usr/bin/python3
"""Inherits from 9-rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from class Rectangle"""
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area method """
        return self.__size * self.__size

    def __str__(self):
        """print using __str__ method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
