#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        for i in range(idx, len(my_list) - 1):
            my_list[i] = my_list[i + 1]
        my_list.pop()
    return my_list
