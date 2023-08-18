#!/usr/bin/python3
"""Defines a square"""


class Square:
    def __init__(self, size=0):
        """
        Initialize square class
        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the value of size
        Args:
            value: new value of size
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator"""
        return self.area() >= other.area()
