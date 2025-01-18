#!/usr/bin/python3

def uppercase(str):
    """
    Print a string in uppercase followed by a new line.

    Args:
        str: The input string to convert to uppercase.
    """
    for char in str:
        # Check if the character is a lowercase letter
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert lowercase to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        # Print the character without a newline
        print("{:s}".format(char), end="")
    # Print a newline at the end
    print()


# Test cases
if __name__ == "__main__":
    uppercase("holberton")
    uppercase("Holberton School 98 Battery street")
    uppercase("")
    uppercase("1234!@#$")
