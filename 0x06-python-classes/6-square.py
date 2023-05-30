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
        return elf.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 position integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """find area of the sqaure"""
        return self.__size ** 2

    def my_print(self):
        """print the ssqaure"""
        if self.__size == 0:
            print()
            return
            for i in range(self.__size):
                print()
            for items in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
