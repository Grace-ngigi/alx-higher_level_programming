#!/usr/bin/python3
"""
returns True if the object is an instance of a class, otherwise False
"""


def inherits_from(obj, a_class):
    """returns Tre if the obj is an instance of a class"""
    if (type(obj) != a_class and isinstance(obj, a_class)):
        return True
    else:
        return False
