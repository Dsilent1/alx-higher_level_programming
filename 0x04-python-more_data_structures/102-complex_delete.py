#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for x, f in tmp.items():
        if value == f:
            my_dict.pop(x)
    return my_dict
