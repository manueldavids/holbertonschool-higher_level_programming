#!/usr/bin/python3
if __name__ == "__main__":
    # Importing the hidden_4 module
    import hidden_4

    # Get all names defined in the module
    all_names = dir(hidden_4)

    # Filter names that do not start with "__"
    valid_names = [name for name in all_names if not name.startswith("__")]

    # Print names in alphabetical order
    for name in sorted(valid_names):
        print(name)
