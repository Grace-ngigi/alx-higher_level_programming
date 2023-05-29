#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for items in range(x):
        try:
            print(f'{my_list[items]}', end='')
        except (IndexError):
            continue
        n += 1
    print()
    return (n)
