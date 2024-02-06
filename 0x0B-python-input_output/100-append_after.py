#!/usr/bin/python3
"""Inserts a line of text to a file, after each line
containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing
    earch_string in filename."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
