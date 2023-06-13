#!/usr/bin/python3
"""return same class or inherit from a class"""


def is_kind_of_class(obj, a_class):
    """Return True if it is an Instance of that class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
