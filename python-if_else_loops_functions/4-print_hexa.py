#!/usr/bin/python3

# Print numbers from 0 to 98 in decimal and hexadecimal
for number in range(99):  # Loop from 0 to 98 (inclusive)
    print("{:d} = 0x{:x}".format(number, number))
