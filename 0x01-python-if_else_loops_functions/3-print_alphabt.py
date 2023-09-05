#!/usr/bin/python3
for elem in range(ord('a'), ord('z') + 1):
    if chr(elem) in ['q', 'e']:
        print("{}".format(chr(elem)), end="")
