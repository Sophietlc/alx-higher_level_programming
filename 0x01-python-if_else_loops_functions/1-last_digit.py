#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    remainder = number % 10
elif number < 0:
    remainder = number % -10
first = "Last digit of "
if remainder > 5:
    print(first  + str(number) + " is " + str(remainder) + " and is greater than 5")
elif remainder == 0:
    print(first  + str(number) + " is " + str(remainder) + " and is 0")
elif remainder < 6 and remainder != 0:
    print(first + str(number) + " is " + str(remainder) + " and is less than 6 and not 0")
