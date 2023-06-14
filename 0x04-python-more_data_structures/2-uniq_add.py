#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = [x for i, x in enumerate(my_list) if x not in my_list[:i]]
    return sum(unique_list)
