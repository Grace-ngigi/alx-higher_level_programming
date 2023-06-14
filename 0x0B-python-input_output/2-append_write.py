#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, 'a') as ffile:
        return ffile.write(text)
