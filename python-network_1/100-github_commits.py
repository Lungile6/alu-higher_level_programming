#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

if __name__ == "__main__":
    # Construct the GitHub API URL for commits
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send an HTTP GET request to the GitHub API
    r = requests.get(url)
    commits = r.json()

    try:
        # Iterate over the first 10 commits and print commit information
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
