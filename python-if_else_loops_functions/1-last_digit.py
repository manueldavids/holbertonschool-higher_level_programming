#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Calculate the absolute value of the last digit of the number
last_digit = abs(number) % 10

# If the number is negative, make the last digit negative
if number < 0:
    last_digit = -last_digit

# Check and print the classification of the last digit
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} "
          "and is less than 6 and not 0")
