#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as exep:
        print("Execption: {}".format(exep), file=sys.stderr)
        return (False)
