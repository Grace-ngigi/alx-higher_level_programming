#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string and returns the number of characters read"""
    with open(filename, "w", encoding="utf-8") as ffile:
        return ffile.write(text)
