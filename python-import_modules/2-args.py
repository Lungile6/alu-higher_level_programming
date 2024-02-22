#!/usr/bin/python3

if_name_="_main_":
    """Print number of and  list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument.")
    elif count == 1:
        print(" 1 argument:")
    else:
        print("{} arguments:".format(coount))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
