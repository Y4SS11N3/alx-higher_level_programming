#!/usr/bin/python3
"""
Python script that takes 2 arguments to list 10 commits (from the most recent
to oldest) of a specified repository by a specified user using the GitHub API.
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i]["sha"]
            author_name = commits[i]["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
