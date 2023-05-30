#!/usr/bin/python3
"""An empty class defining a square"""


class Square:
    """Define a class square"""
    def __init__(self, size=0):
        """Initialize the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """find area of the sqaure"""
        return self.__size ** 2
