#!/usr/bin/python3
"""Reads and prints a text file."""


def read_file(filename=""):
    """Prints the contents of filename to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
