#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        new_list = my_list.reversed()
        for i in new_list:
            print("{:d}".format(new_list[i]))
