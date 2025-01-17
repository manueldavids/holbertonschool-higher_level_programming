#!/usr/bin/python3

# Print numbers from 0 to 99 in ascending order, separated by ", "
for number in range(100):  # Loop from 0 to 99
    if number != 99:  # For numbers 0 to 98, include ", " after the number
        print("{:02d}, ".format(number), end="")
    else:  # For the last number (99), print without ", " and with a newline
        print("{:02d}".format(number))
