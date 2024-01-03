#!/usr/bin/python3

def uppercase(input_string):
    
    for char in input_string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
            print("{}".format(char), end="")
            print("")
