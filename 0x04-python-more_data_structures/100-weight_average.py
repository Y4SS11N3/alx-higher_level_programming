#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    tw = sum(w for _, w in my_list)
    ws = sum(s * w for s, w in my_list)

    return (ws / tw if tw > 0 else 0)
