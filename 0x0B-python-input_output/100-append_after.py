#!/usr/bin/python3
"""inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    with open(filename, 'r') as ffile:
        lines = ffile.readlines()
    with open(filename, 'w') as ffile:
        for line in lines:
            if search_string in line:
                ffile.write(line + new_string)
            else:
                ffile.write(line)
