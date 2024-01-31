#!/usr/bin/python3
"""Defines a function to indent text after specific punctuation marks."""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    space_skipped = False  # Flag to indicate if initial spaces are skipped
    while i < len(text):
        if text[i] in ".?:":
            print(text[i] + "\n\n", end="")
            space_skipped = False  # Reset the flag after punctuation
            i += 1
        elif text[i] == ' ' and not space_skipped:
            # Skip initial spaces after punctuation and new lines
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            # Print non-space characters and set the flag to True
            print(text[i], end="")
            space_skipped = True
            i += 1
