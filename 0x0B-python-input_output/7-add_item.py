#!/usr/bin/python3
"""Adds all arguments to a list and saves them to a file."""
import sys


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
