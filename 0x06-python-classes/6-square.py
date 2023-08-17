#!/usr/bin/python3
"""An empty class defining a square"""


class Square:
    """Define a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        "define private variable position"""
        return self.__position

    """property setter to set position"""
    @position.setter
    def position(self, value):
        """check if value is a tuple of 2 positive integers"""
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """public instance method"""
    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.position[1] > 0:
            print("\n" * self.position[1], end="")

        for i in range(self.__size):
            if self.position[0] > 0:
                print(" " * self.position[0], end="")
            print("#" * self.__size)
