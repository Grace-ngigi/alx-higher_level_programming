#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Sqaure inherits from Rectangle which inherits from BaseGeometry"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
