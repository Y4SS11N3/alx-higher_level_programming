#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            uppercase_str += c
            print(uppercase_str)
