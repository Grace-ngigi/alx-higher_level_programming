#!/usr/bin/python3
"""An Empty base geometry class"""


class BaseGeometry:
    """An empty base geometry class"""
    def area(self):
        """public instance method for area calculations"""
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(self, name, value):
        """vaidates Value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry Class"""
    def __init__(self, width, height):
        """validate Width and Height"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print using __str__ method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
