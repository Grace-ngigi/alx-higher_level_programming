#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    return sum(list(set(my_list)))
