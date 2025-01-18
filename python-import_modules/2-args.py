#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the script name
    argc = len(argv)  # Number of arguments

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
