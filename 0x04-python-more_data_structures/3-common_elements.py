#!/usr/bin/python3
def common_elements(set_1, set_2):
    for i in set_1:
        for j in set_2:
            if i in set_2 and j in set_1:
                return i
