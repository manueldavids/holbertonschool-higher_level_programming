#!/usr/bin/python3

# Print numbers from 0 to 99 in ascending order with proper formatting
for number in range(100):  # Loop from 0 to 99
    print("{:02d}".format(number), end=", " if number != 99 else "\n")
