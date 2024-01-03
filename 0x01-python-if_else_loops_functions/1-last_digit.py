#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
j = abs(number) % 10

if number < 0:
    j = -j
print(f"Last digit of {number:d} is {j:d} and is ", end="")
if j > 5:
    print("greater than 5")
elif j == 0:
    print("0")
else:
    print("less than 6 and not 0")
