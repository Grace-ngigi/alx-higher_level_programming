#!/usr/bin/python3
"""adds a new attr to an obj if its possible"""


def add_attribute(objt, name, value):
    """adds a new attr to an obj if its possible"""
    if hasattr(objt, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(objt, name, value)
