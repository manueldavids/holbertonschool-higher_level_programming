#!/usr/bin/python3

def fizzbuzz():
    """
    Print numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    Each output is separated by a space.
    """
    for number in range(1, 101):  # Loop from 1 to 100 inclusive
        if number % 3 == 0 and number % 5 == 0:  # Multiple of both 3 and 5
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:  # Multiple of 3
            print("Fizz", end=" ")
        elif number % 5 == 0:  # Multiple of 5
            print("Buzz", end=" ")
        else:  # Not a multiple of 3 or 5
            print("{}".format(number), end=" ")
