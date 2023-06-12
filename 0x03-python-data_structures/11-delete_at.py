#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        position = my_list[idx]
        my_list.remove(position)
    return my_list
