#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
# Use abs() to get the absolute value of the number, then use % 10 to get the last digit
last_digit = abs(number) % 10

# If the number is negative, make the last digit negative
if number < 0:
    last_digit = -last_digit

# Print the last digit and its classification
print(f"Last digit of {number} is {last_digit} and is greater than 5")

# Check if the last digit is greater than 5
if last_digit > 5:
    print("and is greater than 5")
# Check if the last digit is 0
elif last_digit == 0:
    print("and is 0")
# Check if the last digit is less than 6 and not 0
else:
    print("and is less than 6 and not 0")
