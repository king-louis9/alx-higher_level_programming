#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    las_dgt = number % -10
else:
    las_dgt = number % 10

if las_dgt > 5:
    print(f"Last digit of {number} is {las_dgt} and is greater than 5")
elif las_dgt == 0:
    print(f"Last digit of {number} is {las_dgt} and is 0")
else:
    print(f"Last digit of {number} is {las_dgt} and is less than 6 and not 0")
