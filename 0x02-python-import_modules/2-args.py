#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    print("{} ".format(total - 1), end="")
    if total == 1:
        print("arguments.")
    elif total > 1:
        if total == 2:
            print("argument:")
        elif total > 2:
            print("arguments:")
        for i in range(total - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
