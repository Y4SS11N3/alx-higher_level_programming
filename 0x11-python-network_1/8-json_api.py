#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            id = json_response.get("id")
            name = json_response.get("name")
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
