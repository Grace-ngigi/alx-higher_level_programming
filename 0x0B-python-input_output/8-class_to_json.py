#!/usr/bin/python3
"""returns dictionary description with simple data structure"""


def class_to_json(obj):
    """returns dictionary description with simple data structure"""
    return obj.__dict__
