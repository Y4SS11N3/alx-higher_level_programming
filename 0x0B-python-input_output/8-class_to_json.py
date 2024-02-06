#!/usr/bin/python3
"""Returns the dictionary description with simple
data structure for JSON serialization of an object."""


def class_to_json(obj):
    """Dictionary description for JSON serialization of obj."""
    return obj.__dict__
