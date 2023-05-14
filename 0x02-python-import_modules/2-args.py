#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv) - 1
    if (total == 0):
        print("{} arguments.".format(total))
    elif (total == 1):
        print("{} argument:".format(total))
    else:
        print("{}: arguments:".format(total))
    if total >= 1:
        total = 0
        for i in sys.argv:
            if total != 0:
                print("{}: {}".format(total, i))
            total += 1
