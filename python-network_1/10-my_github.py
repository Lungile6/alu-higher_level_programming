#!/usr/bin/python3
"""
This script retrieves the user's GitHub ID using
the GitHub API with HTTP Basic Authentication.
"""

import requests
import sys

if __name__ == '__main__':
    # Get the GitHub username and password from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send a GET request to the GitHub API for the user information
    response = requests.get(
        url="https://api.github.com/user",
        auth=(requests.auth.HTTPBasicAuth(username, password))
    )

    try:
        # Attempt to parse the response as JSON and print the user's GitHub ID
        json_response = response.json()
        print("{}".format(json_response["id"]))
    except KeyError:
        # If the JSON response does not contain an "id" key, print None
        print(None)
    except ValueError:
        # If the response is not valid JSON, print None
        print(None)
