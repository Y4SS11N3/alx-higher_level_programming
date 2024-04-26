#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    query = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=query)
    try:
        json_response = response.json()
        if json_response == {}:
            print("No result")
        else:
            id = json_response.get("id")
            name = json_response.get("name")
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
