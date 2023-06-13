#!/usr/bin/python3
"""An Empty base geometry class"""


class BaseGeometry:
    """An empty base geometry class"""
    def area(self):
        """public instance method for area calculations"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """vaidates Value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
