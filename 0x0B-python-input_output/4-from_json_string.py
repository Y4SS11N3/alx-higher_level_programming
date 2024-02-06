#!/usr/bin/python3
"""Returns an object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Returns an object represented by my_str."""
    return json.loads(my_str)
