#!/usr/bin/python3

# Print numbers from 0 to 98 in decimal and hexadecimal
for number in range(0, 99):  # Ensure the range is from 0 to 98 inclusive
    print("{:d} = 0x{:x}".format(number, number))
