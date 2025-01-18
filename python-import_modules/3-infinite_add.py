#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Exclude the script name and cast arguments to integers
    arguments = map(int, sys.argv[1:])

    # Calculate the sum of arguments
    total = sum(arguments)

    # Print the result
    print(total)
