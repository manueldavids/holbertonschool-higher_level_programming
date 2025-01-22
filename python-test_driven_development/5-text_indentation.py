#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = {'.', '?', ':'}
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            # Skip spaces after punctuation
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print each line without leading or trailing spaces
    print("\n".join([line.strip() for line in result.split("\n")]))
