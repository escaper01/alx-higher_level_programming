#!/usr/bin/python3
def pow(a, b):
    res = 1
    base = 1
    num = 0

    if b < 0:
        num = b
        b = (-1) * b

    for i in range(b):
        res *= a
        base = res * res

    if num < 0:
        res /= base
    return res
