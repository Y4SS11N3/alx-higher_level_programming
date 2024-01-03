#!/usr/bin/python3

def uppercase(input_string):
    output_string = ""
    for char in input_string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        output_string += char
    print("{}".format(output_string))
