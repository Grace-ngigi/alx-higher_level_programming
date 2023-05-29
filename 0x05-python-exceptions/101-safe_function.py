#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        fin = fct(*args)
    except Execption as excep:
        sys.stderr.write("Exception: {}\n".format(excep))
        fin = None
    return (fin)
