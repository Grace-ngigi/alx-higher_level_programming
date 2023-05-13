#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total  = len(sys.argv) - 1
    if (total == 0):
        print("{} arguments.".format(total))
    elif (total == 1):
        print("{}: argument: {}".format(total, sys.argv[0]))
        print("1:", sys.argv[1])
    else:
        print("{}: arguments:".format(total))
        for i in range (1, total + 1):
            print("{}: {}".format(i, sys.argv[i]))
