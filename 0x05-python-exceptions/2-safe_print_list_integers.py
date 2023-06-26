#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            counter += 1
    except(ValueError, TypeError):
        pass
    print()
    return counter
