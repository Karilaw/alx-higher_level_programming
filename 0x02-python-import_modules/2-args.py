#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num_args))
    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
