#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a newline after each character
print("".join("{:c}".format(letter) for letter in range(97, 123)))
