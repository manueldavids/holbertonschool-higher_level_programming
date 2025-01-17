#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a newline after each character
for letter in range(97, 123):
    print("{:c}".format(letter), end="")
