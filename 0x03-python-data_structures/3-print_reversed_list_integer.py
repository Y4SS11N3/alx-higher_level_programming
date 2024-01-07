#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for idx in range(length - 1, -1, -1):
        print("{:d}".format(my_list[idx]))
