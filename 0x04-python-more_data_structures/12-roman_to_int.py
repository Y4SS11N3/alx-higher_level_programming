#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    prev_value = 0

    for char in reversed(roman_string):
        current = roman_num[char]
        if current < prev_value:
            int_value -= current
        else:
            int_value += current
        prev_value = current

    return (int_value)
