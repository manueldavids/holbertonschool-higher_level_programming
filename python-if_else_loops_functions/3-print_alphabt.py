#!/usr/bin/python3

# Print the ASCII alphabet in lowercase except 'q' and 'e', without a newline
for letter in range(97, 123):
    if letter != 113 and letter != 101:  # Exclude 'q' (113) and 'e' (101)
        print("{:c}".format(letter), end="")
