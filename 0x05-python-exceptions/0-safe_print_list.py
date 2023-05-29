#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for items in range(x):
            print(my_list[items], end="")
            n += 1
            for (x in range(n):
                print("", end="")
        print()
        return (n)
    except IndexError:
        print()
        return (n)
