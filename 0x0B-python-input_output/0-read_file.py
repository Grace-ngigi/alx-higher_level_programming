#!/usr/bin/python3
"""reads a text file and prints it"""


def read_file(filename=""):
    """reads a text file and prints it"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
