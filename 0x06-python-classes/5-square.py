#!/usr/bin/python3
"""An empty class defining a square"""


class Square:
    """Define a class square"""
    def __init__(self, size=0):
        """Initialize the square"""
        self.__size = size

    @property
    def size(self):
        """defin private variable size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value to size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """find area of the sqaure"""
        return self.__size ** 2

    def my_print(self):
        """print the ssqaure"""
        if self.__size == 0:
            print()
        else:
            for items in range(self.__size):
                print("#" * self.__size)
