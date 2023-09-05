#!/usr/bin/python3
def uppercase(str):
    new_end = ""
    str_size = len(str)
    if len(str) == 0:
        return "\n"
    for index, i in enumerate(str):
        if index == str_size - 1:
            new_end = "\n"
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i) - 32)), end=new_end)
        else:
            print("{}".format(i), end=new_end)

