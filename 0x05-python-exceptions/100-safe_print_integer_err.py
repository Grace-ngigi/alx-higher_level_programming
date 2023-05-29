#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except (Exception) as excep:
        sys.stderr.write('Execption: ' + str(excep) + '\n')
        return (False)
    return (True)
