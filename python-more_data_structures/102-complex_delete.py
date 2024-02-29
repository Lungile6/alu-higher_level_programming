#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for keys, v in tmp.items():
        if v == value:
            a_dictionary.pop(keys)
        return a_dictionary
